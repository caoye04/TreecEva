import math

# Simulated sensor array data from environmental monitoring station
def fetch_sensor_data():
    raw_values = [3, 5, 7, 11, 13, 17, 19, 23]
    # Apply non-linear calibration curve (real transformation)
    calibrated = [math.log(x) * 1.7 for x in raw_values]
    return calibrated

# Irrelevant helper: formats timestamp string (distractor)
def format_timestamp(ts):
    return f"{ts:06d}"[-6:] if ts > 0 else "000000"

# Unused signal smoothing function (dead code path)
def smooth_signal(signal_list):
    smoothed = []
    for i in range(len(signal_list)):
        neighbors = signal_list[max(0, i-1):min(i+2, len(signal_list))]
        smoothed.append(sum(neighbors) / len(neighbors))
    return smoothed  # Never called

# Real processing: detect anomalies based on variance threshold
def identify_anomalies(data_seq):
    mean_val = sum(data_seq) / len(data_seq)
    variance = sum((x - mean_val) ** 2 for x in data_seq) / len(data_seq)
    anomaly_threshold = 0.45
    anomalies = [x for x in data_seq if abs(x - mean_val) > anomaly_threshold * mean_val]
    return anomalies, variance

# String-based flag encoder (mixed paradigm distractor)
def encode_flags(flag_list):
    encoding_map = {'low': 'L', 'mid': 'M', 'high': 'H'}
    flag_str = ''.join([encoding_map.get(f, 'X') for f in flag_list])
    # Use string method to obfuscate relevance
    return flag_str.replace('X', '').ljust(5, 'Z')  # Distractor computation

# Core analysis pipeline
def process_signal_chain(raw_input):
    stage_one = [math.sin(x) + 0.5 for x in raw_input]  # Non-linear transform
    stage_two = [abs(x) ** 1.8 for x in stage_one]       # Amplify weak signals
    
    # Introduce bit manipulation for 'digital filtering' label (red herring)
    filter_tag = (len(stage_two) << 2) ^ 0b1101
    tag_parity = bin(filter_tag).count('1') % 2  # Meaningless but looks important
    
    # Actual relevant transformation: normalize and scale
    max_val = max(stage_two)
    normalized = [x / max_val * 100 for x in stage_two]
    
    # Inject unrelated counting logic (distractor)
    even_count = sum(1 for x in normalized if int(x) % 2 == 0)
    category_bins = {key: 0 for key in ['A','B','C']}
    for x in normalized:
        if x < 30: category_bins['A'] += 1
        elif x < 70: category_bins['B'] += 1
        else: category_bins['C'] += 1
    
    return normalized

# Final diagnostic engine
def analyze_readings(validated_data):
    # Compute weighted score using trigonometric weighting
    weights = [math.cos(i * 0.3) + 1.1 for i in range(len(validated_data))]
    weighted_sum = sum(val * weights[i] for i, val in enumerate(validated_data))
    
    # Secondary metric: pulse count above threshold
    pulse_count = sum(1 for x in validated_data if x > 85)
    
    # Decoy calculation with string method (irrelevant)
    status_code = "PULSE_DIAG_" + str(pulse_count)
    padded_code = status_code.rjust(20, '0')
    checksum = sum(ord(c) for c in padded_code if c.isdigit())
    
    # Critical real calculation: combine using fixed formula
    base_score = weighted_sum * 0.73
    adjustment = (pulse_count * 2.3) if pulse_count > 3 else (pulse_count * -1.8)
    final_score = base_score + adjustment
    
    # This is the actual answer variable
    final_diagnostic = int(round(final_score * 1.05))
    
    return final_diagnostic

# Orchestration sequence
if __name__ == "__main__":
    # Fetch and process real data
    raw_sensor_output = fetch_sensor_data()
    processed_signals = process_signal_chain(raw_sensor_output)
    
    # Dead code invocation (never affects anything)
    _ = encode_flags(['mid', 'high', 'low'])
    _ = format_timestamp(12345)
    
    # Key execution point
    final_diagnostic = analyze_readings(processed_signals)
    
    # Output result as required
    print(f"Target result: {final_diagnostic}")