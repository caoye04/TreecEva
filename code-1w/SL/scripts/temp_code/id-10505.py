from collections import defaultdict, Counter
import math

# Simulated sensor data with multiple metrics
data = [
    {'id': 'A1', 'temp': 36.8, 'hr': 72, 'spo2': 98, 'activity': 'walking'},
    {'id': 'B2', 'temp': 37.5, 'hr': 88, 'spo2': 96, 'activity': 'running'},
    {'id': 'C3', 'temp': 38.1, 'hr': 95, 'spo2': 94, 'activity': 'running'},
    {'id': 'D4', 'temp': 36.9, 'hr': 70, 'spo2': 99, 'activity': 'resting'},
    {'id': 'E5', 'temp': 37.2, 'hr': 78, 'spo2': 97, 'activity': 'walking'}
]

# Thresholds for health risk assessment
thresholds = {
    'fever': 37.4,
    'tachycardia': 90,
    'hypoxia': 95
}

# Irrelevant baseline constants (distractors)
BASELINE_METRICS = {
    'normal_temp_range': (36.1, 37.2),
    'avg_hr_rest': 75,
    'spo2_critical': 90
}

NORMALIZATION_FACTOR = 1.07
SCALING_OFFSET = 0.89

# Decoy function - never called
def analyze_trend(history):
    cumulative = 0
    for record in history:
        cumulative += record.get('temp', 0) * 1.5
    return cumulative / len(history) if history else 0

# Unused utility
def calculate_bmi(weight, height):
    return weight / (height ** 2)

# Auxiliary transformation (partially relevant)
def normalize_value(val, min_val, max_val):
    return (val - min_val) / (max_val - min_val) if max_val != min_val else 0

# Core processing with red herrings
def evaluate_risk_level(entry):
    risk_points = 0
    warnings = []
    
    # Primary checks
    if entry['temp'] > thresholds['fever']:
        risk_points += 2
        warnings.append('fever')
    
    if entry['hr'] > thresholds['tachycardia']:
        risk_points += 3
        warnings.append('tachycardia')
    
    if entry['spo2'] < thresholds['hypoxia']:
        risk_points += 4
        warnings.append('hypoxia')
    
    # Distractor logic: activity-based adjustment (not used in final score)
    if entry['activity'] == 'running':
        adjusted_hr = entry['hr'] * 0.92  # simulated correction
        if adjusted_hr < thresholds['tachycardia']:
            risk_points -= 1  # misleading reduction
    
    # Another decoy calculation
    temp_z_score = (entry['temp'] - 36.8) / 0.6
    if abs(temp_z_score) > 2.0:
        warnings.append('extreme_temp_deviation')
    
    return risk_points, warnings

def process_results(data, config):
    # Aggregation structures
    risk_map = defaultdict(int)
    all_warnings = []
    id_scores = {}
    
    # Intermediate tracking (some irrelevant)
    activity_breakdown = Counter([item['activity'] for item in data])
    total_entries = len(data)
    
    # Hidden normalization reference (distractor)
    max_hr_recorded = max(item['hr'] for item in data)
    hr_normalization = normalize_value(max_hr_recorded, 60, 100)
    
    # Main evaluation loop
    for item in data:
        base_risk, alerts = evaluate_risk_level(item)
        
        # Apply fake context adjustment
        if item['id'].startswith('A'):
            temporal_factor = math.sin(0.1 * total_entries)
            base_risk += int(abs(temporal_factor * 2))
        
        # Real contribution to final score
        risk_map[item['activity']] += base_risk
        all_warnings.extend(alerts)
        id_scores[item['id']] = base_risk * NORMALIZATION_FACTOR  # scaled but not used directly
    
    # Critical computation path
    raw_aggregate = sum(risk_map.values())
    
    # Distractor: unused complex structure
    detailed_report = {
        'summary': {
            'total_risk_units': raw_aggregate,
            'incident_count': len(all_warnings),
            'distribution': dict(risk_map)
        },
        'metadata': {
            'source': 'sensor_fusion_v2',
            'calibration': SCALING_OFFSET
        }
    }
    
    # Final transformation - only this matters
    adjustment = 0
    if 'hypoxia' in all_warnings:
        adjustment -= 2
    if risk_map['running'] >= 5:
        adjustment += 1
    
    # Key statement
    final_score = raw_aggregate * 10 + adjustment
    
    # Dead code branch (never executes due to data)
    if len([x for x in data if x['temp'] > 40]) > 0:
        emergency_override = True
        final_score = 999  # decoy override
    
    return final_score

# Execution point of interest
final_score = process_results(data, thresholds)
print(f"Result: {final_score}")