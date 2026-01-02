import math

# Sensor data processing for environmental monitoring system
def collect_readings():
    raw_samples = [127, 255, 193, 64, 88, 201, 142, 73]
    scaling_factor = 0.75
    adjusted = [x * scaling_factor for x in raw_samples]
    return adjusted

def compute_checksum(data):
    # Irrelevant cryptographic checksum (red herring)
    checksum = 0
    for val in data:
        checksum ^= int(val)
    return checksum % 256

def filter_outliers(values):
    mean_val = sum(values) / len(values)
    deviances = [(v - mean_val) ** 2 for v in values]
    variance = sum(deviances) / len(deviances)
    std_dev = math.sqrt(variance)
    # Filter values beyond 1.5 std dev (actual relevant logic)
    return [v for v in values if abs(v - mean_val) <= 1.5 * std_dev]

def generate_bands(signal):
    # Unused frequency band generator (dead code path)
    bands = {'low': [], 'mid': [], 'high': []}
    for s in signal:
        if s < 50: bands['low'].append(s)
        elif s < 100: bands['mid'].append(s)
        else: bands['high'].append(s)
    return bands

def evaluate_stability(metrics):
    # Misleading stability metric with no impact on final result
    if len(metrics) < 5:
        return 'UNSTABLE'
    trend = metrics[-1] - metrics[0]
    return 'STABLE' if abs(trend) < 30 else 'OSCILLATING'

def build_index_map(data):
    # Distractor: builds unused index map
    return {i: val for i, val in enumerate(data)}

def analyze_readings(valid_data, base_ref):
    # Core analysis combining set logic and arithmetic
    base_set = base_ref
    current_set = set([int(x) for x in valid_data])
    
    # Key set operations (relevant)
    common_elements = current_set.intersection(base_set)
    unique_only = current_set.symmetric_difference(base_set)
    
    score_a = sum(common_elements) * 1.25
    score_b = len(unique_only) * 17
    
    # Secondary adjustment using bit manipulation (relevant)
    raw_total = int(score_a - score_b)
    shifted = (raw_total << 2) & 0xFFFF  # Simulate register truncation
    masked = shifted ^ 0xAAAA
    
    # Final computation chain
    correction = len(current_set.difference(base_set))
    if masked > 10000:
        final_score = masked // 100 - correction * 8
    else:
        final_score = masked + 200 - correction * 8
    
    # Decoy variables and computations
    diagnostic_flag = 'OK' if final_score > 500 else 'CHECK'
    audit_trace = [final_score, masked, correction]
    
    return final_score

# Main execution flow
if __name__ == '__main__':
    # Baseline reference set (simulated calibration data)
    baseline_set = {96, 144, 120, 72, 66, 150, 108}
    
    # Collect sensor readings
    all_readings = collect_readings()
    
    # Compute irrelevant checksum
    chk = compute_checksum(all_readings)
    
    # Filter valid metrics (key preprocessing step)
    filtered_metrics = filter_outliers(all_readings)
    
    # Generate unused frequency bands
    spectral_bands = generate_bands(filtered_metrics)
    
    # Evaluate misleading stability status
    status = evaluate_stability(filtered_metrics)
    
    # Build unused index structure
    index_lookup = build_index_map(filtered_metrics)
    
    # Perform final diagnostic analysis (critical statement)
    final_diagnostic = analyze_readings(filtered_metrics, baseline_set)
    
    # Output target result
    print(f"Result: {final_diagnostic}")