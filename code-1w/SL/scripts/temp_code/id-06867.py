from collections import defaultdict, Counter

# Simulated health monitoring system with multiple sensor inputs
def analyze_vital(vital, baseline):
    return abs(vital - baseline) > 15

def compute_stability_index(readings):
    if len(readings) < 2:
        return 0
    diffs = [abs(readings[i] - readings[i-1]) for i in range(1, len(readings))]
    return sum(diffs) / len(diffs)

def detect_anomaly_cluster(logs):
    count = 0
    for log in logs:
        if log > 80:
            count += 1
            if count >= 3:
                return True
    return False

# Irrelevant helper function (decoy)
def calculate_fitness_score(age, bmi):
    score = 100 - abs(age - 30) * 0.5 - abs(bmi - 22) * 2
    bonus = 10 if bmi < 25 else 0
    return score + bonus

# Unused complex transformation (dead code path)
def transform_readings(raw):
    processed = []
    for val in raw:
        transformed = (val ** 0.5) * 3.14159
        if transformed > 50:
            processed.append(transformed / 2.5)
        else:
            processed.append(transformed + 10)
    return [round(p, 2) for p in processed]

# Misleading intermediate metric (distractor)
current_variability = 47.2
trend_projection = None
diagnostic_flag = False
baseline_shift = 0

# Core data structures
vital_signs = {
    'heart_rate': [72, 75, 78, 85, 92, 95, 90, 88],
    'oxygen_level': [98, 97, 96, 95, 94, 93, 92, 91],
    'respiratory_rate': [16, 17, 18, 20, 22, 24, 25, 26]
}

# Sensor metadata (partially irrelevant)
sensor_info = defaultdict(lambda: 'unknown')
sensor_info['device_id'] = 'HMS-7X'
sensor_info['firmware'] = '2.1.8'
sensor_info['calibration'] = '2023-11-05'

# Threshold configuration (critical)
thresholds = {
    'stability_limit': 7.5,
    'critical_spikes': 3,
    'baseline_drift': 12
}

# Historical anomaly records (distractor data)
historical_logs = [
    {'timestamp': '2023-10-01', 'severity': 2, 'type': 'spike'},
    {'timestamp': '2023-10-05', 'severity': 1, 'type': 'drift'},
    {'timestamp': '2023-10-12', 'severity': 3, 'type': 'spike'}
]

# Simulated current health data stream
health_data = [
    {'time': '13:00', 'hr': 72, 'ox': 98, 'rr': 16},
    {'time': '13:05', 'hr': 75, 'ox': 97, 'rr': 17},
    {'time': '13:10', 'hr': 78, 'ox': 96, 'rr': 18},
    {'time': '13:15', 'hr': 85, 'ox': 95, 'rr': 20},
    {'time': '13:20', 'hr': 92, 'ox': 94, 'rr': 22},
    {'time': '13:25', 'hr': 95, 'ox': 93, 'rr': 24},
    {'time': '13:30', 'hr': 90, 'ox': 92, 'rr': 25},
    {'time': '13:35', 'hr': 88, 'ox': 91, 'rr': 26}
]

# Auxiliary processing functions
def extract_trend(data, key_map):
    return [entry[key_map] for entry in data]

# Complex multi-step analysis pipeline
def process_metrics(data, config):
    # Extract relevant sequences
    heart_rates = extract_trend(data, 'hr')
    oxygen_levels = extract_trend(data, 'ox')
    respiratory_rates = extract_trend(data, 'rr')
    
    # Compute derived metrics
    hr_stability = compute_stability_index(heart_rates)
    ox_stability = compute_stability_index(oxygen_levels)
    rr_stability = compute_stability_index(respiratory_rates)
    
    # Detect deviation from normal patterns
    normal_baseline = 72
    elevated_periods = sum(1 for hr in heart_rates if analyze_vital(hr, normal_baseline))
    
    # Check for dangerous clustering
    severe_oxygen_drops = [1 for ox in oxygen_levels if ox < 93]
    
    # Primary diagnostic logic
    risk_factors = 0
    if hr_stability > config['stability_limit']:
        risk_factors += 2
    if len(severe_oxygen_drops) >= config['critical_spikes']:
        risk_factors += 3
    if elevated_periods >= config['baseline_drift']:
        risk_factors += 1
    
    # Secondary correlation analysis
    comp_count = Counter()
    for hr, ox in zip(heart_rates, oxygen_levels):
        if hr > 85 and ox < 95:
            comp_count['stress_event'] += 1
        elif hr < 75 and ox > 96:
            comp_count['resting_state'] += 1
    
    # Final risk calculation
    base_risk = risk_factors * 17
    modifier = comp_count['stress_event'] - comp_count['resting_state']
    final_score = base_risk + (modifier * 5)
    
    # Diagnostic mapping
    if final_score < 20:
        diagnosis_code = 101
    elif final_score < 40:
        diagnosis_code = 205
    elif final_score < 60:
        diagnosis_code = 312
    else:
        diagnosis_code = 418
    
    # Red herring computation (unused)
    avg_hr = sum(heart_rates) / len(heart_rates)
    peak_deviation = max(heart_rates) - min(heart_rates)
    trend_projection = (avg_hr + peak_deviation) / 2
    
    return diagnosis_code

# Execute main analysis
final_diagnostic = process_metrics(health_data, thresholds)

# Print result as required
print(f"Target result: {final_diagnostic}")