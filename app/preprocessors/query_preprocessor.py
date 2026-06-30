import re
from spellchecker import SpellChecker

_ABBREVIATIONS = {
    "u": "you",
    "ur": "your",
    "r": "are",
    "pls": "please",
    "plz": "please",
    "thx": "thanks",
    "ty": "thank you",
    "wht": "what",
    "wat": "what",
    "hw": "how",
    "whr": "where",
    "wen": "when",
    "y": "why",
    "cn": "can",
    "cant": "can't",
    "dont": "don't",
    "wont": "won't",
    "coz": "because",
    "bcz": "because",
    "abt": "about",
    "info": "information",
    "hstl": "hostel",
    "hostl": "hostel",
    "hostel": "hostel",
    "wifi": "wi-fi",
    "wi-fi": "wi-fi",
    "wi": "wi-fi",
}

spell = SpellChecker()

_PROTECTED_WORDS = {
    "vnrvjiet",
    "vnr",
    "cse",
    "ece",
    "eee",
    "it",
    "civil",
    "mechanical",
    "aids",
    "aiml",
    "mba",
    "mca",
    "eapcet",
    "tseapcet",
    "jee",
    "hostel",
    "cutoff",
    "scholarship",
    "placements",
}


def expand_abbreviations(query: str) -> str:
    """
    Expand common chat abbreviations into their full forms.
    Example:
        wht -> what
        cn -> can
        plz -> please
    """
    words = query.split()

    expanded = [
        _ABBREVIATIONS.get(word.lower(), word)
        for word in words
    ]

    return " ".join(expanded)

def correct_spelling(query: str) -> str:
    """
    Correct spelling mistakes while preserving protected college terms.
    """
    corrected = []

    for word in query.split():

        clean = re.sub(r"[^\w]", "", word.lower())

        if clean in _PROTECTED_WORDS:
            corrected.append(word)
            continue

        corrected_word = spell.correction(clean)

        corrected.append(corrected_word if corrected_word else word)

    return " ".join(corrected)

def normalize_repeated_letters(query: str) -> str:
    """
    Normalize repeated characters.

    Examples:
        helloooo -> hello
        hiiiiii -> hii
        pleassseee -> pleasse
    """
    return re.sub(r"(.)\1{2,}", r"\1", query)

def clean_punctuation(query: str) -> str:
    """
    Remove unnecessary punctuation while preserving ? and .
    """
    query = re.sub(r"[!]{2,}", "!", query)
    query = re.sub(r"[?]{2,}", "?", query)
    query = re.sub(r"\.{2,}", ".", query)
    return query


def normalize_spaces(query: str) -> str:
    """
    Remove extra spaces.
    """
    return " ".join(query.split())


def preprocess_query(query: str) -> str:
    """
    Complete preprocessing pipeline.
    """

    query = normalize_repeated_letters(query)

    query = expand_abbreviations(query)

    query = correct_spelling(query)

    query = clean_punctuation(query)

    query = normalize_spaces(query)

    return query


