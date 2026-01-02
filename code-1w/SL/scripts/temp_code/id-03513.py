import math

# Simulated sensor fusion system for autonomous drone navigation
def analyze_stability(readings):
    filtered = [x for x in readings if abs(x) > 0.1]
    return sum(filtered) / len(filtered) if filtered else 0

def calculate_variance(data):
    mean = sum(data) / len(data)
    return sum((x - mean) ** 2 for x in data) / len(data)

def detect_outliers(values, threshold=2):
    var = calculate_variance(values)
    std_dev = math.sqrt(var)
    mean = sum(values) / len(values)
    return [v for v in values if abs(v - mean) > threshold * std_dev]

def normalize_signal(signal):
    max_val = max(abs(x) for x in signal)
    return [x / max_val for x in signal] if max_val != 0 else signal

def integrate_sensor_data(primary, secondary):
    # Misleading fusion with irrelevant weighting
    alpha = 0.7
    beta = 0.4  # Unused weight (red herring)
    gamma = 0.3
    combined = [alpha * p + gamma * s for p, s in zip(primary, secondary)]
    
    # Dead code path - never executed due to logic
    if len(primary) < 0:  # Impossible condition
        combined = [math.sin(x) for x in combined]
    
    return normalize_signal(combined)

def assess_risk_level(value):
    if value < -1.0:
        return 'CRITICAL'
    elif value < 0:
        return 'WARNING'
    else:
        return 'NORMAL'

# Irrelevant telemetry logging (distractor)
def log_telemetry(timestamp, data):
    entry = f"[{timestamp}] SYS_MONITOR: {sum(data)} | {len(data)}"
    # Simulated log buffer (never used)
    logs = []
    logs.append(entry)
    return None  # No actual logging

def recursive_filter(sequence, depth=0):
    if depth >= 3 or len(sequence) < 2:
        return sequence
    smoothed = [(sequence[i] + sequence[i+1]) / 2 for i in range(len(sequence)-1)]
    return recursive_filter(smoothed, depth + 1)

def evaluate_performance(metrics, weights):
    # Complex weighted scoring with red herrings
    base_score = 0
    penalty = 0
    
    # Meaningful metrics processing
    for i, (name, val) in enumerate(metrics.items()):
        weight = weights.get(name, 0)
        if name == 'stability_index':
            base_score += val * weight
        elif name == 'response_time':
            base_score += (1.0 / val) * weight if val > 0 else 0
        elif name == 'data_consistency':
            adjustment = 10 if val > 0.8 else -5
            base_score += val * weight + adjustment
        else:
            # Unused branches (distractions)
            if val < 0:
                penalty += 2
    
    # Decoy calculation with unused variables
    theoretical_max = sum(weights.values()) * 100
    efficiency_ratio = base_score / theoretical_max if theoretical_max else 0
    hidden_bias = 3.14159 * 0.01  # Distractor constant
    
    # Critical result computation
    final_score = base_score - penalty + hidden_bias * 0  # Neutralized term
    
    # Dead code block (misleading)
    temp_result = []
    for x in range(5):
        temp_result.append(x ** 2 - x)  # Computation has no effect
    
    return final_score

# Main execution flow
if __name__ == "__main__":
    # Simulated drone sensor inputs
    gyro_readings = [0.12, -0.05, 0.33, 0.21, -0.18, 0.09, 0.44, -0.22]
    accel_readings = [0.08, 0.11, -0.03, 0.25, 0.19, -0.07, 0.31, 0.14]
    
    # Irrelevant preprocessing (distraction)
    outlier_gyro = detect_outliers(gyro_readings)
    outlier_accel = detect_outliers(accel_readings)
    
    # Log generation (no side effects)
    log_telemetry("2023-11-15T08:34:22", gyro_readings)
    log_telemetry("2023-11-15T08:34:23", accel_readings)
    
    # Signal integration
    fused_signal = integrate_sensor_data(gyro_readings, accel_readings)
    processed = recursive_filter(fused_signal)
    
    # Stability analysis
    stability_metric = analyze_stability(processed)
    
    # Consistency check with list comprehension (key feature)
    consistency_samples = [abs(fused_signal[i] - fused_signal[i-1]) for i in range(1, len(fused_signal))]
    data_consistency = 1 - calculate_variance(consistency_samples)
    
    # Response time simulation (fixed for determinism)
    response_time = 0.42 + len(outlier_gyro) * 0.01
    
    # Metrics dictionary construction
    metrics = {
        'stability_index': abs(stability_metric),
        'response_time': response_time,
        'data_consistency': data_consistency,
        'redundant_flag': 1  # Unused metric (distractor)
    }
    
    # Weighting scheme (some weights are misleading)
    weights = {
        'stability_index': 40,
        'response_time': 30,
        'data_consistency': 20,
        'fallback_mode': 10  # Weight for non-existent metric
    }
    
    # Key statement
    final_score = evaluate_performance(metrics, weights)
    
    # Output result
    print(f"Result: {final_score}")