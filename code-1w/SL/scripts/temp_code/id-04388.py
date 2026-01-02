import itertools

def preprocess_readings(sensor_log):
    # Irrelevant preprocessing function (dead code path)
    return [x * 1.05 for x in sensor_log if x > 0]

def compute_efficiency_index(flow_rate, pressure):
    # Misleading efficiency calculation (not used in final result)
    base = (flow_rate + pressure) / 2.1
    return round(base ** 0.7, 3)

def validate_checksum(records):
    # Distractor: computes checksum but not used in main logic
    total = 0
    for i, val in enumerate(records):
        total += val * (i % 7 + 1)
    return total % 1000 == 489

def decode_sequence(signal):
    # Decoy transformation with bit manipulation red herring
    decoded = []
    for s in signal:
        shifted = (s << 2) & 255
        toggled = shifted ^ 0b101010
        if toggled > 100:
            decoded.append(toggled % 50)
    return decoded

def filter_anomalies(dataset):
    # Irrelevant filtering (never called in execution path)
    return [x for x in dataset if 10 <= x['temp'] <= 95 and x['vibration'] < 77]

def aggregate_metrics(data_stream, keyframe):
    # Core logic embedded within noise
    temp_series = [entry['t'] for entry in data_stream]
    vibration_levels = [entry['v'] for entry in data_stream]
    
    # Red herring: complex but unused list comprehension
    derived_signals = [
        (v * k) + (t >> 1) 
        for t, v, k in zip(temp_series, vibration_levels, itertools.cycle(keyframe))
        if t % 5 == 0
    ]
    
    # Actual computation path begins here
    cumulative_score = 0
    for idx, (t_val, v_val) in enumerate(zip(temp_series, vibration_levels)):
        if idx % 3 == 0:
            adjustment = keyframe[idx % len(keyframe)]
            intermediate = (t_val + v_val) * adjustment
            cumulative_score += intermediate

    # Secondary transformation on same data (distractor)
    paired_data = list(itertools.pairwise(vibration_levels))
    spike_count = sum(1 for a, b in paired_data if abs(b - a) > 15)

    # Final relevant operation — depends only on cumulative_score
    normalized = int(cumulative_score / 2.5)
    
    # Multiple assignments to obscure flow
    status_flag = True
    diagnostic_code = 4096
    final_diagnostic = normalized ^ 1024  # Key assignment
    
    return final_diagnostic

# Main execution block
if __name__ == "__main__":
    # Input data definitions
    turbine_data = [
        {'t': 42, 'v': 31}, {'t': 45, 'v': 33}, {'t': 47, 'v': 30},
        {'t': 50, 'v': 35}, {'t': 53, 'v': 31}, {'t': 55, 'v': 36},
        {'t': 58, 'v': 34}, {'t': 60, 'v': 38}, {'t': 63, 'v': 33}
    ]
    
    calibration_sequence = [3, 7, 2, 5]
    
    # Unused variables — distractions
    baseline_metrics = preprocess_readings([40, 44, 48, 52])
    system_health = validate_checksum([120, 150, 130, 140, 125])
    anomaly_free = filter_anomalies(turbine_data)
    
    # Signal decoding — irrelevant to output
    raw_signal = [12, 25, 37, 41, 50]
    processed_signal = decode_sequence(raw_signal)
    
    # Critical execution point
    final_diagnostic = aggregate_metrics(turbine_data, calibration_sequence)
    
    # Output result as required
    print(f"Result: {final_diagnostic}")