from collections import defaultdict

def transform_id(doc_id):
    transformed = ''
    for i, char in enumerate(doc_id):
        if i % 3 == 0:
            transformed += chr((ord(char) * 17) % 97 + 32)
        elif i % 3 == 1:
            transformed += chr((ord(char) + 13) % 97 + 32)
        else:
            transformed += chr((ord(char) ^ 42) % 97 + 32)
    return transformed

doc_ids = ['MAT2023', 'PHY2024', 'CS2025']
hash_tracker = defaultdict(int)
verification_code = 0

for idx, doc_id in enumerate(doc_ids):
    stage1_transform = transform_id(doc_id)
    hash_val = hash(stage1_transform) % 1000
    hash_tracker[idx] = hash_val
    
    if idx > 0:
        prev_hash = hash_tracker[idx-1]
        delta = abs(hash_val - prev_hash)
        if delta % 7 == 0:
            verification_code += delta // 7
        else:
            verification_code += (delta % 5) * 3
    else:
        verification_code = hash_val % 100
        
    # Apply modular adjustment
    verification_code = (verification_code * 13 + idx) % 1000

# Final adjustment based on total hashes
verification_code = (verification_code + sum(hash_tracker.values()) % 100) % 1000
print(f"Result: {verification_code}")