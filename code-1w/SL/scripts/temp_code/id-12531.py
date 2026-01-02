def analyze_pattern(seq, factor):
    # Irrelevant transformation
    temp_result = [x * factor for x in seq if x % 2 == 0]
    ignored_sum = sum(temp_result) * 0.1  # Distractor
    return [x ** 0.5 for x in seq if x > 0]

segments = [16, 9, 25, 4, 36, 1]
weights = [0.5, -0.2, 0.3, 0.7, -0.5, 0.9]

# Dead code path (never used)
def legacy_calculate(arr):
    total = 0
    for i in range(len(arr)):
        total += arr[i] * (i + 1)
    return total

# Unused but plausible-looking helper
def normalize_vector(vec):
    norm = sum([v**2 for v in vec]) ** 0.5
    return [v / norm for v in vec] if norm else vec

# Misleading intermediate calculation
decoy_score = 0
for idx, val in enumerate(segments):
    if idx % 2 == 0:
        decoy_score += val // 2
    else:
        decoy_score -= val // 3

decoy_score = max(decoy_score, 0)  # Further obfuscation

# Real computation buried among distractions
scaling_factor = 1.5
adjusted_weights = [w * scaling_factor for w in weights]

# Another red herring: bit manipulation with no effect
bit_mask = 0b101010
masked_values = [seg & bit_mask for seg in segments]

# Core logic disguised within complex structure
def process_segments(data, weight_map):
    score = 0.0
    # Use of enumerate and zip as required
    for i, (val, w) in enumerate(zip(data, weight_map)):
        # Slicing to ignore first and last elements in transformed view
        context_window = data[max(0, i-1):i+2]  # Overlapping windows
        center_contribution = val ** 0.5  # Actual key operation
        weight_influence = w * len(context_window)  # Minor amplification
        score += center_contribution * weight_influence
    # Final adjustment using only relevant components
    return int(score + 0.5)  # Round to nearest integer

# Secondary distraction: unused list comprehension with slicing
reversed_tail = segments[::-1][:4]
processed_tail = [x // 4 for x in reversed_tail]

# Key execution point
final_score = process_segments(segments, weights)

print(f"Result: {final_score}")