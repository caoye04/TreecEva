import hashlib
from collections import Counter
def fibonacci_sequence(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

def hash_token(token):
    return int(hashlib.md5(token.encode()).hexdigest()[:8], 16)

message = "secure communication protocol design"
tokens = message.split()
fib_nums = list(fibonacci_sequence(len(tokens)))
token_hashes = [hash_token(token) for token in tokens]
hash_counter = Counter(token_hashes)
combined_values = []
for i, token_hash in enumerate(token_hashes):
    freq = hash_counter[token_hash]
    combined_value = token_hash ^ fib_nums[i] ^ (freq << 4)
    combined_values.append(combined_value)

session_key = 0
for val in combined_values:
    session_key = (session_key + val) & 0xFFFFFFFF

print(f"Result: {session_key}")