import math

# Simulated sensor fusion system for environmental monitoring
sensors = ['temp', 'pressure', 'humidity', 'co2', 'pm25']
data_log = [
    [23.5, 1013.25, 45.0, 415, 12],
    [24.1, 1012.8, 47.3, 421, 15],
    [22.8, 1014.1, 43.7, 409, 11],
    [25.6, 1011.9, 50.2, 435, 18],
    [26.7, 1010.5, 52.8, 450, 23]
]

# Irrelevant calibration coefficients (distractor)
calibration_offsets = {s: (i + 1) * 0.07 for i, s in enumerate(sensors)}
temp_correction_factor = 1.02

# Real metric weights for analysis (used later)
metric_weights = {
    'temp': 0.15,
    'pressure': 0.1,
    'humidity': 0.2,
    'co2': 0.25,
    'pm25': 0.3
}

# Dummy transformation to mislead (dead code path)
def deprecated_normalize(data):
    max_val = max(data)
    return [x / max_val for x in data]  # Never called

# Preprocessing with list comprehension and zip
processed_metrics = []
for idx, reading in enumerate(data_log):
    adjusted = [
        val * (0.98 + i * 0.01) for i, val in enumerate(reading)  # Minor adjustment
    ]
    zipped = list(zip(sensors, adjusted))
    processed_metrics.append({
        sensor: value * metric_weights[sensor] for sensor, value in zipped
    })

# Extraneous signal smoothing function (not used)
def smooth_signal(signal, window=3):
    smoothed = []
    for i in range(len(signal)):
        start = max(0, i - window // 2)
        end = min(len(signal), i + window // 2 + 1)
        smoothed.append(sum(signal[start:end]) / (end - start))
    return smoothed

# Threshold configuration map (actually used)
threshold_map = {
    'temp': (22.0, 26.0),
    'pressure': (1010.0, 1015.0),
    'humidity': (40.0, 50.0),
    'co2': (400, 440),
    'pm25': (10, 20)
}

# Auxiliary diagnostic function (red herring)
def legacy_diagnostic(metrics):
    score = 0
    for m in metrics:
        if m.get('temp', 0) > 25:
            score += 10
    return score * 1.5  # Unused result

# Core analysis logic with lambda and enumerate
def analyze_signals(metrics_list, thresholds):
    anomaly_scores = []
    for i, metrics in enumerate(metrics_list):
        # Compute deviation using lambda
        deviations = map(lambda item: 
            abs(metrics[item[0]] - (thresholds[item[0]][0] + thresholds[item[0]][1]) / 2 * metric_weights[item[0]]),
            filter(lambda x: x[0] in metrics and x[0] in thresholds, 
                   [(k, v) for k, v in metric_weights.items()])
        )
        total_deviation = sum(deviations)
        anomaly_scores.append(total_deviation)
    
    # Apply conditional weighting based on sequence position
    weighted_scores = [
        score * (1.1 if i % 2 == 0 else 0.9) for i, score in enumerate(anomaly_scores)
    ]
    
    # Final aggregation
    base_aggregate = sum(weighted_scores)
    
    # Secondary transformation (looks important but is actually fixed)
    secondary_buffer = [base_aggregate * 0.1] * 3
    secondary_sum = sum(secondary_buffer)
    
    # Tertiary adjustment using trigonometric red herring
    angle_radians = math.radians(45)
    cosine_weight = math.cos(angle_radians)  # Constant value, misleading
    
    final_value = base_aggregate + secondary_sum * cosine_weight
    
    # Dead branch - never executes due to data constraints
    if final_value < 0:
        fallback_correction = 0
        for j in range(5):
            fallback_correction += j ** 2
        final_value -= fallback_correction
    
    return final_value

# Spurious data transformation (unused)
transformed_logs = [
    {s: d[i] for i, s in enumerate(sensors)} for d in data_log
]

# Key execution point
final_diagnostic = analyze_signals(processed_metrics, threshold_map)

# Irrelevant caching layer
cache_key = hash(str(final_diagnostic)[:5])
lookup_table = {cache_key: final_diagnostic * 1.001}  # Not accessed

# Output result
print(f"Result: {final_diagnostic}")