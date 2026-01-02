from collections import defaultdict

# Simulate sensor data aggregation and scoring with noise filtering
def process_sensor_data(raw_readings):
    filtered = []
    noise_count = 0
    for val in raw_readings:
        if abs(val - 50.0) > 40:  # Filter extreme outliers
            noise_count += 1
            continue
        if val < 30:
            adjusted = val * 1.2
        elif val > 70:
            adjusted = val * 0.9
        else:
            adjusted = val + 5
        filtered.append(adjusted)
    
    # Irrelevant tracking
    stats = defaultdict(int)
    for v in filtered:
        if v < 40:
            stats['low'] += 1
        elif v < 60:
            stats['medium'] += 1
        else:
            stats['high'] += 1
    
    return filtered

# Weighted scoring with normalization
def normalize(values):
    total = sum(values)
    if total == 0:
        return [0] * len(values)
    return [v / total for v in values]

# Complex scoring logic with distractors
def calculate_final_score(data, weights):
    base_scores = [d * 0.8 for d in data]
    
    # Distractor: entropy calculation not used in final score
    from math import log
    entropy = 0
    prob_dist = normalize(base_scores)
    for p in prob_dist:
        if p > 0:
            entropy -= p * log(p, 2)
    
    # Actual scoring path
    weighted = [b * w for b, w in zip(base_scores, weights)]
    avg_weighted = sum(weighted) / len(weighted)
    
    # Secondary adjustment based on data characteristics
    median_guess = sorted(base_scores)[len(base_scores)//2]
    adjustment_factor = 1.0
    if median_guess > 45:
        adjustment_factor = 1.1
    elif median_guess < 35:
        adjustment_factor = 0.95
    
    preliminary = avg_weighted * adjustment_factor
    
    # Apply diminishing returns
    final_score = preliminary * (0.95 ** (len(data) > 8))  # Minor penalty if many readings
    
    # Red herring: unused transformation
    transformed = [round(x**0.5, 3) for x in weighted]
    
    return round(final_score, 4)

# Main execution
raw_data = [25, 67, 89, 45, 33, 72, 58, 41, 60, 29, 95, 54]
weights = [0.1, 0.15, 0.2, 0.1, 0.05, 0.1, 0.05, 0.1, 0.05, 0.05]

# Process data
processed = process_sensor_data(raw_data)

# Normalize weights (even though already normalized)
dummy_normalized_weights = normalize(weights)

# Calculate final score
cutoff = 40
extra_filter = [x for x in processed if x > cutoff]  # Unused branch

final_score = calculate_final_score(processed, weights)
print(f"Result: {final_score}")