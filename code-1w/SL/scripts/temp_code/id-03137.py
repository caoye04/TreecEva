from collections import defaultdict, Counter
import math

# Simulated sensor array data for a distributed environmental monitoring system
temperature_reads = [23.4, 24.1, 22.9, 25.3, 26.0, 24.8, 23.9]
humidity_reads = [45, 47, 50, 52, 48, 55, 53]
pressure_reads = [1013, 1015, 1012, 1010, 1008, 1011, 1014]

# Irrelevant auxiliary data (distractor)
color_spectrum = ['red', 'green', 'blue', 'infrared']
spectral_weights = {'red': 0.25, 'green': 0.35, 'blue': 0.30, 'infrared': 0.10}
weighted_avg = sum(spectral_weights[c] for c in color_spectrum)

# Baseline calibration map (used later)
baseline_readings = {
    'temp_norm': 24.0,
    'humidity_norm': 50,
    'pressure_norm': 1012
}

# Derived metrics with red herrings
avg_temp = sum(temperature_reads) / len(temperature_reads)
median_humidity = sorted(humidity_reads)[len(humidity_reads)//2]
std_dev_pressure = (sum((p - sum(pressure_reads)/len(pressure_reads))**2 for p in pressure_reads) / len(pressure_reads)) ** 0.5

# Bit manipulation decoy (irrelevant to final result)
decoys = []
for i in range(5):
    val = (i << 3) | 7
    decoys.append(val ^ 5)

# Health signature generation (core logic starts here)
health_signature = []
for t, h, p in zip(temperature_reads, humidity_reads, pressure_reads):
    t_score = abs(t - baseline_readings['temp_norm']) * 1.5
    h_score = max(0, abs(h - baseline_readings['humidity_norm']) - 2) * 1.2
    p_score = min(5, (abs(p - baseline_readings['pressure_norm']) / 3) * 2)
    
    # Composite health index per reading
    composite = round(t_score + h_score + p_score, 3)
    health_signature.append(composite)

# Unused transformation path (dead code path - distractor)
def transform_readings(data_list, factor=1.1):
    return [x * factor for x in data_list if x > 0]

transformed_temp = transform_readings(temperature_reads, 1.05)
transformed_humid = transform_readings(humidity_reads, 0.98)

# Aggregation using defaultdict (actual usage)
aggregated_diagnostics = defaultdict(float)
for i, score in enumerate(health_signature):
    category = 'high' if score > 3.0 else 'moderate' if score > 1.5 else 'low'
    aggregated_diagnostics[category] += score

# Misleading intermediate summary (distractor)
summary_report = {
    'total_anomalies': len([s for s in health_signature if s > 2.0]),
    'peak_stress': max(health_signature),
    'stability_index': 100 * math.exp(-sum(health_signature)/10)
}

# Core processing function with lambda and set operations
outlier_threshold = 2.5
filter_outliers = lambda scores: {s for s in scores if s >= outlier_threshold}

valid_metrics = set(health_signature) - filter_outliers(health_signature)  # Remove high outliers

# Final processing with Counter and conditional weighting
def process_metrics(signature, baseline):
    count_dist = Counter(signature)
    base_adjustment = (baseline['temp_norm'] - 20) * 0.1
    
    # Simulate diagnostic decay over readings
    weighted_sum = 0.0
    for idx, val in enumerate(signature):
        decay = 0.95 ** idx
        contribution = val * decay * (1 + base_adjustment)
        weighted_sum += contribution
    
    # Apply correction based on mode frequency (decoy branch)
    most_common_val, freq = count_dist.most_common(1)[0]
    if freq > 2:
        weighted_sum *= 0.9  # supposed 'overfitting' correction
    
    # Set-based integrity check (actually affects logic)
    unique_count = len(set(signature))
    if unique_count < len(signature) * 0.5:
        weighted_sum += 5.0  # entropy penalty
    
    return round(weighted_sum, 4)

# Critical execution point
final_diagnostic = process_metrics(health_signature, baseline_readings)
print(f"Result: {final_diagnostic}")