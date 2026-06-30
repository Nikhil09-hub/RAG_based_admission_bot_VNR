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

# 2. Campus Life TXT

**File:** `Campus_Life.txt`  
**Document Type:** `campus_life`  
**Strategy:** Section-wise chunking

| Heading Found | Chunk Name |
|---------------|------------|
| Professional Chapters / Societies | professional_chapters |
| Clubs | student_clubs |
| Campus Celebrations | campus_celebrations |

### Detailed Chunk Mapping

| Section / Topic | Chunk Name |
|----------------|------------|
| ACM | acm_chapter |
| ASME | asme_chapter |
| CSI | csi_chapter |
| Diurnalis | diurnalis_chapter |
| GSDC | gsdc_chapter |
| ICI | ici_chapter |
| IEEE | ieee_chapter |
| IEI | iei_chapter |
| IGBC | igbc_chapter |
| Art of Living | art_of_living_club |
| CANDLEVES | candleves_club |
| Nrithya Tarang | nrithya_tarang_club |
| Creative Arts | creative_arts_club |
| Crescendo | crescendo_club |
| Dramatrix | dramatrix_club |
| Data Questers Club | data_questers_club |
| Livewire | livewire_club |
| Kritomedh | kritomedh_club |
| N Army | n_army_club |
| NSS | nss_club |
| Scintillate | scintillate_club |
| Social Media Club | social_media_club |
| Stentorian | stentorian_club |
| Vignana Jyothi | vignana_jyothi_club |
| Sahithi Vanam | sahithi_vanam_club |
| VJ Theatro | vj_theatro |
| VJ Spectral Pyramid | vj_spectral_pyramid |
| VJ ARC | vj_arc |
| VNRSF | vnrsf |
| Electoral Literacy Club | electoral_literacy_club |
| Annual Day | annual_day |
| Convergence | convergence |
| Cultural Day | cultural_day |
| Ecficio | ecficio |
| National Engineers Day | engineers_day |
| ICMACC | icmacc |
| International Women's Day | womens_day |
| International Yoga Day | yoga_day |
| National Mathematics Day | mathematics_day |
| Open House | open_house |
| Sintillashunz | sintillashunz |
| Sports Fest | sports_fest |
| National Science Day | science_day |
| National Teachers Day | teachers_day |
| National Technology Day | technology_day |
| Republic Day | republic_day |
| Independence Day | independence_day |
| Traditional Day | traditional_day |
| TEDx VNRVJIET | tedx_vnrvjiet |
| World IP Day | world_ip_day |
| World Environment Day | environment_day |
| World Water Day | water_day |

**Long sections that may need smaller chunks:**

| Parent Section | Child Chunk Suggestions |
|----------------|------------------------|
| Professional Chapters / Societies | acm_chapter, asme_chapter, csi_chapter, ieee_chapter, iei_chapter, gsdc_chapter |
| Clubs | technical_clubs, cultural_clubs, service_clubs, literary_clubs, media_clubs |
| Campus Celebrations | academic_events, cultural_events, national_days, international_days |
| Clubs (large section) | arts_and_music_clubs, technical_clubs, social_service_clubs, communication_clubs |
| Campus Celebrations (large section) | annual_festivals, awareness_days, departmental_events, national_celebrations |

---
# 3. Category A Reporting Flowchart – Admissions 2026

**File:** `Category A Reporting Flowchart – Admissions 2026`
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

# 4. Department Websites TXT

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


# 5. Department Overview TXT

**File:** `Department_Overview.txt`
**Document Type:** `departments`
**Strategy:** Department-wise chunking

| Heading Found | Chunk Name |
|---------------|------------|
| Automobile Engineering Department | automobile_engineering |
| Chemistry Department | chemistry_department |
| Civil Engineering Department | civil_engineering |
| Biotechnology Department | biotechnology_department |
| Computer Science & Engineering Department | cse_department |
| AI & ML / IoT Branch | ai_ml_iot |
| Cyber Security / Data Science / AI&DS Branch | cybersecurity_datascience |
| Electrical & Electronics Engineering Department | eee_department |
| Electronics & Communication Engineering Department | ece_department |
| Electronics Engineering (VLSI Design & Technology) | vlsi_department |
| English Department | english_department |
| Information Technology Department | it_department |
| Mathematics & Management Sciences Department | mathematics_management |
| Mechanical Engineering Department | mechanical_engineering |
| Physics Department | physics_department |

## Detailed Chunk Mapping

