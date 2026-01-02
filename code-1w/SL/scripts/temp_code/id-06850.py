from itertools import combinations
import math

# Simulated sensor data from environmental monitoring stations
temperature_readings = [23.5, 24.1, 22.9, 25.3, 26.0, 24.8, 23.7]
humidity_readings = [45, 48, 52, 44, 55, 49, 51]
co2_levels = [410, 415, 420, 405, 430, 418, 425]

# Auxiliary function to smooth noisy sensor inputs
def smooth_signal(signal):
    smoothed = []
    for i in range(len(signal)):
        start = max(0, i - 1)
        end = min(len(signal), i + 2)
        window_avg = sum(signal[start:end]) / (end - start)
        smoothed.append(round(window_avg, 2))
    return smoothed

# Apply smoothing to raw data
temp_smooth = smooth_signal(temperature_readings)
humi_smooth = smooth_signal(humidity_readings)
co2_smooth = smooth_signal(co2_levels)

# Normalize readings to 0-1 scale using min-max scaling
def normalize(data):
    min_val, max_val = min(data), max(data)
    return [(x - min_val) / (max_val - min_val) if max_val != min_val else 0 for x in data]

normalized_temp = normalize(temp_smooth)
normalized_humi = normalize(humi_smooth)
normalized_co2 = normalize(co2_smooth)

# Misleading distraction: analyze all 3-element subsequences for "anomalies"
anomaly_candidates = []
for i in range(len(normalized_temp) - 2):
    subseq = normalized_temp[i:i+3]
    variance = sum((x - sum(subseq)/3)**2 for x in subseq) / 3
    if variance > 0.01:
        anomaly_candidates.append((i, round(variance, 4)))

# Irrelevant computation: generate all pairwise correlations between indices
index_pairs = list(combinations(range(5), 2))
pairwise_metrics = {}
for i, j in index_pairs:
    diff_metric = abs(normalized_temp[i] - normalized_temp[j])
    pairwise_metrics[(i,j)] = round(diff_metric, 3)

# Real metric weights based on empirical calibration
metric_weights = {
    'temperature': 0.4,
    'humidity': 0.3,
    'co2': lambda x: 0.3 * (1 + math.sin(x * math.pi / len(x))) # Weight modulated by position
}

# Core evaluation logic
def evaluate_performance(weights, norm_data):
    # Extract aggregated central tendencies
    temp_base = sum(norm_data[0]) / len(norm_data[0])
    humi_base = sum(norm_data[1]) / len(norm_data[1])
    co2_base = sum(norm_data[2]) / len(norm_data[2])
    
    # Position-dependent CO2 weight adjustment using lambda
    adjusted_co2_weight = sum(
        weights['co2']([co2_base] * 3) for _ in range(2)
    ) / 2
    
    # Composite score calculation
    composite = (
        weights['temperature'] * temp_base +
        weights['humidity'] * humi_base +
        adjusted_co2_weight * co2_base
    )
    
    # Secondary adjustment based on data stability
    stability_factor = 1.0
    for data in norm_data:
        diffs = [abs(data[i] - data[i-1]) for i in range(1, len(data))]
        avg_diff = sum(diffs) / len(diffs) if diffs else 0
        if avg_diff > 0.1:
            stability_factor *= 0.95
    
    # Final weighted performance score
    final_raw = composite * stability_factor
    
    # Distractor: unused transformation chain
    transformed = list(map(lambda x: x**2 + 0.1, norm_data[0]))
    entropy = -sum(x * math.log(x + 1e-8) for x in transformed)
    
    return round(final_raw * 100, 2)  # Scale to percentage-like metric

# Execute main evaluation
final_score = evaluate_performance(metric_weights, [normalized_temp, normalized_humi, normalized_co2])

# Print result as required
print(f"Result: {final_score}")