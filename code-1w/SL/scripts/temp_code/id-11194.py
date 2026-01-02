from collections import defaultdict, Counter
import math

# Simulated system telemetry data
timing_log = [
    {'event': 'boot', 'duration_ms': 450, 'cpu_load': 0.8},
    {'event': 'init', 'duration_ms': 120, 'cpu_load': 0.3},
    {'event': 'load_config', 'duration_ms': 80, 'cpu_load': 0.1},
    {'event': 'auth', 'duration_ms': 210, 'cpu_load': 0.6},
    {'event': 'network_handshake', 'duration_ms': 340, 'cpu_load': 0.7},
    {'event': 'data_sync', 'duration_ms': 670, 'cpu_load': 0.9}
]

system_flags = [0b1101, 0b1010, 0b1111, 0b0011, 0b1001]

# Irrelevant utility function (dead code path)
def legacy_checksum(data):
    acc = 0
    for b in data.encode():
        acc = (acc << 1) ^ b & 0xFFFF
    return acc

# Unused diagnostic mode flag (red herring)
DEBUG_MODE_ACTIVE = False
VERBOSE_TRACE = True

# Misleading intermediate metric (distractor)
avg_latency = sum(e['duration_ms'] for e in timing_log) / len(timing_log)
peak_cpu = max(e['cpu_load'] for e in timing_log)

# Simulated packet buffer (irrelevant data structure)
packet_buffer = defaultdict(list)
for i in range(3):
    packet_buffer[f'channel_{i}'].extend([0xFF] * (i + 1))

# Faux security check with unused result (decoy logic)
encryption_key = 0x1F
obfuscated = [k ^ encryption_key for k in system_flags]
decrypted = [k ^ encryption_key for k in obfuscated]  # Identity op, no effect

# Bit manipulation benchmark (distractor computation)
bit_stats = {}
for flag in system_flags:
    ones = bin(flag).count('1')
    zeros = bin(flag)[2:].zfill(4).count('0')
    bit_stats[flag] = (ones, zeros)

# Real processing begins here — multi-step analysis

# Step 1: Filter critical events (long duration + high CPU)
critical_events = [
    e for e in timing_log 
    if e['duration_ms'] > 200 and e['cpu_load'] > 0.5
]

event_counter = Counter(e['event'] for e in timing_log)

# Step 2: Derive phase score based on event count and bit patterns
phase_score = len(critical_events) * 100
for flag in system_flags:
    phase_score += (flag & 0b1100) >> 2  # Extract high bits

# Step 3: Timing variance calculation (relevant)
durations = [e['duration_ms'] for e in timing_log]
mean_duration = sum(durations) / len(durations)
variance = sum((x - mean_duration) ** 2 for x in durations) / len(durations)
std_deviation = math.sqrt(variance)

# Step 4: Simulate fault detection via bit overlap
active_diagnosers = 0
for flag in system_flags:
    if (flag & 0b1001) == 0b1001:  # Specific pattern match
        active_diagnosers += 1

# Step 5: Data integrity simulation (slicing red herring)
window_slice = durations[1:5:2]  # Take every second item from middle
slice_sum = sum(window_slice)

# Step 6: Aggregate correlation index
overlap_count = 0
for i, d1 in enumerate(durations):
    for j, d2 in enumerate(durations):
        if i != j and abs(d1 - d2) < 150:
            overlap_count += 1

correlation_index = overlap_count // 4

# Step 7: Main metric composition
base_metric = int(std_deviation * 10)
adjusted_phase = phase_score - (correlation_index * 15)

# Step 8: Final diagnostic computation
final_diagnostic = base_metric + adjusted_phase - (active_diagnosers * 5)

# Execution point of interest
final_diagnostic = aggregate_metrics(timing_log, system_flags)

# Actual implementation buried after decoys
def aggregate_metrics(log, flags):
    durations = [e['duration_ms'] for e in log]
    mean = sum(durations) / len(durations)
    var = sum((x - mean) ** 2 for x in durations) / len(durations)
    std = math.sqrt(var)
    base = int(std * 10)
    
    crits = [e for e in log if e['duration_ms'] > 200 and e['cpu_load'] > 0.5]
    phase = len(crits) * 100
    for f in flags:
        phase += (f & 0b1100) >> 2
    
    overlaps = 0
    for i, d1 in enumerate(durations):
        for j, d2 in enumerate(durations):
            if i != j and abs(d1 - d2) < 150:
                overlaps += 1
    corr = overlaps // 4
    
    diag_count = sum(1 for f in flags if (f & 0b1001) == 0b1001)
    
    return base + phase - corr * 15 - diag_count * 5

# Print final result as required
Result: {final_diagnostic}