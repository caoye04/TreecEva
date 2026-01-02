from collections import defaultdict, Counter
import math

# Simulated sensor network diagnostics with noise filtering and anomaly detection
def preprocess_readings(raw_readings):
    filtered = []
    for val in raw_readings:
        if val < -200 or val > 200:  # Noise threshold
            continue
        if val % 7 == 0:  # Red herring: irrelevant divisibility filter
            continue
        filtered.append(abs(val))
    return filtered

# Legacy function – unused but looks important
def deprecated_normalization(data):
    mean = sum(data) / len(data)
    return [x - mean for x in data]

# Misleading statistical analysis (dead code path)
def compute_skewness(data):
    n = len(data)
    if n <= 2:
        return 0.0
    mean = sum(data) / n
    variance = sum((x - mean) ** 2 for x in data) / n
    if variance == 0:
        return 0.0
    std_dev = math.sqrt(variance)
    skew = sum(((x - mean) / std_dev) ** 3 for x in data) / n
    return round(skew, 4)

# Core logic hidden among distractions
def detect_spike_sequence(values, window=3):
    spikes = 0
    for i in range(len(values) - window + 1):
        window_sum = sum(values[i:i+window])
        if window_sum > 150 and values[i] < values[i+1] > values[i+2]:
            spikes += 1
    return spikes

# Real computation buried in complexity
def aggregate_metrics(data_stream, config):
    readings = []
    for chunk in data_stream:
        readings.extend(chunk)
    
    # Irrelevant transformation chain
    temp_state = [x * 1.1 for x in readings if x > 0]
    temp_state = [int(x) for x in temp_state]
    temp_counter = Counter(temp_state)  # Distractor: counts modified values
    
    # Actual preprocessing
    cleaned = preprocess_readings(readings)
    
    # More red herrings
    stats_summary = defaultdict(float)
    stats_summary['max_raw'] = max(readings) if readings else 0
    stats_summary['min_raw'] = min(readings) if readings else 0
    stats_summary['median_estimate'] = sorted(cleaned)[len(cleaned)//2] if cleaned else 0
    
    # Critical logic step 1: find sequences
    spike_count = detect_spike_sequence(cleaned)
    
    # Critical logic step 2: accumulation with conditional logic
    cumulative_energy = 0
    for val in cleaned:
        if val > config.get('threshold', 50):
            cumulative_energy += int(math.log(val, 2)) * 3
    
    # Critical logic step 3: bit manipulation decoy
    encoded_flag = 0
    for shift in [1, 3, 2]:
        encoded_flag |= (spike_count << shift) & 0b1111
    encoded_flag ^= 0b1010  # More distraction
    
    # Critical logic step 4: slicing operation that matters
    segment = cleaned[::2]  # Every other reading
    bonus = sum(segment[:5]) // 5 if len(segment) >= 5 else 0
    
    # Final diagnostic score - the real answer
    final_score = cumulative_energy + bonus + (spike_count * 7)
    
    # Dead assignment - misleading
    final_score = final_score if final_score != 0 else -999
    
    # Return the actual target
    return final_score

# Simulated input data
sensor_packets = [
    [12, -250, 35, 67, 89],
    [15, 0, 73, -44, 91],
    [27, 55, 103, 18, 14]
]

tuning_params = {
    'threshold': 45,
    'sensitivity': 'high',
    'calibration': [0.9, 1.1, 1.0]
}

# Unused variables to increase interference
baseline_profile = [math.sin(i * 0.1) for i in range(10)]
diagnostic_trace = compute_skewness(baseline_profile)
shadow_buffer = sensor_packets[0][::-1]  # Reversed slice - unused

# Key execution point
final_diagnostic = aggregate_metrics(sensor_packets, tuning_params)
print(f"Result: {final_diagnostic}")