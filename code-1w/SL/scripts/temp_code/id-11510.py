from itertools import combinations

# Simulate sensor data stream with noise and valid readings
def generate_filtered_data(raw_sequence):
    filtered = [x for x in raw_sequence if x > 0]
    smoothed = [sum(filtered[i:i+3]) / 3 for i in range(len(filtered) - 2)]
    return smoothed[:10]  # Return first 10 smoothed values

# Identify anomalous patterns using sliding window and threshold
def detect_anomalies(series, threshold=0.45):
    anomaly_count = 0
    moving_avg = sum(series) / len(series)
    variance_proxy = sum((x - moving_avg) ** 2 for x in series) / len(series)
    std_dev = variance_proxy ** 0.5
    
    for i in range(len(series) - 4):
        window = series[i:i+5]
        win_avg = sum(window) / 5
        if abs(win_avg - moving_avg) > threshold * std_dev:
            anomaly_count += 1
    
    # Distractor: unused calculation
    peak_magnitude = max(series) - min(series)
    normalized_energy = sum(x**2 for x in series)
    return anomaly_count

# Calculate composite score based on pattern diversity and stability
def calculate_pattern_richness(seq):
    subsequences = list(combinations(seq, 4))  # All 4-element combos
    unique_patterns = set()
    for sub in subsequences:
        diffs = tuple(round(b - a, 2) for a, b in zip(sub, sub[1:]))
        unique_patterns.add(diffs)
    
    diversity_index = len(unique_patterns)
    stability_factor = sum(1 for a, b in zip(seq, seq[1:]) if abs(b - a) < 0.1)
    
    # Irrelevant transformation
    transformed_seq = [x * 1.05 for x in seq]
    entropy_proxy = len(seq) / (diversity_index + 1e-5)
    
    return diversity_index * 0.7 + stability_factor * 0.3

# Main scoring logic
def calculate_final_score(time_series):
    baseline_ref = sum(time_series) / len(time_series)
    deviation_scores = [abs(x - baseline_ref) for x in time_series]
    avg_dev = sum(deviation_scores) / len(deviation_scores)
    
    # Use slice to analyze trend in second half
    recent_trend = time_series[len(time_series)//2:]
    trend_slope = recent_trend[-1] - recent_trend[0]
    
    # Primary components for final score
    anomaly_detector = detect_anomalies(time_series)
    richness_metric = calculate_pattern_richness(time_series)
    
    # Final score computation
    raw_score = (richness_metric * 1.5) - (anomaly_detector * 2.0) + (trend_slope * 0.5)
    final_score = int(round(raw_score))
    
    # Red herring variables
    temp_adjustment = baseline_ref * 0.1
    secondary_correction = sum(deviation_scores[i] for i in range(0, len(deviation_scores), 2))
    
    return final_score

# Simulated input: corrupted sensor readings with offset
raw_input_stream = [0.1, -0.5, 0.3, 0.25, 0.35, -0.2, 0.4, 0.38, 0.42, 0.41, -0.1, 0.44, 0.43]
data_window = generate_filtered_data(raw_input_stream)
final_score = calculate_final_score(data_window)
print(f"Result: {final_score}")