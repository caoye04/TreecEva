from collections import defaultdict, Counter
import math

# Simulated telemetry data from satellite subsystems
telemetry = {
    'power': [12.4, 12.6, 12.5, 11.9, 12.0],
    'temp_core': [67, 68, 72, 75, 73],
    'temp_solar': [45, 50, 52, 49, 47],
    'radiation': [0.8, 0.9, 1.2, 1.1, 1.3],
    'attitude': [0.02, 0.05, 0.04, 0.06, 0.03]
}

# Thresholds for anomaly detection
thresholds = {
    'power_low': 12.0,
    'temp_high': 70,
    'rad_high': 1.0,
    'attitude_drift': 0.05
}

# Irrelevant baseline metrics (distractor)
baseline_metrics = defaultdict(float)
for key in telemetry:
    baseline_metrics[key] = sum(telemetry[key]) / len(telemetry[key])

# Historical fault patterns - mostly unused (dead path)
fault_patterns = Counter()
fault_patterns['overheat'] = 3
fault_patterns['low_power'] = 1
fault_patterns['noise_spike'] = 5

# Decoy function that looks important but isn't called
def compute_orbit_stability(data):
    stability_score = 0
    for val in data.get('attitude', []):
        stability_score += math.cos(val) * 0.1
    return round(stability_score, 3)

# Fake calibration routine (unused)
calibration_map = {}
for i, reading in enumerate(telemetry['radiation']):
    calibration_map[i] = reading * (1.0 + 0.05 * math.sin(i))

# Auxiliary transformation with partial relevance
transformed = {k: [round(x * 1.02, 2) for x in v] for k, v in telemetry.items()}

# Red herring: complex-looking normalization (only one value used later)
normalized = {}
for key, values in transformed.items():
    mean_val = sum(values) / len(values)
    normalized[key] = [round((v - mean_val) / mean_val * 100, 3) for v in values]

# Spurious statistical computation (mostly irrelevant)
skew_estimate = 0.0
for vals in normalized.values():
    if len(vals) > 2:
        cube_dev = sum((x - sum(vals)/len(vals))**3 for x in vals)
        skew_estimate += cube_dev / len(vals)

# Decoy list of diagnostic codes (misleading)
diag_codes = [f"ERR_{100+i}" for i in range(len(telemetry) * 2)]

def detect_anomalies(stream, limits):
    anomalies = []
    # Check each telemetry stream against thresholds
    for key, readings in stream.items():
        if key == 'power':
            for r in readings:
                if r < limits['power_low']:
                    anomalies.append((key, r, 'LOW'))
        elif key == 'temp_core':
            for r in readings:
                if r > limits['temp_high']:
                    anomalies.append((key, r, 'HIGH'))
        elif key == 'radiation':
            for r in readings:
                if r > limits['rad_high']:
                    anomalies.append((key, r, 'HIGH'))
        elif key == 'attitude':
            for r in readings:
                if r > limits['attitude_drift']:
                    anomalies.append((key, r, 'DRIFT'))
    return anomalies

# Secondary analysis with lambda (partially relevant)
evaluate_risk_level = lambda anomalies: max([0] + [len(anomalies)//2])

# Unused predictive model stub (dead code)
predict_failure_window = lambda count: "unknown"
if evaluate_risk_level([]) > 3:
    predict_failure_window(1)

# Core diagnostic logic
anomaly_list = detect_anomalies(telemetry, thresholds)
risk_score = evaluate_risk_level(anomaly_list)

# Misdirection: entropy calculation on irrelevant data
symbol_freq = Counter()
for tp in ['A','B','A','C','B','A']:
    symbol_freq[tp] += 1
entropy = 0.0
for freq in symbol_freq.values():
    p = freq / 6.0
    entropy -= p * math.log(p, 2)

# Real work happens here: state classification
state_flags = defaultdict(bool)
for comp, val, typ in anomaly_list:
    if comp == 'temp_core' and typ == 'HIGH':
        state_flags['thermal_issue'] = True
    if comp == 'power' and typ == 'LOW':
        state_flags['power_issue'] = True

# Another distraction: bit manipulation on sensor index
sensor_signature = 0
for i, k in enumerate(sorted(telemetry.keys())):
    shift = i % 4
    sensor_signature ^= (hash(k) & 0xFF) << shift

# Final system health analysis
def analyze_system_state(data, thres):
    # Re-check critical conditions
    temp_readings = data['temp_core']
    high_temps = [t for t in temp_readings if t > thres['temp_high']]
    power_issues = [p for p in data['power'] if p < thres['power_low']]
    
    # Critical path: only this computation matters for final answer
    base_severity = len(high_temps) * 2 + len(power_issues) * 3
    
    # Distracting adjustment based on radiation (not actually impactful)
    rad_bursts = [r for r in data['radiation'] if r > thres['rad_high']]
    if len(rad_bursts) > 2:
        base_severity += 1  # Rarely triggered
    
    # Key adjustment: attitude oscillation increases severity
    drift_events = [a for a in data['attitude'] if a > thres['attitude_drift']]
    if len(drift_events) >= 2:
        base_severity += 2
    
    # Final nonlinear scaling
    severity_index = int(math.pow(base_severity, 1.5)) if base_severity > 0 else 0
    
    # Irrelevant formatting
    status_code = f"SYS-{severity_index:03d}"
    
    # This is the actual answer variable
    final_diagnostic = severity_index + 100
    
    return final_diagnostic

# Execute main analysis
final_diagnostic = analyze_system_state(telemetry, thresholds)

# Print result as required
print(f"Target result: {final_diagnostic}")