import math

# Simulated sensor array data with noise and redundancy
data_stream = [
    (1.2, 'active', 100), (3.4, 'idle', 105), (2.1, 'active', 98),
    (5.6, 'fault', 110), (4.3, 'active', 102), (6.7, 'idle', 103),
    (0.9, 'active', 99), (8.8, 'fault', 115), (7.2, 'active', 101)
]

# Irrelevant metadata (distractor)
system_logs = {'version': '2.1.0', 'uptime': 87451, 'cores': 4}
calibration_offsets = [0.1, -0.05, 0.2, 0.0]  # Unused in final logic

# Noise threshold parameters (some are red herrings)
noise_threshold = 5.0
stability_window = 3
min_signal_strength = 0.5

# Extract relevant entries: only 'active' status and above minimum signal
raw_signals = [entry[0] for entry in data_stream if entry[1] == 'active' and entry[0] >= min_signal_strength]
statuses = [entry[1] for entry in data_stream]  # Distractor list - unused later

# Apply moving average filter to smooth signal (relevant)
smoothed_signals = []
for i in range(len(raw_signals)):
    window = raw_signals[max(0, i - stability_window + 1):i + 1]
    smoothed_signals.append(sum(window) / len(window))

# Secondary processing: detect anomalies (partially irrelevant)
anomalies = []
decoy_result = 0
for val in smoothed_signals:
    if val > noise_threshold:
        anomalies.append(val * 0.9)
    else:
        decaying_val = val
        for _ in range(3):
            decaying_val = math.sqrt(decaying_val)  # Complex but irrelevant transformation
        decoy_result += decaying_val

# Real signal filtering based on bounded deviation from mean (key path)
mean_signal = sum(smoothed_signals) / len(smoothed_signals)
filtered_data = [s for s in smoothed_signals if abs(s - mean_signal) <= 1.5]

# Checksum decoy computation (dead path)
temp_checksum = 0
for idx, val in enumerate(filtered_data):
    temp_checksum ^= int(val * 10) & 0xFF  # Bit manipulation red herring

# Dummy function that looks important but isn't called
def compute_integrity_score(data):
    return sum(math.log(abs(x) + 1) for x in data) % 17

# Actual calibration factor derived from system uptime (misleading comment)
# Note: uptime is from logs but not actually used
calibration_factor = (system_logs['uptime'] % 100) * 0.01  # Evaluates to 51 * 0.01 = 0.51

# Core diagnostic processor
def process_readings(readings, factor):
    adjusted = [r * factor for r in readings]
    
    # Nested conditional with short-circuiting (relevant)
    base_score = 0
    for a in adjusted:
        if a > 1.0 or (a > 0.5 and len(readings) > 3):
            base_score += a ** 2
        else:
            base_score -= a
    
    # Complex aggregation using dictionary accumulation (relevant)
    stats = {}
    for i, v in enumerate(adjusted):
        bucket = i % 3
        stats[bucket] = stats.get(bucket, 0) + v * (i + 1)
    
    # Final score combines list comprehension and conditional logic
    bonus = sum([stats[k] * 0.1 for k in stats if k in filtered_data])  # Mixed-type comparison fails silently
    
    # Ultimate result uses modular arithmetic and summation
    total = int(round(base_score * 100 + bonus)) % 99999
    return total

# Execute main logic
device_state = 'nominal'
if device_state != 'faulty':
    intermediate_flag = any([x > 4.0 for x in raw_signals])
    if intermediate_flag:
        scaling_hint = sum(1 for x in statuses if x == 'idle')  # Distractor count
        # The real work happens here:
        final_diagnostic = process_readings(filtered_data, calibration_factor)

print(f"Target result: {final_diagnostic}")