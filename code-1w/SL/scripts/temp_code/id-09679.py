from collections import defaultdict, Counter

# Simulate sensor data with some noise and repeated readings
def fetch_sensor_data():
    raw_readings = [
        (1, 23.1), (2, 45.0), (1, 23.3), (3, 67.8), (2, 44.9),
        (1, 22.9), (4, 12.5), (3, 68.0), (2, 45.1), (1, 23.2)
    ]
    return raw_readings

# Process data: group by sensor ID and compute average, ignore outliers
def process_sensor_data(raw_data):
    grouped = defaultdict(list)
    outlier_count = 0

    for sid, value in raw_data:
        if 10 < value < 70:  # valid range
            grouped[sid].append(value)
        else:
            outlier_count += 1  # distractor: counted but not used later

    averages = {}
    for sid in grouped:
        avg = sum(grouped[sid]) / len(grouped[sid])
        averages[sid] = round(avg, 2)
    
    return averages

# Analyze consistency across sensors using simple variance proxy
def analyze_consistency(data_averages):
    values = list(data_averages.values())
    mean = sum(values) / len(values)
    variance_proxy = sum((v - mean) ** 2 for v in values) / len(values)
    consistency_flag = variance_proxy < 200  # always true here, distractor logic
    return variance_proxy  # not used in final score

# Calculate final diagnostic score based on weighted contributions
def calculate_final_score(averages):
    weights = {1: 0.4, 2: 0.35, 3: 0.25}  # sensor importance weights
    score = 0.0
    temp_buffer = []  # red herring: collected but unused

    for sid, avg in averages.items():
        if sid in weights:
            contribution = avg * weights[sid]
            score += contribution
            temp_buffer.append(contribution)  # written but never used

    # Additional adjustment based on presence of sensor 4 (not present)
    if 4 in averages:
        score *= 0.9  # dead code path
    else:
        penalty_adjustment = -5  # calculated but not applied

    # Final non-linear transformation
    final_score = int((score ** 1.05) + 10)
    return final_score

# Misleading auxiliary function that appears important
def generate_diagnostic_report(data):
    count_stats = Counter([sid for sid, _ in data])
    report = {
        'total_entries': sum(count_stats.values()),
        'unique_sensors': len(count_stats),
        'max_occurrence': max(count_stats.values())
    }
    return report  # computed but irrelevant to main task

# Main execution flow
if __name__ == '__main__':
    data = fetch_sensor_data()
    processed_data = process_sensor_data(data)
    
    # Distraction: multiple side computations
    consistency_metric = analyze_consistency(processed_data)
    diagnostic = generate_diagnostic_report(data)
    
    # Key statement
    final_score = calculate_final_score(processed_data)
    
    # Output result as required
    print(f"Result: {final_score}")