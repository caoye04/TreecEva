import math

# Simulated sensor array diagnostics with noise filtering and health scoring
def collect_sensor_data(baseline, offset=1.0):
    readings = [baseline * (1.0 + 0.1 * i) + offset for i in range(5)]
    normalized = [r / (sum(readings) / len(readings)) for r in readings]
    return normalized

def apply_noise_filter(signal_list, threshold=0.95):
    filtered = []
    noise_log = []  # Distractor: logged but unused
    for val in signal_list:
        if abs(val - 1.0) > threshold:
            noise_log.append(val)
        else:
            filtered.append(val)
    return filtered or [1.0]  # Ensure non-empty

def compress_signal_data(data):
    # Dead function: never called, red herring
    return [d * 0.5 for d in data[::2]]

def calculate_coherence_score(seq):
    score = 0.0
    for i in range(len(seq) - 1):
        score += abs(seq[i] - seq[i+1])
    return max(1.0, 10.0 - score)

def extract_timing_metadata(raw_seq):
    timing_info = {}
    for idx, val in enumerate(raw_seq):
        timing_info[f't_{idx}'] = val * idx if idx % 2 == 0 else val / (idx + 1)
    avg_time = sum(timing_info.values()) / len(timing_info)  # Computed but irrelevant
    return avg_time

def process_critical_flag(flag_code, mask=0b1101):
    # Bitwise analysis with decoy logic
    masked = flag_code & mask
    is_urgent = bool(masked & 0b1000)
    is_recoverable = bool(masked & 0b0100)
    checksum = (masked ^ 0b1111) + 1  # Distractor computation
    return is_urgent and not is_recoverable

def recursive_diagnostic(depth, data_packet):
    if depth <= 0:
        return sum(data_packet) % 7
    transformed = [math.sin(x) + depth for x in data_packet]
    return recursive_diagnostic(depth - 1, transformed[:3])

def group_anomalies(signal_set):
    groups = {'minor': [], 'critical': []}
    for s in signal_set:
        if s > 1.2:
            groups['critical'].append(s)
        elif s < 0.8:
            groups['minor'].append(s)
    return groups  # Calculated but not used directly

def analyze_readings(validated_data):
    # Core logic embedded within distractions
    base_value = sum(validated_data) / len(validated_data)
    
    # Conditional expression usage (required Python feature)
    adjustment = 2.5 if all(x > 0.9 for x in validated_data) else 1.1
    
    temp_score = base_value * adjustment
    
    # Bitwise operation mixed with arithmetic
    flag_input = int(temp_score * 10)  # e.g., 12 → 0b1100
    urgency = process_critical_flag(flag_input)
    
    # Recursive call with controlled depth
    recursion_seed = [temp_score, adjustment, 1.0]
    recursive_trace = recursive_diagnostic(2, recursion_seed)
    
    # Final computation combining multiple concepts
    coherence = calculate_coherence_score(validated_data)
    final_diagnostic = int((temp_score * coherence) + recursive_trace)
    
    # Irrelevant grouping
    _ = group_anomalies(validated_data)
    
    # Unused conditional side-path
    if len(validated_data) > 10:
        fallback = sum(validated_data) // 2
    else:
        fallback = -999  # Dead path value
    
    return final_diagnostic

# Main execution flow
if __name__ == '__main__':
    raw_baseline = 0.95
    sensor_output = collect_sensor_data(raw_baseline, offset=0.05)
    processed_signals = apply_noise_filter(sensor_output, threshold=0.95)
    
    # Extraneous data transformation
    dummy_metadata = extract_timing_metadata(sensor_output)
    
    # Key statement
    final_diagnostic = analyze_readings(processed_signals)
    
    # Output result as required
    print(f"Result: {final_diagnostic}")