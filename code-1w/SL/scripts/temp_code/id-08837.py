import itertools

# Simulated sensor data from a distributed monitoring system
def generate_sensor_stream():
    return [1.2, 0.9, 1.5, 2.1, 1.8, 2.4, 3.0, 2.7, 2.0, 1.6]

# Irrelevant helper - looks important but unused in critical path
def calculate_entropy(seq):
    from math import log
    freq = {}
    for x in seq:
        freq[x] = freq.get(x, 0) + 1
    total = len(seq)
    entropy = 0
    for count in freq.values():
        p = count / total
        entropy -= p * log(p)
    return entropy

# Distractor function: appears related but not used in final calculation
def analyze_trend(data):
    diffs = [data[i+1] - data[i] for i in range(len(data)-1)]
    trend_score = sum(1 for d in diffs if d > 0) - sum(1 for d in diffs if d < 0)
    return abs(trend_score) * 0.5

# Core processing chain
sensor_data = generate_sensor_stream()
filtered_readings = [x for x in sensor_data if x >= 1.5]  # Filter noise

# Bit manipulation red herring
obfuscation_key = 0b101010
encoded_offset = (len(filtered_readings) << 2) ^ obfuscation_key

# Real computation begins here
rolling_avg = sum(filtered_readings[-4:]) / 4  # Average of last 4 valid readings

# Character counting distraction (simulated log analysis)
log_snippet = "ERR|WARN|INFO|DEBUG|ERR|ERR|WARN"
error_count = log_snippet.count("ERR")
debug_count = log_snippet.count("DEBUG")

# String splitting/joining decoy
tokens = log_snippet.split('|')
unique_levels = list(set(tokens))
reconstructed = '|'.join(sorted(unique_levels))

# Dictionary-based mapping - partially relevant
severity_map = {"ERR": 3, "WARN": 2, "INFO": 1, "DEBUG": 0}
raw_severity = sum(severity_map.get(t, 0) for t in tokens)

# Another irrelevant list transformation
shifted_tokens = tokens[2:] + tokens[:2]
cyclic_hash = len(shifted_tokens) * 3

# Build health signature using slicing and itertools
truncated_readings = filtered_readings[:6]
expanded_readings = list(itertools.chain.from_iterable(
    [[x] * 2 for x in truncated_readings[::-1]]  # Reverse and duplicate
))

# Key intermediate values
amplitude = max(expanded_readings) - min(expanded_readings)
frequency_mod = len(expanded_readings) % 7

# System load simulation (fixed for determinism)
system_load = 42.0
load_factor = system_load / 100.0

# Health signature constructed via complex steps
base_health = rolling_avg * amplitude
adjusted_health = base_health * (1 - load_factor)

# Decoy dictionary operations
snapshot = {
    'timestamp': '2023-12-05T10:30:00Z',
    'node_id': 'N7A-204',
    'readings_count': len(sensor_data),
    'status_flag': (len(filtered_readings) > 5) << 1 | 1
}

# Unused nested structure - dead code path
if snapshot['status_flag'] & 2:
    snapshot['diagnostics'] = {
        'entropy': calculate_entropy(filtered_readings),
        'trend': analyze_trend(filtered_readings)
    }

# Critical function with multiple concepts
def process_metrics(health_sig, load):
    # String method distraction
    code_name = "DIAG-XR-{}".format("ACTIVE" if load > 30 else "STANDBY").lower()
    prefix_value = sum(ord(c) for c in code_name[:4]) % 19
    
    # Boolean logic and arithmetic mix
    threshold = 5.0 if 'active' in code_name else 3.5
    metric_ceiling = 100 if len(code_name) > 8 else 85
    
    # Actual computation hidden among distractions
    temp_score = health_sig + prefix_value
    if temp_score > threshold:
        temp_score *= (metric_ceiling / 100)
    
    # Bitwise operation as red herring
    masked_score = int(temp_score) ^ 0b1101
    
    # Final adjustment using conditional logic
    if load > 40:
        final_adjustment = temp_score * 0.85  # Only this branch matters
    else:
        final_adjustment = temp_score * 1.1
    
    # Slicing distraction on string representation
    score_str = str(final_adjustment)
    digit_slice = score_str[::2]  # Every other digit
    digit_sum = sum(int(d) for d in digit_slice if d.isdigit())
    
    # The real answer is final_adjustment, not digit_sum
    return final_adjustment

# Execution point of interest
final_diagnostic = process_metrics(adjusted_health, system_load)
print(f"Target result: {final_diagnostic}")