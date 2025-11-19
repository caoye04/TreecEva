from collections import defaultdict
import hashlib

def tokenize_and_classify(text_passage):
    tokens = text_passage.split()
    hash_buckets = defaultdict(int)
    classified_count = 0
    
    for token in tokens:
        # Normalize token: remove punctuation and convert to lowercase
        clean_token = ''.join(ch for ch in token if ch.isalnum()).lower()
        if not clean_token:
            continue
            
        # Compute hash and use modular arithmetic for bucket assignment
        token_hash = int(hashlib.md5(clean_token.encode()).hexdigest(), 16)
        bucket_id = token_hash % 7  # 7 categories for classification
        
        # Apply conditional logic for classification
        if len(clean_token) > 3 and bucket_id in [1, 3, 5]:
            hash_buckets[bucket_id] += 1
            classified_count += (bucket_id * len(clean_token))
        elif len(clean_token) <= 3 and bucket_id in [0, 2, 4, 6]:
            hash_buckets[bucket_id] += 2  # Short tokens get double count
            classified_count -= (bucket_id + len(clean_token))
    
    # Post-processing adjustment based on distribution
    if sum(hash_buckets.values()) > 10:
        classified_count = (classified_count * 3) % 100
    else:
        classified_count = (classified_count + 42) % 100
        
    return classified_count

# Process the ancient manuscript passage
manuscript_passage = "O mighty Caesar! Why dost thou conspire With thy own thoughts, that lov'st to palliate So forcibly the trespass of thy heart?"
classified_count = tokenize_and_classify(manuscript_passage)
print(f"Result: {classified_count}")