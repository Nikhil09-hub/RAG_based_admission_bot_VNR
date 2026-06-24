
from __future__ import annotations

import argparse
import hashlib
import os
import re
from pathlib import Path
from typing import Generator

from pinecone import Pinecone, ServerlessSpec
from openai import OpenAI

from app.config import get_settings

settings = get_settings()

# ── Clients ───────────────────────────────────────────────────
_openai_client: OpenAI | None = None
_pinecone_index = None


def _get_openai() -> OpenAI:
    global _openai_client
    if _openai_client is None:
        _openai_client = OpenAI(api_key=settings.OPENAI_API_KEY)
    return _openai_client


def _get_index():
    global _pinecone_index
    if _pinecone_index is None:
        pc = Pinecone(api_key=settings.PINECONE_API_KEY)

        # Create index if it doesn't exist
        existing = [idx.name for idx in pc.list_indexes()]
        if settings.PINECONE_INDEX_NAME not in existing:
            pc.create_index(
                name=settings.PINECONE_INDEX_NAME,
                dimension=1536,  # text-embedding-3-small
                metric="cosine",
                spec=ServerlessSpec(
                    cloud="aws",
                    region=settings.PINECONE_ENVIRONMENT,
                ),
            )
            print(f"✅  Created Pinecone index: {settings.PINECONE_INDEX_NAME}")

        _pinecone_index = pc.Index(settings.PINECONE_INDEX_NAME)
    return _pinecone_index


# ── Text extraction ───────────────────────────────────────────

def _read_text_file(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="ignore")


def _read_pdf_file(path: Path) -> str:
    """Extract text from PDF, with special handling for tables."""
    try:
        import pdfplumber
    except ImportError:
        raise ImportError("Install pdfplumber:  pip install pdfplumber")

    parts: list[str] = []
    with pdfplumber.open(str(path)) as pdf:
        for page_num, page in enumerate(pdf.pages, 1):
            # Try extracting tables first
            tables = page.extract_tables()
            if tables:
                for table in tables:
                    if not table:
                        continue
                    # First row as headers
                    headers = [str(c).strip() if c else "" for c in table[0]]
                    for row in table[1:]:
                        cells = [str(c).strip() if c else "" for c in row]
                        if not any(cells):
                            continue
                        entry_parts = []
                        for h, v in zip(headers, cells):
                            if v:
                                entry_parts.append(f"{h}: {v}")
                        if entry_parts:
                            parts.append(", ".join(entry_parts))

            # Also extract non-table text from the page
            text = page.extract_text() or ""
            # Remove text that's already captured in tables to avoid duplication
            if text.strip() and not tables:
                parts.append(text.strip())

    return "\n".join(parts)


def _read_excel_file(path: Path) -> str:
    """Extract text from Excel (.xlsx, .xls) – converts each sheet to readable text."""
    try:
        import openpyxl
    except ImportError:
        raise ImportError("Install openpyxl:  pip install openpyxl")

    wb = openpyxl.load_workbook(str(path), read_only=True, data_only=True)
    parts: list[str] = []

    for sheet_name in wb.sheetnames:
        ws = wb[sheet_name]
        rows = list(ws.iter_rows(values_only=True))
        if not rows:
            continue

        parts.append(f"## Sheet: {sheet_name}")

        # First row as headers
        headers = [str(c) if c is not None else "" for c in rows[0]]

        for row in rows[1:]:
            cells = [str(c) if c is not None else "" for c in row]
            # Skip completely empty rows
            if not any(cells):
                continue
            # Format as "Header: Value" pairs for better RAG retrieval
            entry_parts = []
            for h, v in zip(headers, cells):
                if v:
                    entry_parts.append(f"{h}: {v}")
            if entry_parts:
                parts.append(", ".join(entry_parts))

    wb.close()
    return "\n".join(parts)


def _read_csv_file(path: Path) -> str:
    """Extract text from CSV files."""
    import csv

    parts: list[str] = []
    with open(path, "r", encoding="utf-8", errors="ignore") as f:
        reader = csv.reader(f)
        rows = list(reader)

    if not rows:
        return ""

    headers = rows[0]
    for row in rows[1:]:
        if not any(row):
            continue
        entry_parts = []
        for h, v in zip(headers, row):
            if v:
                entry_parts.append(f"{h}: {v}")
        if entry_parts:
            parts.append(", ".join(entry_parts))

    return "\n".join(parts)


