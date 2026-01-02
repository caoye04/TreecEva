import itertools

# Simulated system telemetry data
sensor_ids = [101, 102, 103, 104]
timestamps = [1623456780, 1623456785, 1623456790, 1623456795]
raw_readings = [512, 768, 256, 896]

# Irrelevant auxiliary mappings (distractor)
id_to_location = {101: 'A', 102: 'B', 103: 'C', 104: 'D'}
anomaly_weights = {'A': 0.1, 'B': 0.3, 'C': 0.2, 'D': 0.4}

# System state trackers (some relevant, some misleading)
current_state = {'status': 'active', 'mode': 'diagnostic'}
historical_max = 1024
device_uptime = 43200  # seconds

# Noise filter parameters (partially irrelevant)
noise_floor = 64
smoothing_factor = 0.85

# Diagnostic configuration
system_threshold = 700
activation_limit = 500
grace_period = 5

# False alarm risk calculator (dead function - red herring)
def calculate_farf(readings):
    if not readings:
        return 0.0
    peak = max(readings)
    return (peak / historical_max) * 0.1

# Unused legacy function (decoy)
def legacy_analysis(seq):
    return sum(x ** 0.5 for x in seq if x > 0)

# Core processing pipeline
log_data = list(zip(sensor_ids, timestamps, raw_readings))

def extract_anomalies(data, threshold):
    anomalies = []
    for sid, ts, val in data:
        if val > threshold:
            anomalies.append((sid, val))
    return anomalies

# Bit manipulation for checksum (reused later - relevant)
def compute_checksum(value):
    shifted = (value << 3) & 0xFF
    xor_fold = shifted ^ (shifted >> 4)
    return xor_fold % 256

# Higher-order function with lambda (required feature)
reading_filter = lambda func, data: list(filter(func, data))

# Data enrichment with distractors
enriched_logs = []
for entry in log_data:
    sensor_id, tstamp, reading = entry
    checksum = compute_checksum(reading)
    # Add decoy fields
    score_metric = (reading // 10) * 2  # irrelevant
    risk_flag = score_metric > 90  # misleading
    enriched_logs.append((*entry, checksum, score_metric, risk_flag))

# Apply filter to find high-energy events
high_energy = reading_filter(lambda x: x[2] > activation_limit, log_data)

# Simulate temporal grouping (itertools usage - required feature)
grouped_by_time = []
for key, group in itertools.groupby(enriched_logs, key=lambda x: x[1] // 100):
    grouped_by_time.append(list(group))

# Secondary filtering - only groups with multiple entries
significant_groups = [g for g in grouped_by_time if len(g) >= 2]

# Compute aggregated metrics
aggregated_peak = 0
if significant_groups:
    all_vals = [item[2] for group in significant_groups for item in group]
    aggregated_peak = max(all_vals) if all_vals else 0
else:
    aggregated_peak = max(r for _, _, r in log_data)

# Checksum-based validation chain
validation_chain = []
for log in enriched_logs:
    _, _, r, csum, _, _ = log
    if r > system_threshold:
        validation_chain.append(csum)

# Recursive reduction (relevant logic)
def reduce_checksums(checksums):
    if len(checksums) <= 1:
        return checksums[0] if checksums else 0
    reduced = [(a ^ b) + 1 for a, b in zip(checksums[::2], checksums[1::2])]
    return reduce_checksums(reduced)

validation_score = reduce_checksums(validation_chain)

# Final diagnostic computation path
anomaly_list = extract_anomalies(log_data, system_threshold)
diagnostic_weight = len(anomaly_list) * 100

# Multi-factor diagnostic fusion
fusion_factors = [
    diagnostic_weight,
    validation_score * 5,
    aggregated_peak - 200,
    50  # baseline offset
]

intermediate_diagnostic = sum(fusion_factors)

# Final nonlinear transformation
final_diagnostic = int((intermediate_diagnostic ** 0.5) * 3.141592) % 100000

# Output target result
print(f"Result: {final_diagnostic}")