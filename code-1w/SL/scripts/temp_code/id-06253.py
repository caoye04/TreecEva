from itertools import combinations
from collections import defaultdict

# Simulate sensor data aggregation and scoring with noise filtering
def preprocess_ranks(raw_ranks):
    filtered = [x for x in raw_ranks if 1 <= x <= 100]
    sorted_ranks = sorted(filtered, reverse=True)
    top_quartile = sorted_ranks[:len(sorted_ranks)//4 + 1]
    return top_quartile

# Misleading helper: appears useful but not used in final logic
def legacy_normalize(data):
    max_val = max(data) if data else 1
    return [round(x / max_val, 3) for x in data]

# Core transformation function
def apply_weight_shift(ranks, shift_factor):
    shifted = []
    for i, val in enumerate(ranks):
        # Exponential decay weighting by position
        weight = 1 / (1 + i) ** 0.5
        shifted.append(val * weight * (1 + shift_factor))
    return shifted

# Auxiliary computation - counts digit patterns (distractor)
def count_even_digits_in_range(limit):
    count = 0
    for n in range(limit):
        count += len([d for d in str(n) if int(d) % 2 == 0])
    return count

# Main scoring logic
def calculate_final_score(rank_list, weights):
    base_score = sum(rank_list)
    
    # Apply dynamic weighting using dictionary mapping
    weight_map = {i: w for i, w in enumerate(weights)}
    enhanced_score = base_score
    
    for idx, rank in enumerate(rank_list):
        if idx in weight_map:
            enhanced_score += rank * weight_map[idx]
    
    # Use set to deduplicate (redundant here, but adds cognitive load)
    unique_ranks = list(set(rank_list))
    diversity_bonus = len(unique_ranks) // 3
    
    # Spurious combination check (never triggers due to data constraints)
    triplet_count = 0
    for comb in combinations(unique_ranks, 3):
        if sum(comb) > 150 and comb[0] % 2 == 0:
            triplet_count += 1
    
    # Final adjustment using auxiliary variable
    adjustment = 7 if diversity_bonus > 2 else 3
    final_raw = enhanced_score + diversity_bonus * adjustment
    
    # Dead code path - unreachable due to fixed input size
    if len(rank_list) > 50:
        final_raw = round(final_raw * 0.95)
        
    return int(final_raw)

# Simulated input data
raw_sensor_data = [88, 92, 76, 95, 85, 90, 44, 98, 87, 82, 93, 40, 105, -5, 99]
bonus_shift = 0.15
bonus_weights = [0.1, 0.2, 0.15, 0.3, 0.05, 0.2, 0.1, 0.08, 0.12, 0.1]

# Intermediate processing steps with distractors
effective_ranks = preprocess_ranks(raw_sensor_data)
applied_shift = apply_weight_shift(effective_ranks, bonus_shift)

# Unused variable - adds interference
rank_frequencies = defaultdict(int)
for r in effective_ranks:
    rank_frequencies[r] += 1

# Auxiliary distraction
digit_noise = count_even_digits_in_range(40)

# Key statement
final_score = calculate_final_score(effective_ranks, bonus_weights)

print(f"Result: {final_score}")