from itertools import combinations

# Simulate signal processing from sensor array
def analyze_peaks(signal):
    peak_count = 0
    temp_energy = 0
    for i in range(1, len(signal) - 1):
        if signal[i-1] < signal[i] > signal[i+1]:
            peak_count += 1
            temp_energy += signal[i] ** 0.5
    return peak_count

# Process time-series segments with weighted aggregation
def process_segments(data, weight_map):
    raw_segments = [x for x in data if x > 0]
    normalized = [round(x / sum(raw_segments), 4) for x in raw_segments]
    
    # Irrelevant combination generation (distractor)
    combo_count = 0
    for r in range(2, 4):
        for _ in combinations(normalized, r):
            combo_count += 1
    
    # Actual computation path
    weighted_sum = 0.0
    for i, val in enumerate(normalized):
        if i % 2 == 0:
            weighted_sum += val * weight_map.get('even', 1.2)
        else:
            weighted_sum += val * weight_map.get('odd', 0.8)
    
    # Dead code: this block is never executed due to logic above
    if len(normalized) > 100:
        fallback = 0
        for j in range(len(normalized)):
            fallback += normalized[j] * j
        weighted_sum = fallback

    final_score = int(weighted_sum * 1000)
    return final_score

# Sensor readings (simulated)
sensor_signal = [12, 34, 21, 55, 18, 42, 9, 61, 33]
segment_data = [sum(sensor_signal[i:i+3]) for i in range(0, len(sensor_signal), 3)]
weights = {'even': 1.5, 'odd': 0.7, 'bonus': 2.0}

# Analyze peaks (irrelevant to final result but adds cognitive load)
peak_analysis = analyze_peaks(sensor_signal)
scaling_factor = peak_analysis * 0.5

# Key execution point
final_score = process_segments(segment_data, weights)
print(f"Result: {final_score}")