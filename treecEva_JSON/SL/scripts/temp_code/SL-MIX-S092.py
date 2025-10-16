import hashlib

def tokenize_and_hash(sentence):
    tokens = [token.strip(',.!?;') for token in sentence.lower().split()]
    hashes = [int(hashlib.md5(token.encode()).hexdigest(), 16) % 1000000 for token in tokens]
    return hashes

def merge_hashes(hash_list1, hash_list2):
    combined = hash_list1 + hash_list2
    unique_hashes = list(set(combined))
    return sorted(unique_hashes)

def transform_hashes(sorted_hashes):
    transformed = [(h ^ (h >> 4)) & 0xFFFF for h in sorted_hashes if h % 3 != 0]
    return transformed

text_corpus = [
    "The quick brown fox jumps over the lazy dog.",
    "Pack my box with five dozen liquor jugs!",
    "How vexingly quick daft zebras jump!"
]

# Process each sentence
processed_hashes = [tokenize_and_hash(sentence) for sentence in text_corpus]

# Apply divide and conquer merging
while len(processed_hashes) > 1:
    merged = []
    for i in range(0, len(processed_hashes), 2):
        if i+1 < len(processed_hashes):
            merged.append(merge_hashes(processed_hashes[i], processed_hashes[i+1]))
        else:
            merged.append(processed_hashes[i])
    processed_hashes = merged

# Final sorting and transformation
final_hashes = processed_hashes[0]
transformed_values = transform_hashes(final_hashes)

# Calculate linguistic signature
linguistic_signature = sum(transformed_values) % 10000

print(f"Result: {linguistic_signature}")