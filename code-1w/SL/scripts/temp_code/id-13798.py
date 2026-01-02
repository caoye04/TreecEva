import math

# Simulated health monitoring system with diagnostic logic
def analyze_heart_rate(hr):
    if hr < 40 or hr > 180:
        return 'critical'
    elif hr < 60:
        return 'low'
    elif hr > 100:
        return 'high'
    return 'normal'

def compute_stress_index(vals):
    mean_val = sum(vals) / len(vals)
    variance = sum((x - mean_val) ** 2 for x in vals) / len(vals)
    return int(math.sqrt(variance))

def evaluate_risk(age, stress_level, bp):
    risk = 0
    if age > 50:
        risk += 3
    if stress_level > 7:
        risk += 4
    if bp > 140:
        risk += 2
    return 'high' if risk >= 7 else 'moderate' if risk >= 4 else 'low'

# Irrelevant helper: environmental noise filter (unused in final path)
def apply_noise_filter(signal):
    return [int(x * 0.95) for x in signal]

# Distractor function: sleep quality estimator (never called)
def estimate_sleep_quality(rem_cycles, interruptions):
    base_score = rem_cycles * 20
    penalty = interruptions * 15
    return max(0, base_score - penalty)

# Misleading data structure
vital_trends = {
    'hr': [72, 75, 70, 80, 85],
    'spo2': [98, 97, 96, 98, 97],
    'temp': [36.6, 36.8, 37.0, 36.9, 37.1]
}

# Fake calibration constants (unused)
CALIBRATION_OFFSET = 0.37
REFERENCE_VOLTAGE = 3.3
NOISE_FLOOR_DB = -85

# Real processing begins here
raw_readings = [68, 72, 74, 69, 85, 88, 73, 71, 77, 89]
filtered_readings = [val for val in raw_readings if 60 <= val <= 100]  # Remove outliers

# Compute auxiliary metrics (some irrelevant)
avg_hr = sum(filtered_readings) / len(filtered_readings)
stress_values = [abs(filtered_readings[i] - filtered_readings[i-1]) for i in range(1, len(filtered_readings))]
stress_index = compute_stress_index(stress_values)

# Simulated blood pressure and age
patient_age = 54
blood_pressure_systolic = 145

# Conditional expression used as required
risk_category = 'elevated' if stress_index > 8 else ('caution' if stress_index > 5 else 'stable')

# Unused intermediate calculations (distractors)
temp_normalization_factor = math.log(sum(filtered_readings[:3]) + 1)
duplicate_check_set = set(filtered_readings)
reoccurrence_count = sum(1 for x in filtered_readings if x in [72, 73])

# Health data aggregation (key relevant structure)
health_data = {
    'readings': filtered_readings,
    'baseline': avg_hr,
    'stress_marker': stress_index,
    'age_risk': patient_age > 50,
    'bp_risk': blood_pressure_systolic > 140
}

# Threshold configuration (appears important but only some fields matter)
threshold = {
    'max_stress': 7,
    'allow_high_bp': False,
    'ignore_age': False,
    'calibration_needed': False
}

# Core decision logic hidden among noise
def process_metrics(data, config):
    hr_status = analyze_heart_rate(data['baseline'])
    stress_level = data['stress_marker']
    
    # Nested conditional logic with red herrings
    if data['bp_risk'] and not config['allow_high_bp']:
        if data['age_risk']:
            primary_risk = evaluate_risk(data['age_risk'], stress_level, 150)
        else:
            primary_risk = 'moderate'
        stress_adjustment = 2 if stress_level > config['max_stress'] else 0
        adjusted_risk_score = stress_level + stress_adjustment
        
        # Complex branching with decoy operations
        temp_flag = False
        for reading in data['readings']:
            if reading > 85:
                temp_flag = True
                break
        
        secondary_score = 0
        for i, val in enumerate(data['readings']):
            if i % 2 == 0 and val > 75:
                secondary_score += 1
        
        # Critical calculation buried in logic
        if primary_risk == 'high' or adjusted_risk_score > 9:
            diagnostic_code = 404  # Meaningless code
            fallback_value = sum(data['readings']) // len(data['readings'])
            # Actual answer generation
            result = fallback_value - adjusted_risk_score * 2
        else:
            result = 999
    else:
        result = -123
    
    # Final override based on obscure rule
    if hr_status == 'normal' and stress_level < 5:
        result = 1000  # Red herring: condition not met
    
    # One last distraction
    metadata_log = f"Final processed at {len(data['readings'])} points"
    debug_sum = sum([result % (i+1) for i in range(1, 5)])  # unused
    
    return int(result)

# Execution point of interest
final_diagnostic = process_metrics(health_data, threshold)
print(f"Target result: {final_diagnostic}")