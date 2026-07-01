import hashlib

CACHE = {}

def generate_cache_key(query: str):
    return hashlib.sha256(query.lower().strip().encode()).hexdigest()

def get_cache(key):
    print(f"Looking for key: {key}")
    print(f"Current cache size: {len(CACHE)}")
    return CACHE.get(key)

def set_cache(key, value):
    CACHE[key] = value
    print(f"Stored key: {key}")
    print(f"Cache size after storing: {len(CACHE)}")