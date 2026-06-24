import re

def _section_aware_chunk(
    text,
    max_tokens=350,
    overlap_tokens=50
):
    sections = re.split(
        r"(?:\n\s*#{1,4}\s+|\n{2,})",
        text
    )

    sections = [s.strip() for s in sections if s.strip()]

    for section in sections:
        yield section


sample = """
Category-A

Some content...

Category-B

Some content...

Lateral Entry

Some content...
"""

chunks = list(_section_aware_chunk(sample))

for i, chunk in enumerate(chunks):
    print("\n-----")
    print(i)
    print(chunk)