def _read_docx_file(path: Path) -> str:
    """Extract text from Word .docx files."""
    try:
        from docx import Document
    except ImportError:
        raise ImportError("Install python-docx:  pip install python-docx")

    doc = Document(str(path))
    parts: list[str] = []
    
    for paragraph in doc.paragraphs:
        text = paragraph.text.strip()
        if text:
            parts.append(text)
    
    # Also extract text from tables
    for table in doc.tables:
        for row in table.rows:
            row_text = [cell.text.strip() for cell in row.cells]
            if any(row_text):
                parts.append(" | ".join(row_text))
    
    return "\n\n".join(parts)


def _extract_text(path: Path) -> str:
    ext = path.suffix.lower()
    if ext == ".pdf":
        return _read_pdf_file(path)
    if ext == ".docx":
        return _read_docx_file(path)
    if ext in (".xlsx", ".xls"):
        return _read_excel_file(path)
    if ext == ".csv":
        return _read_csv_file(path)
    if ext in (".txt", ".md", ".markdown"):
        return _read_text_file(path)
    raise ValueError(f"Unsupported file type: {ext}")




def detect_section(chunk_text: str) -> str:

    text = chunk_text.upper()
    #=== NRI FN OCI ADMISSIONS ====
    # ===== Branch Intake Document =====

    if "BRANCH CODE: AID" in text:
        return "branch_aids"

    elif "BRANCH CODE: AUT" in text:
        return "branch_automobile"

    elif "BRANCH CODE: BIO" in text:
        return "branch_biotechnology"

    elif "BRANCH CODE: CIV" in text:
        return "branch_civil"

    elif "BRANCH CODE: CSB" in text:
        return "branch_csbs"

    elif "BRANCH CODE: CSE" in text:
        return "branch_cse"

    elif "BRANCH CODE: CSE-CSM" in text:
        return "branch_cse_aiml"

    elif "BRANCH CODE: CSE-CSC" in text:
        return "branch_cse_cyber"

    elif "BRANCH CODE: CSE-CSD" in text:
        return "branch_cse_ds"

    elif "BRANCH CODE: CSE-CSO" in text:
        return "branch_cse_iot"

    elif "BRANCH CODE: CSE" in text:
        return "branch_cse"
    elif "BRANCH CODE: EEE" in text:
        return "branch_eee"

    elif "BRANCH CODE: EIE" in text:
        return "branch_eie"

    elif "BRANCH CODE: ECE" in text:
        return "branch_ece"

    elif "BRANCH CODE: VLSI" in text:
        return "branch_vlsi"

    elif "BRANCH CODE: IT" in text:
        return "branch_it"

    elif "BRANCH CODE: ME" in text:
        return "branch_mechanical"

    elif "BRANCH CODE: RAI" in text:
        return "branch_rai"
    elif "POWER SYSTEMS (EEE)" in text:
        return "mtech_power_systems"

    elif "DATA SCIENCE (DS)" in text:
        return "mtech_data_science"
    #==== =====
    elif "NRI / FN / OCI / CIWG QUOTA ADMISSIONS" in text:
        return "nri_admission"

    elif "ELIGIBILITY CRITERIA" in text:
        return "nri_eligibility"

    elif "DOCUMENTS REQUIRED" in text:
        return "nri_documents"

    elif "NRI SEATS AVAILABLE" in text:
        return "nri_seat_availability"
    # ===== Department Sections =====

    elif "COMPUTER SCIENCE & ENGINEERING (CSE)" in text:
        return "dept_cse"

    elif "CSE (ARTIFICIAL INTELLIGENCE" in text:
        return "dept_cse_aiml"

    elif "CSE (DATA SCIENCE & CYBER SECURITY)" in text:
        return "dept_cse_ds_cys"

    elif "INFORMATION TECHNOLOGY (IT)" in text:
        return "dept_it"

    elif "ELECTRONICS & COMMUNICATION ENGINEERING (ECE)" in text:
        return "dept_ece"

    elif "ELECTRICAL & ELECTRONICS ENGINEERING (EEE)" in text:
        return "dept_eee"

    elif "ELECTRONICS & INSTRUMENTATION ENGINEERING (EIE)" in text:
        return "dept_eie"

    elif "MECHANICAL ENGINEERING DEPARTMENT" in text:
        return "dept_mechanical"

    elif "CIVIL ENGINEERING DEPARTMENT" in text:
        return "dept_civil"

    elif "AUTOMOBILE ENGINEERING DEPARTMENT" in text:
        return "dept_automobile"

    elif "BIOTECHNOLOGY DEPARTMENT" in text:
        return "dept_biotechnology"

    elif "CHEMISTRY DEPARTMENT" in text:
        return "dept_chemistry"

    elif "PHYSICS DEPARTMENT" in text:
        return "dept_physics"

    elif "ENGLISH (HUMANITIES) DEPARTMENT" in text:
        return "dept_english"

    elif "MATHEMATICS & MANAGEMENT SCIENCES DEPARTMENT" in text:
        return "dept_mathematics"

    elif "GENERAL DEPARTMENTS OVERVIEW PAGE" in text:
        return "dept_overview"

    elif "HOW TO USE THESE LINKS" in text:
        return "dept_usage_guide"

    elif "CONTACT INFORMATION" in text:
        return "department_contact_info"

    # ===== Category A Reporting =====
    elif "DOCUMENTS REQUIRED FOR CATEGORY A" in text:
        return "category_a_documents"

    elif "STEP 1" in text:
        return "category_a_step1"

    elif "STEP 2" in text:
        return "category_a_step2"

    elif "STEP 3" in text:
        return "category_a_step3"

    elif "STEP 4" in text:
        return "category_a_step4"

    # ===== Admissions =====
    elif "APPLICATION FEES" in text:
        return "application_fees"

    elif "UNDERGRADUATE PROGRAMMES" in text:
        return "ug_admissions"

    elif "POST GRADUATE ADMISSIONS" in text:
        return "pg_admissions"

    elif "IMPORTANT LINKS" in text:
        return "important_links"

    elif "GENERAL ENQUIRY" in text:
        return "general_enquiry"

    elif "FN / OCI / CIWG" in text:
        return "international_admission"

    elif "LATERAL ENTRY" in text:
        return "lateral_entry"

    elif "CATEGORY-A" in text:
        return "convener_quota"
    # ===== Seat Intake =====

    elif "CODE: CIV" in text:
        return "seat_civil"

    elif "CODE: EEE" in text:
        return "seat_eee"

    elif "CODE: MEC" in text:
        return "seat_mechanical"

    elif "CODE: ECE" in text:
        return "seat_ece"

    elif "CODE: CSE" in text:
        return "seat_cse"

    elif "CODE: EIE" in text:
        return "seat_eie"

    elif "CODE: INF" in text:
        return "seat_it"

    elif "CODE: AUT" in text:
        return "seat_automobile"

    elif "CODE: CSB" in text:
        return "seat_csbs"

    elif "CODE: CSD" in text:
        return "seat_cse_ds"

    elif "CODE: CSM" in text:
        return "seat_cse_aiml"

    elif "CODE: CSC" in text:
        return "seat_cse_cys"

    elif "CODE: CSO" in text:
        return "seat_cse_iot"

    elif "CODE: AID" in text:
        return "seat_aids"

    elif "CODE: BIO" in text:
        return "seat_biotech"

    elif "CODE: EVL" in text:
        return "seat_vlsi"

    elif "CODE: RAI" in text:
        return "seat_rai"

    elif "CATEGORY-B" in text:
        return "management_quota"

    # ===== Hostel =====
    elif "STUDENT INFORMATION REQUIREMENTS" in text:
        return "hostel_student_information"

    elif "DISCIPLINE & CONDUCT" in text:
        return "hostel_discipline_conduct"

    elif "FEES & ACCOMMODATION" in text:
        return "hostel_fees_accommodation"

    elif "ANTI-RAGGING & PROHIBITED ACTIVITIES" in text:
        return "hostel_anti_ragging"

    elif "VISITORS & LEAVE POLICY" in text:
        return "hostel_visitors_leave"

    elif "SECURITY & INSPECTION" in text:
        return "hostel_security_inspection"

    elif "DAMAGE & PENALTIES" in text:
        return "hostel_damage_penalties"

    elif "GENERAL INFORMATION" in text:
        return "hostel_general_information"

    elif "FOOD & DINING FACILITIES" in text:
        return "hostel_food_dining"

    elif "SECURITY & SAFETY" in text:
        return "hostel_security_safety"

    elif "SPORTS & FITNESS" in text:
        return "hostel_sports_fitness"

    elif "MEDICAL & UTILITIES" in text:
        return "hostel_medical_utilities"

    elif "TRAINING & LEARNING FACILITIES" in text:
        return "hostel_training_learning"

    elif "ENTERTAINMENT & RECREATION" in text:
        return "hostel_entertainment_recreation"

    elif "ADDITIONAL FACILITIES" in text:
        return "hostel_additional_facilities"

    elif "FEE STRUCTURE" in text:
        return "hostel_fee_structure"

    elif "CONTACT DETAILS" in text:
        return "hostel_contact_details"

    # ===== Training & Placements =====
    elif "VISION" in text:
        return "tp_vision"

    elif "MISSION" in text:
        return "tp_mission"

    elif "TRAINING OBJECTIVES" in text:
        return "tp_training_objectives"

    elif "PLACEMENT OBJECTIVES" in text:
        return "tp_placement_objectives"

    elif "STUDENT ELIGIBILITY" in text:
        return "tp_student_eligibility"

    elif "SECTION 8: CAMPUS PLACEMENT STATISTICS" in text:
        return "tp_placement_statistics"

    elif "INTERNSHIP HIGHLIGHTS" in text:
        return "tp_internship_highlights"

    elif "TRAINING ROADMAP" in text:
        return "tp_training_roadmap"

    elif "SCHOLARSHIP" in text:
        return "tp_scholarship"

    elif "AWARDS" in text:
        return "tp_awards"

    # ===== Anti Fraud =====
    elif "FRAUD REPORTING ONLY" in text:
        return "fraud_reporting"

    elif "IMPORTANT CONTACT INFORMATION" in text:
        return "contact_information"

    elif "ADMISSIONS POLICY" in text:
        return "admissions_policy"

    elif "BEWARE OF FRAUDSTERS" in text:
        return "fraud_warning"

    # ===== Campus Life =====
    elif "PROFESSIONAL CHAPTERS" in text:
        return "professional_societies"

    elif "CLUBS" in text:
        return "campus_clubs"

    elif "CAMPUS CELEBRATIONS" in text:
        return "campus_celebrations"
    #==== Eligibility ====
    elif "OCI CARD HOLDERS" in text:
        return "oci_admission"

    elif "CIWG CATEGORY" in text:
        return "ciwg_admission"

    elif "FOREIGN NATIONALS" in text:
        return "foreign_national_admission"

    elif "ELIGIBILITY CRITERIA FOR FN/OCI/CIWG" in text:
        return "fn_oci_ciwg_eligibility"
    elif "INTRODUCTION" in text:
        return "college_introduction"

    elif "VNRVJIET AT A GLANCE" in text:
        return "college_at_a_glance"

    elif "RESEARCH & DEVELOPMENT" in text:
        return "college_research_development"

    elif "PROGRAMMES OFFERED" in text:
        return "college_programmes"

    elif "EXTRA-CURRICULAR ACTIVITIES" in text:
        return "college_extra_curricular"

    elif "CO-CURRICULAR ACTIVITIES" in text:
        return "college_co_curricular"
    
    

    return "general"