| Section / Topic | Chunk Name |
|----------------|------------|
| Automobile Programs | automobile_programs |
| Automobile Labs & Infrastructure | automobile_labs |
| Automobile Industry Collaborations | automobile_industry |
| Chemistry Courses | chemistry_courses |
| Chemistry Research Activities | chemistry_research |
| Chemistry Infrastructure | chemistry_infrastructure |
| Civil Programs | civil_programs |
| Civil Laboratories | civil_labs |
| Civil Research & Consulting | civil_research |
| Biotechnology Programs | biotechnology_programs |
| Biotechnology Focus Areas | biotechnology_specializations |
| Biotechnology Labs | biotechnology_labs |
| Biotechnology Career Paths | biotechnology_careers |
| CSE Programs | cse_programs |
| CSE Infrastructure | cse_infrastructure |
| CSE Research & Industry | cse_research |
| AI & DS Program | ai_ds_program |
| AI & ML Curriculum | ai_ml_curriculum |
| AI & ML Labs | ai_ml_labs |
| Cyber Security Program | cyber_security_program |
| Data Science Program | data_science_program |
| Cyber Security Labs | cyber_security_labs |
| EEE Programs | eee_programs |
| EEE Facilities | eee_labs |
| EEE Research Areas | eee_research |
| ECE Programs | ece_programs |
| ECE Laboratories | ece_labs |
| ECE Placements | ece_placements |
| ECE Research & Patents | ece_research |
| VLSI Program | vlsi_program |
| VLSI Infrastructure | vlsi_labs |
| Semiconductor Industry Focus | semiconductor_industry |
| English Curriculum | english_curriculum |
| English Research | english_research |
| Communication Skills Training | communication_skills |
| IT Programs | it_programs |
| IT Infrastructure | it_labs |
| IT Curriculum | it_curriculum |
| Mathematics Courses | mathematics_courses |
| Management Courses | management_courses |
| Analytics & Business Studies | analytics_business |
| Mechanical Programs | mechanical_programs |
| Mechanical Laboratories | mechanical_labs |
| Mechanical Research | mechanical_research |
| Mechanical Placements | mechanical_placements |
| Physics Courses | physics_courses |
| Physics Laboratories | physics_labs |
| Physics Research | physics_research |

### Long Sections that may need smaller chunks

| Parent Section | Child Chunk Suggestions |
|----------------|------------------------|
| Computer Science & Engineering Department | cse_programs, cse_infrastructure, cse_research, cse_industry_collaborations |
| Electronics & Communication Engineering Department | ece_programs, ece_labs, ece_placements, ece_research, ece_patents |
| Mechanical Engineering Department | mechanical_programs, mechanical_labs, mechanical_research, mechanical_placements |
| Civil Engineering Department | civil_programs, civil_labs, civil_research, civil_consulting |
| Biotechnology Department | biotechnology_specializations, biotechnology_labs, biotechnology_industry, biotechnology_careers |
| AI & ML / IoT Branch | ai_ml_curriculum, deep_learning, computer_vision, iot_projects |
| Cyber Security / Data Science Branch | cyber_security_curriculum, ethical_hacking, machine_learning, big_data |
| Mathematics & Management Sciences Department | mathematics_courses, management_courses, analytics_business |
| ECE Department | vlsi_research, embedded_systems, communication_systems, semiconductor_training |

---
# 6. Eligibility Criteria for FN / OCI / CIWG Category

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
# 7. Hostel Information TXT

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
| FEE STRUCTURE (2026-27) | hostel_fee_structure |
| CONTACT DETAILS | hostel_contact_details |
| DOWNLOAD OFFICIAL DOCUMENTS | hostel_download_links |

# 8. NRI / FN / OCI / CIWG Admissions TXT

**File:** `NRI_FN_OCI_CIWG_Admissions.txt`
**Document Type:** `international_admissions`
**Strategy:** Hybrid Chunking (Section-wise + Topic-wise)

| Heading Found | Chunk Name |
|---------------|------------|
| Application Fee | application_fee |
| Branch Codes | branch_codes |
| Seat Category | seat_categories |
| Fee Structure (FY 2065-27) | nri_fee_structure |
| Eligibility Criteria | eligibility_criteria |
| Documents Required | required_documents |
| Admission Process | admission_process |
| NRI Seats Available (Branchwise) | nri_seat_matrix |
| Important Notice (Anti-Fraud) | anti_fraud_notice |

## Detailed Chunk Mapping

