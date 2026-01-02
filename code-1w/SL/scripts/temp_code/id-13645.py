def analyze_patterns(sequence):
    freq_map = {}
    for item in sequence:
        freq_map[item] = freq_map.get(item, 0) + 1
    
    # Distractor: unused frequency analysis
    rare_items = [k for k, v in freq_map.items() if v < 2]
    common_threshold = len(sequence) // 4
    abundant_items = [k for k, v in freq_map.items() if v > common_threshold]

    # Semi-relevant transformation
    normalized = [x / max(freq_map.values()) for x in freq_map.values()]
    return normalized


def calculate_entropy(values):
    import math
    entropy = 0
    total = sum(values)
    if total == 0:
        return 0
    for v in values:
        prob = v / total
        if prob > 0:
            entropy -= prob * math.log2(prob)
    return entropy

# Main data processing
raw_data = [3, 7, 3, 2, 8, 7, 3, 9, 2, 8, 7, 3, 1, 9, 7]
data_set = set(raw_data)  # Remove duplicates for unique analysis

# Weight assignment with distractors
weights = {}
for i, val in enumerate(sorted(data_set)):
    weights[val] = round(1 / (i + 1), 3)

# Extra irrelevant computation on weights
weight_sum = sum(weights.values())
inverse_weights = {k: 1/v for k, v in weights.items() if v != 0}
discount_factor = len(inverse_weights) / (weight_sum + 1)

# Core logic with key variable construction
effective_values = []
for key in sorted(data_set):
    count_in_raw = raw_data.count(key)
    weight = weights[key]
    contribution = count_in_raw * weight * 0.5
    effective_values.append(contribution)

# Secondary distractor: unused clustering attempt
paired = list(zip(sorted(data_set), analyze_patterns(raw_data)))
cluster_flag = any(p[1] > 0.3 for p in paired)

# Final score calculation
entropy_component = calculate_entropy(effective_values)
size_bonus = len(data_set) * 0.25
base_total = sum(effective_values)

# Key statement
final_score = base_total + entropy_component + size_bonus

# Print result as required
print(f"Result: {final_score}")