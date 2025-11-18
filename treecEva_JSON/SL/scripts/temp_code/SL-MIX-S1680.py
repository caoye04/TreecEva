import heapq
from functools import wraps

def prime_key_validator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
        if result in primes:
            wrapper.valid_count += 1
        return result
    wrapper.valid_count = 0
    return wrapper

@prime_key_validator
def generate_session_key(seed):
    return (seed * 17 + 23) % 30

session_seeds = [4, 7, 12, 15, 21, 25, 28]
key_heap = []

for seed in session_seeds:
    key = generate_session_key(seed)
    heapq.heappush(key_heap, -key)  # Max-heap using negative values

secure_sessions = 0
while key_heap:
    current_key = -heapq.heappop(key_heap)
    if current_key > 10:
        secure_sessions += 1
    else:
        break  # Early termination on condition

# Additional validation step
if generate_session_key.valid_count >= 3:
    secure_sessions *= 2
else:
    secure_sessions -= 1

print(f"Result: {secure_sessions}")