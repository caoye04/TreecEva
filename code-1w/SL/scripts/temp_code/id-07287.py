def analyze_patterns(sequence):
    counts = {}
    for char in sequence:
        counts[char] = counts.get(char, 0) + 1
    return counts

# Simulate sensor data with noise filtering
def filter_noisy_readings(readings):
    filtered = []
    for val in readings:
        if abs(val - sum(filtered) / len(filtered) if filtered else 0) < 50:
            filtered.append(val)
    return filtered

# Main scoring logic
def calculate_final_score(raw_data, importance_weights):
    normalized = [x / max(raw_data) for x in raw_data]
    
    # Misleading intermediate transformation (not used later)
    inverted = [1.0 / (1 + x) for x in normalized]
    temp_sum = sum(inverted) * 0.1  # Distractor calculation

    # Actual relevant processing
    weighted_vals = []
    for i, val in enumerate(normalized):
        weight = importance_weights[i % len(importance_weights)]
        weighted_vals.append(val * weight)
    
    # Character pattern analysis on metadata (red herring)
    meta_tag = "sensor_{}_log".format(len(raw_data))
    char_freq = analyze_patterns(meta_tag)
    offset = len([k for k, v in char_freq.items() if v > 1])  # Unused complexity

    # Real score computation
    base_score = sum(weighted_vals)
    adjustment = 0.0
    for i, (idx, val) in enumerate(zip(range(len(weighted_vals)), weighted_vals)):
        if idx % 2 == 0 and val > 0.5:
            adjustment += 0.05
    
    final_component = base_score + adjustment
    total_score = int(round(final_component * 100))
    
    # Dead code path (never reached due to structure)
    if False:
        backup = sum(normalized) * 75
        total_score = int(backup)

    return total_score

# Input data setup
data = [85, 170, 255, 45, 130, 200, 60]
weights = [0.8, 1.2, 0.5, 1.0]

# Noise simulation and cleanup (some irrelevant steps)
raw_input = [x + 10 for x in data]
denoised = filter_noisy_readings(raw_input)
scaled_input = [x - 10 for x in denoised]  # Restore original

# Key execution point
total_score = calculate_final_score(data, weights)
print(f"Result: {total_score}")