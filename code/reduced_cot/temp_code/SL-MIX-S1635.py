import hashlib

def tokenize(text):
    return [token.strip('.,!?;') for token in text.split()]

def compute_hash(token):
    return int(hashlib.md5(token.encode()).hexdigest(), 16) % 1000

def is_valid_token(token):
    return len(token) > 3 and token.isalpha()

document_fragment = "The quick brown fox jumps over the lazy dog."
tokens = tokenize(document_fragment)
filtered_tokens = [t for t in tokens if is_valid_token(t)]
hash_values = [compute_hash(t) for t in filtered_tokens]

# Logical filtering: keep hashes that are even AND greater than 500
valid_hashes = [h for h in hash_values if (h % 2 == 0) and (h > 500)]

# Calculate aggregated score using XOR operations on valid hashes
aggregated_score = 0
for h in valid_hashes:
    aggregated_score ^= h

print(f"Result: {aggregated_score}")