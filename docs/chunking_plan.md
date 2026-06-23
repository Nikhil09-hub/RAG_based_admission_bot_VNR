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


# Category A Reporting Flowchart – Admissions 2025

**File:** `Category A Reporting Flowchart – Admissions 2025`
**Document Type:** `category_a_reporting_flowchart`
**Strategy:** Section-wise chunking

| Heading Found                                       | Chunk Name                                   |
|-----------------------------------------------------|----------------------------------------------|
| Overview, branch code, application fee, refund rule | category_a_admission_overview                |
| Mandatory documents list                            | category_a_mandatory_documents               |
| Reserved-category and additional documents          | category_a_special_category_documents        |
| General document instructions                       | category_a_document_submission_notes         |
| Step 1: Scanning documents and Google Form          | category_a_step1_google_form_submission      |
| Step 2: Eduprime Reporting                          | category_a_step2_eduprime_reporting          |
| Step 2: Printed acknowledgement pages               | category_a_step2_acknowledgement_pages       |
| Step 3: Fee Payment                                 | category_a_step3_fee_payment                 |
| Step 4: Receipt and Temporary ID Card               | category_a_step4_acknowledgement_and_temp_id |
| Temporary ID instructions                           | category_a_temporary_id_instructions         |


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


# Eligibility Criteria for FN / OCI / CIWG Category

**File:** `Eligibility Criteria for FN OCI CIWG Category`  
**Document Type:** `international_admission_eligibility`  
**Strategy:** Section-wise chunking  

| Heading Found | Chunk Name | Chunk Details |
|---|---|---|
| Quota applicability, eligible programmes, and application fee | `fn_oci_ciwg_admission_overview` | Contains that FN / OCI / CIWG supernumerary quota is only for B.Tech admissions, not for M.Tech or MCA, along with B.Tech and M.Tech application fees and the non-refundable fee rule. |
| OCI Card Holder eligibility | `oci_eligibility_and_documents` | Contains OCI eligibility condition and required proof: student passport and OCI card. |
| CIWG category eligibility | `ciwg_eligibility_and_documents` | Contains CIWG eligibility condition: parent working in a GCC country with valid visa, work permit, or residence permit applicable to the admission year. |
| GCC countries list | `ciwg_gcc_countries` | Contains the GCC country names: Bahrain, Kuwait, Oman, Qatar, Saudi Arabia, and the United Arab Emirates. |
| Foreign National eligibility | `foreign_national_eligibility_and_documents` | Contains eligibility for foreign citizens who completed education abroad and required proof: student passport, educational records, visa documents, and parents’ passports. |


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


# Course Intake Distribution

**File:** `Course Intake Distribution`  
**Document Type:** `course_intake_distribution`  
**Strategy:** Table-aware section-wise chunking  

| Heading Found | Chunk Name | Chunk Details |
|---|---|---|
| Application fees and non-refundable rule | `course_intake_application_fees` | Contains B.Tech application fee ₹2,000, M.Tech application fee ₹1,000, and the non-refundable fee condition. |
| Branch codes | `course_intake_branch_codes` | Contains B.Tech EAPCET branch code `VJEC` and M.Tech/MCA branch code `VJEC1`. |
| B.Tech admission quotas | `btech_admission_quota_distribution` | Contains B.Tech seat distribution: Category-A/Convenor quota 70%, Management quota 30%, Management split into Category-B and NRI, and FN/OCI/CIWG supernumerary seats. |
| M.Tech admission quotas | `mtech_admission_quota_distribution` | Contains M.Tech Category-A quota 70%, Management quota 30%, Category-B and NRI details, and that supernumerary quota is not applicable for M.Tech/MCA. |
| Course intake table — Civil to ECE | `course_intake_table_core_branches` | Contains course codes, total intake, management seats, Category-B seats, and NRI seats for Civil, EEE, Mechanical, and ECE. |
| Course intake table — CSE to CSE Cyber Security | `course_intake_table_computing_branches` | Contains intake distribution for CSE, EIE, IT, Automobile, CSBS, CSE Data Science, CSE AIML, and CSE Cyber Security. |
| Course intake table — CSE IoT to Robotics and AI | `course_intake_table_specialized_branches` | Contains intake distribution for CSE IoT, AI & Data Science, Biotechnology, VLSI Design and Technology, and Robotics & AI. |
| Overall intake totals | `course_intake_totals` | Contains total intake, total management seats, total Category-B seats, and total NRI seats across all B.Tech branches. |


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


# VNRVJIET Admissions, Fees, Facilities and General Information

**File:** `VNRVJIET General Admission Information`  
**Document Type:** `vnrvjiet_general_admission_information`  
**Strategy:** Section-wise chunking with table-aware chunking for NRI programme fees and FAQ-wise chunking.

