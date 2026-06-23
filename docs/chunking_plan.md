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
# 1. Official Notice TXT

**File:** `official_notice.txt`
**Document Type:** `admission_notice`
**Strategy:** Section-wise chunking

| Heading Found                 | Chunk Name                    |
|-------------------------------|-------------------------------|
| ATTENTION                     | fraud_warning_notice          |
| FRAUD REPORTING ONLY          | fraud_reporting_contact       |
| IMPORTANT CONTACT INFORMATION | admission_contact_information |
| General Admission Inquiries   | general_admission_contacts    |
| Office Telephone & Address    | institute_contact_details     |
| ADMISSIONS POLICY             | admission_policy              |
| BEWARE OF FRAUDSTERS          | fraud_prevention_guidelines   |

---
# 2. Department Websites TXT

**File:** `department_websites.txt`
**Document Type:** `department_websites`
**Strategy:** Section-wise chunking

| Heading Found | Chunk Name |
|----------------------------------------------|----------------------------------|
| Computer Science & Engineering (CSE) Department                  | cse_department |
| CSE (Artificial Intelligence, Machine Learning & IoT) Department |cse_aiml_iot_department |
| CSE (Data Science & Cyber Security) Department                   | cse_ds_cys_department |
| Information Technology (IT) Department                           | it_department |
| Electronics & Communication Engineering (ECE) Department         | ece_department |
| Electrical & Electronics Engineering (EEE) Department            | eee_department |
| Electronics & Instrumentation Engineering (EIE) Department       | eie_department |
| Mechanical Engineering Department                                | mechanical_department |
| Civil Engineering Department                                     | civil_department |
| Automobile Engineering Department                                | automobile_department |
| Biotechnology Department                                         | biotechnology_department |
| Chemistry Department                                             | chemistry_department |
| Physics Department                                               | physics_department |
| English (Humanities) Department                                  | humanities_english_department |
| Mathematics & Management Sciences Department                    | mathematics_management_department |
| General Departments Overview Page                                 | departments_overview |
| HOW TO USE THESE LINKS                                            | website_usage_guidelines |
| CONTACT INFORMATION                                               | department_contact_information |

---
# 3. Hostel Information TXT

**File:** `hostel_information.txt`
**Document Type:** `hostel_information`
**Strategy:** Section-wise chunking

| Heading Found | Chunk Name |
|----------------------------------|----------------------------------|
| GENERAL INFORMATION | hostel_general_information |
| OFFICIAL HOSTEL DOCUMENTS | hostel_documents |
| FOOD & DINING FACILITIES | hostel_food_dining |
| SECURITY & SAFETY | hostel_security_safety |
| SPORTS & FITNESS | hostel_sports_fitness |
| MEDICAL & UTILITIES | hostel_medical_utilities |
| TRAINING & LEARNING FACILITIES | hostel_training_learning |
| ENTERTAINMENT & RECREATION | hostel_entertainment |
| ADDITIONAL FACILITIES | hostel_additional_facilities |
| FEE STRUCTURE (2025-26) | hostel_fee_structure |
| CONTACT DETAILS | hostel_contact_details |
| DOWNLOAD OFFICIAL DOCUMENTS | hostel_download_links |

---
# 4. Training & Placements TXT

**File:** `training_placements.txt`
**Document Type:** `training_placements`
**Strategy:** Hybrid chunking

| Heading Found | Chunk Name |
|----------------------------------|----------------------------------|
| VISION | placement_vision |
| MISSION | placement_mission |
| TRAINING OBJECTIVES | training_objectives |
| PLACEMENT OBJECTIVES | placement_objectives |
| INTEGRATED MENTORING MODEL | mentoring_model |
| STUDENT ELIGIBILITY FOR CAMPUS PLACEMENT | placement_eligibility |
| FINISHING SCHOOL | finishing_school |
| CAMPUS PLACEMENT STATISTICS | placement_statistics |
| INTERNSHIP HIGHLIGHTS | internship_highlights |
| INDUSTRY TRAINING PROGRAM OUTCOMES | industry_training_outcomes |
| TRAINING ROADMAP | training_roadmap |
| SCHOLARSHIP | scholarship_details |
| MAJOR MoUs | industry_mous |
| PROGRAMS OFFERED | academic_programs |
| AWARDS & RECOGNITION | awards_recognition |

