import math

# Simulated sensor data processing with diagnostic metrics
def analyze_signal_strength(raw_readings):
    filtered = [x for x in raw_readings if x > -50]  # Remove weak signals
    avg = sum(filtered) / len(filtered) if filtered else 0
    return avg * 1.8 + 20

# Legacy system compatibility wrapper (unused but looks important)
def legacy_calibrate(x):
    return (x << 2) ^ 0xCAFEBABE

# Environmental correction factor based on temperature drift
def temp_compensate(value, temp):
    factor = 1 + (temp - 25) * 0.015
    return value * factor

# Core logic: performance evaluation under variable conditions
def compute_adaptive_weight(n):
    if n <= 1:
        return 1
    return n * compute_adaptive_weight(n - 2)  # Recursive weighting

# Diagnostic trace generator (distractor - appears relevant)
def generate_diagnostics(data):
    stats = {}
    stats['peak'] = max(data) if data else 0
    stats['entropy'] = sum([-x*math.log2(x+1e-9) for x in data])
    stats['checksum'] = sum([x ^ (i*3) for i, x in enumerate(data)])
    return stats

# Misleading intermediate transformation (dead path)
def deprecated_transform(seq):
    return [((x | 7) & 15) ^ 3 for x in seq]

# Main evaluation function with critical logic buried in noise
def evaluate_performance(metrics, threshold):
    # Irrelevant preprocessing block (red herring)
    adjusted_metrics = []
    for val in metrics:
        if val < 0:
            adjusted_metrics.append(abs(val) ** 0.5 * 2.5)
        else:
            adjusted_metrics.append(val + math.sin(val))
    
    # Decoy analysis using bitwise operations (looks important)
    magic_sum = 0
    for i, v in enumerate(adjusted_metrics):
        magic_sum += int(v) ^ (i + 1) | 0xFF
    
    # Real logic begins here — subtle and obscured by prior noise
    base = 0
    for m in metrics:
        if m > threshold:
            base += 1
    
    # Apply recursive weight only to count
    weighted_count = compute_adaptive_weight(base)
    
    # Secondary filter: harmonic significance
    harmonic_val = 0
    for i in range(1, base + 1):
        harmonic_val += 1 / i if i % 2 == 1 else 0
    
    # Actual answer derivation (non-obvious)
    temp_correction = temp_compensate(weighted_count, 30)
    final_component = temp_correction * (1 + harmonic_val)
    
    # Critical assignment — this is the target
    final_score = int(final_component * 100) // 10
    
    # Unused but distracting post-processing
    debug_meta = {
        'version': '2.1-alpha',
        'calibration': legacy_calibrate(42),
        'aux_data': deprecated_transform([10, 20, 30])
    }
    
    return final_score

# Simulated input data
raw_sensor_data = [-60, -45, 30, 75, 80, -55, 20]
metric_data = [
    analyze_signal_strength(raw_sensor_data),
    65.0,
    70.0,
    85.0,
    90.0
]
base_threshold = 68.0

# Dead code path invocation (misleads static analysis)
diag_report = generate_diagnostics(raw_sensor_data)

# Key execution point
final_score = evaluate_performance(metric_data, base_threshold)

# Output result as required
print(f"Result: {final_score}")