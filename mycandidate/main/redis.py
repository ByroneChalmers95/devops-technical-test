import os
import redis

# Get Redis URL from environment or fallback to local default
redis_url = os.getenv("REDIS_URL", "redis://localhost:6379/0")

# Initialize Redis client
try:
    redis_client = redis.StrictRedis.from_url(redis_url)
    # Quick ping test
    redis_client.ping()
    print(f"[INFO] Connected to Redis at {redis_url}")
except Exception as e:
    print(f"[ERROR] Failed to connect to Redis at {redis_url}: {e}")
    redis_client = None


def get_cached_data_or_fetch(key, fetch_func, expire=60):
    """Get data from Redis cache or call fetch_func to populate it."""
    if redis_client:
        try:
            cached = redis_client.get(key)
            if cached:
                return cached.decode("utf-8")
            value = fetch_func()
            redis_client.setex(key, expire, value)
            return value
        except Exception as e:
            print(f"[WARN] Redis error: {e}")
            return fetch_func()
    else:
        return fetch_func()
