from collections import defaultdict, Counter
import math

def analyze_component_health(sensor_readings, thresholds):
    # Irrelevant aggregation (distractor)
    stats = defaultdict(float)
    for k, v in sensor_readings.items():
        if v > thresholds.get(k, 0):
            stats[k] = v * 1.5
        else:
            stats[k] = v * 0.8
    return stats

def compute_latency_burst(peaks, base=2):
    # Unused function - red herring
    return sum([base ** p for p in peaks if p > 0])

def validate_checksum(frame):
    # Bit manipulation decoy
    checksum = 0
    for b in frame:
        checksum ^= b
        checksum = (checksum << 1) & 0xFF | (checksum >> 7)
    return checksum == 0xAA

def decode_signal_pattern(signal_str):
    # String processing distraction
    segments = signal_str.split('|')
    filtered = [s.strip().lower() for s in segments if 'err' not in s]
    freq = Counter(''.join(filtered))
    return ''.join([k for k, v in freq.items() if v % 2 == 1])

def process_timing_sequence(raw_timings):
    # Relevant but obfuscated transformation
    adjusted = []
    for t in raw_timings:
        if t <= 0:
            continue
        adj = t - 0.1
        if adj > 0.5:
            adj = math.log(adj) + 0.3
        adjusted.append(round(adj, 4))
    # Dead code path
    if len(adjusted) > 100:
        return [x * 2 for x in adjusted]  # Never reached
    return adjusted

def evaluate_system_stability(config_matrix):
    # Complex irrelevant logic
    risk_score = 0
    for row in config_matrix:
        for val in row:
            if val & 1:
                risk_score += (val ^ 3) % 4
    return risk_score * 0.7

def aggregate_metrics(log, flags):
    # Core calculation hidden among distractions
    base_value = 0
    multiplier = 1
    
    # Key conditional buried in noise
    if 'overclock' in flags and flags['overclock']:
        multiplier *= 1.25
    if 'safe_mode' in flags and flags['safe_mode']:
        multiplier *= 0.75
    
    # Actual data being used
    for entry in log:
        if entry['response'] > 0.3:
            base_value += entry['response'] * 0.9
        else:
            base_value += entry['response'] * 1.1
    
    # Decoy operations on same variable
    base_value = abs(base_value - 0.1)  # Misleading adjustment
    base_value = max(base_value, 0.5)   # Another distraction
    
    # The real final computation
    result = int((base_value * multiplier) * 1000)
    
    # Unused transformations
    temp_result = result ^ 0xFFFF
    temp_result = (temp_result >> 4) + 100
    
    return result

# Simulated input data
sensor_data = {'cpu': 75.3, 'gpu': 82.1, 'ram': 60.0}
threshold_limits = {'cpu': 70, 'gpu': 80, 'ram': 65}

# Unused complex structure
system_matrix = [
    [0x1A, 0x2C, 0x0F],
    [0x3E, 0x0B, 0x2D],
    [0x11, 0x22, 0x33]
]

# Critical timing data (used)
timing_samples = [0.15, 0.45, 0.65, 0.23, 0.71, 0.34]
timing_log = []
for raw_val in timing_samples:
    processed = raw_val
    if processed > 0.2:
        processed -= 0.05
    timing_log.append({'timestamp': processed, 'response': processed})

# System configuration with meaningful flags
system_flags = {
    'overclock': True,
    'safe_mode': False,
    'debug_trace': True,  # unused
    'verbose': True       # unused
}

# Call irrelevant functions to create noise
diag_stats = analyze_component_health(sensor_data, threshold_limits)
matrix_risk = evaluate_system_stability(system_matrix)

# Signal pattern decoy
decoded_pattern = decode_signal_pattern("SYNC|DATA|ERR|FRAME")

# Process the actual needed sequence
timing_log = process_timing_sequence(timing_samples)

# Key assignment - target of question
final_diagnostic = aggregate_metrics(timing_log, system_flags)

print(f"Target result: {final_diagnostic}")