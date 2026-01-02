from collections import defaultdict

# Simulate sensor data with noise and valid readings
def preprocess_sensor_data(raw_data):
    cleaned = []
    noise_count = 0
    for val in raw_data:
        if abs(val) > 100:  # Assume outliers beyond ±100 are noise
            noise_count += 1
            continue
        cleaned.append(val)
    return cleaned, noise_count

# Analyze frequency of readings
def analyze_frequency(data):
    freq = defaultdict(int)
    for d in data:
        freq[round(d)] += 1
    return freq

# Main scoring logic
def calculate_final_score(data, weights):
    total = 0.0
    base_score = 0
    adjustment_factor = 1.0

    # Irrelevant intermediate calculation (distractor)
    temp_buffer = [x * 0.1 for x in data if x > 0]
    buffer_sum = sum(temp_buffer)

    # Real processing steps
    for i, val in enumerate(data):
        if i % 2 == 0:
            base_score += val * weights[i % len(weights)]
        else:
            base_score -= val * 0.5

    # Frequency-based bonus
    freq = analyze_frequency(data)
    mode_estimate = max(freq, key=freq.get)
    if mode_estimate > 0:
        adjustment_factor += 0.2

    # Dummy loop with no effect (dead code path - distractor)
    running_avg = 0
    for _ in range(3):
        temp = [x + running_avg for x in data]
        running_avg = sum(temp) / len(temp)

    # Final composition
    total += base_score * adjustment_factor

    # Additional irrelevant transformation
    scaled_vals = [x ** 0.5 for x in data if x > 0]
    if len(scaled_vals) > 5:
        total -= sum(scaled_vals[:2])

    return int(total)

# Driver code
if __name__ == "__main__":
    raw_sensor_readings = [12.5, -8.3, 45.0, 45.0, 7.2, 45.0, 91.8, 33.1, 45.0, 10.9, 1020, -500]
    weights = [0.8, 1.2, 0.5]

    # Preprocess data
    valid_readings, dropped = preprocess_sensor_data(raw_sensor_readings)

    # Track metadata (unused later - distractor)
    stats_summary = {}
    for idx, (i, v) in enumerate(enumerate(valid_readings)):
        stats_summary[idx] = f"Index{i[0]}: {i[1]}"

    # Core computation
    final_score = calculate_final_score(valid_readings, weights)

    print(f"Result: {final_score}")