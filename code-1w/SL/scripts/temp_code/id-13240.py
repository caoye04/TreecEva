def analyze_readings(sensor_data):
    adjusted_values = []
    outlier_count = 0
    temporal_gaps = []

    for i, reading in enumerate(sensor_data):
        if reading < -50 or reading > 50:
            outlier_count += 1
            continue
        
        adjusted_value = reading * 0.98 + 2.1
        adjusted_values.append(adjusted_value)
        
        if i > 0:
            gap = i - (i - 1)
            temporal_gaps.append(gap)

    avg_gap = sum(temporal_gaps) / len(temporal_gaps) if temporal_gaps else 0
    stats_summary = {
        'count': len(adjusted_values),
        'outliers': outlier_count,
        'smoothness': avg_gap
    }
    
    return adjusted_values, stats_summary


def filter_anomalies(data_list):
    clean_data = []
    anomaly_flags = []
    
    threshold = sum(data_list) / len(data_list) if data_list else 0
    
    for val in data_list:
        flag = 1 if abs(val - threshold) > 2 * threshold else 0
        anomaly_flags.append(flag)
        if not flag:
            clean_data.append(val)
    
    # Irrelevant aggregation
    cumulative = 0
    running_tally = []
    for x in clean_data:
        cumulative += x * 0.1
        running_tally.append(cumulative)
    
    return clean_data


def compute_final_score(cleaned):
    base = 100
    penalty = 0
    
    for i, value in enumerate(cleaned):
        if i % 3 == 0 and value > 0:
            penalty += 3
        elif i % 4 == 0 and value < 10:
            penalty += 1

    for j in range(len(cleaned)):
        if cleaned[j] > 15:
            base *= 1.05

    # Distractor loop: computes unused metric
    max_run = 0
    current_run = 0
    for val in cleaned:
        if val > 5:
            current_run += 1
            max_run = max(max_run, current_run)
        else:
            current_run = 0
    
    final_score = int(base - penalty)
    return final_score

# Main execution
raw_readings = [23, -65, 18, 41, 55, 12, -30, 9, 16, 44]
processed, info = analyze_readings(raw_readings)
denoised = filter_anomalies(processed)
final_score = compute_final_score(denoised)
print(f"Result: {final_score}")