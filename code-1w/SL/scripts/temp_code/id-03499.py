import math

# Simulated health monitoring system with diagnostic logic
def analyze_biomarker(value, ref_min, ref_max, severity_factor):
    if value < ref_min:
        return (ref_min - value) * severity_factor
    elif value > ref_max:
        return (value - ref_max) * severity_factor
    return 0.0

def calculate_trend_score(readings):
    if len(readings) < 2:
        return 0
    trend = sum(readings[i+1] - readings[i] for i in range(len(readings)-1))
    return trend / (len(readings) - 1) if readings else 0

def normalize_signal(amplitude, frequency):
    # Irrelevant function - signal processing red herring
    return (amplitude * math.sin(frequency)) / (frequency + 1e-9)

def legacy_calculate_risk(age, gender_marker):
    # Outdated risk model - dead code path
    base = 0.5 if gender_marker == 1 else 0.3
    return base + age * 0.02

def evaluate_stress_index(heart_rate_variability, sleep_hours, caffeine_intake):
    # Distractor computation with misleading intermediate
    stress_raw = heart_rate_variability * 0.3 + (8 - sleep_hours) * 1.2 + caffeine_intake * 0.1
    return max(0, 10 - stress_raw)

def filter_outliers(data, threshold=3):
    mean_val = sum(data) / len(data)
    std_dev = math.sqrt(sum((x - mean_val)**2 for x in data) / len(data))
    return [x for x in data if abs(x - mean_val) <= threshold * std_dev]

def compute_entropy(values):
    # Complex but irrelevant metric
    total = sum(values)
    if total == 0:
        return 0
    probs = [v / total for v in values]
    return -sum(p * math.log(p) for p in probs if p > 0)

def process_metrics(data, config):
    # Core diagnostic logic
    biomarkers = data['biomarkers']
    vitals = data['vitals']
    
    # Real metrics used in final calculation
    liver_score = analyze_biomarker(biomarkers['ALT'], 7, 56, 1.8)
    kidney_score = analyze_biomarker(biomarkers['creatinine'], 0.7, 1.3, 2.5)
    
    cholesterol_trend = calculate_trend_score(vitals['cholesterol_history'])
    blood_pressure_trend = calculate_trend_score(vitals['bp_history'])
    
    # Conditional expression - required python feature
    metabolic_risk = liver_score + kidney_score if cholesterol_trend > 0 else liver_score * 0.7
    
    # Primary logic chain
    base_risk = metabolic_risk + abs(cholesterol_trend) * 2.1 + abs(blood_pressure_trend) * 1.4
    
    # Filtering step that looks important but isn't used in final answer
    filtered_chol = filter_outliers(vitals['cholesterol_history'])
    entropy_measure = compute_entropy(filtered_chol)  # Red herring
    
    # Additional distractor variables
    signal_norm = normalize_signal(2.3, 1.7)
    stress_eval = evaluate_stress_index(vitals['hrv'], 6.5, 3)
    legacy_risk = legacy_calculate_risk(52, 1)
    
    # Final computation using only specific components
    adjustment_factor = config['weighting']['metabolic']
    final_diagnostic = round(base_risk * adjustment_factor + 17.3, 4)
    
    # Unused complex structure - decoy
    report_summary = {
        'patient_id': 'DXX-9021',
        'anomalies': [],
        'priority_level': 'medium',
        'recommendations': []
    }
    
    return final_diagnostic

# Main execution
if __name__ == '__main__':
    # Input data
    health_data = {
        'biomarkers': {
            'ALT': 68,
            'creatinine': 1.42,
            'glucose': 96
        },
        'vitals': {
            'cholesterol_history': [190, 192, 198, 205, 210],
            'bp_history': [120, 124, 126, 130, 132],
            'hrv': 45
        }
    }
    
    thresholds = {
        'weighting': {
            'metabolic': 1.35
        },
        'alert_levels': {
            'critical': 9.0
        }
    }
    
    # Extraneous pre-processing (distraction)
    avg_chol = sum(health_data['vitals']['cholesterol_history']) / len(health_data['vitals']['cholesterol_history'])
    peak_bp = max(health_data['vitals']['bp_history'])
    
    # Key execution point
    final_diagnostic = process_metrics(health_data, thresholds)
    
    # Output result as required
    print(f"Target result: {final_diagnostic}")