from itertools import combinations

def analyze_temperature_patterns(data):
    # Irrelevant pattern analysis (distractor)
    increasing_trends = []
    decreasing_trends = []
    for i in range(len(data) - 2):
        if data[i] < data[i+1] < data[i+2]:
            increasing_trends.append((i, i+2))
        elif data[i] > data[i+1] > data[i+2]:
            decreasing_trends.append((i, i+2))
    
    # Semi-relevant transformation: normalize around mean
    mean_val = sum(data) / len(data)
    normalized = [round(x - mean_val, 2) for x in data]
    
    # Misleading secondary metric
    volatility = sum(abs(normalized[i] - normalized[i+1]) for i in range(len(normalized)-1))
    
    return normalized

def filter_outliers(values, threshold=2.0):
    mean_v = sum(values) / len(values)
    std_dev = (sum((x - mean_v)**2 for x in values) / len(values)) ** 0.5
    filtered = [v for v in values if abs(v - mean_v) <= threshold * std_dev]
    
    # Dead code path - never used later (distractor)
    if len(filtered) < len(values) * 0.5:
        return values  # fallback that won't trigger
    
    return filtered

def transform_case(strings):
    # Case conversion logic with red herring
    upper_count = sum(1 for s in strings if s.isupper())
    lower_count = sum(1 for s in strings if s.islower())
    mixed_count = len(strings) - upper_count - lower_count
    
    # Distractor: unused metrics
    entropy_estimate = (upper_count + mixed_count * 0.5) / len(strings) if strings else 0
    
    return [s.upper() if len(s) % 2 == 0 else s.lower() for s in strings]

def calculate_final_score(data_points):
    # Core scoring logic
    weights = [0.1, 0.2, 0.3, 0.4]
    weighted_sum = sum(d * w for d, w in zip(data_points, weights))
    
    # Apply nonlinearity
    score = pow(weighted_sum, 2) if weighted_sum > 0 else 0
    
    # Final adjustment based on parity of sum
    total = int(sum(data_points))
    if total % 2 == 0:
        score += 5
    else:
        score -= 3
    
    return int(score)

# Main execution flow
raw_temperatures = [23.5, 24.1, 22.9, 25.6]
raw_labels = ['cold', 'warm', 'cool', 'hot']

# Step 1: Process temperature sequence
adjusted_temps = analyze_temperature_patterns(raw_temperatures)

# Step 2: Simulate sensor correction (has side effect of rounding)
corrected_temps = [round(t + 0.1, 1) for t in adjusted_temps]

# Step 3: Filter spurious readings (though none will be removed)
filtered_temps = filter_outliers(corrected_temps, threshold=3.0)

# Step 4: Transform labels - includes irrelevant operation
cased_labels = transform_case(raw_labels)
label_length_sum = sum(len(label) for label in cased_labels)  # semi-irrelevant

# Step 5: Generate derived features using lambda and enumerate
feature_engineer = lambda x, i: x * (i + 1) * 0.5
enhanced_features = [feature_engineer(val, idx) for idx, val in enumerate(filtered_temps)]

# Step 6: Use itertools to generate pairs for validation (but only size matters)
pairwise_combinations = list(combinations(filtered_temps, 2))
combination_count = len(pairwise_combinations)  # distractor variable

# Step 7: Normalize feature set before scoring
processed_data = [min(f, 10) for f in enhanced_features]  # clamp values

# Step 8: Calculate final score (key statement)
final_score = calculate_final_score(processed_data)

print(f"Result: {final_score}")