import itertools

def preprocess_ranks(raw_ranks):
    # Normalize ranks by inverting (lower rank = higher score)
    normalized = [max(raw_ranks) - x + 1 for x in raw_ranks]
    adjustment = sum(normalized) / len(normalized)
    adjusted = [val + adjustment * 0.1 for val in normalized]  # Minor tweak
    return adjusted

def calculate_efficiency_index(values):
    # Irrelevant helper function – not used in final computation
    return sum(v ** 0.5 for v in values if v > 0) / len(values)

def generate_combinations(data):
    # Distractor: generates pairs but unused
    return list(itertools.combinations(data, 2))

def calculate_final_score(ranks, weights):
    weighted_sum = 0
    total_weight = 0
    
    for i, rank in enumerate(ranks):
        if i % 2 == 0:
            contribution = (rank * 1.5) * weights[i]
        else:
            contribution = (rank * 0.8) * weights[i]
        weighted_sum += contribution
        total_weight += weights[i]
    
    avg_weighted = weighted_sum / total_weight
    
    # Apply non-linear boost
    boosted = avg_weighted ** 1.2
    
    # Dead code path – never executed due to fixed input size
    if len(ranks) > 20:
        boosted *= 0.9  # Correction factor (unreachable)
    
    return int(boosted)

# Main execution
base_ranks = [3, 1, 4, 1, 5, 9, 2, 6]
bonus_weights = [2, 1, 3, 1, 2, 3, 1, 2]

# Preprocessing step with side-variable
processed_ranks = preprocess_ranks(base_ranks)
duplicate_check = list(set(processed_ranks))  # No duplicates expected

# Unused combination analysis
all_pairs = generate_combinations(base_ranks)  # Stored but not used

# Efficiency metric calculated but not used
efficiency = calculate_efficiency_index(base_ranks)

# Key statement
final_score = calculate_final_score(processed_ranks, bonus_weights)

# Output result
print(f"Result: {final_score}")