def _section_aware_chunk(
    text: str,
    max_tokens: int = 350,
    overlap_tokens: int = 50,
):
    """
    Section-first chunking.
    """

    sections = re.split(
        r"\n-{20,}\n\s*\d+\.\s",
        text
    )

    sections = [s.strip() for s in sections if s.strip()]

    for section in sections:

        words = section.split()

        if len(words) <= max_tokens:
            yield section

        else:
            start = 0

            while start < len(words):

                end = min(start + max_tokens, len(words))

                yield " ".join(words[start:end])

                if end == len(words):
                    break

                start = end - overlap_tokens
def _branch_intake_chunk(text: str):

    sections = re.split(
        r"(?=\n\d+\.\s[A-Z])",
        text
    )

    sections = [s.strip() for s in sections if s.strip()]

    for section in sections:
        yield section

def _departments_chunk(text: str):

    sections = re.split(
        r"(?=##\s)",
        text
    )

    sections = [s.strip() for s in sections if s.strip()]
    for i, section in enumerate(sections):
        print(f"SECTION {i}:")
        print(section[:100])
        print()

    for section in sections:
        yield section

def _campus_life_chunk(text: str):
    sections = re.split(
        r"(?=\n\s*\d+\.\s)",
        text
    )

    sections = [s.strip() for s in sections if s.strip()]

    for section in sections:
        yield section

