from collections import defaultdict, Counter
import math

# Simulated spacecraft subsystem telemetry and fault analysis

def collect_telemetry():
    # Real data generator (relevant)
    log = []
    for t in range(60):
        entry = {
            'time': t,
            'voltage': 120 + (t % 7),
            'temp_core': 45 + (t * 0.3),
            'status_flag': t ^ (t % 5),
            'packet_id': (t * 11) % 13
        }
        log.append(entry)
    return log

def compute_redundancy_checksum(data):
    # Irrelevant computation - red herring
    total = 0
    for d in data:
        total += d['packet_id'] * 3
    return total % 1000

def evaluate_power_risk(voltage_series):
    # Misleading risk model - dead end
    avg_v = sum(voltage_series) / len(voltage_series)
    if avg_v < 122:
        return 'ELEVATED'
    return 'NORMAL'

def extract_anomalies(telemetry):
    # Extracts anomalies but used to distract
    anomalies = []
    for entry in telemetry:
        if entry['temp_core'] > 60:
            anomalies.append(entry['time'])
    return anomalies

def generate_synthetic_diagnostics(anomalies):
    # Decoy function - generates fake metrics
    if not anomalies:
        return [0] * 5
    synthetic = []
    for a in anomalies:
        val = (a * 17) % 19
        if val > 10:
            val = val ^ 5
        synthetic.append(val)
    return synthetic

def calculate_entropy(signal):
    # Complex but irrelevant entropy calculation
    counts = Counter(signal)
    total = len(signal)
    entropy = 0.0
    for count in counts.values():
        p = count / total
        if p > 0:
            entropy -= p * math.log2(p)
    return round(entropy, 4)

def validate_system_integrity(telemetry):
    # Unused integrity check - distractor
    packet_sequence = [e['packet_id'] for e in telemetry]
    expected = list(range(13)) * 5 + list(range(10))
    return packet_sequence == expected

def decode_fault_signature(flags):
    # Core relevant logic: processes status flags using bitwise analysis
    signature = 0
    for flag in flags:
        # Transform flag via XOR and bit rotation
        rotated = ((flag << 1) | (flag >> 7)) & 0xFF
        signature ^= rotated
    return signature

def analyze_fault_sequence(log_entries, flags):
    # Key function: combines multiple concepts
    voltage_series = [e['voltage'] for e in log_entries]
    temp_series = [e['temp_core'] for e in log_entries]
    
    # Irrelevant assignments (distractors)
    avg_temp = sum(temp_series) / len(temp_series)
    peak_voltage = max(voltage_series)
    stability_score = (peak_voltage - avg_temp) * 0.7
    
    # Red herring conditional
    if stability_score > 100:
        diagnostic_offset = 50
    else:
        diagnostic_offset = 25
    
    # Extract status flags (relevant path)
    raw_flags = [e['status_flag'] for e in log_entries]
    
    # Apply complex transformation (key step)
    filtered_flags = []
    for f in raw_flags:
        # Non-linear filtering
        if (f ^ 3) % 4 == 0:
            filtered_flags.append(f & 0x0F)
    
    # Secondary filtering based on time correlation
    correlated_flags = []
    for i, flag in enumerate(filtered_flags):
        if i == 0:
            correlated_flags.append(flag)
        else:
            # Cross-correlate with previous state using XOR
            prev = correlated_flags[-1]
            combined = (flag ^ prev) & 0x07
            if combined != 0:
                correlated_flags.append(combined)
    
    # Compute final signature from correlated flags
    base_signature = decode_fault_signature(correlated_flags)
    
    # Final adjustment using mathematical operations
    adjustment = len(correlated_flags) ** 2
    final_value = base_signature * 3 + adjustment - diagnostic_offset
    
    # Dead code path - never reached due to logic above
    if False and len(log_entries) > 1000:
        fallback = sum([e['packet_id'] for e in log_entries])
        final_value = fallback // 10
    
    return int(final_value)

# Main execution flow
if __name__ == '__main__':
    # Generate real telemetry data
    telemetry_log = collect_telemetry()
    
    # Irrelevant data structures (distractors)
    voltage_readings = [entry['voltage'] for entry in telemetry_log]
    time_stamps = [entry['time'] for entry in telemetry_log]
    packet_cycle = [p['packet_id'] for p in telemetry_log]
    
    # Compute useless metrics (red herrings)
    checksum = compute_redundancy_checksum(telemetry_log)
    power_risk = evaluate_power_risk(voltage_readings)
    anomaly_list = extract_anomalies(telemetry_log)
    synthetic_metrics = generate_synthetic_diagnostics(anomaly_list)
    entropy_metric = calculate_entropy(packet_cycle)
    integrity_status = validate_system_integrity(telemetry_log)
    
    # System flags derived from telemetry (used in actual logic)
    system_flags = [entry['status_flag'] for entry in telemetry_log]
    
    # Core diagnostic analysis (critical path)
    final_diagnostic = analyze_fault_sequence(telemetry_log, system_flags)
    
    # Print result as required
    print(f"Target result: {final_diagnostic}")