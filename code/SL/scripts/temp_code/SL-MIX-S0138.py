import heapq
from itertools import combinations

def calculate_entropy(key):
    return len(set(key))  # Simplified entropy as unique character count

def key_score_aggregate(keys):
    return sum(hash(k) % 100 for k in keys)  # Simplified scoring

# Initial set of encryption keys
encryption_keys = ['abc123', 'xyz789', 'def456', 'abc123', 'uvw000']
key_heap = []

# Populate heap with (entropy, key) tuples
for key in encryption_keys:
    entropy = calculate_entropy(key)
    heapq.heappush(key_heap, (entropy, key))

# Process: Remove keys with entropy < 5 or duplicate keys
processed_keys = set()
filtered_heap = []

while key_heap:
    entropy, key = heapq.heappop(key_heap)
    # Short-circuit evaluation: check entropy first, then duplication
    if entropy >= 5 and key not in processed_keys:
        processed_keys.add(key)
        heapq.heappush(filtered_heap, (entropy, key))
    
# Add new keys from combinatorial generation
base_components = ['a', 'b', 'c', '1', '2', '3']
generated_keys = [''.join(combo) for combo in combinations(base_components, 4)]

for key in generated_keys[:10]:  # Limit to first 10 combinations
    entropy = calculate_entropy(key)
    if entropy >= 3:  # Only add keys with minimum entropy
        heapq.heappush(filtered_heap, (entropy, key))

# Final processing: calculate aggregate score of remaining keys
final_key_score = key_score_aggregate([key for _, key in filtered_heap])

print(f"Result: {final_key_score}")