def _admissions_chunk(text: str):

    sections = re.split(r"\n=+\n", text)

    sections = [s.strip() for s in sections if s.strip()]

    for section in sections:
        yield section

def _placements_chunk(text: str):
    """
    Chunk Training & Placements document
    using SECTION 1:, SECTION 2:, ... markers.
    """

    sections = re.split(
        r"(?=SECTION\s+\d+\s*:)",
        text,
        flags=re.IGNORECASE
    )

    sections = [s.strip() for s in sections if s.strip()]

    for section in sections:
        yield section

def _category_a_reporting_chunk(text: str):
    """
    Chunk Category-A Reporting Flowchart document.
    Split by major workflow steps.
    """

    sections = re.split(
        r"(?=STEP\s+\d+\s*:)",
        text,
        flags=re.IGNORECASE
    )

    sections = [s.strip() for s in sections if s.strip()]

    for section in sections:
        yield section
    
def _nri_admission_chunk(text: str):

    sections = re.split(
        r"(?=Application Fee|Branch Codes|Seat Category|Fee Structure|Eligibility Criteria|Documents Required|Admission Process|NRI Seats Available|Important Notice)",
        text,
        flags=re.IGNORECASE
    )

    sections = [s.strip() for s in sections if s.strip()]

    for section in sections:
        yield section
