def calculate_final_score(records):
    base_multiplier = 3
    bonus_threshold = 85
    penalty_factor = 0.9
    temp_offset = 12
    
    # Irrelevant precomputation (distractor)
    avg_temp = sum([r['temp'] for r in records]) / len(records) if records else 0
    adjusted_temps = [r['temp'] + temp_offset for r in records]
    
    # Real logic begins: extract scores and apply conditions
    raw_scores = [r['score'] for r in records]
    weight_map = {i: (1.1 if s >= bonus_threshold else 0.8) for i, s in enumerate(raw_scores)}
    
    # Apply bitwise adjustment based on record index (moderate complexity)
    bit_adjusted = []
    for idx, score in enumerate(raw_scores):
        shifted = (idx & 7) ^ score  # XOR with lower 3 bits of index
        bit_adjusted.append(shifted)
    
    # Lambda-based conditional scaling
    scale_func = lambda x, w: x * w * base_multiplier
    scaled_scores = [scale_func(score, weight_map[i]) for i, score in enumerate(bit_adjusted)]
    
    # Accumulate with filtering (ignore negative adjusted scores)
    filtered_sum = sum(s for s in scaled_scores if s > 0)
    
    # Red herring: unused complex calculation
    peak_detection = max(scaled_scores) > 100 and any(s < 0 for s in scaled_scores)
    stability_check = all(abs(a - b) < 50 for a, b in zip(scaled_scores, scaled_scores[1:]))
    
    # Final computation
    total_weight = sum(weight_map.values())
    final_score = int((filtered_sum * penalty_factor) / total_weight) if total_weight else 0
    
    return final_score

# Input data
data = [
    {'score': 76, 'temp': 22},
    {'score': 88, 'temp': 19},
    {'score': 91, 'temp': 25},
    {'score': 73, 'temp': 20},
    {'score': 85, 'temp': 23}
]

# Execution point
final_score = calculate_final_score(data)
print(f"Result: {final_score}")