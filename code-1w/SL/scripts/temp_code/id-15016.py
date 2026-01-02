from collections import defaultdict, Counter
import math

# Simulated health monitoring system with diagnostic logic
def collect_telemetry(sensor_inputs):
    raw_metrics = defaultdict(float)
    for sensor, readings in sensor_inputs.items():
        raw_metrics[sensor] = sum(readings) / len(readings)
    return raw_metrics

def compute_baselines(metrics):
    baselines = {}
    for k, v in metrics.items():
        baselines[k] = v * 0.95 if v > 70 else v * 1.05
    return baselines

def filter_anomalies(data, limit=50):
    # Irrelevant filtering (dead-end path)
    anomalies = [x for x in data if x > limit]
    return anomalies  # Unused later

def generate_placebo_report(records):
    # Distractor function: looks important but unused
    report = {'status': 'stable', 'flags': 0}
    for r in records:
        if r['value'] > 80:
            report['flags'] += 1
    return report

def rolling_window_smooth(values, window_size=3):
    smoothed = []
    for i in range(len(values)):
        start = max(0, i - window_size + 1)
        end = i + 1
        smoothed.append(sum(values[start:end]) / (end - start))
    return smoothed

def evaluate_risk_profile(baseline_dict):
    # Complex but irrelevant risk computation
    risk_score = 0.0
    for key, val in baseline_dict.items():
        if 'temp' in key:
            risk_score += math.sin(val / 10) * 2
        elif 'heart' in key:
            risk_score -= math.log(val + 1) / 3
    return round(risk_score, 4)

def extract_critical_flags(metrics):
    flags = []
    for metric_name, value in metrics.items():
        if 'o2' in metric_name and value < 95:
            flags.append((metric_name, 'LOW_O2'))
        if 'bp' in metric_name and (value > 140 or value < 90):
            flags.append((metric_name, 'BP_ALERT'))
    return flags

def analyze_metrics(data, config):
    # Core processing chain
    avg_metrics = collect_telemetry(data)
    base_refs = compute_baselines(avg_metrics)
    
    # Real usage begins
    o2_values = data['o2_saturation']
    smoothed_o2 = rolling_window_smooth(o2_values)
    latest_o2 = smoothed_o2[-1]
    
    bp_sys = data['blood_pressure_systolic']
    heart_rate_vals = data['heart_rate_bpm']
    
    # Intermediate decoy calculation
    hr_rolling_avg = [sum(heart_rate_vals[i:i+2])/2 for i in range(len(heart_rate_vals)-1)]
    hr_trend = 'rising' if hr_rolling_avg[-1] > hr_rolling_avg[0] else 'falling'
    
    # Key logic hidden among distractors
    deviation_score = 0
    if latest_o2 < config['o2_threshold']:
        deviation_score += int((config['o2_threshold'] - latest_o2) * 10)
    
    avg_bp = sum(bp_sys) / len(bp_sys)
    if avg_bp > config['bp_high_warn']:
        deviation_score += 15
    elif avg_bp < config['bp_low_warn']:
        deviation_score += 10
    
    # Hidden dependency on heart rate variability
    hr_set = set(heart_rate_vals)
    if len(hr_set) > 8:  # High variability
        deviation_score += 5
    
    # Critical flag extraction (used)
    active_flags = extract_critical_flags(avg_metrics)
    flag_penalty = len(active_flags) * 12
    
    # Final diagnostic is only here
    final_diagnostic = deviation_score + flag_penalty
    
    # Dead-end transformations
    summary_counter = Counter([f[1] for f in active_flags])
    baseline_snapshot = list(base_refs.values())[:3]
    placebo = generate_placebo_report([{'value': v} for v in baseline_snapshot])
    
    # Unused complex expression
    cryptic_score = sum(math.ceil(v/5) for v in baseline_snapshot) - len(placebo['status'])
    
    return final_diagnostic

# Simulated input data
health_data = {
    'o2_saturation': [96, 94, 92, 90, 88, 87, 86, 88, 89],
    'blood_pressure_systolic': [130, 135, 142, 145, 148, 150, 147],
    'heart_rate_bpm': [72, 75, 78, 80, 82, 85, 88, 90, 92, 95, 98],
    'temperature_f': [98.6, 98.8, 99.1, 99.3, 99.5],
    'respiratory_rate': [16, 17, 18, 19, 20, 22, 24, 26]
}

thresholds = {
    'o2_threshold': 90,
    'bp_high_warn': 140,
    'bp_low_warn': 90
}

# Execution point of interest
final_diagnostic = analyze_metrics(health_data, thresholds)
print(f"Target result: {final_diagnostic}")