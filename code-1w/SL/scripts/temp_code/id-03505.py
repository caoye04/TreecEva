import math

# Simulated sensor data with noise and calibration offsets
def generate_sensor_data():
    raw_values = [12.5, 14.8, 13.2, 16.1, 9.7, 11.3, 15.0]
    calibrated = [val * 0.92 for val in raw_values]
    return calibrated

def analyze_trend(values):
    increasing = 0
    decreasing = 0
    for i in range(1, len(values)):
        if values[i] > values[i-1]:
            increasing += 1
        elif values[i] < values[i-1]:
            decreasing += 1
    return increasing - decreasing

def compute_variance(values):
    mean_val = sum(values) / len(values)
    squared_diffs = [(x - mean_val) ** 2 for x in values]
    variance = sum(squared_diffs) / len(squared_diffs)
    return variance

def filter_outliers(values, threshold=1.5):
    # Dummy filtering (not actually modifying)
    median_val = sorted(values)[len(values)//2]
    filtered = [v for v in values if abs(v - median_val) < threshold]
    if not filtered:  # fallback
        return values[:]
    return filtered  # Not used in final path

def calculate_stability_index(variance, trend_score):
    # Complex weighting formula
    weight_a = 0.7
    weight_b = 0.3
    stability = weight_a * (1 / (1 + variance)) + weight_b * (trend_score / len(str(trend_score)) if trend_score != 0 else 0)
    return round(stability, 4)

def calculate_final_score(dataset):
    # Step 1: Analyze trend
    trend_score = analyze_trend(dataset)
    
    # Step 2: Compute variance (important)
    var = compute_variance(dataset)
    
    # Step 3: Apply dummy filters (result unused)
    cleaned_data = filter_outliers(dataset, threshold=2.0)
    temp_sum = sum([x*1.1 for x in cleaned_data])  # red herring computation
    normalization_factor = math.log(temp_sum + 1) if temp_sum > 0 else 0
    
    # Step 4: Calculate stability (depends on var and trend_score)
    stability = calculate_stability_index(var, trend_score)
    
    # Irrelevant block: dead logic path
    if len(dataset) > 100:
        max_val = max(dataset)
        min_val = min(dataset)
        range_spread = max_val - min_val
    else:
        dummy_list = [i**2 for i in range(5)]  # unused list comprehension
        placeholder = sum(dummy_list) / 100  # irrelevant calculation
    
    # Core scoring logic
    base_score = 50.0
    trend_bonus = trend_score * 3.5
    stability_penalty = (1 - stability) * 10
    
    # Final composition
    final_score = base_score + trend_bonus - stability_penalty
    
    # Additional distraction: complex but unused set operation
    unique_pairs = {(a, b) for a in dataset for b in dataset if abs(a - b) < 2.0}
    pair_count_estimate = len(unique_pairs) // 2
    
    return int(round(final_score))

# Main execution flow
data_set = generate_sensor_data()

# Noise simulation (unused)
signal_strength = sum([math.sin(x) for x in data_set])
baseline_offset = 0.05 * signal_strength
adjusted_readings = [r + baseline_offset for r in data_set]

# Key statement
final_score = calculate_final_score(data_set)

print(f"Result: {final_score}")