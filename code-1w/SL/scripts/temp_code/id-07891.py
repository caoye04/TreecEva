from collections import defaultdict, Counter
import math

# Simulated system telemetry data
telemetry_packets = [
    [12, 15, 14, 16, 13],
    [8, 9, 10, 11, 12],
    [20, 18, 22, 19, 21],
    [5, 7, 6, 8, 9],
    [30, 31, 29, 32, 33]
]

# Irrelevant cache initialization (distractor)
cache_map = defaultdict(lambda: 'uncached')
for i in range(10):
    cache_map[i] = 'cached'

# Misleading diagnostic flag (red herring)
anomaly_detected = False

# Simulate fake error log processing (dead code path)
error_codes = {101, 102, 105}
error_count = 0
for packet in telemetry_packets:
    if sum(packet) > 100:
        error_count += 1  # Unused metric

# Real data processing begins here
log_stats = []
system_load = []

for idx, packet in enumerate(telemetry_packets):
    avg_val = sum(packet) / len(packet)
    variance = sum((x - avg_val) ** 2 for x in packet) / len(packet)
    std_dev = math.sqrt(variance)
    
    # Distractor transformation (not used later)
    normalized = [round((x - avg_val) / (std_dev + 1e-8), 2) for x in packet]
    
    # Relevant metrics
    log_stats.append({'mean': avg_val, 'dev': std_dev})
    system_load.append(len([x for x in packet if x > avg_val]))

# Fake security checksum (decoy)
checksum = 0
for i in range(len(system_load)):
    checksum ^= (system_load[i] * i + 7) % 13

# Another red herring: performance score with no impact
perf_score = 0
for stat in log_stats:
    perf_score += stat['mean'] // (stat['dev'] + 1)

# Critical function that combines actual logic
def analyze_pattern(seq):
    count_seq = Counter(seq)
    mode_val = max(count_seq, key=count_seq.get)
    return mode_val * len(count_seq)

# Secondary analysis with misleading intermediate
threshold_alerts = []
for stat in log_stats:
    if stat['mean'] > 15:
        threshold_alerts.append(True)
    else:
        threshold_alerts.append(False)

alert_code = sum(1 << i for i, val in enumerate(threshold_alerts) if val)

# Actual core logic buried among distractions
def compute_stability_index(metrics, load_profile):
    base_index = 0
    for m in metrics:
        base_index += int(m['mean'] * (m['dev'] + 1))
    
    adjustment = 0
    for i, load in enumerate(load_profile):
        if i % 2 == 0:
            adjustment += load * 2
        else:
            adjustment -= load
    
    return base_index + adjustment

# Fake recursive function (never called - dead code)
def bad_recursive(n):
    if n <= 1:
        return 1
    return bad_recursive(n-1) + bad_recursive(n-2)

# Real processing function
def process_metrics(metrics, load_profile):
    stability = compute_stability_index(metrics, load_profile)
    pattern_weight = analyze_pattern(load_profile)
    
    # Final computation (answer depends only on these)
    raw_result = stability + pattern_weight
    
    # Apply meaningless obfuscation
    encoded = (raw_result ^ 0xCAFEBABE) & 0xFFFFFFFF
    decoded = (encoded ^ 0xCAFEBABE) & 0xFFFFFFFF
    
    return decoded

# Execution point of interest
final_diagnostic = process_metrics(log_stats, system_load)

# Print result as required
print(f"Target result: {final_diagnostic}")