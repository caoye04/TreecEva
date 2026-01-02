from collections import defaultdict
from itertools import combinations

# Simulate sensor data aggregation and weighted anomaly detection
def collect_diagnostics(raw_readings):
    readings = [x for x in raw_readings if x > 0]
    stats = defaultdict(int)
    anomalies = []

    for val in readings:
        if val > 80:
            anomalies.append(val)
        stats['total'] += val
        stats['count'] += 1
        if val % 5 == 0:
            stats['divisible_by_5'] += 1

    avg = stats['total'] / stats['count'] if stats['count'] else 0
    stats['average'] = round(avg, 2)

    # Distractor: generate unused pattern pairs
    unused_pairs = list(combinations(readings[:5], 2))
    temp_sum = 0
    for p in unused_pairs:
        temp_sum += p[0] * p[1]  # Not used later

    return stats, anomalies

def calculate_threshold(base, factor=1.2):
    # Extra logic that mimics calibration but isn't critical
    adjusted = base * factor
    if adjusted < 50:
        adjusted = 50
    return int(adjusted)

def process_metrics(sensor_data, importance_weights):
    metrics, issues = collect_diagnostics(sensor_data)
    
    # Real computation path
    score = 0
    weight_sum = sum(importance_weights.values())
    
    # Meaningful contributions
    if metrics['divisible_by_5'] > 2:
        score += 15
    
    if metrics['average'] > 45:
        score += 25
    
    # Irrelevant intermediate calculation (distractor)
    phantom_score = 0
    for i in range(len(issues)):
        phantom_score += issues[i] // (i + 1) if i < 3 else 0  # Unused
    
    # More distractors: simulate alternate scoring
    alt_scores = []
    for w in importance_weights:
        temp_val = len(w) * metrics['total'] // 100
        alt_scores.append(temp_val)
    
    # Actual use of weights
    for key, weight in importance_weights.items():
        if key in ['critical', 'vital']:
            score += weight * 2

    # Final adjustment based on issue count
    penalty = len(issues) * 3
    score -= penalty

    # Key assignment point
    final_score = score + 10  # Final transformation

    # Dead code branch (never executed, but looks relevant)
    if False:
        backup = metrics['total'] - sum(alt_scores)
        final_score = max(final_score, backup)

    return final_score

# Main execution
sensor_inputs = [65, 0, 85, 90, 40, 70, 55, -5, 95]
weights = {'critical': 7, 'optional': 3, 'vital': 5, 'aux': 1}
data = [x for x in sensor_inputs if x != 0]

interim = calculate_threshold(42)
diag_stats, detected_anomalies = collect_diagnostics(data)
temp_factor = diag_stats['average'] // 10

final_score = process_metrics(data, weights)
print(f"Result: {final_score}")