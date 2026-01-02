def detect_anomalies(sensor_data, threshold=0.75):
    moving_avg = [sum(sensor_data[i:i+3]) / 3 for i in range(len(sensor_data) - 2)]
    anomalies = [i for i, v in enumerate(moving_avg) if v > threshold]
    return set(anomalies)


def generate_checksum(sequence):
    checksum = 0
    for i, val in enumerate(sequence):
        checksum ^= (val * (i + 1)) % 256
    return checksum

# Simulated system telemetry
technical_flags = {"overheat": 1, "pressure_drop": 0, "flow_alert": 1, "calibration_error": 1}
sensor_readings = [0.4, 0.82, 0.83, 0.67, 0.91, 0.74, 0.88]

# Irrelevant diagnostic routine (dead path)
def legacy_diagnostic(proto_data):
    if len(proto_data) > 10:
        return sum(x ** 0.5 for x in proto_data if x > 5)
    else:
        return -1

# Unused intermediate variables (distractors)
baseline_correction = [x * 0.98 for x in sensor_readings]
adjusted_flow = sum(baseline_correction) * 1.05
dummy_matrix = [[i*j for j in range(3)] for i in range(3)]

# Core logic disguised among noise
fault_codes = [101, 205, 101, 307, 205, 404, 500]
error_freq = {}
for code in fault_codes:
    error_freq[code] = error_freq.get(code, 0) + 1

unique_codes = set(fault_codes)
repeated_codes = set([code for code, count in error_freq.items() if count > 1])

# Real but obscured computation chain
system_uptime = 1274  # minutes
maintenance_cycle = system_uptime // 60
is_active = technical_flags["flow_alert"] and not technical_flags["calibration_error"]

# Set operations with meaningful use
pending_alerts = {101, 205, 404}
resolved_alerts = {404, 500}
active_faults = pending_alerts - resolved_alerts

# Simulated log with red herring entries
system_log = {
    'events': ['startup', 'sensor_sync', 'data_dump', 'reboot'],
    'priority': [1, 3, 2, 1],
    'codes': [101, 307, 205, 101]
}

# Decoy function that's defined but not used
def compute_entropy(values):
    from math import log
    total = sum(values)
    probabilities = [v / total for v in values if v > 0]
    return -sum(p * log(p) for p in probabilities)

# Another irrelevant transformation
shifted_codes = [((code >> 2) | (code << 6)) & 0xFF for code in fault_codes]

# Key data extraction buried in logic
raw_sequence = [system_log['priority'][i] for i in range(len(system_log['priority'])) if system_log['codes'][i] in active_faults]

# Conditional mutation (looks complex but deterministic)
counted_risks = 0
for code in active_faults:
    if code in error_freq:
        counted_risks += error_freq[code]

# Distractor: unused statistical summary
mean_priority = sum(system_log['priority']) / len(system_log['priority'])
mode_code = max(set(fault_codes), key=fault_codes.count)

# Critical function using set and logical operations
def analyze_fault_codes(codes, log_entry):
    # Extract indices where codes in log match active interest
    indices = [i for i, c in enumerate(log_entry['codes']) if c in codes]
    values = [log_entry['priority'][i] for i in indices]
    
    # Real computation: weighted impact
    impact = 0
    for v in values:
        impact += v * (v + 1) // 2  # triangular weighting
    
    # Additional logic gate
    if technical_flags["overheat"] or "reboot" in log_entry['events']:
        impact *= 2
    
    # Final adjustment based on system state
    if maintenance_cycle > 20 and is_active:
        impact += 5
    else:
        impact -= 3
    
    return int(impact)

# Redundant checksum calculation (not used in final result)
checksum_value = generate_checksum(shifted_codes)
legacy_result = legacy_diagnostic([1, 2, 3])

# Actual execution point of interest
relevant_codes = active_faults.union({205})  # Redundant union for distraction
final_diagnostic = analyze_fault_codes(relevant_codes, system_log)

print(f"Target result: {final_diagnostic}")