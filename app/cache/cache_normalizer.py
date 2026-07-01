import re

STOP_WORDS = {
    "what",
    "is",
    "are",
    "the",
    "a",
    "an",
    "tell",
    "me",
    "please",
    "can",
    "could",
    "would",
    "give",
    "show",
    "about",
    "of",
    "to",
    "for",
    "i",
    "want",
    "know",
    "kindly",
}

SYNONYMS = {
    "fees": "fee",
    "hostels": "hostel",
    "departments": "department",
    "placements": "placement",
    "clubs": "club",
    "courses": "course",
}


def normalize_cache_query(query: str) -> str:

    query = query.lower()

    query = re.sub(r"[^\w\s]", " ", query)

    words = []

    for word in query.split():

        if word in STOP_WORDS:
            continue

        word = SYNONYMS.get(word, word)

        words.append(word)

    return " ".join(words)