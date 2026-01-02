def normalize_values(data):
    min_val, max_val = min(data), max(data)
    if max_val == min_val:
        return [0.5 for _ in data]
    return [(x - min_val) / (max_val - min_val) for x in data]


def filter_outliers(values):
    mean = sum(values) / len(values)
    variance = sum((x - mean) ** 2 for x in values) / len(values)
    std_dev = variance ** 0.5
    threshold = 2 * std_dev
    return [v for v in values if abs(v - mean) <= threshold]


def compute_final_score(raw_data):
    # Irrelevant transformation: reverse and slice
    reversed_slice = raw_data[::-1][1:]
    temp_offset = sum(reversed_slice[:3]) if len(reversed_slice) >= 3 else 0
    
    cleaned_data = filter_outliers(raw_data)
    normalized = normalize_values(cleaned_data)
    
    # Distractor: unused weighting
    weights = [0.1, 0.2, 0.3, 0.4][:len(normalized)]
    weighted_sum = sum(n * w for n, w in zip(normalized, weights))
    
    # Key logic: average + bonus if over threshold
    base_score = sum(normalized) / len(normalized)
    bonus = 10 if all(x > 0.15 for x in normalized) else 0
    
    # Extra distraction: simulate calibration drift
    drift_correction = 0
    for i in range(len(normalized)):
        if i % 3 == 0:
            drift_correction += 0.01 * i
    
    final = int((base_score * 100) + bonus - drift_correction)
    return final

# Simulated sensor readings with one outlier
sensor_readings = [120, 135, 110, 90, 145, 130, 105, 1000, 115, 125]

# Preprocessing step with slicing
trimmed_data = sensor_readings[1:8] + sensor_readings[-2:]
processed_data = [x // 5 * 2 for x in trimmed_data]  # Scale down resolution

# Misleading intermediate calculation
aggregate_peak = max(processed_data) * len(processed_data)

# Critical execution point
final_score = compute_final_score(processed_data)
print(f"Result: {final_score}")