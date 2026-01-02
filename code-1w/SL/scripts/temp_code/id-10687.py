import math

# Simulated sensor fusion system with diagnostic metrics
def analyze_sensor_health(raw_readings, threshold=75):
    healthy_count = 0
    stress_flags = []
    for idx, val in enumerate(raw_readings):
        normalized = (val - 20) * 1.5 if val > 30 else (val + 10) * 0.8
        is_stable = normalized < threshold and (normalized % 4 == 0)
        health_score = int(is_stable) * 100 - (idx * 2)  # Position penalty
        healthy_count += int(is_stable)
        stress_flags.append(health_score > 40)
    return healthy_count, stress_flags


def compute_entropy(data):
    # Irrelevant complexity: entropy calculation not used in final path
    from collections import Counter
    counts = Counter(data)
    total = len(data)
    entropy = 0
    for count in counts.values():
        p = count / total
        entropy -= p * math.log2(p)
    return round(entropy, 3)


def transform_signal(signal_stream, mode='fast'):
    # Dead-end transformation function with misleading intermediate outputs
    if mode == 'fast':
        shifted = [(x << 1) ^ 3 for x in signal_stream]
        filtered = [s for s in shifted if s % 5 != 0]
        return [f >> 1 for f in filtered]
    else:
        return [int(math.sqrt(x)) if x > 0 else 0 for x in signal_stream]


def detect_anomalies(pattern_trace):
    # Unused anomaly detector - red herring
    anomalies = 0
    for i in range(1, len(pattern_trace)):
        if abs(pattern_trace[i] - pattern_trace[i-1]) > 25:
            anomalies += 1
    return anomalies > 3


def integrate_subsystems(sys_a, sys_b):
    # Distractor: complex integration that isn't part of main logic
    magic_const = 0xDEADBEEF % 1000
    combined = []
    for a, b in zip(sys_a, sys_b):
        fused = (a ^ b) + ((a & 5) * (b | 3))
        combined.append((fused + magic_const) % 97)
    return combined


def aggregate_metrics(sensor_input, scale_factor):
    # Core logic buried within distractions
    base_adjustment = sum(x & 7 for x in sensor_input)  # Bitwise contribution
    
    # Conditional expression determining processing path
    modifier = 2.5 if all(x > 10 for x in sensor_input[:3]) else 1.8
    
    temp_series = [int(x * modifier) for x in sensor_input]
    
    # Key intermediate computation
    running_total = 0
    for i, t in enumerate(temp_series):
        if i % 2 == 0:
            running_total += t // (i + 1)
        else:
            running_total -= t % 11
    
    # Additional irrelevant transformations
    shadow_copy = [t ^ 15 for t in temp_series]  # Unused obfuscation
    peak_value = max(shadow_copy) * 0.75  # Misleading metric
    decay_curve = [peak_value / (j + 1) for j in range(5)]  # Never used
    
    # Final calculation using core result and scale factor
    raw_result = (running_total + base_adjustment) * scale_factor
    
    # Secondary conditional adjustment
    final_diagnostic = int(raw_result) if raw_result >= 0 else abs(int(raw_result)) + 100
    
    # Diagnostic print - distractor
    debug_checksum = sum(final_diagnostic.to_bytes(4, 'little'))
    
    return final_diagnostic

# Main execution sequence
if __name__ == '__main__':
    # Initialize sensor array with realistic values
    sensor_array = [23, 85, 64, 12, 91, 33, 47]
    
    # Irrelevant preprocessing steps
    processed_chain = transform_signal(sensor_array, mode='fast')
    entropy_metric = compute_entropy(processed_chain)  # Not used
    anomaly_flag = detect_anomalies(processed_chain)   # Not used
    
    # Calibration factor derived from bitwise logic
    flags = [v > 50 for v in sensor_array]
    bit_accum = 0
    for i, flag in enumerate(flags):
        bit_accum |= (1 << i) if flag else 0
    
    # Real but obscured calibration computation
    calibration_factor = ((bit_accum ^ 0xAA) & 0xFF) / 10.0  # Results in 11.0
    
    # Core health analysis - partially relevant
    health_count, stress_indicators = analyze_sensor_health(sensor_array)
    
    # Unused system integration
    dummy_system_1 = [10, 20, 30, 40]
    dummy_system_2 = [15, 25, 35, 45]
    integrated_output = integrate_subsystems(dummy_system_1, dummy_system_2)
    
    # Critical statement containing answer derivation
    final_diagnostic = aggregate_metrics(sensor_array, calibration_factor)
    
    # Output required result
    print(f"Result: {final_diagnostic}")