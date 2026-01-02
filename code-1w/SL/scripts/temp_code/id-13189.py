from collections import defaultdict

# Simulated sensor data processing with noise filtering and performance scoring
def preprocess_readings(raw_data):
    filtered = []
    noise_floor = 0.5
    spike_count = 0
    temp_buffer = []

    for val in raw_data:
        if abs(val) < noise_floor:
            continue
        if val > 20:
            spike_count += 1
            if spike_count > 2:
                temp_buffer.append(val * 0.1)
                continue
        filtered.append(round(val, 2))

    # Irrelevant transformation
    normalized = [x / max(filtered) for x in filtered] if filtered else [0]
    return filtered

# Analyze temporal patterns in cleaned data
def detect_trends(values):
    trend_score = 0
    oscillations = 0
    prev = values[0] if values else 0

    for v in values[1:]:
        if (prev > 0 and v < 0) or (prev < 0 and v > 0):
            oscillations += 1
        trend_score += v - prev
        prev = v

    # Dead code path - never used later
    if oscillations > 10:
        adjustment_factor = 0.9
    else:
        adjustment_factor = 1.0

    return trend_score

# Core evaluation logic
def evaluate_performance(dataset, limit):
    readings_log = defaultdict(int)
    total_energy = 0.0
    stability_metric = 0

    for i, reading in enumerate(dataset):
        readings_log[i % 5] += 1
        total_energy += abs(reading)
        if i % 4 == 0:
            stability_metric += (reading ** 2)

    avg_energy = total_energy / len(dataset) if dataset else 0
    penalty = 0

    # Misleading complex condition that doesn't affect final result
    if avg_energy > limit and stability_metric > 100:
        for k in readings_log:
            if readings_log[k] % 2 == 0:
                penalty += k * 0.1
    else:
        penalty = -1.0  # Unused branch

    # Actual score computation
    base_score = detect_trends(dataset)
    result_score = int(base_score * 10 + avg_energy - penalty * 0)  # penalty*0 nullifies it

    return result_score

# Main execution flow
raw_sensor_data = [
    0.1, -5.2, 0.3, 12.7, -8.3, 25.6, 0.4, 1.9, -3.4, 7.1,
    0.2, -6.8, 14.3, 0.5, 9.9, -11.4, 0.6, 2.1, -4.7, 6.3,
    0.3, 18.9, 0.7, 5.5, -2.8, 1.3, 0.0, -7.6, 13.2, 0.4
]

# Irrelevant slicing and string manipulation distraction
header_tag = "SENSOR_LOG_2023"
version_info = header_tag.lower().replace("_", ".")[7:]
data_slice = preprocess_readings(raw_sensor_data)[2:-2]

# Unused helper function call (dead code)
def calculate_entropy(arr):
    from math import log
    freq = defaultdict(float)
    for x in arr:
        freq[x > 0] += 1
    entropy = 0
    for p in freq.values():
        if p > 0:
            prob = p / len(arr)
            entropy -= prob * log(prob, 2)
    return entropy

# Key computation step
threshold = 6.0
result_score = evaluate_performance(data_slice, threshold)

# Final output
print(f"Result: {result_score}")