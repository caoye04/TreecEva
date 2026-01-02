from collections import defaultdict

# Simulate ranking-based evaluation with noise and filtering
def preprocess_ranks(raw_scores):
    rank_map = defaultdict(int)
    for i, score in enumerate(raw_scores):
        if score > 0:
            rank_map[i] = score * (i + 1)
    # Distractor: irrelevant transformation
    temp_offsets = [x % 7 for x in raw_scores if x > 5]
    offset_sum = sum(temp_offsets) // 2 if temp_offsets else 0
    return dict(rank_map), offset_sum

def calculate_entropy(values):
    # Dead function - not used in final computation
    from math import log
    total = sum(values)
    entropy = 0
    for v in values:
        p = v / total
        entropy -= p * log(p)
    return entropy

def calculate_final_score(ranks, weight_config):
    base_score = 0
    bonus = 0
    # Real logic begins
    sorted_ranks = sorted(ranks.items(), key=lambda x: x[1], reverse=True)
    
    # Apply weighted scoring with decay
    for idx, (pos, val) in enumerate(sorted_ranks):
        weight = weight_config.get(pos, 0.5)
        base_score += val * weight
        if idx % 3 == 0 and val > 10:  # Bonus condition
            bonus += 5
    
    # Irrelevant bitwise distraction
    masked_bonus = bonus ^ 17 & 10
    adjusted_score = base_score + (masked_bonus >> 1)
    
    # Additional red herring: unused loop over zipped elements
    checksum = 0
    for a, b in zip(weight_config.values(), weight_config.values()):
        checksum += a & b  # Does nothing useful
    
    return int(adjusted_score)

# Main execution
raw_performance = [8, 12, 0, 15, 7, 11]
weights = {0: 1.2, 1: 0.9, 2: 1.5, 3: 0.7, 4: 0.6, 5: 0.8}

rank_data, _ = preprocess_ranks(raw_performance)

# Extraneous data structure manipulation
summary_stats = {}
for k, v in rank_data.items():
    summary_stats[k] = {
        'value': v,
        'flagged': v > 20,
        'tier': 'A' if v > 25 else 'B'
    }

# Unused list comprehension with complex filtering
ignored_analysis = [
    (k, v) for k, v in rank_data.items()
    if v % 4 == 0 and k in weights
]

final_score = calculate_final_score(rank_data, weights)
print(f"Result: {final_score}")