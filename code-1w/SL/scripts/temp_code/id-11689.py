from collections import defaultdict, Counter
import math

# Simulated system health monitoring with diagnostic filtering
def analyze_component_log(log_entries):
    severity_count = defaultdict(int)
    for entry in log_entries:
        _, severity = entry.split('_')
        severity_count[severity] += 1
    return dict(severity_count)

def compute_stability_score(metrics):
    base_score = sum(metrics) / len(metrics)
    variance_penalty = (max(metrics) - min(metrics)) * 0.1
    return round(base_score - variance_penalty, 3)

def filter_anomalies(data_stream, limit=25):
    anomalies = []
    for val in data_stream:
        if val > 90 or val < 10:
            anomalies.append(val)
    # Dead code path - never used
    if len(anomalies) > limit:
        return anomalies[:limit]
    return anomalies

def generate_report_snapshot(raw_logs):
    event_types = [log.split('_')[0] for log in raw_logs]
    type_freq = Counter(event_types)
    return {k: v for k, v in type_freq.items() if v > 1}

def calculate_phase_shift(signal_a, signal_b):
    shift = 0
    for i in range(min(len(signal_a), len(signal_b))):
        shift += (signal_a[i] - signal_b[i]) ** 2
    rms = math.sqrt(shift / len(signal_a))
    return round(rms, 4)

def merge_threshold_profiles(profiles):
    merged = {}
    for profile in profiles:
        for k, v in profile.items():
            merged[k] = merged.get(k, 0) + v
    return merged

def evaluate_system_integrity(checksums):
    total = 0
    for cs in checksums:
        total ^= int(cs, 16)  # Bitwise XOR of hex checksums
    return total % 1000

def process_diagnostics(trace, config):
    # Core logic begins
    diagnostics = defaultdict(float)
    
    # Component analysis (relevant)
    comp_analysis = analyze_component_log(trace['components'])
    critical_errors = comp_analysis.get('CRITICAL', 0)
    warnings = comp_analysis.get('WARNING', 0)
    
    # Stability metrics (relevant)
    stability = compute_stability_score(trace['performance'])
    diagnostics['stability'] = stability
    
    # Anomaly filtering (distractor - result not used directly)
    _ = filter_anomalies(trace['sensor_data'])
    
    # Phase calculation on signals (partially relevant)
    signal_x = trace['signals']['X']
    signal_y = trace['signals']['Y']
    phase_diff = calculate_phase_shift(signal_x, signal_y)
    diagnostics['drift'] = phase_diff * 100
    
    # Threshold comparison logic (critical)
    threshold_drift = config['drift_tolerance']
    threshold_errors = config['max_critical_errors']
    
    # Misleading intermediate computation (red herring)
    fake_risk_score = (warnings * 1.5 + critical_errors * 3) / (stability + 1)
    diagnostics['risk_proxy'] = fake_risk_score  # Not used in final decision
    
    # Data integrity verification (relevant but indirect)
    integrity_code = evaluate_system_integrity(trace['checksums'])
    
    # Final weighting logic
    error_penalty = critical_errors > threshold_errors
    drift_severity = diagnostics['drift'] > threshold_drift
    
    # Key branching logic
    if error_penalty and drift_severity:
        diagnostics['status'] = 2
    elif error_penalty or drift_severity:
        diagnostics['status'] = 1
    else:
        diagnostics['status'] = 0
    
    # Final diagnostic score generation (answer point)
    base = 1000
    modifier = (integrity_code % 50) - 25
    adjustment = -(critical_errors * 17) + (stability // 2)
    
    # Actual answer computation
    final_diagnostic = base + modifier + adjustment
    
    # Unused complex transformation (distractor)
    report_summary = generate_report_snapshot(trace['components'])
    profile_set = [{'drift': 12.3}, {'drift': 8.7}, {'drift': 15.1}]
    _ = merge_threshold_profiles(profile_set)
    
    return final_diagnostic

# Input data setup
health_trace = {
    'components': [
        'SYS_INIT_OK', 'MEM_WARN', 'DISK_CRITICAL', 'NET_OK',
        'CPU_WARNING', 'SECURITY_OK', 'DISK_CRITICAL', 'FAN_OK'
    ],
    'performance': [85, 88, 76, 92, 83],
    'sensor_data': [102, 45, 67, 89, 203, 73, 91, 22],
    'signals': {
        'X': [1, 2, 3, 4, 5],
        'Y': [1.1, 1.9, 3.2, 3.8, 5.1]
    },
    'checksums': ['1a3f', 'bc2e', '00ff', 'dead', 'beef']
}

thresholds = {
    'drift_tolerance': 40.0,
    'max_critical_errors': 1
}

# Execution point
final_diagnostic = process_diagnostics(health_trace, thresholds)
print(f"Target result: {final_diagnostic}")