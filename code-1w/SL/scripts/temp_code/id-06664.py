import math

# Simulated system telemetry data
telemetry_stream = [14, 28, 19, 25, 33, 11, 22, 37, 41, 8]
baseline_threshold = 20
anomaly_window = 3

# Irrelevant signal processing functions (dead code path)
def apply_filter(signal):
    return [x * 0.9 for x in signal if x > 15]

def normalize_signal(signal):
    max_val = max(signal)
    return [x / max_val for x in signal]

# Unused transformation chain
temp_filtered = apply_filter(telemetry_stream)
normalized_telemetry = normalize_signal(telemetry_stream)

# Core diagnostic logic
anomaly_flags = []
for i in range(len(telemetry_stream)):
    window_start = max(0, i - anomaly_window + 1)
    window = telemetry_stream[window_start:i+1]
    window_avg = sum(window) / len(window)
    
    # Flag anomalies based on dynamic threshold
    dynamic_threshold = baseline_threshold * (1 + 0.1 * len([x for x in window if x > baseline_threshold]))
    if telemetry_stream[i] > dynamic_threshold and window_avg > baseline_threshold:
        anomaly_flags.append(True)
    else:
        anomaly_flags.append(False)

# Secondary metric: stability index
stability_index = 0
for i in range(1, len(telemetry_stream)):
    if abs(telemetry_stream[i] - telemetry_stream[i-1]) <= 5:
        stability_index += 1
stability_index = stability_index / (len(telemetry_stream) - 1) if len(telemetry_stream) > 1 else 0

# Log compilation with irrelevant fields
metrics_log = {
    "raw_sum": sum(telemetry_stream),
    "peak_value": max(telemetry_stream),
    "valid_readings": len([x for x in telemetry_stream if x >= 10]),
    "instability_events": len([x for x in telemetry_stream if x < 10 or x > 35]),
    "stability_ratio": stability_index,
    "anomaly_count": sum(1 for x in anomaly_flags if x),
    "system_age": 7,  # Red herring
    "calibration_offset": 0.05,  # Unused parameter
    "last_reboot_code": 201  # Misleading diagnostic code
}

# Decoy analysis function (never called)
calculate_risk_factor = lambda flags, log: sum(flags) * log["instability_events"] * 1.5

# Key evaluation logic
def evaluate_performance(flags, log_entry):
    base_score = 100
    
    # Deduct for anomalies
    anomaly_penalty = sum(1 for f in flags if f) * 8
    base_score -= anomaly_penalty
    
    # Adjust for stability
    if log_entry["stability_ratio"] > 0.6:
        base_score += 15
    elif log_entry["stability_ratio"] > 0.3:
        base_score += 5
    else:
        base_score -= 10
    
    # Bonus for high valid reading ratio
    valid_ratio = log_entry["valid_readings"] / len(telemetry_stream)
    if valid_ratio >= 0.9:
        base_score += 20
    elif valid_ratio >= 0.7:
        base_score += 10
    
    # Penalty for excessive instability events
    if log_entry["instability_events"] > 3:
        base_score -= log_entry["instability_events"] * 3
    
    # Apply logarithmic scaling (obscure but deterministic)
    adjusted_score = math.log(base_score) * 10
    
    # Final nonlinear transformation using modular arithmetic
    final = int((adjusted_score * 73) % 997)
    
    # Dead computation branch (distractor)
    if final > 500:
        final = final // 2 + 25  # Never executed due to mod cap
        
    return final

# Execution point of interest
final_score = evaluate_performance(anomaly_flags, metrics_log)

# Irrelevant post-processing
encryption_key = 0
for i, val in enumerate(telemetry_stream):
    encryption_key ^= (val * (i + 1)) % 256

# Output result as required
print(f"Result: {final_score}")