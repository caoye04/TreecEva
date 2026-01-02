from collections import defaultdict, Counter
import math

# Simulated patient health monitoring system with diagnostic logic
def analyze_vital_signs(readings):
    stats = defaultdict(float)
    anomalies = []
    temp_sum = 0.0
    heart_rate_count = 0

    for r in readings:
        category = r['type']
        value = r['value']
        stats[category] += value

        if category == 'temperature' and (value < 36.0 or value > 38.0):
            anomalies.append('TEMP_OUT')
        elif category == 'heart_rate' and (value < 50 or value > 100):
            anomalies.append('HR_OUT')

        if category == 'temperature':
            temp_sum += value

    avg_temp = temp_sum / len([r for r in readings if r['type'] == 'temperature'])
    stats['avg_temperature'] = avg_temp

    # Irrelevant transformation
    squared_map = {i: i**2 for i in range(len(anomalies) + 1)}

    return dict(stats), anomalies

def compute_rolling_average(data, window=3):
    # Dead function - never used in execution path
    rolling = []
    for i in range(len(data) - window + 1):
        rolling.append(sum(data[i:i+window]) / window)
    return rolling

def evaluate_stability(metrics):
    # Distractor logic - computes stability but not used in final result
    score = 0
    for k, v in metrics.items():
        if 'rate' in k:
            score += 1 if 60 <= v <= 80 else -1
        elif 'pressure' in k:
            score += 2 if 110 <= v <= 140 else -2
    return max(-10, min(10, score))

def filter_noisy_data(logs):
    # Unused preprocessing function
    clean_logs = []
    for log in logs:
        if 'error' not in log.get('status', '').lower():
            clean_logs.append(log)
    return clean_logs

def generate_summary_report(patients):
    # Complex but irrelevant aggregation
    summary = Counter()
    for p in patients:
        summary['total'] += 1
        if p.get('risk_level') == 'high':
            summary['high_risk'] += 1
    return dict(summary)

def process_metrics(data, config):
    # Core processing function with critical logic
    base_score = 0
    adjustment = 0

    # Real data processing
    for entry in data:
        typ = entry['type']
        val = entry['value']

        if typ == 'oxygen_saturation':
            if val >= 95:
                base_score += 10
            elif val >= 90:
                base_score += 5
            else:
                base_score -= 15

        elif typ == 'respiratory_rate':
            if 12 <= val <= 20:
                base_score += 7
            else:
                base_score -= 10

        elif typ == 'systolic_pressure':
            if 120 <= val <= 130:
                base_score += 8
            elif 110 <= val < 120:
                adjustment += 2
            elif 130 < val <= 140:
                adjustment += 1
            else:
                base_score -= 12

    # Decoy calculation chain
    temp_result = math.sin(math.pi / 4) * base_score
    temp_result = abs(temp_result) * config.get('weight', 1)

    # Critical branching logic
    threshold_met = base_score >= config.get('critical_threshold', 20)

    if threshold_met:
        multiplier = config.get('multiplier', 1.5)
    else:
        multiplier = config.get('recovery_factor', 0.5)

    intermediate = (base_score + adjustment) * multiplier

    # Final transformation using dictionary operations
    lookup = {i: i * 1.1 for i in range(-50, 51)}
    index = int(intermediate)

    if index in lookup:
        final_value = lookup[index]
    else:
        final_value = intermediate * 1.05

    # Red herring: complex bit manipulation with no impact
    decoy_flag = 0b1010 ^ 0b1100 & 0b1111
    decoy_flag = (decoy_flag << 2) | 0b10

    # Another irrelevant list comprehension
    [x**3 for x in range(5) if x % 2 == 0]

    return round(final_value, 4)

# Main execution block
if __name__ == '__main__':
    # Simulated health sensor readings
    health_data = [
        {'type': 'temperature', 'value': 36.8},
        {'type': 'heart_rate', 'value': 72},
        {'type': 'oxygen_saturation', 'value': 92},
        {'type': 'respiratory_rate', 'value': 18},
        {'type': 'systolic_pressure', 'value': 135},
        {'type': 'oxygen_saturation', 'value': 96},
        {'type': 'respiratory_rate', 'value': 22},
        {'type': 'systolic_pressure', 'value': 118}
    ]

    # Configuration with misleading keys
    thresholds = {
        'critical_threshold': 25,
        'weight': 1.2,
        'multiplier': 1.8,
        'recovery_factor': 0.4,
        'debug_mode': False,
        'version': '2.1a',
        'timeout': 3000
    }

    # Unused data structures
    historical_trends = defaultdict(list)
    event_counter = Counter(['boot', 'calibrate', 'update'])

    # Key analysis steps
    vital_stats, detected_issues = analyze_vital_signs(health_data)

    # Irrelevant filtering operation
    filtered_issues = [issue for issue in detected_issues if 'HR' not in issue]

    # Diagnostic scoring (only this affects final outcome)
    final_diagnostic = process_metrics(health_data, thresholds)

    # Print result as required
    print(f"Target result: {final_diagnostic}")