| Section / Topic | Chunk Name |
|----------------|------------|
| B.Tech Application Fee | btech_application_fee |
| M.Tech Application Fee | mtech_application_fee |
| Fee Refund Policy | fee_refund_policy |
| EAPCET Branch Code | eapcet_branch_code |
| M.Tech / MCA Branch Code | pg_branch_code |
| Convenor / Category-A Quota | category_a_quota |
| Management Quota | management_quota |
| NRI Quota | nri_quota |
| FN / OCI / CIWG Supernumerary Seats | supernumerary_quota |
| B.Tech Fee Structure ($5000 Category) | fee_structure_tier1 |
| B.Tech Fee Structure ($3500 Category) | fee_structure_tier2 |
| B.Tech Fee Structure ($3000 Category) | fee_structure_tier3 |
| Exchange Rate Reference | exchange_rate_reference |
| OCI Eligibility | oci_eligibility |
| CIWG Eligibility | ciwg_eligibility |
| Foreign National Eligibility | foreign_national_eligibility |
| Passport Requirements | passport_documents |
| Academic Certificates | academic_documents |
| Migration & Transfer Certificates | migration_documents |
| Admission Contact Details | admission_contact |
| Admission Guidance Process | admission_guidance |
| Branch-wise NRI Seat Availability | branchwise_nri_seats |
| Anti-Fraud Warning | anti_fraud_warning |
| Fraud Reporting Contact | fraud_reporting_contact |

### Fee Structure Child Chunks

| Parent Section | Child Chunk Suggestions |
|----------------|------------------------|
| Fee Structure (FY 2026-27) | premium_branches_fee, core_branches_fee, special_branches_fee |
| Tier-1 Fee Group ($5000) | cse_related_branches_fee, ai_ds_fee, ece_fee, it_fee |
| Tier-2 Fee Group ($3500) | civil_fee, eee_fee, mechanical_fee |
| Tier-3 Fee Group ($3000) | automobile_fee, eie_fee |

### Eligibility Child Chunks

| Parent Section | Child Chunk Suggestions |
|----------------|------------------------|
| Eligibility Criteria | oci_eligibility, ciwg_eligibility, foreign_national_eligibility |
| OCI Category | oci_documents, oci_requirements |
| CIWG Category | gulf_country_requirements, ciwg_documents |
| Foreign Nationals | fn_documents, fn_requirements |

### Documents Child Chunks

| Parent Section | Child Chunk Suggestions |
|----------------|------------------------|
| Documents Required | identity_documents, academic_documents, migration_documents |
| Identity Documents | passport, oci_card, visa_permit, aadhar |
| Academic Documents | tenth_marks_memo, twelfth_marks_memo, transfer_certificate |
| Supporting Documents | photographs, migration_certificate |

### NRI Seat Matrix Child Chunks

| Parent Section | Child Chunk Suggestions |
|----------------|------------------------|
| NRI Seats Available | cse_family_seats, core_branch_seats, emerging_technology_seats |
| CSE Family Branches | cse_seats, cse_ai_ml_seats, cse_ds_seats, cse_cys_seats, cse_iot_seats |
| Emerging Programs | aids_seats, csbs_seats, rai_seats, biotechnology_seats, vlsi_seats |
| Core Engineering Branches | ece_seats, eee_seats, mechanical_seats, civil_seats, automobile_seats, eie_seats |

### Long Sections that may need smaller chunks

| Parent Section | Child Chunk Suggestions |
|----------------|------------------------|
| Seat Category | category_a_quota, management_quota, nri_quota, supernumerary_quota |
| Fee Structure (FY 2026-27) | fee_structure_tier1, fee_structure_tier2, fee_structure_tier3 |
| Eligibility Criteria | oci_eligibility, ciwg_eligibility, foreign_national_eligibility |
| Documents Required | identity_documents, academic_documents, supporting_documents |
| NRI Seats Available | cse_family_seats, core_branch_seats, emerging_technology_seats |
| Important Notice (Anti-Fraud) | anti_fraud_warning, fraud_reporting_contact |

---
# 9. Course Intake Distribution

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
# 10. Training & Placements TXT

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

# 11. Admission Procedure TXT

**File:** `Admission_Procedure.txt`
**Document Type:** `admission_procedure`
**Strategy:** Section-wise Chunking

