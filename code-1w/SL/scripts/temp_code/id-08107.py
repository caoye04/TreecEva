from collections import defaultdict, Counter

# Simulated sensor data processing with diagnostic interference
def collect_sensor_readings():
    readings = [17, 23, 17, 45, 61, 23, 17, 9, 45, 61]
    noise_floor = 8
    adjusted = [r ^ noise_floor for r in readings]  # Bitwise interference
    return adjusted

def filter_anomalies(data):
    freq = Counter(data)
    anomalies = [k for k, v in freq.items() if v == 1]
    baseline = sum(data) // len(data)
    fluctuation = 0
    for i in range(len(data)):
        fluctuation += abs(data[i] - baseline)
    # Red herring: unused computation
    decoy_entropy = sum([v * v for v in freq.values()]) // (len(freq) + 1)
    return [x for x in data if x not in anomalies], fluctuation

def generate_signature(sequence):
    signature = 0
    for val in sequence:
        signature = (signature << 1) ^ val
        if signature > 10000:
            signature = signature % 9887
    # Distractor transformation
    mirror_val = sum([(signature >> i) & 1 for i in range(16)])
    return signature

def update_diagnostics(log, code, severity, timestamp):
    log[code] = {'severity': severity, 'ts': timestamp}
    # Dead path: never accessed later
    if severity > 5:
        log[code]['action'] = 'flagged'
    return len(log)

def analyze_pattern(buffer, log):
    pattern_value = buffer
    shift_key = len(log) % 7
    intermediate = (pattern_value >> shift_key) ^ (pattern_value << (6 - shift_key))
    intermediate &= 0xFFFF  # Clamp to 16 bits
    # Complex but irrelevant side-check
    parity_check = bin(intermediate).count('1') % 2
    decoy_sum = sum((intermediate >> i) & 3 for i in range(0, 16, 2))
    result = intermediate ^ 0xAAAA
    return result if result != 0 else 9999

# Main execution flow
if __name__ == '__main__':
    raw_data = collect_sensor_readings()

    # Irrelevant pre-processing (distractor)
    normalized = [x % 100 + 5 for x in raw_data]
    avg_normalized = sum(normalized) / len(normalized)
    deviation_score = sum(abs(n - avg_normalized) for n in normalized)

    clean_data, fluctuation_metric = filter_anomalies(raw_data)

    # Unused alternate path
    sorted_unique = sorted(set(clean_data))
    if len(sorted_unique) > 5:
        mid_vals = sorted_unique[1:-1]
    else:
        mid_vals = sorted_unique

    signature_buffer = generate_signature(clean_data)

    # Build diagnostic log with red herrings
    diagnostics_log = {}
    update_diagnostics(diagnostics_log, 'ERR_X1', 3, 1001)
    update_diagnostics(diagnostics_log, 'WARN_Y2', 6, 1003)
    update_diagnostics(diagnostics_log, 'INFO_Z3', 1, 1005)
    update_diagnostics(diagnostics_log, 'CRIT_A4', 8, 1007)

    # Add meaningless string manipulation distraction
    log_keys = ''.join(sorted(diagnostics_log.keys()))
    key_hash = 0
    for c in log_keys:
        key_hash = (key_hash * 31 + ord(c)) % 10007

    # Core answer-determining statement
    final_diagnostic = analyze_pattern(signature_buffer, diagnostics_log)

    # Additional decoy logic
    validation_set = {signature_buffer, key_hash, fluctuation_metric}
    if len(validation_set) % 2 == 0:
        final_diagnostic ^= 0x5555

    print(f"Result: {final_diagnostic}")