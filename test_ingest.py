# test_ingest.py
print("SCRIPT STARTED")
from pathlib import Path
from app.rag.ingest import ingest_file

def main():
    file_path = Path("docs/txt/VNR_Admissions_Procedure.txt")

    print(f"\nTesting ingestion: {file_path.name}\n")

    chunks = ingest_file(
        file_path,
        source_label="admissions_docs",
        year=2026
    )

    print(f"\n✅ Total chunks ingested: {chunks}")

if __name__ == "__main__":
    main()