def _seat_intake_chunk(text: str):
    """
    Split seat intake document branch-wise.
    Each branch becomes one chunk.
    """

    sections = re.split(
        r"(?=\n\d+\.\s)",
        text
    )

    sections = [s.strip() for s in sections if s.strip()]

    for section in sections:
        yield section

# ── Embedding ─────────────────────────────────────────────────

def _embed_texts(texts: list[str]) -> list[list[float]]:
    """Embed a batch of texts using OpenAI."""
    client = _get_openai()
    response = client.embeddings.create(
        input=texts,
        model=settings.OPENAI_EMBEDDING_MODEL,
    )
    return [item.embedding for item in response.data]


# ── Ingestion ─────────────────────────────────────────────────

# def ingest_file(
#     path: Path,
#     source_label: str = "document",
#     year: int = 2025,
#     batch_size: int = 50,
# ) -> int:
#     """
#     Ingest a single document into Pinecone.

#     Returns the number of chunks upserted.
#     """
#     text = _extract_text(path)
#     chunks = list(_section_aware_chunk(text))
#     print(f"\nTotal Chunks Created: {len(chunks)}\n")

#     for idx, chunk in enumerate(chunks):
#         print("\n" + "=" * 80)
#         print(f"CHUNK {idx}")
#     print("=" * 80)
#     print(chunk[:500])
    

#     if not chunks:
#         print(f"⚠️  No content extracted from {path.name}")
#         return 0

#     index = _get_index()
#     total = 0

#     for i in range(0, len(chunks), batch_size):
#         batch = chunks[i : i + batch_size]
#         embeddings = _embed_texts(batch)

