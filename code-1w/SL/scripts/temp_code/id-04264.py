import math

# Simulated health monitoring system with diagnostic logic
def analyze_heart_rate(hr):
    return 'elevated' if hr > 100 else 'normal'

def analyze_bp(systolic, diastolic):
    if systolic < 90 or diastolic < 60:
        return 'low'
    elif systolic > 140 or diastolic > 90:
        return 'high'
    return 'normal'

def compute_stress_index(hr, temp, resp):
    return (hr * 0.4) + (temp * 5) + (resp * 3)

def evaluate_hydration(level):
    levels = {'low': 1, 'normal': 2, 'high': 3}
    return levels.get(level, 0)

def calculate_recovery_score(age, stress, hydration):
    base = 100 - age * 0.5
    penalty = stress * 0.3
    bonus = hydration * 2.5
    return max(0, round(base - penalty + bonus))

def generate_report(data):
    report_lines = []
    for k, v in data.items():
        report_lines.append(f'{k}: {v}')
    return '\n'.join(report_lines)

def normalize_readings(readings):
    mean = sum(readings) / len(readings)
    normalized = [(x - mean) / mean for x in readings]
    return [round(x, 2) for x in normalized]

def detect_anomaly_pattern(values):
    # Irrelevant anomaly detection (dead-end function)
    count = 0
    for i in range(1, len(values)):
        if abs(values[i] - values[i-1]) > 15:
            count += 1
    return count > 3

def legacy_calculate_risk_factor(age, hr, bp_sys):
    # Outdated risk model (distractor)
    risk = (age * 0.8) + (hr * 0.2)
    if bp_sys > 160:
        risk *= 1.3
    return min(risk, 100)

def deprecated_process_vitals(vitals):
    # Unused complex transformation (red herring)
    transformed = {}
    for k, v in vitals.items():
        if isinstance(v, (int, float)):
            transformed[k] = (v ** 0.5) * 7
        else:
            transformed[k] = len(v) * 2
    return transformed

def auxiliary_score_calculator(metrics):
    # Misleading scoring function with no impact
    weights = {'stress': 0.3, 'sleep': 0.2, 'activity': 0.25, 'diet': 0.25}
    total = 0.0
    for k, v in metrics.items():
        total += v * weights.get(k, 0)
    return round(total, 2)

def get_vital_trend(history):
    # Complex trend analysis that isn't used
    if len(history) < 3:
        return 'insufficient'
    diffs = [history[i+1] - history[i] for i in range(len(history)-1)]
    avg_change = sum(diffs) / len(diffs)
    return 'increasing' if avg_change > 0.5 else 'decreasing' if avg_change < -0.5 else 'stable'

def process_metrics(data, config):
    # Core processing with distractors and multiple steps
    
    # Step 1: Extract primary vitals
    hr = data['heart_rate']
    bp_sys = data['bp'][0]
    bp_dia = data['bp'][1]
    temp = data['temperature']
    resp = data['respiratory_rate']
    age = data['age']
    hydration = data['hydration_status']
    sleep_hours = data['sleep_hours']
    
    # Step 2: Compute derived metrics (some irrelevant)
    stress_index = compute_stress_index(hr, temp, resp)
    heart_analysis = analyze_heart_rate(hr)
    bp_analysis = analyze_bp(bp_sys, bp_dia)
    hydration_score = evaluate_hydration(hydration)
    
    # Step 3: Create intermediate structures (distractor)
    vital_stats = {
        'mean_hr': hr * 1.05,
        'max_temp_threshold': temp + 0.8,
        'breathing_efficiency': resp / (hr / 10),
        'thermal_load': temp * hr / 100
    }
    
    # Step 4: Normalize historical data (unused but plausible)
    hr_history = [78, 82, 85, hr, 88]
    normalized_history = normalize_readings(hr_history)
    
    # Step 5: Apply conditional logic with lambda (required feature)
    categorize = lambda x, t: 'above' if x > t else 'below'
    stress_label = categorize(stress_index, config['stress_threshold'])
    sleep_quality = 'good' if sleep_hours >= 7 else 'poor'
    
    # Step 6: Build diagnostic dictionary (red herring structure)
    preliminary_diag = {
        'cardiac_risk': 'moderate' if heart_analysis == 'elevated' else 'low',
        'bp_category': bp_analysis,
        'thermal_state': 'fever' if temp > 37.5 else 'normal',
        'respiratory_flag': 'warning' if resp > 20 else 'clear',
        'stress_level': stress_label
    }
    
    # Step 7: Calculate recovery score (actually used)
    recovery_score = calculate_recovery_score(age, stress_index, hydration_score)
    
    # Step 8: Apply config-based adjustments (key step)
    adjustment_factor = 1.0
    if bp_analysis == 'high' and stress_index > 85:
        adjustment_factor = 0.85
    elif heart_analysis == 'elevated' and sleep_quality == 'poor':
        adjustment_factor = 0.9
    
    adjusted_recovery = math.floor(recovery_score * adjustment_factor)
    
    # Step 9: Final decision logic with conditional expression (required feature)
    final_diagnostic = adjusted_recovery if adjusted_recovery > 50 else (40 if age < 40 else 30)
    
    # Step 10: Irrelevant reporting operations
    report_data = generate_report(preliminary_diag)
    legacy_risk = legacy_calculate_risk_factor(age, hr, bp_sys)
    
    # Step 11: Dead-end dictionary operation (distractor)
    summary_stats = {}
    summary_stats.update(vital_stats)
    summary_stats['anomaly_count'] = len([x for x in normalized_history if abs(x) > 0.5])
    summary_stats['stability'] = get_vital_trend(hr_history)
    
    # Step 12: Return final result (only this matters)
    return final_diagnostic

# Main execution
if __name__ == '__main__':
    # Input data
    health_data = {
        'heart_rate': 98,
        'bp': (142, 88),
        'temperature': 36.9,
        'respiratory_rate': 18,
        'age': 45,
        'hydration_status': 'normal',
        'sleep_hours': 6.5
    }
    
    # Threshold configuration
    thresholds = {
        'stress_threshold': 85,
        'min_sleep': 7,
        'max_hr_warning': 100
    }
    
    # Execute main logic
    final_diagnostic = process_metrics(health_data, thresholds)
    
    # Output result
    print(f"Result: {final_diagnostic}")