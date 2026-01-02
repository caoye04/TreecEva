import math

def preprocess_signals(raw_data):
    # Irrelevant signal processing (dead-end function)
    filtered = [x * 0.9 for x in raw_data if x > 5]
    normalized = [y / max(filtered) for y in filtered]
    return normalized

def compute_checksum(sequence):
    # Distractor: checksum computation not used in main logic
    checksum = 0
    for i, val in enumerate(sequence):
        checksum ^= (val + i) % 256
    return checksum

def evaluate_stability(readings):
    # Misleading stability metric with partial relevance
    avg = sum(readings) / len(readings)
    variance = sum((x - avg) ** 2 for x in readings) / len(readings)
    return variance < 3.5

def aggregate_logs(log_entries):
    # Complex but irrelevant log aggregation with dictionary distractions
    log_summary = {}
    for entry in log_entries:
        tag = entry['type']
        if tag not in log_summary:
            log_summary[tag] = 0
        log_summary[tag] += 1
    
    # Decoy transformations
    inverted = {v: k for k, v in log_summary.items()}
    sorted_items = sorted(log_summary.items(), key=lambda x: x[1], reverse=True)
    return sorted_items  # Not used later

def analyze_metrics(diagnostics, thresholds):
    # Core relevant logic buried in noise
    temp_history = diagnostics['temperature']
    pressure_log = diagnostics['pressure']
    flow_rate = diagnostics['flow']

    # Red herring: unused derived values
    peak_temp = max(temp_history)
    baseline = min(pressure_log)
    total_flow = sum(flow_rate)

    # Real computation chain (8-12 steps)
    step_1 = sum(temp_history) / len(temp_history)
    step_2 = step_1 * 1.8 + 32  # Convert to Fahrenheit (intermediate)
    step_3 = math.log(step_1 + 1)  # Nonlinear scaling
    
    # Conditional bit manipulation red herring
    flag = 0
    if step_1 > 40:
        flag |= 1 << 3
    else:
        flag |= 1 << 1

    # Real path continues here
    adjusted_pressure = []
    for p in pressure_log:
        if p < thresholds['p_min']:
            adjusted_pressure.append(thresholds['p_min'])
        elif p > thresholds['p_max']:
            adjusted_pressure.append(thresholds['p_max'])
        else:
            adjusted_pressure.append(p)
    
    avg_pressure = sum(adjusted_pressure) / len(adjusted_pressure)
    
    # Key cross-variable interaction
    score_a = step_3 * 0.7
    score_b = avg_pressure * 0.3
    composite_score = score_a + score_b
    
    # Final decision logic
    if composite_score > thresholds['critical_level']:
        final_diagnostic = 98765
    else:
        final_diagnostic = 12345
    
    # Dead code branch (never reached due to prior assignment)
    for reading in temp_history:
        if reading > 100:
            final_diagnostic = -99999  # Never executed
            break
    
    return final_diagnostic

# Main execution block
if __name__ == '__main__':
    # Input data setup
    sensor_diagnostics = {
        'temperature': [35, 38, 42, 40, 37, 39],
        'pressure': [20, 25, 50, 30, 22, 28, 35],
        'flow': [15, 14, 16, 15, 17]
    }
    
    threshold_settings = {
        'p_min': 20,
        'p_max': 40,
        'critical_level': 45.0
    }
    
    # Irrelevant preprocessing calls (distractors)
    signals = [10, 12, 8, 15, 20, 25]
    processed = preprocess_signals(signals)
    chk = compute_checksum([1, 2, 3, 4])
    stable = evaluate_stability([1.0, 1.1, 0.9, 1.05])
    logs = [
        {'type': 'sensor', 'id': 1},
        {'type': 'system', 'id': 2},
        {'type': 'sensor', 'id': 3}
    ]
    summary = aggregate_logs(logs)
    
    # Key statement
    final_diagnostic = analyze_metrics(sensor_diagnostics, threshold_settings)
    
    # Output result
    print(f"Result: {final_diagnostic}")