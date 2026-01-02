def analyze_pattern(sequence):
    counts = {x: sequence.count(x) for x in set(sequence)}
    frequencies = [v for k, v in sorted(counts.items())]
    temp_sum = sum(frequencies)
    adjustment = temp_sum % 3
    return adjustment

# Simulate sensor data drift correction
data = [12, 15, 12, 18, 15, 21, 12, 18]
weights = [0.1, 0.3, 0.2, 0.4]

# Irrelevant normalization (distractor)
normalized_data = [round((x - min(data)) / (max(data) - min(data)) * 100) for x in data]
duplicate_check = len(data) != len(set(data))  # Just a flag, not used later

# Weighted transformation using zip and lambda
weighted_pairs = list(zip(data, weights))
weighted_transform = list(map(lambda pair: pair[0] * pair[1] * 2, weighted_pairs))

# Secondary processing with enumerate and distractor accumulation
accumulated = 0
for i, val in enumerate(weighted_transform):
    if i % 2 == 0:
        accumulated += val + i
    else:
        accumulated -= val

# Dummy set operations for interference
even_set = {x for x in data if x % 2 == 0}
odd_set = {x for x in data if x % 2 == 1}
symmetric_diff = even_set ^ odd_set  # Unused
intersection_size = len(even_set & odd_set)  # Always 0, irrelevant

# Core calculation chain
def calculate_final_score(values, coeffs):
    base_score = sum(v * c for v, c in zip(values, coeffs))
    penalty = analyze_pattern(values) * 1.5
    bonus = len([v for v in values if v > 14]) * 0.7
    return int(base_score - penalty + bonus)

intermediate_result = sum(weighted_transform) / len(weighted_transform)
final_score = calculate_final_score(data, weights)
print(f"Result: {final_score}")