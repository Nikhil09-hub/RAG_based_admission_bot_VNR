# Chunking Plan — VNRVJIET Admission Chatbot

## Goal

Create meaningful chunks from official admission documents.

Rules:

* One important topic = one chunk.
* Do not merge unrelated sections.
* Use section-wise chunking for normal sections.
* Use hybrid chunking only when one section is very long:

  * first split by heading
  * then split that same section into smaller chunks if needed
* Keep headings inside the chunk text.
* Store `document_type`, `section`, and `last_updated` as metadata.

---

# 1. Admission Procedure PDF

**File:** `Admission Procedure.pdf`
**Document Type:** `admission_procedure`
**Strategy:** Section-wise chunking

| Heading Found                          | Chunk Name                   |
| -------------------------------------- | ---------------------------- |
| Admission to First-Year B.Tech         | btech_admission_overview     |
| Category-A / Convenor Quota            | convener_quota               |
| Category-B / Management Quota          | management_quota             |
| Spot Admission Procedure for B.Tech    | btech_spot_admission         |
| FN / OCI / CIWG Supernumerary Seats    | international_admission      |
| Lateral Entry B.Tech Admission         | lateral_entry                |
| Lateral Entry Spot Admission           | lateral_entry_spot_admission |
| Postgraduate Admission                 | pg_admission                 |
| M.Tech and MCA Category-A / Category-B | pg_quota_admission           |
| PG Spot Admission Procedure            | pg_spot_admission            |
| Official Websites and Contact Details  | admission_contact_details    |

---

# 2. Hostel Brochure PDF

**File:** `VNRVJIET-Hostel-Brochure-2026-27.pdf`
**Document Type:** `hostel`
**Strategy:** Section-wise chunking

| Heading Found                 | Chunk Name                |
| ----------------------------- | ------------------------- |
| Hostel Overview               | hostel_overview           |
| Food                          | food_and_mess             |
| Hostel Facilities             | hostel_facilities         |
| Security                      | hostel_security           |
| Sports and Fitness            | sports_and_fitness        |
| Training and Learning Centres | training_learning_centres |
| Entertainment                 | hostel_entertainment      |
| Miscellaneous                 | hostel_miscellaneous      |
| Contact Details               | hostel_contact_details    |

---

# 3. Placement Brochure PDF

**File:** `VNRVJIET-Placement-Brochure-2026-27.pdf`
**Document Type:** `placements`
**Strategy:** Hybrid chunking

| Heading Found                          | Chunk Name                |
| -------------------------------------- | ------------------------- |
| Training and Placement Cell Details    | placement_cell_contact    |
| About VNRVJIET Training and Placements | placement_about           |
| Courses Offered                        | placement_courses         |
| Training and Placement Committee       | placement_committee       |
| Career Vision Approach                 | career_vision_approach    |
| Training Roadmap for 4 Years           | training_roadmap          |
| Industry Collaborations and MOUs       | industry_collaborations   |
| Recruiters                             | recruiters                |
| Internship                             | internships               |
| Contact Information                    | placement_contact_details |

**Long sections that may need smaller chunks:**

| Parent Section                   | Child Chunk Suggestions                                                              |
| -------------------------------- | ------------------------------------------------------------------------------------ |
| Career Vision Approach           | first_year_training, second_year_training, third_year_training, fourth_year_training |
| Training Roadmap                 | year_wise_training_roadmap                                                           |
| Industry Collaborations and MOUs | collaboration_examples, mou_details                                                  |
| Recruiters                       | recruiter_list                                                                       |
| Internship                       | internship_process, internship_support                                               |

---

# 4. Institute Brochure PDF

**File:** `VNRVJIET-Institute-Brochure-2026-27.pdf`
**Document Type:** `institute_brochure`
**Strategy:** Hybrid chunking

| Heading Found                                 | Chunk Name               |
| --------------------------------------------- | ------------------------ |
| About VNRVJIET                                | about_vnrvjiet           |
| Why Students Choose VNRVJIET                  | why_choose_vnrvjiet      |
| Programmes / Courses Offered                  | programmes_offered       |
| B.Tech Programmes                             | btech_programmes         |
| M.Tech Programmes                             | mtech_programmes         |
| MCA Programme                                 | mca_programme            |
| Ph.D. Programmes                              | phd_programmes           |
| Research and Development                      | research_and_development |
| Campus Life                                   | campus_life              |
| Extra-Curricular and Co-Curricular Activities | student_activities       |
| Placements                                    | placement_highlights     |
| International Students                        | international_students   |

**Long sections that may need smaller chunks:**

| Parent Section           | Child Chunk Suggestions                                            |
| ------------------------ | ------------------------------------------------------------------ |
| Programmes Offered       | btech_programmes, mtech_programmes, mca_programme, phd_programmes  |
| Campus Life              | clubs, events, sports, student_development                         |
| Research and Development | research_labs, startups, patents, collaborations                   |
| Placements               | placement_statistics, recruiters, package_highlights               |
| International Students   | fn_eligibility, oci_eligibility, ciwg_eligibility, required_proofs |

---

# Metadata Design

Every chunk should contain:

```json
{
  "filename": "Admission Procedure.pdf",
  "source": "admissions_docs",
  "year": 2026,
  "document_type": "admission_procedure",
  "section": "convener_quota",
  "chunk_index": 0,
  "last_updated": "2026-06-22T19:30:00+05:30"
}
```

Possible `document_type` values:

```text
admission_procedure
hostel
placements
institute_brochure
fees
cutoffs
seat_intake
nri_admission
```

---

# Final Chunking Strategy Summary

| Document                | Strategy              |
| ----------------------- | --------------------- |
| Admission Procedure PDF | Section-wise chunking |
| Hostel Brochure PDF     | Section-wise chunking |
| Placement Brochure PDF  | Hybrid chunking       |
| Institute Brochure PDF  | Hybrid chunking       |

## Hybrid Chunking Rule

```text
Heading detected
↓
Keep the heading section separate
↓
If section is short → one chunk
↓
If section is long → split only that section into smaller chunks
↓
Keep the same heading in every child chunk
```
