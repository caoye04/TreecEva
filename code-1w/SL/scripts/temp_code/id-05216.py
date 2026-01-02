from itertools import combinations

def preprocess_entry(entry):
    # Irrelevant transformation for some entries (not all used)
    if len(entry['tags']) > 2:
        return entry['value'] * 1.1
    else:
        return entry['value']

def calculate_similarity(a, b):
    # Dummy similarity function (not actually used in final logic)
    return abs(a - b) / max(a, b) if a != b else 0.0

def calculate_final_score(entries, weights):
    base_values = [e['value'] for e in entries]
    adjusted_values = [preprocess_entry(e) for e in entries]
    
    # Real computation begins
    weighted_sum = sum(base_values[i] * weights[i] for i in range(len(weights)))
    
    # Distraction: complex unused similarity matrix
    similarity_matrix = [[calculate_similarity(base_values[i], base_values[j]) 
                         for j in range(len(base_values))] 
                        for i in range(len(base_values))]
    
    # Additional distraction: generate unused pairs
    high_value_pairs = list(combinations([v for v in base_values if v > 50], 2))
    pair_count = len(high_value_pairs)
    avg_pair_diff = sum(abs(a - b) for a, b in high_value_pairs) if pair_count > 0 else 0
    
    # Actual key logic: correction factor based on tag count
    total_tags = sum(len(e['tags']) for e in entries)
    correction_factor = 1.0 + (total_tags * 0.05) if total_tags < 10 else 1.4
    
    # Final score depends only on weighted_sum and correction_factor
    intermediate_score = weighted_sum * correction_factor
    
    # Red herring: entropy-like calculation (unused)
    import math
    if weighted_sum > 0:
        entropy = -sum((v / weighted_sum) * math.log(v / weighted_sum) for v in base_values if v > 0)
    
    # Final adjustment: cap at 500, floor at 0
    final_score = max(0, min(500, intermediate_score))
    
    return final_score

# Main data setup
data_entries = [
    {'value': 30, 'tags': ['A', 'B']},
    {'value': 45, 'tags': ['B', 'C', 'D']},
    {'value': 60, 'tags': ['A', 'D']},
    {'value': 25, 'tags': ['C']}
]

weights = [0.2, 0.3, 0.4, 0.1]

# Extra unused variables (distraction)
baseline_avg = sum(e['value'] for e in data_entries) / len(data_entries)
duplicate_entries = [e for e in data_entries for _ in range(2)]

final_score = calculate_final_score(data_entries, weights)
print(f"Result: {final_score}")