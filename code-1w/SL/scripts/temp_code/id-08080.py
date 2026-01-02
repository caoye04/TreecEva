from collections import defaultdict, Counter

# Simulated sensor data aggregation for a biomedical monitoring system
def collect_telemetry():
    readings = [
        ('temp', 36.8), ('hr', 72), ('spo2', 98),
        ('temp', 37.1), ('hr', 75), ('spo2', 97),
        ('temp', 37.5), ('hr', 80), ('spo2', 96),
        ('temp', 38.2), ('hr', 88), ('spo2', 95)
    ]
    
    # Aggregating by metric type
    data = defaultdict(list)
    for key, value in readings:
        data[key].append(value)
    
    return data

# Auxiliary function to compute moving average (distraction: not used in final path)
def moving_average(values, window=2):
    if len(values) < window:
        return [values[0]]
    return [sum(values[i:i+window]) / window for i in range(len(values)-window+1)]

# Misleading diagnostic using variance (dead code path)
def assess_stability(metrics):
    variances = {}
    for k, v in metrics.items():
        mean_val = sum(v) / len(v)
        variances[k] = sum((x - mean_val)**2 for x in v) / len(v)
    return variances  # Never used

# Core processing function with relevant logic buried among distractors
def normalize_signal(x, baseline=37.0):
    return abs(x - baseline) * 1.618

def evaluate_risk_level(value, category):
    thresholds = {
        'temp': (37.0, 38.0, 39.0),
        'hr': (100, 110, 120),
        'spo2': (95, 90, 85)
    }
    low, med, high = thresholds.get(category, (0, 0, 0))
    return 1 if value > low else 0

# Real computation path obscured by irrelevant transformations
def transform_readings(raw_data):
    processed = {}
    temp_vals = raw_data['temp']
    hr_vals = raw_data['hr']
    spo2_vals = raw_data['spo2']

    # Distractor: complex but unused transformation chain
    smoothed_temp = [round(t * 0.98 + 0.5, 2) for t in temp_vals]
    hr_shifted = [(h + 5) % 120 for h in hr_vals]
    
    # Relevant only in part: we take last temp and apply normalization
    latest_temp = temp_vals[-1]
    normalized_deviation = normalize_signal(latest_temp)
    
    # Dead logic branch
    if len(spo2_vals) > 5:
        critical_drop = any(s < 90 for s in spo2_vals)
    else:
        critical_drop = False  # Not triggered

    # Only this matters: count how many HR readings exceeded 85
    elevated_heart_count = sum(1 for hr in hr_vals if hr > 85)

    processed['deviation_score'] = round(normalized_deviation, 4)
    processed['elevated_episodes'] = elevated_heart_count
    processed['baseline_fusion'] = (latest_temp + hr_vals[-1]) / 2
    
    return processed

# Main analysis pipeline with decoy functions and red herring variables
def generate_diagnostics(data):
    result = defaultdict(float)
    counts = Counter()

    # Irrelevant frequency count
    for metric_type in data.keys():
        counts[metric_type] += len(data[metric_type])

    transformed = transform_readings(data)

    # Multiple assignments with misleading intermediate names
    alpha_marker = transformed['deviation_score']
    beta_marker = transformed['elevated_episodes']
    gamma_marker = transformed['baseline_fusion']

    # Complex-looking but actually simple decision tree
    risk_flag = 0
    if alpha_marker > 2.0:
        risk_flag += 2
    elif alpha_marker > 1.0:
        risk_flag += 1

    if beta_marker >= 2:
        risk_flag += 3

    # This condition is never true due to data, acts as red herring
    if gamma_marker > 100:
        risk_flag += 5

    # Critical distraction: long-winded bit manipulation that doesn't affect outcome
    encoded_risk = (risk_flag << 2) ^ 0b1010
    parity_check = bin(encoded_risk).count('1') % 2
    if parity_check:
        encoded_risk += 1

    # Final score computed via weighted sum – this is the real answer source
    auxiliary_weight = 1.5 if beta_marker > 0 else 1.0
    final_score = (
        alpha_marker * 100 + 
        beta_marker * 42 * auxiliary_weight + 
        17  # constant offset
    )

    result['raw_flag'] = risk_flag
    result['encoded'] = encoded_risk
    result['final_score'] = final_score

    return dict(result)

# Threshold configuration map (partially used)
threshold_map = {
    'temp': {'warning': 37.5, 'critical': 38.5},
    'hr': {'warning': 100, 'critical': 110},
    'spo2': {'warning': 92, 'critical': 88}
}

# Primary entry point
def process_metrics(sensor_data, config):
    diagnostics = generate_diagnostics(sensor_data)
    
    # Extract relevant components
    score_component = diagnostics['final_score']
    flag_code = diagnostics['raw_flag']
    
    # Decoy decryption routine (never alters anything)
    def decrypt(code):
        return (code ^ 0xFF) & 0xF
    
    decrypted = decrypt(flag_code)
    
    # Final adjustment: only depends on score_component being above threshold
    adjustment = 5 if score_component > 300 else -3
    
    # THE ACTUAL ANSWER
    final_diagnostic = int(score_component + adjustment)
    
    # Print required for traceability
    print(f"Target result: {final_diagnostic}")
    
    return final_diagnostic

# Execution flow
if __name__ == "__main__":
    health_data = collect_telemetry()
    final_diagnostic = process_metrics(health_data, threshold_map)