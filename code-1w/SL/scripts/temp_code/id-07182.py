import math

def preprocess_readings(raw_readings):
    # Irrelevant preprocessing (dead code path)
    filtered = [x for x in raw_readings if x > 0]
    normalized = [math.log(x + 1) for x in filtered]
    return normalized

def compute_bmi(weight_kg, height_m):
    # Distractor function: not used in final calculation
    if height_m == 0:
        return 0
    return weight_kg / (height_m ** 2)

def detect_outliers(values, factor=1.5):
    # Unused outlier detection (red herring)
    q1 = sorted(values)[len(values)//4]
    q3 = sorted(values)[3*len(values)//4]
    iqr = q3 - q1
    lower_bound = q1 - factor * iqr
    upper_bound = q3 + factor * iqr
    return [v for v in values if v < lower_bound or v > upper_bound]

def aggregate_metrics(samples):
    # Complex but irrelevant aggregation
    stats = {}
    samples_set = set(samples)
    stats['unique_count'] = len(samples_set)
    stats['mode'] = max(set(samples), key=samples.count)
    stats['range'] = max(samples) - min(samples)
    return stats

def evaluate_stability(readings):
    # Decoy analysis with misleading intermediate result
    diffs = [abs(readings[i] - readings[i-1]) for i in range(1, len(readings))]
    avg_diff = sum(diffs) / len(diffs) if diffs else 0
    return avg_diff < 5

def analyze_symptoms(data, config):
    # Core logic hidden among distractions
    temperature = data.get('temp_c', 0)
    heart_rate = data.get('hr_bpm', 0)
    systolic = data.get('bp_systolic', 0)
    oxygen = data.get('o2_saturation', 100)
    
    # Distractor variables
    metabolic_index = 0
    neural_trend = []
    baseline_shift = False
    
    # Irrelevant nested condition (never reached)
    if temperature < 0:
        for _ in range(3):
            metabolic_index += 2
    
    # Real logic begins here — multi-step reasoning
    fever = temperature > config['fever_threshold']
    tachycardia = heart_rate > config['hr_threshold']
    hypertension = systolic > config['bp_threshold']
    hypoxemia = oxygen < config['o2_threshold']
    
    # Scoring with weighted conditions
    score = 0
    if fever:
        score += 3
    if tachycardia:
        score += 2
    if hypertension:
        score += 2
    if hypoxemia:
        score -= 1  # Counterintuitive penalty for comorbidity
    
    # Hidden adjustment via character count in symptom history
    history = data.get('symptom_log', '')
    uppercase_count = sum(1 for c in history if c.isupper())
    lowercase_count = sum(1 for c in history if c.islower())
    if uppercase_count > lowercase_count:
        score += 1
    
    # Final determination using set intersection logic (key step)
    critical_signs = {'fever', 'tachycardia', 'hypertension', 'hypoxemia'}
    observed = {k for k, v in {'fever': fever, 'tachycardia': tachycardia,
                              'hypertension': hypertension, 'hypoxemia': hypoxemia}.items() if v}
    overlap = critical_signs & observed
    
    # Primary answer derivation
    base_value = len(overlap) * 100
    adjustment = score * 5
    final_risk = base_value + adjustment
    
    # Diagnostic mapping (final assignment)
    if final_risk >= 400:
        level = 4
    elif final_risk >= 300:
        level = 3
    elif final_risk >= 200:
        level = 2
    elif final_risk >= 100:
        level = 1
    else:
        level = 0
    
    final_diagnostic = level * 173  # Key transformation
    return final_diagnostic

# Main execution
if __name__ == '__main__':
    # Patient data with embedded logic triggers
    patient_data = {
        'temp_c': 38.7,
        'hr_bpm': 112,
        'bp_systolic': 148,
        'o2_saturation': 92,
        'symptom_log': 'SEVERE HEADACHE and mild dizziness'
    }
    
    # Threshold configuration
    thresholds = {
        'fever_threshold': 38.0,
        'hr_threshold': 100,
        'bp_threshold': 140,
        'o2_threshold': 95
    }
    
    # Irrelevant initializations (distractors)
    raw_vitals = [36.5, 37.1, 38.7, 39.0, 38.2]
    preprocessed = preprocess_readings(raw_vitals)
    bmi = compute_bmi(78.5, 1.76)
    stability = evaluate_stability(raw_vitals)
    metrics = aggregate_metrics(raw_vitals)
    outliers = detect_outliers(raw_vitals)
    
    # Execution point of interest
    final_diagnostic = analyze_symptoms(patient_data, thresholds)
    
    # Output result
    print(f"Result: {final_diagnostic}")