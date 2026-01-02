from collections import defaultdict
from itertools import combinations

# Simulate sensor data from a structural monitoring system
def generate_readings():
    return [104, 98, 110, 95, 102, 115, 97, 108]

# Analyze raw readings for anomaly detection
def detect_anomalies(data):
    threshold = sum(data) / len(data) + 5
    anomalies = []
    for i, val in enumerate(data):
        if val > threshold:
            anomalies.append((i, val))
    return anomalies

# Compute risk severity based on anomaly patterns
def compute_severity(anomalies, base_risk=10):
    severity = base_risk
    temp_flag = False
    for idx, value in anomalies:
        if value > 110:
            severity += 8
            temp_flag = True
        elif value > 105:
            severity += 4
    adjustment_factor = 1.2 if temp_flag else 1.0
    severity *= adjustment_factor
    return int(severity)

# Track historical anomaly trends (distractor function - not used in final result)
def track_trends(anomalies):
    history = defaultdict(int)
    for idx, val in anomalies:
        history['high'] += 1 if val > 105 else 0
        history['moderate'] += 1
    return dict(history)

# Evaluate system stability using risk profile
def evaluate_stability(profile):
    score = profile['severity']
    constraints = profile['constraints']
    
    # Simulated constraint validation with nested logic
    fail_count = 0
    for c in constraints:
        broken = False
        for level in c['thresholds']:
            if level < 90 or level > 120:
                broken = True
        if broken and c['critical']:
            fail_count += 1
    
    # Introduce auxiliary calculation (semi-relevant)
    penalty = 0
    if fail_count >= 2:
        penalty = 25
    elif fail_count == 1:
        penalty = 10

    # Additional distraction: combinatorial analysis of non-critical constraints
    non_critical = [c for c in constraints if not c['critical']]
    combo_count = 0
    for combo in combinations(non_critical, 2):
        combo_count += 1  # Count all pairs (irrelevant to final result)
    
    # Final diagnostic computation
    final_diagnostic = score - penalty
    
    # Dead code path - never executed due to logic above
    if combo_count > 100:
        final_diagnostic += 5
        
    return final_diagnostic

# Main execution flow
sensor_data = generate_readings()
anomalies = detect_anomalies(sensor_data)
severity_level = compute_severity(anomalies)

# Build constraint structure (mixture of critical/non-critical)
constraints = [
    {'thresholds': [95, 103, 115], 'critical': True},
    {'thresholds': [85, 92], 'critical': True},  # Will trigger fail due to <90
    {'thresholds': [98, 107], 'critical': False},
    {'thresholds': [110, 118, 125], 'critical': False}  # 125 > 120 → broken but non-critical
]

risk_profile = {
    'severity': severity_level,
    'constraints': constraints,
    'timestamp': '2023-11-05',
    'location': 'Sector_7'
}

# Key statement
final_diagnostic = evaluate_stability(risk_profile)
print(f"Result: {final_diagnostic}")