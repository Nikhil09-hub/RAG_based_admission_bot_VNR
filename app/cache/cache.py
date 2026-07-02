CACHE_TTL = 3600  # 1 hour
import json

import redis
from app.schemas.chat import ChatResponse
from app.cache.cache_key import generate_cache_key
from app.config import get_settings

settings = get_settings()

CACHE = {}

redis_client = None

if settings.REDIS_URL:
    try:
        redis_client = redis.from_url(
            settings.REDIS_URL,
            decode_responses=True,
        )
        redis_client.ping()
        print("✅ Redis Connected")
    except Exception as e:
        print(f"⚠️ Redis unavailable. Using in-memory cache. {e}")
        redis_client = None


def get_cache(key):
    print(f"Looking for key: {key}")

    # ---------- Redis ----------
    if redis_client:
        cached = redis_client.get(key)

        if cached:
            print("✅ Redis Cache Hit")
            return ChatResponse(**json.loads(cached))

        print("❌ Redis Cache Miss")
        return None

    # ---------- Local ----------
    print(f"Current cache size: {len(CACHE)}")
    return CACHE.get(key)
def set_cache(key, value):

    # ---------- Redis ----------
    if redis_client:

        redis_client.set(
            key,
            json.dumps(value.model_dump()),
            ex=CACHE_TTL,
)

        print("💾 Stored in Redis")
        return

    # ---------- Local ----------
    CACHE[key] = value

    print(f"Stored key: {key}")
    print(f"Cache size after storing: {len(CACHE)}")