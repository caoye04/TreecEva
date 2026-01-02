from collections import defaultdict

def analyze_performance(records):
    stats = defaultdict(lambda: {'count': 0, 'total': 0.0})
    anomalies = []
    temp_buffer = []

    for record in records:
        category = record['category']
        value = record['value']
        stats[category]['count'] += 1
        stats[category]['total'] += value

        if value < 0:
            anomalies.append((category, value))

    # Irrelevant aggregation
    total_entries = sum(stat['count'] for stat in stats.values())
    overall_sum = sum(stat['total'] for stat in stats.values())
    average_global = overall_sum / total_entries if total_entries else 0

    # Misleading intermediate calculation
    penalty_factor = 0
    for val in [x['value'] for x in records if x['value'] > 100]:
        penalty_factor += val * 0.01

    return stats, average_global, penalty_factor


def calculate_adjusted_average(values, limits):
    filtered = [v for v in values if limits[0] <= v <= limits[1]]
    adjustment = 0.0

    # Simulate historical drift (distractor logic)
    historical_bias = []
    for i, val in enumerate(filtered):
        if i % 3 == 0:
            historical_bias.append(val * 0.95)

    if len(historical_bias) > 2:
        adjustment = (sum(historical_bias) / len(historical_bias)) * 0.05

    raw_avg = sum(filtered) / len(filtered) if filtered else 0
    return raw_avg + adjustment

# Main execution
if __name__ == '__main__':
    student_data = [
        {'name': 'Alice', 'category': 'math', 'value': 85},
        {'name': 'Bob', 'category': 'math', 'value': 92},
        {'name': 'Charlie', 'category': 'science', 'value': 78},
        {'name': 'Diana', 'category': 'math', 'value': 96},
        {'name': 'Eve', 'category': 'science', 'value': 88},
        {'name': 'Frank', 'category': 'math', 'value': -5},  # Anomaly
        {'name': 'Grace', 'category': 'science', 'value': 91}
    ]

    # Extract grades using enumerate and zip
    names = [d['name'] for d in student_data]
    grades = [d['value'] for d in student_data]

    index_map = {i: name for i, name in enumerate(names)}
    paired_data = list(zip(enumerate(grades), names))

    # Unused but plausible structure
    processed = []
    for idx, grade in enumerate(grades):
        status = 'pass' if grade >= 70 else 'fail'
        processed.append({'index': idx, 'grade': grade, 'status': status})

    # Distractor: complex state tracking
    tracker = defaultdict(int)
    for entry in processed:
        tracker[entry['status']] += 1

    # Thresholds for valid grade range
    min_thresh, max_thresh = 0, 100
    thresholds = (min_thresh, max_thresh)

    # Core computation buried among distractions
    final_score = calculate_adjusted_average(grades, thresholds)

    # Additional red herring: unused transformation
    normalized = [max(0, min(100, g)) for g in grades]
    capped_avg = sum(normalized) / len(normalized)

    Result: {final_score}