| Heading Found | Chunk Name | Chunk Details |
|---|---|---|
| About VNRVJIET | `vnrvjiet_about_institute` | Contains institute location, establishment year, JNTUH affiliation, AICTE approval, autonomous status, NAAC grade, and NBA accreditation details. |
| Application Fee | `vnrvjiet_application_fees` | Contains B.Tech and M.Tech application fees and the non-refundable fee note. |
| Admission Process – B.Tech: Category-A | `btech_category_a_admission_process` | Contains Category-A / Convenor quota seat percentage, TS EAPCET counselling process, TSCHE role, and EAPCET code `VJEC`. |
| Admission Process – B.Tech: Management | `btech_management_admission_process` | Contains Management quota seat percentage, Category-B and NRI routes, TS EAPCET/JEE Main basis, and direct application instructions. |
| Admission Process – B.Tech: FN / OCI / CIWG | `btech_supernumerary_admission_process` | Contains supernumerary admission information, eligible categories, GCC criteria, NRI/FN/OCI fee range, admissions contact details, and no-agent warning. |
| Admission Process – M.Tech / MCA | `mtech_mca_admission_process` | Contains M.Tech/MCA branch code `VJEC1`, Category-A and Management quota distribution, entrance examinations, and supernumerary quota restriction. |
| Eligibility Criteria | `btech_admission_eligibility_criteria` | Contains required Intermediate subjects, aggregate percentage criteria, TS EAPCET/JEE score requirement, and Telangana domicile requirement for Convenor quota. |
| Documents Required for Admission | `general_admission_documents_required` | Contains common admission document checklist including rank card, certificates, TC, Aadhaar, photos, study certificates, and category-related documents. |
| Fee Structure – B.Tech, M.Tech, MCA, Hostel | `general_fee_structure_2025_26` | Contains B.Tech Convenor fee, M.Tech fee, MCA fee, hostel fee, miscellaneous fee note, reimbursement information, and non-refundable rule. |
| Lateral Entry Fee Structure | `lateral_entry_fee_structure` | Contains Diploma-to-B.Tech lateral-entry fee, link to Category-A fee, TAFRC regulation note, and non-refundable condition. |
| Transportation Fee | `transportation_fee_information` | Contains first-year and senior-year B.Tech transportation fee document links. |
| Scholarships | `vnrvjiet_scholarships` | Contains Telangana reimbursement, Central Sector, Post-Matric, merit-based, and National Merit scholarship information. |
| Campus Facilities | `vnrvjiet_campus_facilities` | Contains campus size, labs, library, Wi-Fi, sports, auditorium, cafeteria, and medical facility details. |
| Hostel Information | `vnrvjiet_hostel_information` | Contains boys’ and girls’ hostel availability, rooms, security, mess, laundry, Wi-Fi, study table, chair, and lockers. |
| NRI B.Tech Programme Fees: $5000 branches | `nri_btech_fee_5000_branches` | Contains branch-wise NRI fees for CSE and allied branches, ECE, IT, VLSI, Biotechnology, and Robotics & AI programmes charged at $5000 per annum. |
| NRI B.Tech Programme Fees: $3500 and $3000 branches | `nri_btech_fee_other_branches` | Contains Civil, EEE, Mechanical fees at $3500 and Automobile/EIE fees at $3000 per annum. |
| Fee Conversion Reference | `nri_fee_currency_conversion_note` | Contains exchange-rate-based fee conversion note and warning that branch-wise fees may change by academic year. |
| Placement Highlights | `vnrvjiet_placement_highlights` | Contains placement rate, recruiters, highest package, average package, company visits, and placement cell information. |
| Contact Information | `vnrvjiet_contact_information` | Contains campus address, phone numbers, admissions email, and official website. |
| Official Social Media and Resources | `vnrvjiet_official_social_links` | Contains official website, Facebook, Instagram, LinkedIn, and purpose of social media updates. |
| FAQ: College quality and accreditations | `faq_vnrvjiet_college_quality` | Answers whether VNRVJIET is a good college and includes accreditation information. |
| FAQ: Branch codes | `faq_vnrvjiet_branch_codes` | Answers EAPCET B.Tech code `VJEC` and M.Tech/MCA code `VJEC1`. |
| FAQ: Hostel requirement | `faq_vnrvjiet_hostel_mandatory` | Answers whether hostel is compulsory. |
| FAQ: JEE Main acceptance | `faq_vnrvjiet_jee_main_acceptance` | Answers whether JEE Main is accepted for Management admissions. |
| FAQ: Nearest metro | `faq_vnrvjiet_nearest_metro` | Contains nearest metro station information and approximate distance from campus. |

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



# VNRVJIET Hostel Rules and Regulations

**File:** `VNRVJIET Hostel Rules and Regulations`  
**Document Type:** `hostel_rules_and_regulations`  
**Strategy:** Section-wise chunking  

| Heading Found | Chunk Name | Chunk Details |
|---|---|---|
| Student Information Requirements | `hostel_student_information_requirements` | Contains parent/guardian contact details, permanent-address update requirement, and hostel ID card requirement. |
| Discipline and Conduct | `hostel_discipline_and_conduct_rules` | Contains room cleanliness, noise restrictions, wall posters prohibition, college-hour room stay rule, room exchange restriction, party prohibition, games restriction, and Warden/Principal authority. |
| Fees and Accommodation | `hostel_fees_and_accommodation_rules` | Contains hostel fee payment timing, renewal based on semester performance, possible fee revision, and room handover process at year end. |
| Anti-Ragging Policy | `hostel_anti_ragging_policy` | Contains ragging prohibition and the statement that ragging is a criminal offence. |
| Prohibited Items and Activities | `hostel_prohibited_items_and_activities` | Contains alcohol, drugs, gutka, tobacco, cigarettes, sedative materials, outside food, food wastage, mess timing rules, and vehicle restrictions. |
| Visitors and Leave Policy | `hostel_visitors_and_leave_policy` | Contains guest restrictions, parent/local guardian visiting days, visiting hours, advance leave application, written permission, and stay-address requirement. |
| Security and Inspection | `hostel_security_and_inspection_policy` | Contains personal belongings responsibility disclaimer, inspection rights for rooms/bags/almirahs, and accident responsibility disclaimer. |
| Damage and Penalties | `hostel_damage_and_penalty_rules` | Contains hostel property damage responsibility, individual or collective fines, penalties, and possible hostel expulsion. |

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