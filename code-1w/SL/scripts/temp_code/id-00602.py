from collections import defaultdict, Counter
import math

# Simulated system telemetry data
timing_log = [
    (100, 'cpu_temp', 75), (101, 'gpu_temp', 68), (102, 'cpu_temp', 80),
    (103, 'fan_rpm', 2000), (104, 'cpu_temp', 85), (105, 'gpu_temp', 70),
    (106, 'disk_io', 120), (107, 'cpu_temp', 90), (108, 'fan_rpm', 2500)
]

system_flags = [True, False, True, True, False]
diagnostic_keys = ['cpu_temp', 'gpu_temp', 'fan_rpm']
baseline_readings = {'cpu_temp': 70, 'gpu_temp': 65, 'fan_rpm': 1800}

# Irrelevant auxiliary functions (decoy logic)
def legacy_calibrate(x):
    return (x * 0.95) + 5

def validate_checksum(data):
    return sum(h[0] for h in data) % 7 == 0

# Unused transformation pipeline
temp_scaling = lambda x: math.log(x) * 1.5

# Misleading intermediate aggregations
false_peak = max(val for _, key, val in timing_log if key == 'cpu_temp' and val > 100) if any(val > 100 for _, _, val in timing_log) else 0
spurious_avg = sum(val for _, key, val in timing_log if key == 'disk_io') / 2  # Only one disk_io entry

# Real processing begins here — deeply nested and mixed with noise
def extract_critical(readings, labels):
    result = defaultdict(list)
    for seq, tag, val in readings:
        if tag in labels:
            result[tag].append(val)
    return result

def compute_anomaly_score(data, base):
    score = 0
    for k, values in data.items():
        threshold = base[k]
        above_threshold = len([v for v in values if v > threshold])
        score += above_threshold * 1.5
    return score

# Bit manipulation red herring
def encrypt_sequence(seq):
    acc = 0
    for s in seq:
        acc ^= s << 2  # irrelevant bit shifting
    return acc % 1000

# Real aggregation function intertwined with distractions
def aggregate_metrics(logs, flags):
    # Step 1: Extract relevant sensor data
    filtered_data = extract_critical(logs, diagnostic_keys)
    
    # Step 2: Compute real anomaly score
    anomaly_score = compute_anomaly_score(filtered_data, baseline_readings)
    
    # Step 3: Use enumerate and zip in a meaningful but obscured way
    flag_pairs = list(zip(enumerate([f for f in flags if f]), [10, 20, 30]))
    adjustment_factor = sum(i * w for (i, _), w in flag_pairs)  # depends on active flags
    
    # Step 4: Apply adjustment using lambda in non-trivial context
    modifier = (lambda x: x ** 1.1 if x > 10 else x + 5)(adjustment_factor)
    
    # Step 5: Spurious use of Counter (distraction)
    key_distribution = Counter(key for _, key, _ in logs)
    phantom_entropy = sum(math.log(v) for v in key_distribution.values() if v > 1)
    
    # Step 6: Actual signal — count how many CPU temp readings exceed 80
    high_cpu_events = len([v for _, k, v in logs if k == 'cpu_temp' and v > 80])
    
    # Step 7: Combine real components
    raw_metric = anomaly_score + modifier
    
    # Step 8: Final computation path (obscured by surrounding noise)
    final_diagnostic = int(raw_metric) * 1000 + high_cpu_events  # core answer formation
    
    # Dead code branch (never executed)
    if False:
        fallback = encrypt_sequence([row[0] for row in logs])
        final_diagnostic -= fallback
    
    return final_diagnostic

# Execution point of interest
final_diagnostic = aggregate_metrics(timing_log, system_flags)
print(f"Target result: {final_diagnostic}")