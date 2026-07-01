import hashlib

def generate_cache_key(query: str):
    normalized = query.lower().strip()
    return hashlib.sha256(normalized.encode()).hexdigest()