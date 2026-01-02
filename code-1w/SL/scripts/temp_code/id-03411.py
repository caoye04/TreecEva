from collections import defaultdict, Counter
import itertools

# Simulated sensor network data processing with diagnostic analysis

def collect_readings():
    # Real data collection (relevant)
    timestamps = list(range(100, 200, 3))
    raw_values = [t * 0.7 + ((t ** 2) % 17) for t in timestamps]
    return list(zip(timestamps, raw_values))

# Irrelevant auxiliary function - dead path
def deprecated_normalization(data):
    mean_val = sum(data) / len(data)
    normalized = [(x - mean_val) / mean_val for x in data]
    return normalized

# Misleading preprocessing - looks important but unused
def generate_shadow_metrics(readings):
    shadow = []
    for t, v in readings:
        s_val = (v * 1.05) ** 0.5 if v > 50 else v * 0.9
        parity_flag = bin(int(v)).count('1') % 2
        noise_estimate = (s_val * 123.456) % 1.0
        shadow.append((t, s_val, parity_flag, noise_estimate))
    return shadow

# Decoy transformation chain
transformation_pipeline = [
    lambda x: x * 1.1,
    lambda x: x + (x % 7),
    lambda x: abs(x - 100),
    lambda x: x ** 0.8
]

# Unused statistical baseline
baseline_stats = {
    'mean_ref': 42.5,
    'variance_floor': 12.1,
    'peak_threshold': 88.9
}

# Red herring: complex but unused bit manipulation
def analyze_pattern_entropy(value):
    shifted = (int(value * 100) ^ 0xFF) >> 2
    bitstring = bin(shifted)[2:]
    ones_ratio = bitstring.count('1') / len(bitstring) if bitstring else 0
    return shifted & 0xF, ones_ratio

# Main processing function with critical logic embedded

threshold_map = defaultdict(lambda: 65.0)
threshold_map.update({
    110: 70.1, 125: 68.2, 140: 72.3, 155: 69.8, 170: 75.4
})

status_flags = []
for ts in range(100, 200, 15):
    flag_code = 0
    if ts < 130:
        flag_code |= 1
    if ts % 25 == 0:
        flag_code |= 4
    if ts in {110, 140, 170}:
        flag_code |= 2
    status_flags.append((ts, flag_code))

flag_counter = Counter(flag for _, flag in status_flags)

# Critical function: filters and processes real data

def filter_anomalous_readings(raw_readings, safe_range=(40, 90)):
    filtered = []
    anomaly_log = []  # Collected but not used
    for t, v in raw_readings:
        if safe_range[0] <= v <= safe_range[1]:
            filtered.append((t, v))
        else:
            anomaly_entry = f"Anomaly at {t}: {v:.2f}"
            anomaly_log.append(anomaly_entry)
    return filtered

# Unused signal smoothing
smoothing_kernel = [0.25, 0.5, 0.25]
convolved_signal = []

# Key processing steps
sensor_data = collect_readings()
filtered_data = filter_anomalous_readings(sensor_data)

# Simulated calibration offset (irrelevant)
calibration_registry = {}
for i, (t, v) in enumerate(filtered_data):
    calib_key = f"CAL_{(t+i)%10}"
    calibration_registry[calib_key] = (v * 0.01) % 0.5

# Decoy: advanced frequency analysis (dead code)
frequency_components = []
for window in itertools.zip_longest(*[iter([r[1] for r in filtered_data])]*5):
    clean_window = [w for w in window if w is not None]
    component = sum(w * (-1)**i for i, w in enumerate(clean_window))
    frequency_components.append(component)

# Actual diagnostic logic

def compute_health_score(segment):
    base = sum(v for _, v in segment) / len(segment)
    penalty = 0
    if len(segment) < 10:
        penalty += 5.5
    return base - penalty

# Multi-stage conditional processing
interim_results = []
for i in range(0, len(filtered_data), 7):
    chunk = filtered_data[i:i+7]
    if len(chunk) >= 5:
        score = compute_health_score(chunk)
        timestamp_focus = chunk[len(chunk)//2][0]
        if timestamp_focus in threshold_map:
            if score > threshold_map[timestamp_focus]:
                interim_results.append(score * 0.95)
            else:
                interim_results.append(score * 1.05)
        else:
            interim_results.append(score)

aggregated_score = sum(interim_results)

# Final diagnostic calculation - this is the key statement
final_diagnostic = 0
for item in interim_results:
    if item > 60:
        final_diagnostic += item * 0.7
    else:
        final_diagnostic += item * 1.3

final_diagnostic = int(final_diagnostic // 1)  # Floor to integer

# Additional irrelevant computation
entity_tracker = defaultdict(int)
for ts, _ in filtered_data:
    entity_tracker[f"E_{ts%13}"] += 1

summary_keys = sorted(entity_tracker.keys())
key_hash = sum(int(k[2:]) * (i+1) for i, k in enumerate(summary_keys)) % 1000

# Output the required result
print(f"Result: {final_diagnostic}")