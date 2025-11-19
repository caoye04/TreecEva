import hashlib
from collections import defaultdict
from itertools import combinations

def process_geohash_data():
    locations = ['A3F9', 'B7K2', 'C1M8', 'D4N5']
    hash_map = defaultdict(int)
    
    # Stage 1: Hash each location and store mod 1000
    for loc in locations:
        hex_hash = hashlib.md5(loc.encode()).hexdigest()
        numeric_hash = int(hex_hash[:8], 16)
        hash_map[loc] = numeric_hash % 1000
    
    # Stage 2: Create pairwise combinations and calculate floating adjustments
    adjustments = []
    for combo in combinations(hash_map.keys(), 2):
        val1, val2 = hash_map[combo[0]], hash_map[combo[1]]
        avg_float = (val1 + val2) / 2.0
        adjustment = int(avg_float * 1.73) % 100
        adjustments.append(adjustment)
    
    # Stage 3: Apply string transformation and accumulate checksum
    transformed_values = [str(x)[::-1] for x in adjustments if x > 10]
    digit_sum = sum(int(d) for s in transformed_values for d in s)
    
    # Final stage: Modular checksum computation
    final_checksum = (digit_sum * 37 + len(transformed_values)) % 991
    return final_checksum

final_checksum = process_geohash_data()
print(f"Result: {final_checksum}")