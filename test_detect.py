def detect_section(chunk_text: str) -> str:

    if "Category-A" in chunk_text:
        return "convener_quota"

    elif "Category-B" in chunk_text:
        return "management_quota"

    elif "FN / OCI / CIWG" in chunk_text:
        return "international_admission"

    elif "Lateral Entry" in chunk_text:
        return "lateral_entry"

    return "general"


sample = """
Category-B admissions are offered through management quota
"""

print(detect_section(sample))