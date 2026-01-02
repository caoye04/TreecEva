from collections import defaultdict, Counter
import math

# Simulated system telemetry data
timing_log = [
    (0.45, 'sensor_A', 'read'),
    (0.32, 'sensor_B', 'read'),
    (0.67, 'sensor_A', 'write'),
    (0.21, 'sensor_C', 'read'),
    (0.89, 'sensor_B', 'write'),
    (0.11, 'sensor_A', 'read'),
    (0.55, 'sensor_D', 'write'),
    (0.76, 'sensor_C', 'write')
]

system_flags = [1, 0, 1, 1, 0, 1]
system_state = {'active': True, 'calibrated': False, 'mode': 'hybrid'}

# Irrelevant helper: counts character frequency in sensor names (distractor)
def count_chars_in_labels(log):
    char_counter = Counter()
    for _, sensor, _ in log:
        for c in sensor:
            char_counter[c] += 1
    return char_counter

# Misleading diagnostic function (never called)
def legacy_diagnostic(seq):
    total = 0
    for x in seq:
        total += int(x * 100) ^ 255
    return total % 97

# Auxiliary transformation: extract timing values above threshold
def high_latency_ops(log, threshold=0.5):
    return [latency for latency, _, op in log if latency > threshold]

# Another red herring: computes XOR of flag bits (not used in final result)
def compute_flag_hash(flags):
    hashed = 0
    for i, f in enumerate(flags):
        hashed ^= (f << (i % 6))
    return hashed + 500  # arbitrary offset

# Real processing begins here
flag_sum = sum(system_flags)
dropped_packets = 0
if system_state['calibrated'] and not system_state['active']:
    dropped_packets = len(timing_log) // 4

# Extract latencies and group by sensor (used later)
sensor_data = defaultdict(list)
for latency, sensor, op in timing_log:
    sensor_data[sensor].append(latency)

# Compute average per sensor (some used, some not)
sensor_averages = {}
for sensor, latencies in sensor_data.items():
    avg = sum(latencies) / len(latencies)
    sensor_averages[sensor] = round(avg, 4)

# Dead code path: only runs if mode is 'debug'
if system_state['mode'] == 'debug':
    max_sensor_avg = max(sensor_averages.values())
else:
    # This branch looks important but only stores intermediate
    temp_vals = []
    for k, v in sensor_averages.items():
        if 'B' in k or 'D' in k:
            temp_vals.append(v * 1.1)
        else:
            temp_vals.append(v * 0.9)

# Core metric calculation
base_metric = 0
for latency, sensor, op in timing_log:
    if op == 'write':
        base_metric += latency * 100

# Secondary adjustment based on flag patterns
flag_pattern_value = 0
for i, flag in enumerate(system_flags):
    if flag == 1:
        flag_pattern_value += (i + 1) * 2

# Tertiary component: harmonic mean of high-latency ops
high_latencies = high_latency_ops(timing_log, 0.4)
if high_latencies:
    inv_sum = sum(1 / x for x in high_latencies)
    harmonic_mean = len(high_latencies) / inv_sum
else:
    harmonic_mean = 0

# Final aggregation function
def aggregate_metrics(log, flags):
    # Step 1: Sum all write operation latencies scaled by 100
    write_total = sum(latency * 100 for latency, _, op in log if op == 'write')
    
    # Step 2: Count read operations
    read_count = sum(1 for _, _, op in log if op == 'read')
    
    # Step 3: Apply flag multiplier (sum of flags + 1)
    flag_multiplier = sum(flags) + 1
    
    # Step 4: Add harmonic mean contribution (scaled)
    h_contrib = round(harmonic_mean * 10, 2) if 'harmonic_mean' in globals() else 0
    
    # Step 5: Adjust with sensor A's average latency if present
    a_latency = sensor_averages.get('sensor_A', 0) * 50 if 'sensor_averages' in globals() else 0
    
    # Step 6: Apply complex formula
    intermediate = (write_total + (read_count * flag_multiplier * 10))
    intermediate += h_contrib + a_latency
    
    # Step 7: Final bit manipulation mask (simulates hardware constraint)
    masked = int(intermediate) & 0xFFFF  # Keep lower 16 bits
    
    # Step 8: Map through mathematical transform
    result = (masked ^ 42) * 1.5  # XOR with magic number and scale
    
    return result

# Execute critical statement
final_diagnostic = aggregate_metrics(timing_log, system_flags)

# Print result as required
print(f"Target result: {final_diagnostic}")