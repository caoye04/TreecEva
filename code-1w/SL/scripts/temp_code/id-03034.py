from collections import defaultdict, Counter

# Simulate sensor data with noise and redundancy
def generate_noisy_data():
    raw_data = [10, 15, 10, 20, 15, 25, 10, 30, 20, 15]
    noise_offsets = [2, -1, 0, 1, -2, 0, 1, 0, -1, 2]
    return [raw_data[i] + noise_offsets[i] for i in range(len(raw_data))]

def analyze_trends(data):
    trend_counter = defaultdict(int)
    for i in range(1, len(data)):
        if data[i] > data[i-1]:
            trend_counter['increasing'] += 1
        elif data[i] < data[i-1]:
            trend_counter['decreasing'] += 1
        else:
            trend_counter['stable'] += 1
    return trend_counter

def filter_outliers(data, threshold=25):
    filtered = [x for x in data if x <= threshold]
    outlier_count = len(data) - len(filtered)
    # Redundant tracking of outlier positions (not used later)
    outlier_positions = [i for i, x in enumerate(data) if x > threshold]
    return filtered

def compute_variance(data):
    mean_val = sum(data) / len(data)
    squared_diffs = [(x - mean_val) ** 2 for x in data]
    variance = sum(squared_diffs) / len(squared_diffs)
    std_dev = variance ** 0.5
    # Extra computation: normalize values (not used)
    normalized = [(x - mean_val) / (std_dev + 1e-8) for x in data]
    return variance

def assess_consistency(data):
    counts = Counter(data)
    mode_freq = max(counts.values())
    consistency_ratio = mode_freq / len(data)
    # Distractor logic: check for rare values
    rare_values = [k for k, v in counts.items() if v == 1]
    rare_sum = sum(rare_values)
    return consistency_ratio

def calculate_final_score(data, thresholds):
    # Step 1: Filter data
    clean_data = filter_outliers(data, threshold=thresholds['outlier'])
    
    # Step 2: Compute statistical properties
    var = compute_variance(clean_data)
    trend = analyze_trends(clean_data)
    consistency = assess_consistency(clean_data)
    
    # Step 3: Trend-based score adjustment
    trend_score = 0
    if trend['increasing'] >= trend['decreasing']:
        trend_score = 10
    else:
        trend_score = -5
    
    # Step 4: Variance penalty
    var_penalty = 0
    if var > thresholds['variance']:
        var_penalty = -8
    
    # Step 5: Consistency bonus
    consistency_bonus = int(consistency * 20)
    
    # Step 6: Apply all components
    base_score = 50
    final_score = base_score + trend_score + var_penalty + consistency_bonus
    
    # Irrelevant transformation chain (dead-end variables)
    temp_result = final_score * 1.05
    adjusted_temp = round(temp_result)
    capped_result = min(adjusted_temp, 100)
    
    return final_score

# Main execution
sensor_readings = generate_noisy_data()
data = sensor_readings.copy()

# Modify data slightly to introduce common value
if len(data) > 5:
    data[5] = 15  # Increase frequency of 15

thresholds = {
    'outlier': 25,
    'variance': 30
}

# Track auxiliary metrics (unused)
aux_metrics = {}
aux_metrics['length_before'] = len(sensor_readings)
aux_metrics['length_after'] = len(data)

final_score = calculate_final_score(data, thresholds)
print(f"Result: {final_score}")