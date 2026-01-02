from collections import defaultdict, Counter

# Simulate sensor data with noise and validity flags
def generate_noisy_data():
    raw_values = [23.5, 24.1, 22.8, 25.6, 23.9, 24.0, 23.7]
    timestamps = ['t0', 't1', 't2', 't3', 't4', 't5', 't6']
    validity = [True, True, False, True, True, True, False]
    return list(zip(timestamps, raw_values, validity))

def analyze_trends(series):
    trend_counter = defaultdict(int)
    for i in range(1, len(series)):
        if series[i] > series[i-1]:
            trend_counter['increase'] += 1
        elif series[i] < series[i-1]:
            trend_counter['decrease'] += 1
        else:
            trend_counter['stable'] += 1
    return trend_counter

def calculate_final_score(data, thresholds):
    # Extract valid sensor readings
    valid_readings = []
    invalid_count = 0
    temp_sum = 0.0
    
    for ts, value, valid in data:
        if valid:
            valid_readings.append(value)
            temp_sum += value
        else:
            invalid_count += 1
    
    # Irrelevant distraction: count digit occurrences in timestamps (unused)
    digit_frequency = Counter()
    for t_stamp, _, _ in data:
        for char in t_stamp:
            if char.isdigit():
                digit_frequency[char] += 1
    
    # Compute moving average for smoothing (semi-relevant)
    smoothed = []
    window_size = 3
    for i in range(len(valid_readings)):
        start = max(0, i - window_size + 1)
        segment = valid_readings[start:i+1]
        smoothed.append(sum(segment) / len(segment))
    
    # Analyze trend patterns
    trends = analyze_trends(smoothed)
    
    # Distraction: simulate redundant flag analysis
    increase_weight = 1.0
    decrease_weight = 0.8
    stability_bonus = 0.1
    decay_factor = 0.95
    
    base_score = temp_sum / len(valid_readings) if valid_readings else 0
    
    # Apply conditional adjustments based on trend strength
    adjustment = 0
    if trends['increase'] > thresholds['min_increases']:
        adjustment += 2.5
    if trends['decrease'] >= thresholds['max_decreases_allowed']:
        adjustment -= 1.8
    if trends['stable'] > 2:
        adjustment += stability_bonus * trends['stable']
    
    # Secondary distraction: unused loop over enumerate with dummy logic
    cumulative_offset = 0
    for idx, val in enumerate(smoothed):
        if idx % 2 == 0:
            cumulative_offset += 0.01 * idx
        else:
            continue  # Dead code path
    
    # Final computation chain
    volatility = max(smoothed) - min(smoothed)
    penalty = 0
    if volatility > thresholds['volatility_cap']:
        penalty = (volatility - thresholds['volatility_cap']) * 0.7
    
    final_score = base_score + adjustment - penalty
    
    # This print is required to show result
    print(f"Result: {final_score}")
    return final_score

# Main execution block
data = generate_noisy_data()
thresholds = {
    'min_increases': 2,
    'max_decreases_allowed': 1,
    'volatility_cap': 2.0
}
final_score = calculate_final_score(data, thresholds)