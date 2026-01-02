def normalize_readings(readings):
    min_val, max_val = min(readings), max(readings)
    if max_val == min_val:
        return [0.5 for _ in readings]
    return [(x - min_val) / (max_val - min_val) for x in readings]


def detect_anomalies(data, limit=0.1):
    anomalies = []
    for i, x in enumerate(data):
        if abs(x - 0.5) > limit:
            anomalies.append(i)
    return set(anomalies)


def adjust_for_bias(values, correction_factor=1.1):
    corrected = []
    for v in values:
        adjusted = v * correction_factor
        if adjusted > 1.0:
            adjusted = 1.0
        corrected.append(adjusted)
    return corrected


def compute_aggregate(inputs, criteria):
    total = 0.0
    weights = [0.8, 1.2, 0.9, 1.1, 1.0]
    temp_results = []
    
    for i, (val, crit) in enumerate(zip(inputs, criteria)):
        if i % 2 == 0:
            contribution = val * weights[i % len(weights)]
        else:
            contribution = val * (weights[i % len(weights)] + 0.1)
        temp_results.append(contribution)
    
    filtered = [x for x in temp_results if x >= 0.7]
    
    secondary_sum = 0
    for j, item in enumerate(filtered):
        if j in detect_anomalies(filtered, limit=0.15):
            secondary_sum += item * 0.5
        else:
            secondary_sum += item
    
    scaling_factor = len(temp_results) / (len(filtered) or 1)
    return int(secondary_sum * scaling_factor)

# Main execution
raw_data = [23, 45, 67, 89, 12]
scaled_values = normalize_readings(raw_data)
bias_adjusted = adjust_for_bias(scaled_values, correction_factor=1.05)
dropped_indices = {2, 4}
cleaned = [v for i, v in enumerate(bias_adjusted) if i not in dropped_indices]

thresholds = [True, False, True, False, True]
# Extend cleaned list to match length using dummy logic
while len(cleaned) < len(thresholds):
    cleaned.append(cleaned[-1] * 0.9)

intermediate_sum = sum(cleaned[:3]) * 0.5
placeholder = intermediate_sum ** 2

final_score = compute_aggregate(cleaned, thresholds)
print(f"Result: {final_score}")