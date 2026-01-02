def analyze_pattern(sequence, threshold):
    count = 0
    temp_sum = 0
    for val in sequence:
        if val > threshold:
            count += 1
            temp_sum += val ** 0.5
    return count * temp_sum

baseline = [3, 7, 9, 12, 15]
readings = [8, 11, 6, 14, 10, 5, 13]

# Irrelevant preprocessing (distractor)
decoded = [x ^ 3 for x in readings if x % 2 == 1]
offsets = list(map(lambda y: y + 2, baseline))

# Misleading transformation chain
filtered = []
for i in range(len(readings)):
    if i % 2 == 0:
        filtered.append(readings[i] * 1.5)
    else:
        filtered.append(readings[i] * 0.8)

# Actual logic embedded with noise
def calculate_performance(base, data):
    shift = sum(base) // len(base)
    adjusted = [x - shift for x in data if x >= shift]
    
    # Dead code branch (never executed due to condition)
    if len(adjusted) < 0:  # Always false
        adjusted = [abs(x) for x in adjusted]
    
    # Core computation
    valid_entries = [x for x in adjusted if x % 2 == 0]
    total_weight = sum(valid_entries)
    
    # Semi-relevant but unused metric
    peak_index = -1
    for idx, val in enumerate(data):
        if val == max(data):
            peak_index = idx
    
    # Final score depends only on total_weight and fixed offset
    magic_factor = 4
    final_score = total_weight + magic_factor
    
    # Red herring: complex but irrelevant calculation
    dummy_score = analyze_pattern(data, 10) / (peak_index + 1) if peak_index != -1 else 0
    
    return final_score

# Key execution point
final_score = calculate_performance(baseline, readings)
print(f"Result: {final_score}")