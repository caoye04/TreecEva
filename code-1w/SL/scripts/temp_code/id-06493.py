import math

# Simulated sensor array data from environmental monitoring station
temperature_readings = [23.5, 24.1, 22.8, 25.0, 26.3, 27.1, 25.8, 24.7, 23.9, 22.5]
humidity_readings = [45, 47, 50, 55, 60, 62, 58, 53, 49, 46]
pressure_readings = [1013, 1012, 1015, 1017, 1016, 1014, 1013, 1011, 1010, 1009]

# Irrelevant auxiliary arrays (distractors)
sound_levels = [32, 35, 38, 40, 42, 39, 36, 34, 33, 31]  # Unused in final calculation
light_intensity = [800, 850, 900, 950, 1000, 980, 920, 870, 830, 810]  # Dead code path

# Preprocessing function with red herring logic
def normalize(data, scale=1.0):
    mean_val = sum(data) / len(data)
    normalized = [(x - mean_val) * scale for x in data]
    return normalized

# Misleading transformation chain
temp_normalized = normalize(temperature_readings, 1.1)
humid_normalized = normalize(humidity_readings, 0.9)
press_normalized = normalize(pressure_readings, 0.01)

# Decoy function that appears important but is unused
def calculate_air_quality_index(t, h, p):
    # Complex formula that looks relevant
    t_idx = sum([(x - 25)**2 for x in t]) / len(t)
    h_idx = sum([abs(x - 50) for x in h]) / len(h)
    p_idx = max(p) - min(p)
    return (t_idx * 0.4) + (h_idx * 0.3) + (p_idx * 0.3)

# Another decoy: entropy-based analysis (unused)
def estimate_entropy(data):
    freq_map = {}
    for val in data:
        freq_map[val] = freq_map.get(val, 0) + 1
    total = len(data)
    entropy = -sum((count/total) * math.log2(count/total) for count in freq_map.values())
    return entropy

# Real processing begins here — subtle shift in focus
def filter_outliers(data, threshold=1.5):
    median_val = sorted(data)[len(data)//2]
    deviations = [abs(x - median_val) for x in data]
    mad = sorted(deviations)[len(deviations)//2]  # Median absolute deviation
    if mad == 0:
        return data
    modified_z_scores = [0.6745 * (x - median_val) / mad for x in data]
    return [data[i] for i in range(len(data)) if abs(modified_z_scores[i]) < threshold]

# Apply filtering to temperature only (key relevance)
clean_temps = filter_outliers(temperature_readings, threshold=1.8)

# Secondary processing: detect trend reversals
def count_trend_reversals(data):
    if len(data) < 3:
        return 0
    reversals = 0
    for i in range(1, len(data) - 1):
        left_diff = data[i] - data[i-1]
        right_diff = data[i+1] - data[i]
        if (left_diff > 0 and right_diff < 0) or (left_diff < 0 and right_diff > 0):
            reversals += 1
    return reversals

# Extract features from cleaned data
temp_reversals = count_trend_reversals(clean_temps)

# Hidden critical transformation using lambda and list comprehension
baseline_ref = 24.0
adjusted_deltas = list(map(lambda x: round(x - baseline_ref, 2), clean_temps))
positive_shifts = [delta for delta in adjusted_deltas if delta > 0]
negative_shifts = [delta for delta in adjusted_deltas if delta < 0]

# Compute asymmetry index (actual core logic)
asymmetry_index = len(positive_shifts) - len(negative_shifts)

# Simulate diagnostic scoring with multiple irrelevant inputs
diagnostic_weights = {
    'stability': 0.3,
    'variance_penalty': 0.2,
    'reversal_count': 0.1,
    'asymmetry': 0.4
}

# Fake components to mislead
fake_stability_score = 100 - (max(temperature_readings) - min(temperature_readings)) * 2
fake_variance = sum([(x - sum(temperature_readings)/len(temperature_readings))**2 for x in temperature_readings]) / len(temperature_readings)
fake_reversal_bogus = estimate_entropy(sound_levels)  # Red herring call

# Actual diagnostic uses only one real component despite appearance
processed_data = {
    'size': len(clean_temps),
    'reversals': temp_reversals,
    'asymmetry': asymmetry_index,
    'dummy_ignored': fake_variance  # Included but not used
}

# Final analysis function — narrow actual dependency
def analyze_readings(data_dict):
    size_factor = data_dict['size'] * 0.5
    reversal_impact = 0
    if data_dict['reversals'] > 2:
        reversal_impact = -5
    else:
        reversal_impact = 3
    
    # Only asymmetry contributes meaningfully
    asymmetry_contribution = data_dict['asymmetry'] * 7
    
    # Final result built from mostly irrelevant structure
    score = size_factor + reversal_impact + asymmetry_contribution
    
    # Additional distraction: unused conditional branch
    if data_dict['size'] > 100:
        extra_correction = math.sin(score)
        score += extra_correction  # Never reached
    
    return int(round(score))

# Execute key statement
final_diagnostic = analyze_readings(processed_data)

# Print result as required
print(f"Target result: {final_diagnostic}")