from collections import defaultdict, Counter

# Simulated system telemetry data
timing_samples = [127, 203, 98, 412, 255, 199, 301, 87, 156, 224]
error_sequence = [0, 1, 1, 0, 1, 0, 0, 1, 1, 0]
sensor_ids = ['S1', 'S2', 'S3', 'S4', 'S5', 'S1', 'S2', 'S3', 'S4', 'S5']

# Irrelevant precomputed constants (red herring)
baseline_offset = sum([x % 17 for x in range(50, 70)]) // 3
crypto_key = (2**13 - 1) * (2**19 - 1)
debug_mask = 0xFF0F

# Distractor: unused function
def analyze_signal_strength(signal):
    magnitude = 0
    for bit in range(16):
        magnitude += (signal >> bit) & 1
    return magnitude if magnitude % 2 else magnitude // 2

# Distractor: dead code path
temp_correction = False
if len(timing_samples) > 20:
    temp_correction = True
    adjusted_samples = [x * 1.05 for x in timing_samples]
else:
    buffer_zone = [0] * 15  # Unused allocation

# Real processing begins
system_flags = []
for i, t in enumerate(timing_samples):
    flag = 0
    if t > 200:
        flag |= 1
    if error_sequence[i] == 1:
        flag |= 2
    if sensor_ids[i] in ['S3', 'S4']:
        flag |= 4
    system_flags.append(flag)

timing_log = defaultdict(list)
for i, sid in enumerate(sensor_ids):
    timing_log[sid].append(timing_samples[i])

# Secondary distractor computation (unused)
sequence_stats = Counter(error_sequence)
recovery_attempts = sequence_stats[0] * sequence_stats[1] + 50

# Core logic hidden among distractions
def compute_stability_index(log_entry):
    mean_val = sum(log_entry) / len(log_entry)
    variance = sum((x - mean_val) ** 2 for x in log_entry) / len(log_entry)
    return round(mean_val - variance * 0.3, 4)

def evaluate_consistency(flags):
    transitions = 0
    for i in range(1, len(flags)):
        if (flags[i-1] & 1) != (flags[i] & 1):
            transitions += 1
    return transitions < 5

def aggregate_metrics(log, flags):
    stability_scores = []n    for key in ['S1', 'S2', 'S3', 'S4', 'S5']:
        if key in log and len(log[key]) >= 2:
            score = compute_stability_index(log[key])
            stability_scores.append(score)
    
    # Critical intermediate calculation (masked by other variables)
    raw_aggregate = sum(stability_scores) * 1000
    
    # Red herring: complex but unused bitwise combination
    decoy_result = 0
    for f in flags:
        decoy_result ^= (f << 2) | (f >> 1)
    
    # Actual answer derivation
    consistency_check = evaluate_consistency(flags)
    final_diagnostic = int(raw_aggregate) if consistency_check else -1
    
    # Additional distraction
    audit_trail = ''.join(chr(97 + (f % 26)) for f in flags[:4])
    
    return final_diagnostic

# Execution point of interest
final_diagnostic = aggregate_metrics(timing_log, system_flags)
print(f"Result: {final_diagnostic}")