| Heading Found | Chunk Name |
|---------------|------------|
| Application Fees | application_fees |
| Admission to First Year – B.Tech Programme | btech_admission_overview |
| Category-A (Convenor Quota) | convenor_quota |
| Management Quota | management_quota |
| Spot Admission Procedure for B.Tech | btech_spot_admission |
| FN / OCI / CIWG Supernumerary Admissions | international_admission |
| Lateral Entry – Second Year B.Tech | lateral_entry |
| Lateral Entry Spot Admission Procedure | lateral_entry_spot_admission |
| Post Graduate Admissions (M.Tech & MCA) | pg_admission_overview |
| PG Fee Structure | pg_fee_structure |
| M.Tech & MCA Category-A Admissions | pg_convenor_quota |
| M.Tech & MCA Management Admissions | pg_management_quota |
| Spot Admission Procedure for M.Tech & MCA | pg_spot_admission |
| Important Links | admission_links |
| General Enquiry | admission_contact_details |

## Detailed Chunk Mapping

| Section / Topic | Chunk Name |
|----------------|------------|
| B.Tech Application Fee | btech_application_fee |
| M.Tech Application Fee | mtech_application_fee |
| Non-Refundable Fee Policy | fee_refund_policy |
| B.Tech Admission Process | btech_admission_process |
| EAPCET Branch Code (VJEC) | eapcet_branch_code |
| Category-A Seat Distribution | category_a_admission |
| Management Seat Distribution | management_admission |
| Category-B Admissions | category_b_admission |
| NRI Admissions | nri_admission |
| B.Tech Spot Admissions | btech_spot_admission_process |
| FN Admissions | foreign_national_admission |
| OCI Admissions | oci_admission |
| CIWG Admissions | ciwg_admission |
| Supernumerary Seat Policy | supernumerary_policy |
| TGECET Lateral Entry Admissions | tgecet_lateral_entry |
| Lateral Entry Spot Admissions | lateral_entry_spot_process |
| PG Admissions Overview | pg_admission_process |
| M.Tech Fee Structure | mtech_fee |
| MCA Fee Structure | mca_fee |
| TGPGECET Admissions | tgpgecet_admission |
| GATE Admissions | gate_admission |
| TGICET Admissions | tgicet_admission |
| PG Management Admissions | pg_management_admission |
| PG Spot Admissions | pg_spot_admission_process |
| Admission Websites | admission_websites |
| Convener Websites | convener_websites |
| Admission Contact Numbers | admission_phone_numbers |
| Admission Email | admission_email |

### Long Sections that may need smaller chunks

| Parent Section | Child Chunk Suggestions |
|----------------|------------------------|
| Admission to First Year – B.Tech Programme | btech_admission_process, convenor_quota, management_quota |
| FN / OCI / CIWG Supernumerary Admissions | foreign_national_admission, oci_admission, ciwg_admission, supernumerary_policy |
| Lateral Entry Admissions | tgecet_lateral_entry, lateral_entry_spot_process |
| Post Graduate Admissions | pg_admission_process, pg_fee_structure, pg_convenor_quota, pg_management_quota |
| Important Links | btech_links, lateral_entry_links, mtech_links, mca_links |
| General Enquiry | admission_phone_numbers, admission_email |

### Recommended Child Chunks for Better Retrieval

| Parent Chunk | Child Chunks |
|-------------|-------------|
| btech_admission_overview | category_a_admission, management_admission, btech_spot_admission_process |
| international_admission | foreign_national_admission, oci_admission, ciwg_admission |
| pg_admission_overview | tgpgecet_admission, gate_admission, tgicet_admission |
| admission_links | btech_links, lateral_entry_links, mtech_links, mca_links |
| admission_contact_details | admission_phone_numbers, admission_email |

---
# 12. VNRVJIET Admissions, Fees, Facilities and General Information

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
| Fee Structure – B.Tech, M.Tech, MCA, Hostel | `general_fee_structure_2026_27` | Contains B.Tech Convenor fee, M.Tech fee, MCA fee, hostel fee, miscellaneous fee note, reimbursement information, and non-refundable rule. |
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
# 13. Academic Programs & Intake TXT

**File:** `academic_programs_intake.txt`
**Document Type:** `academic_programs`
**Strategy:** Hybrid chunking

| Heading Found | Chunk Name |
|----------------------------------|----------------------------------|
| Admission Key Information | admission_key_information |
| B.Tech Programmes and Intake Capacity | btech_programs |
| Branch Categories | branch_categories |
| Oldest Programmes (Established 1995) | oldest_programs |
| Newest Programmes (Established 2026) | newest_programs |
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

# 14. College Overview TXT

**File:** `College_Overview.txt`
**Document Type:** `college_overview`
**Strategy:** Section-wise + Topic-wise Chunking

