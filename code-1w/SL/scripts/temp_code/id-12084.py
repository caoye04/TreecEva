from collections import defaultdict, Counter
from itertools import zip_longest

# Simulated sensor data with noise and redundant readings
def generate_sensor_stream(base_value, length, noise_factor=0.1):
    return [int(base_value + (i % 7) * noise_factor * 10) for i in range(length)]

# Irrelevant helper: computes unused spectral index
def compute_spectral_index(signal):
    total = 0
    for i in range(len(signal)):
        if i % 3 == 0:
            total += signal[i] * 1.5
    return int(total % 100)

# Distractor function: never called in main logic
def legacy_calibrate(data):
    adjusted = []
    for x in data:
        adjusted.append(x // 2 if x > 50 else x * 1.2)
    return adjusted

# Core processing pipeline
system_log = generate_sensor_stream(84, 12)
backup_log = generate_sensor_stream(72, 10)

# Inject decoy data structures
device_map = defaultdict(lambda: 'unknown')
device_map['sensor_a'] = 'active'
device_map['sensor_b'] = 'standby'
device_map['sensor_c'] = 'active'

# Redundant frequency analysis
freq_analysis = Counter(system_log)
dominant_freq = freq_analysis.most_common(1)[0][1] if freq_analysis else 0

# Simulated timestamp alignment (unused path)
timestamps = [1000 + i * 10 for i in range(15)]
aligned_data = list(zip_longest(system_log, backup_log, fillvalue=0))

# Decoy transformation chain
temp_shift = [x ^ 15 for x in system_log]
filtered_temp = [x for x in temp_shift if x % 2 == 0]
rolling_avg = sum(filtered_temp[-5:]) // 5 if len(filtered_temp) >= 5 else 0

# Real health trace generation
health_trace = []
for val in system_log:
    if val > 80:
        health_trace.append(val - 5)
    elif val > 70:
        health_trace.append(val - 2)
    else:
        health_trace.append(val)

# Secondary manipulation with slicing distraction
slice_offset = len(health_trace) // 3
working_slice = health_trace[slice_offset: -slice_offset] if slice_offset > 0 else health_trace

# Introduce bitwise red herring
bit_accum = 0
for v in working_slice:
    bit_accum ^= (v & 255) >> 2

# Real metric processor (key logic)
def process_metrics(primary, auxiliary):
    # Step 1: Baseline integrity check
    if not primary or len(primary) < 5:
        return -1
    
    # Step 2: Compute trimmed mean (excluding min/max)
    cleaned = sorted(primary)[1:-1]
    trimmed_mean = sum(cleaned) / len(cleaned)
    
    # Step 3: Apply decay factor based on length
    decay_factor = 0.95 ** (len(primary) - 8)
    
    # Step 4: Detect trend using first and last three elements
    early_avg = sum(primary[:3]) / 3
    late_avg = sum(primary[-3:]) / 3
    trend_score = (late_avg - early_avg) * 2
    
    # Step 5: Combine metrics
    base_score = trimmed_mean * decay_factor
    final_score = base_score + trend_score
    
    # Step 6: Round to nearest integer
    return int(round(final_score))

# Misleading intermediate diagnostic (decoy)
current_state = 'STABLE' if rolling_avg > 60 else 'CAUTION'

# Critical execution point
final_diagnostic = process_metrics(health_trace, system_log)

# Output the required result
print(f"Target result: {final_diagnostic}")