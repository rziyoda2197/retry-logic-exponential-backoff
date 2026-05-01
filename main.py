import time
import random

class RetryLogic:
    def __init__(self, max_attempts, initial_backoff, max_backoff):
        self.max_attempts = max_attempts
        self.initial_backoff = initial_backoff
        self.max_backoff = max_backoff
        self.current_attempt = 0

    def retry(self, func):
        def wrapper(*args, **kwargs):
            while self.current_attempt < self.max_attempts:
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    self.current_attempt += 1
                    backoff = min(self.initial_backoff * (2 ** self.current_attempt), self.max_backoff)
                    time.sleep(backoff + random.uniform(0, 0.1))  # 10% jitter
                    if self.current_attempt >= self.max_attempts:
                        raise
        return wrapper

# Misol uchun API call qilish
def api_call():
    # API call qilish uchun kod
    return "API response"

retry_logic = RetryLogic(max_attempts=5, initial_backoff=1, max_backoff=30)
@retry_logic.retry
def api_call_with_retry():
    return api_call()

print(api_call_with_retry())