| Heading Found | Chunk Name |
|---------------|------------|
| Introduction | college_introduction |
| VNRVJIET At A Glance | institute_highlights |
| Research & Development | research_development |
| 2026 Placement Statistics | placement_statistics_2026 |
| Programmes Offered | programmes_offered |
| Extra-Curricular Activities | extracurricular_activities |
| Co-Curricular Activities | cocurricular_activities |
| Admission Quotas & Fees | admission_quotas_fees |
| Scholarships | scholarships |
| Foreign Admissions | foreign_admissions |
| Contact Emails | contact_emails |

## Detailed Chunk Mapping

| Section / Topic | Chunk Name |
|----------------|------------|
| Institute Overview | institute_overview |
| Student Strength | student_statistics |
| Faculty Strength | faculty_statistics |
| Alumni Network | alumni_statistics |
| Campus Infrastructure | campus_infrastructure |
| NAAC Accreditation | naac_accreditation |
| QS I-GAUGE Rating | qs_rating |
| AICTE-CII Rating | aicte_cii_rating |
| ISO Certification | iso_certification |
| Research Centres | research_centres |
| Academic & Research Labs | research_labs |
| Startup Ecosystem | startup_ecosystem |
| International Collaborations | international_collaborations |
| Industry Collaborations | industry_collaborations |
| Patent Statistics | patents_statistics |
| Research Publications | publications_statistics |
| Funded Projects | funded_projects |
| Placement Overview | placement_overview |
| Highest Packages | highest_packages |
| Placement Statistics | placement_statistics |
| Average CTC | average_ctc |
| B.Tech Programmes | btech_programmes |
| Minor Degree Programmes | minor_programmes |
| M.Tech Programmes | mtech_programmes |
| MCA Programme | mca_programme |
| PhD Programmes | phd_programmes |
| Technical Events | technical_events |
| Cultural Events | cultural_events |
| Sports Activities | sports_activities |
| Hackathons & Coding Contests | hackathons |
| Open House | open_house |
| Workshops & Conferences | workshops_conferences |
| B.Tech Admission Quotas | btech_admission_quota |
| PG Admission Quotas | pg_admission_quota |
| Fee Structure | fee_structure |
| Scholarships Information | scholarship_information |
| FN Admissions | fn_admissions |
| OCI Admissions | oci_admissions |
| CIWG Admissions | ciwg_admissions |
| Admission Eligibility | foreign_admission_eligibility |
| General Admission Email | admissions_email |
| International Admission Email | international_admissions_email |

### Programme Related Child Chunks

| Parent Section | Child Chunk Suggestions |
|----------------|------------------------|
| B.Tech Programmes | cse_related_programmes, core_engineering_programmes, emerging_technology_programmes |
| Minor Degree Programmes | ai_ml_minor, cyber_security_minor, data_science_minor, iot_minor, entrepreneurship_minor |
| M.Tech Programmes | cse_mtech, ece_mtech, civil_mtech, eee_mtech, mechanical_mtech |
| PhD Programmes | phd_ce, phd_cse, phd_ece, phd_eee, phd_me |

### Placement Related Child Chunks

| Parent Section | Child Chunk Suggestions |
|----------------|------------------------|
| Placement Statistics | placement_percentage, total_offers, highest_package, average_ctc |
| Highest Packages | rubrik_package, google_package |
| Offer Distribution | offers_above_10lpa, offers_above_6lpa |

### Research Related Child Chunks

| Parent Section | Child Chunk Suggestions |
|----------------|------------------------|
| Research & Development | patents_statistics, publications_statistics, funded_projects |
| Innovation Ecosystem | startup_ecosystem, incubatees, seed_funding |
| Collaborations | international_collaborations, industry_collaborations |

### Foreign Admission Child Chunks

| Parent Section | Child Chunk Suggestions |
|----------------|------------------------|
| Foreign Admissions | fn_admissions, oci_admissions, ciwg_admissions |
| Eligibility Criteria | foreign_admission_eligibility |
| Required Proof Documents | fn_documents, oci_documents, ciwg_documents |

### Long Sections That Need Smaller Chunks

| Parent Section | Child Chunk Suggestions |
|----------------|------------------------|
| Programmes Offered | btech_programmes, minor_programmes, mtech_programmes, mca_programme, phd_programmes |
| Research & Development | patents_statistics, publications_statistics, funded_projects |
| Placement Statistics | placement_overview, highest_packages, average_ctc |
| Admission Quotas & Fees | btech_admission_quota, pg_admission_quota, fee_structure |
| Foreign Admissions | fn_admissions, oci_admissions, ciwg_admissions |
| VNRVJIET At A Glance | accreditations, rankings, research_centres, collaborations |

---

# 15. VNRVJIET Hostel Rules and Regulations

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