**Long sections that may need smaller chunks:**

| Parent Section | Child Chunk Suggestions |
|----------------------------------|----------------------------------|
| CAMPUS PLACEMENT STATISTICS | placement_stats_2022_23, placement_stats_2021_22, placement_stats_2020_21, placement_stats_2019_20, placement_stats_2018_19, international_placement |
| INTERNSHIP HIGHLIGHTS | internship_companies, internship_stipends |
| INDUSTRY TRAINING PROGRAM OUTCOMES | google_cloud_training, amazon_wow, microsoft_engage, industry_certifications |
| TRAINING ROADMAP | first_year_training, second_year_training, third_year_training, fourth_year_training |
| PROGRAMS OFFERED | ug_programs, pg_programs |

---
# 5. Academic Programs & Intake TXT

**File:** `academic_programs_intake.txt`
**Document Type:** `academic_programs`
**Strategy:** Hybrid chunking

| Heading Found | Chunk Name |
|----------------------------------|----------------------------------|
| Admission Key Information | admission_key_information |
| B.Tech Programmes and Intake Capacity | btech_programs |
| Branch Categories | branch_categories |
| Oldest Programmes (Established 1995) | oldest_programs |
| Newest Programmes (Established 2025) | newest_programs |
| Popular Branches with High Intake | popular_branches |
| M.Tech Programmes Offered at VNRVJIET | mtech_programs |
| M.Tech Programmes by Department | mtech_department_wise |
| Oldest M.Tech Programmes | oldest_mtech_programs |
| Newest M.Tech Programmes | newest_mtech_programs |
| Popular M.Tech Programmes with High Intake | popular_mtech_programs |
| MCA Programme (Master of Computer Applications) | mca_programme |
| Key Curriculum Areas | mca_curriculum |
| Career Opportunities | mca_careers |
| Postgraduate Programmes Summary | postgraduate_summary |

**Long sections that may need smaller chunks:**

| Parent Section | Child Chunk Suggestions |
|----------------------------------|----------------------------------|
| B.Tech Programmes and Intake Capacity | btech_cse, btech_cse_aiml, btech_cse_ds, btech_cse_cybersecurity, btech_it, btech_ece, btech_eee, btech_mechanical, btech_civil, btech_automobile, btech_aids, btech_biotechnology, btech_vlsi, btech_rai, btech_eie, btech_csbs, btech_iot |
| Branch Categories | core_engineering_branches, cs_specializations, emerging_technologies, specialized_engineering |
| M.Tech Programmes Offered at VNRVJIET | mtech_structural_engineering, mtech_embedded_systems, mtech_vlsi, mtech_cse, mtech_software_engineering, mtech_cnis, mtech_power_systems, mtech_power_electronics, mtech_geotechnical, mtech_highway, mtech_cadcam, mtech_advanced_manufacturing, mtech_eie, mtech_aids, mtech_data_science |
| M.Tech Programmes by Department | mtech_ce_programs, mtech_me_programs, mtech_eee_programs, mtech_ece_programs, mtech_cse_programs, mtech_it_programs, mtech_eie_programs, mtech_ai_ds_programs |
| MCA Programme | mca_overview, mca_duration_intake, mca_department |
| Key Curriculum Areas | mca_programming, mca_software_development, mca_database_systems, mca_web_cloud, mca_algorithms, mca_emerging_technologies, mca_practical_training |
| Career Opportunities | mca_career_roles |

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