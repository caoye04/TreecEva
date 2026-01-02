def analyze_events(raw_data, thresholds):
    # Irrelevant preprocessing (distractor)
    normalized = [x * 1.05 for x in raw_data if x > 0]
    adjusted = [y - 0.7 for y in normalized]

    # Real signal extraction
    valid_events = [z for z in raw_data if z % 4 == 3]
    event_sum = sum(valid_events)

    # Dead code path (misleading)
    temp_result = None
    if len(adjusted) > 100:
        temp_result = sum(adjusted) // len(adjusted)

    # Bit manipulation for checksum (relevant)
    checksum = 0
    for val in valid_events:
        checksum ^= (val << 1) | (val >> 2)
    checksum &= 0xFFFF

    return event_sum, checksum


def filter_anomalies(records):
    # Set operations (required feature)
    critical_codes = {911, 808, 707, 505}
    observed = set(record[1] for record in records)
    anomalies = observed & critical_codes

    # Unused computation (red herring)
    suspicious_ratio = len([r for r in records if r[2] < 0]) / len(records) if records else 0

    return len(anomalies) > 0


def compute_diagnostics(data_stream):
    # Modular arithmetic and tuple unpacking
    phases = [(x % 7, x % 5, x % 3) for x in data_stream]
    phase_counts = {}
    for p in phases:
        phase_counts[p] = phase_counts.get(p, 0) + 1

    # Decoy statistical analysis
    avg_phase = sum(p[0] for p in phases) / len(phases) if phases else 0
    variance_proxy = sum((p[1] - avg_phase) ** 2 for p in phases) / len(phases) if phases else 0

    # Core logic: find most frequent phase
    dominant_phase = max(phase_counts, key=lambda item: item[1]) if phase_counts else (0,0,0)
    return (dominant_phase[0] * 100) + (dominant_phase[1] * 10) + dominant_phase[2]


def process_metrics(entries, flags):
    # Main workflow with distractions
    staging_buffer = []
    for entry in entries:
        timestamp, code, value = entry
        if code in flags['safe_list']:
            continue
        if value < flags['threshold']:
            staging_buffer.append(value * 2)
        else:
            staging_buffer.append(value + 1)

    # Distracting string manipulation (irrelevant)
    log_id = "evt-" + "-".join(str(len(entries))[i] for i in range(len(str(len(entries)))))
    metadata_tag = log_id.upper().replace('-', '_')

    # Key transformation chain
    transformed = [t ^ 0xAA for t in staging_buffer]  # Bitwise XOR
    filtered = [t for t in transformed if t % 3 != 0]
    scaled = sum(filtered) * 0.9

    # Tuple-based routing (relevant)
    mode_flag = (flags['debug'], flags['active'])
    if mode_flag == (False, True):
        scaled += 50
    elif mode_flag == (True, False):
        scaled -= 25

    return int(scaled)

# Simulate telemetry input
import math
base_values = [17, 22, 31, 39, 43, 55, 67]
log_entries = []
for i, v in enumerate(base_values):
    code = (v * 13) % 1000
    str_value = ''.join(reversed(str(v)))
    num_value = int(str_value) if str_value.isdigit() else 0
    log_entries.append((1000+i, code, num_value))

# Misleading auxiliary data (distractor)
system_health = {
    'uptime': 97.8,
    'load_avg': [1.2, 1.5, 1.7],
    'cache_hit_ratio': 0.88
}

# Flags with red herrings and relevant settings
system_flags = {
    'safe_list': {123, 456, 789},
    'threshold': 15,
    'debug': False,
    'active': True,
    'timeout_ms': 5000,
    'retries': 3
}

# Orchestration with decoy calls
_, chksum = analyze_events(base_values, system_flags)
anomaly_detected = filter_anomalies(log_entries)
diag_code = compute_diagnostics(base_values)

# Critical execution point
final_diagnostic = process_metrics(log_entries, system_flags)

print(f"Result: {final_diagnostic}")