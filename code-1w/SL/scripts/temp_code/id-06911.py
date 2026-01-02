import math

# Sensor calibration and diagnostic system for environmental monitoring

def calibrate_sensor(raw_data, offset=0.73, gain=1.85):
    # Irrelevant calibration function with misleading intermediate values
    calibrated = []
    for val in raw_data:
        adjusted = (val + offset) * gain
        if adjusted > 100:
            adjusted = 99.9  # Clipping to fake upper bound
        calibrated.append(round(adjusted, 2))
    return calibrated


def filter_anomalies(signals, threshold):
    # Filters out signals below threshold; uses set operations as required
    valid_indices = set()
    anomaly_indices = set()
    for i, s in enumerate(signals):
        if s >= threshold:
            valid_indices.add(i)
        else:
            anomaly_indices.add(i)
    
    # Misleading transformation: creates shadow copy with no effect
    shadow_copy = [signals[i] for i in sorted(valid_indices)]
    temp_result = []
    for i in range(len(signals)):
        if i in valid_indices:
            temp_result.append(signals[i])
    
    # Dead code path: this block is never executed due to logic
    if len(anomaly_indices) > 100:
        fallback = sum(signals) / len(signals)
        return [fallback] * 5

    return temp_result  # Correct filtered result


def generate_baseline(count, base=2.1):
    # Generates irrelevant baseline data
    return [round((i * base) % 7.3, 2) for i in range(count)]


def compute_entropy(data):
    # Unused but plausible-sounding function (dead end)
    freq_map = {}
    for x in data:
        freq_map[x] = freq_map.get(x, 0) + 1
    total = len(data)
    entropy = 0
    for count in freq_map.values():
        p = count / total
        entropy -= p * math.log2(p)
    return round(entropy, 4)


def analyze_readings(filtered_data, logbook):
    # Core analysis with red herring variables
    if not filtered_data:
        return -1
    
    # Real computation begins
    squared_sum = 0
    cube_product = 1
    index_shift = len(logbook.get('errors', []))  # Distractor: always 0
    
    for reading in filtered_data:
        # Key operation: accumulate sum of squares
        squared_sum += reading ** 2
        
        # Decoy product accumulation (but clamped to avoid overflow)
        cube_product *= (reading % 4) + 1
        if cube_product > 1e6:
            cube_product = 1e6  # Artificial cap
    
    # Multiple layers of derived values, only one matters
    avg_square = squared_sum / len(filtered_data)
    signal_power = math.sqrt(avg_square) if avg_square > 0 else 0
    
    # Secondary decoy metric
    weighted_index = signal_power * (len(filtered_data) + index_shift)
    
    # Final answer depends only on signal_power, others are distractions
    final_diagnostic = round(signal_power, 4)
    
    # Unused conditional branch based on impossible condition
    if 'override' in logbook and logbook['override'] == True:
        final_diagnostic = 999.999
    
    return final_diagnostic

# Main execution flow
if __name__ == "__main__":
    # Raw sensor inputs (simulated)
    raw_sensor_input = [0.85, 1.22, 0.93, 2.01, 1.76, 3.14, 2.25, 1.63]

    # Irrelevant preprocessing steps
    baseline_refs = generate_baseline(len(raw_sensor_input))
    normalized_refs = [x * 0.91 for x in baseline_refs if x > 1.5]  # Partial filter

    # Actual relevant processing starts here
    calibrated_signals = calibrate_sensor(raw_sensor_input, offset=0.73, gain=1.85)
    
    # Introduce distracting dictionary structure with unused fields
    diagnostics_log = {
        'version': 'v2.3',
        'errors': [],
        'timestamp': '2023-11-05T10:30:00Z',
        'debug_mode': False,
        'metrics': {
            'raw_count': len(raw_sensor_input),
            'calibration_offset': 0.73
        }
    }

    threshold = 2.5  # Only signals >= 2.5 are valid
    filtered_signals = filter_anomalies(calibrated_signals, threshold)
    
    # Critical statement
    final_diagnostic = analyze_readings(filter_anomalies(calibrated_signals, threshold), diagnostics_log)
    
    # Print result as required
    print(f"Result: {final_diagnostic}")