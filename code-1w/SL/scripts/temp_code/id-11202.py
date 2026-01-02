from collections import defaultdict
from itertools import permutations

def preprocess_data(entries):
    # Irrelevant preprocessing step (distractor)
    normalized = [x % 7 for x in entries if x > 0]
    frequency = defaultdict(int)
    for val in normalized:
        frequency[val] += 1
    return frequency

def compute_bias(sequence):
    # Semi-relevant but not used in final logic
    bias = 0
    for i, val in enumerate(sequence):
        bias += (i + 1) * (val % 3)
    return bias

def generate_combinations(values):
    # Dead code path — never called
    return list(permutations(values, 3))

def evaluate_performance(ranks, multipliers):
    total = 0
    rank_map = defaultdict(int)
    
    # Build rank index
    for idx, rank in enumerate(ranks):
        rank_map[rank] = idx + 1
    
    # Misleading intermediate calculation
    temp_offset = 0
    for k in rank_map:
        if k % 2 == 0:
            temp_offset += k * 0.5
    
    # Actual scoring logic
    scaling_factor = 1.5
    for i, base in enumerate(multipliers):
        position = rank_map.get(i + 1, 0)
        contribution = base * position
        if position > 0:
            contribution *= scaling_factor
        total += int(contribution)  # Truncate to integer

    # Additional red herring: unused transformation
    inverted_ranks = {v: k for k, v in rank_map.items()}
    checksum = sum(inverted_ranks.keys()) if inverted_ranks else 0

    return int(total - 2)  # Final adjustment

# Main execution flow
if __name__ == "__main__":
    raw_input_data = [10, -5, 8, 12, 3, 0, 7]
    rankings = [3, 1, 4, 2, 5]
    base_multipliers = [2, 4, 6, 8, 10]

    # Distractor calls
    _ = preprocess_data(raw_input_data)
    _ = compute_bias(base_multipliers)

    # Key statement
    final_score = evaluate_performance(rankings, base_multipliers)

    print(f"Result: {final_score}")