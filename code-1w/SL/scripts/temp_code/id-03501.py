from collections import defaultdict, Counter
import math

# Simulated health monitoring system with noise and redundant calculations
def analyze_heart_rate(hr):
    if hr < 50:
        return 'bradycardia'
    elif hr > 100:
        return 'tachycardia'
    else:
        return 'normal'

def compute_oxidative_stress(level, exposure):
    # Irrelevant calculation - red herring
    stress_index = (level * 1.7) + (exposure ** 0.5)
    adjusted = stress_index * 0.87
    category = 'low' if adjusted < 40 else 'high'
    return adjusted  # Not used in final logic

def calculate_resilience_score(data):
    # Complex but unused resilience metric
    base = sum([x**0.5 for x in data if x > 20])
    penalty = len([x for x in data if x < 10])
    score = base - (penalty * 2.5)
    return round(score, 2)

def extract_vital_trends(vitals):
    trends = defaultdict(int)
    for key, readings in vitals.items():
        avg = sum(readings) / len(readings)
        trends[key] += avg
    return trends

def filter_anomalies(dataset, limit=50):
    # Dead code path - never actually removes anything
    cleaned = []
    for item in dataset:
        if isinstance(item, dict) and 'value' in item:
            if item['value'] > limit:
                cleaned.append(item)
    return cleaned  # Unused in main flow

def evaluate_metabolic_state(ph, glucose, ketones):
    if ph < 7.35:
        acidosis = True
    else:
        acidosis = False
    
    risk_level = 0
    if glucose > 140:
        risk_level += 2
    if ketones > 0.5:
        risk_level += 3
    if acidosis:
        risk_level += 4
    
    classification = 'critical' if risk_level >= 7 else 'moderate' if risk_level >= 4 else 'stable'
    return classification, risk_level

def process_metrics(data, config):
    # Core logic hidden among distractions
    heart_rates = data['heart_rate_readings']
    avg_hr = sum(heart_rates) / len(heart_rates)
    hr_status = analyze_heart_rate(avg_hr)
    
    # Blood oxygen processing
    spo2_values = data['oxygen_levels']
    median_spo2 = sorted(spo2_values)[len(spo2_values) // 2]
    hypoxia_threshold = config['spo2_critical']
    is_hypoxic = median_spo2 < hypoxemia_threshold  # Note: typo-style name to mislead
    
    # Typo correction through context
    hypoxemia_threshold = config.get('spo2_critical', 92)  # Re-defined after misuse
    is_hypoxic = median_spo2 < hypoxemia_threshold
    
    # Temperature evaluation
    temp_series = data['temperature_readings']
    high_fever = len([t for t in temp_series if t >= 39.0])
    normal_count = len([t for t in temp_series if 36.5 <= t <= 37.5])
    
    fever_severity = 0
    if high_fever > 2:
        fever_severity = 3
    elif high_fever > 0:
        fever_severity = 1
    
    # Neurological indicators (distractor block)
    eeg_patterns = data.get('eeg_data', [])
    spike_count = 0
    for pattern in eeg_patterns:
        freq = pattern.get('frequency', 0)
        if freq > 12:
            spike_count += 1
    seizure_risk = spike_count > 5  # Not used later
    
    # Immune response markers - relevant part
    crp_levels = data['inflammatory_markers']['CRP']
    esr_level = data['inflammatory_markers']['ESR']
    
    inflammation_score = (crp_levels[-1] * 0.7) + (esr_level * 0.3)
    
    acute_phase_response = False
    if crp_levels[-1] > 10 or esr_level > 20:
        acute_phase_response = True
    
    # Final diagnostic integration
    diagnostic_weight = 0
    if hr_status != 'normal':
        diagnostic_weight += 2
    if is_hypoxic:
        diagnostic_weight += 3
    if fever_severity > 0:
        diagnostic_weight += fever_severity
    if acute_phase_response:
        diagnostic_weight += 2
    
    # Hidden rule: override if CRP trend is decreasing
    if len(crp_levels) >= 3:
        recent_trend = (crp_levels[-1] - crp_levels[-3]) / 2
        if recent_trend < -1.0:  # Improving trend
            diagnostic_weight = max(0, diagnostic_weight - 2)
    
    final_diagnostic = 100 - (diagnostic_weight * 8)  # Base health score
    
    # Decoy assignment - looks important but unused
    prognosis_index = calculate_resilience_score(heart_rates)
    
    return final_diagnostic

# Main execution
if __name__ == '__main__':
    # Input data structure
    health_data = {
        'heart_rate_readings': [72, 76, 68, 84, 88, 92, 78],
        'oxygen_levels': [97, 96, 98, 95, 94, 93, 96, 97],
        'temperature_readings': [36.8, 37.1, 37.0, 39.2, 39.5, 38.9, 39.1],
        'inflammatory_markers': {
            'CRP': [18.2, 16.5, 12.1, 9.8],
            'ESR': 24
        },
        'eeg_data': [
            {'frequency': 8, 'amplitude': 4},
            {'frequency': 10, 'amplitude': 5},
            {'frequency': 14, 'amplitude': 6},
            {'frequency': 16, 'amplitude': 7}
        ]
    }

    thresholds = {
        'hr_normal': (60, 100),
        'spo2_critical': 92,
        'fever_threshold': 38.0
    }

    # Trigger decoy functions to increase interference
    baseline_trends = extract_vital_trends({'hr': health_data['heart_rate_readings']})
    dummy_filter = filter_anomalies([{'value': 30}, {'value': 60}], limit=40)
    oxidative_stress = compute_oxidative_stress(35, 12)
    
    # Critical statement
    final_diagnostic = process_metrics(health_data, thresholds)
    
    # Output result
    print(f"Result: {final_diagnostic}")