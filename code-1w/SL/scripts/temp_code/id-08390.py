import math

# Simulated sensor array processing with diagnostic evaluation
def process_sensor_array(raw_readings, calibration_factor):
    adjusted_values = []
    noise_floor = 0.003
    for reading in raw_readings:
        if reading < 0:
            reading = abs(reading)
        corrected = (reading * calibration_factor) + noise_floor
        if corrected > 1.0:
            corrected = 1.0
        adjusted_values.append(round(corrected, 6))
    return adjusted_values

# Signal normalization using z-score with edge case handling
def normalize_signal(signal_data):
    n = len(signal_data)
    mean_val = sum(signal_data) / n
    variance = sum((x - mean_val) ** 2 for x in signal_data) / n
    std_dev = math.sqrt(variance) if variance > 0 else 1.0
    if std_dev == 0:
        return [0.0] * n
    normalized = [(x - mean_val) / std_dev for x in signal_data]
    return [round(x, 6) for x in normalized]

# Auxiliary function - computes entropy for randomness assessment (distractor)
def compute_entropy(values):
    entropy = 0.0
    value_counts = {}
    for v in values:
        key = round(v, 3)
        value_counts[key] = value_counts.get(key, 0) + 1
    total = len(values)
    for count in value_counts.values():
        prob = count / total
        if prob > 0:
            entropy -= prob * math.log2(prob)
    return round(entropy, 6)

# System state classification based on operational thresholds (irrelevant path)
def classify_system_state(metrics):
    avg_metric = sum(metrics) / len(metrics)
    if avg_metric > 0.8:
        return 'OVERLOAD'
    elif avg_metric > 0.5:
        return 'STABLE'
    else:
        return 'IDLE'

# Core aggregation logic - combines normalized signals with state weights
def aggregate_metrics(norm_signals, sys_state):
    # Apply domain-specific transformation based on hypothetical physics model
    transformed = [math.sin(x * math.pi / 2) for x in norm_signals]
    
    # Introduce weighting scheme based on position (simulates sensor layout)
    weights = [0.5 + 0.1 * i for i in range(len(transformed))]
    weighted_sum = sum(t * w for t, w in zip(transformed, weights))
    
    # Normalize by effective length with damping factor
    damping = 0.95 if sys_state == 'STABLE' else 0.75
    effective_length = len(transformed) * damping
    
    # Final integration step
    integrated_score = weighted_sum / effective_length if effective_length != 0 else 0
    
    # Secondary adjustment based on symmetry detection (red herring)
    reversed_vals = list(reversed(transformed))
    symmetry_score = sum(min(a, b) for a, b in zip(transformed, reversed_vals))
    
    # Actual final result does NOT depend on symmetry_score - it's a distractor
    result = integrated_score * 1000  # Scale to integer-friendly range
    return int(round(result))

# Irrelevant utility: generates Fibonacci-like sequence for 'pattern analysis'
def generate_fib_sequence(n):
    fib = [1, 1]
    for i in range(2, n):
        fib.append(fib[i-1] + fib[i-2])
    return fib[:n]

# Unused function - simulates logging but never called
def log_diagnostics(timestamp, data, level='INFO'):
    prefix = f"[{level}] ({timestamp})"
    print(f"{prefix} Diagnostic dump: {data}")

# Main execution flow
if __name__ == '__main__':
    # Initial sensor inputs (simulated quantum interference readings)
    raw_quantum_readings = [0.12, -0.05, 0.34, 0.21, -0.18, 0.45, 0.19, 0.08]
    
    # Calibration parameter from device firmware
    firmware_calibration = 1.87
    
    # Process raw data through adjustment pipeline
    calibrated_readings = process_sensor_array(raw_quantum_readings, firmware_calibration)
    
    # Normalize the calibrated signals
    normalized_signals = normalize_signal(calibrated_readings)
    
    # Compute entropy for no reason (dead end metric)
    entropy_diagnostic = compute_entropy(calibrated_readings)  # unused later
    
    # Generate auxiliary pattern sequence (completely irrelevant)
    pattern_sequence = generate_fib_sequence(len(normalized_signals))
    pattern_weight = sum(pattern_sequence) / len(pattern_sequence)
    
    # Determine system state (used in main calculation)
    system_state = 'STABLE'  # Determined externally, hardcoded for reproducibility
    
    # Aggregate all metrics into final diagnostic code
    final_diagnostic = aggregate_metrics(normalized_signals, system_state)
    
    # Print result as required
    print(f"Result: {final_diagnostic}")