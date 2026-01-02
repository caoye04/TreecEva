def analyze_temperature(readings):
    temp_stats = {}
    high_temp_alerts = 0
    total = sum(readings)
    average = total / len(readings) if readings else 0
    
    for reading in readings:
        if reading > 38:
            high_temp_alerts += 1
        if reading in temp_stats:
            temp_stats[reading] += 1
        else:
            temp_stats[reading] = 1
    
    # Irrelevant aggregation
    squared_sum = sum([x ** 2 for x in readings])
    normalization_factor = squared_sum ** 0.5 if squared_sum else 1
    normalized_readings = [x / normalization_factor for x in readings]
    
    return average, high_temp_alerts, normalized_readings


def transform_labels(raw_labels):
    mapping = {"low": 1, "medium": 2, "high": 3}
    numeric_labels = []
    for label in raw_labels:
        if label.lower() in mapping:
            numeric_labels.append(mapping[label.lower()])
        else:
            numeric_labels.append(0)
    
    # Dead code path - never used
    reverse_map = {v: k for k, v in mapping.items()}
    sorted_keys = sorted(reverse_map.keys())
    
    return numeric_labels


def filter_outliers(data, threshold=1.5):
    if not data:
        return []
    q1 = sorted(data)[len(data)//4]
    q3 = sorted(data)[3*len(data)//4]
    iqr = q3 - q1
    lower_bound = q1 - threshold * iqr
    upper_bound = q3 + threshold * iqr
    
    filtered = [x for x in data if lower_bound <= x <= upper_bound]
    
    # Unused intermediate calculation
    outlier_count = len(data) - len(filtered)
    penalty_score = outlier_count * 0.5
    
    return filtered


def calculate_efficiency(metrics):
    base_efficiency = 0
    adjustment_factor = 1.0
    
    for val in metrics:
        if val > 25:
            base_efficiency += val * 0.8
        elif val > 15:
            base_efficiency += val * 1.1
        else:
            base_efficiency += val * 1.3
    
    # Conditional expression used
    adjustment_factor = 0.95 if len(metrics) > 8 else (0.90 if len(metrics) > 5 else 0.85)
    
    final_efficiency = base_efficiency * adjustment_factor
    
    # Extra computation that doesn't affect result
    max_val = max(metrics) if metrics else 0
    stability_ratio = max_val / (sum(metrics) / len(metrics)) if metrics else 0
    
    return int(final_efficiency)

# Main execution flow
sensor_readings = [35, 37, 39, 40, 36, 38, 34, 33, 37, 36, 35, 38]
avg_temp, alerts, norm_readings = analyze_temperature(sensor_readings)

status_labels = ["medium", "high", "high", "high", "medium", "high", \
                "low", "low", "medium", "medium", "medium", "high"]
numeric_codes = transform_labels(status_labels)

processed_data = filter_outliers(norm_readings + [x * 0.1 for x in numeric_codes], threshold=1.2)

# Key statement
efficiency_score = calculate_efficiency(processed_data)

print(f"Result: {efficiency_score}")