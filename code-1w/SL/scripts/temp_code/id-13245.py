def normalize_values(data):
    max_val = max(data)
    return [x / max_val for x in data]

# Simulate sensor readings from a monitoring system
temperature_readings = [22.5, 23.0, 21.8, 24.1, 23.7]
humidity_readings = [45, 47, 44, 50, 49]
pressure_readings = [1013, 1015, 1012, 1016, 1014]

# Normalize all sensor data
temp_norm = normalize_values(temperature_readings)
humid_norm = normalize_values(humidity_readings)
pressure_norm = normalize_values([float(p) for p in pressure_readings])

# Aggregate baseline metrics
baseline_metrics = []
for i in range(len(temp_norm)):
    avg_sensor = (temp_norm[i] + humid_norm[i] + pressure_norm[i]) / 3
    baseline_metrics.append(avg_sensor)

# Misleading computation - not used in final result
drift_detection = [abs(baseline_metrics[i] - baseline_metrics[i-1]) for i in range(1, len(baseline_metrics))]
threshold_exceeded = any(d > 0.1 for d in drift_detection)

# Real-time anomaly tracking (unused distractor)
current_state = "stable"
anomaly_count = 0
for val in baseline_metrics:
    if val > 0.95 or val < 0.05:
        anomaly_count += 1
        current_state = "unstable"

# Weighted performance evaluation
metrics = [0.88, 0.76, 0.91, 0.67, 0.82]  # Processed KPIs
weights = [0.2, 0.1, 0.3, 0.15, 0.25]   # Importance weights

# Red herring: string-based status check
status_flags = ["OK", "OK", "WARNING", "OK", "CRITICAL"]
flag_points = 0
for flag in status_flags:
    if 'CRITICAL' in flag:
        flag_points -= 1
    elif 'WARNING' in flag:
        flag_points += 0.5

# Actual scoring logic
def evaluate_performance(mets, wts):
    raw_score = sum(m * w for m, w in zip(mets, wts))
    
    # Apply non-linear adjustment based on consistency
    variance_penalty = 0
    mean_metric = sum(mets) / len(mets)
    for m in mets:
        if abs(m - mean_metric) > 0.1:
            variance_penalty += 0.01
    
    adjusted_score = raw_score - variance_penalty
    
    # Additional irrelevant transformation
    temp_str = f"Score: {adjusted_score:.3f}"
    temp_str = temp_str.replace(".", "p").upper()
    temp_length = len(temp_str)
    
    # Dummy entropy-like calculation
    import math
    dummy_entropy = 0
    for c in temp_str:
        if c.isalpha():
            dummy_entropy += math.log(ord(c))
    
    # Final score unaffected by above
    return int(adjusted_score * 100)  # Discretize to integer

final_score = evaluate_performance(metrics, weights)
print(f"Result: {final_score}")