#         vectors = []
#         for j, (chunk, emb) in enumerate(zip(batch, embeddings)):
#             section = detect_section(chunk)
#             chunk_id = hashlib.sha256(
#                 f"{path.name}:{i + j}:{chunk[:64]}".encode()
#             ).hexdigest()[:32]

#             vectors.append(
#                 {
#                     "id": chunk_id,
#                     "values": emb,
#                     "metadata": {
#                         "college": settings.COLLEGE_SHORT_NAME,
#                         "source": source_label,
#                         "year": year,
#                         "filename": path.name,
#                         "section":section,
#                         "chunk_index": i + j,
#                         "text": chunk[:2000],  # Pinecone metadata limit
#                     },
#                 }
#             )

#         index.upsert(vectors=vectors)
#         total += len(vectors)

#     print(f"✅  Ingested {total} chunks from {path.name}")
#     return total


def ingest_file(
    path: Path,
    source_label: str = "document",
    year: int = 2025,
    batch_size: int = 50,
) -> int:
    """
    TEST VERSION
    Only creates and prints chunks.
    Does NOT call OpenAI or Pinecone.
    """

    text = _extract_text(path)

    filename = path.name.lower()

    if "cat-a" in filename or "flowchart" in filename:
        chunks = list(_category_a_reporting_chunk(text))

    elif "admission" in filename:
        chunks = list(_admissions_chunk(text))

    elif "hostel" in filename:
        chunks = list(_section_aware_chunk(text))

    elif "placement" in filename or "t&p" in filename:
        chunks = list(_placements_chunk(text))

    elif "campus" in filename:
        chunks = list(_campus_life_chunk(text))

    elif "department" in filename:
        chunks = list(_departments_chunk(text))
    elif "seat" in filename or "intake" in filename:
        chunks = list(_seat_intake_chunk(text))
    elif "branch_intake" in filename:
        chunks = list(_branch_intake_chunk(text))

    else:
        chunks = list(_section_aware_chunk(text))

    print(f"\n📊 Total Chunks Created: {len(chunks)}\n")


    

    if not chunks:
        print(f"⚠️ No content extracted from {path.name}")
        return 0
    index = _get_index()
    total = 0

    for i in range(0, len(chunks), batch_size):
        batch = chunks[i : i + batch_size]
        embeddings = _embed_texts(batch)

        vectors = []

        for j, (chunk, emb) in enumerate(zip(batch, embeddings)):
            section = detect_section(chunk)

            chunk_id = hashlib.sha256(
                f"{path.name}:{i + j}:{chunk[:64]}".encode()
            ).hexdigest()[:32]

            vectors.append(
                {
                    "id": chunk_id,
                    "values": emb,
                    "metadata": {
                        "college": settings.COLLEGE_SHORT_NAME,
                        "source": source_label,
                        "year": year,
                        "filename": path.name,
                        "section": section,
                        "chunk_index": i + j,
                        "text": chunk[:2000],
                    },
                }
            )

        index.upsert(vectors=vectors)
        total += len(vectors)

    print(f"✅ Ingested {total} chunks from {path.name}")
    return total



def ingest_directory(
    docs_dir: str | Path,
    source_label: str = "document",
    year: int = 2025,
) -> int:
    """Ingest all supported files from a directory."""
    docs_path = Path(docs_dir)
    if not docs_path.is_dir():
        raise FileNotFoundError(f"Directory not found: {docs_dir}")

    supported = {".txt", ".md", ".markdown", ".pdf", ".docx", ".xlsx", ".xls", ".csv"}
    total = 0

    for fpath in sorted(docs_path.iterdir()):
        if fpath.suffix.lower() in supported:
            total += ingest_file(fpath, source_label, year)

    print(f"\n🎉  Total chunks ingested: {total}")
    return total


# ── CLI ───────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(description="Ingest documents into Pinecone")
    parser.add_argument(
        "--docs-dir",
        type=str,
        default="docs",
        help="Path to directory containing documents to ingest",
    )
    parser.add_argument("--source", type=str, default="document")
    parser.add_argument("--year", type=int, default=2025)
    args = parser.parse_args()

    ingest_directory(args.docs_dir, args.source, args.year)


if __name__ == "__main__":
    main()
