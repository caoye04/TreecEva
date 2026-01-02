from itertools import combinations

def analyze_pattern(sequence):
    count = 0
    temp_sum = 0
    distractor_buffer = [0] * len(sequence)

    # Irrelevant smoothing pass
    for i in range(len(sequence)):
        distractor_buffer[i] = sequence[i] + (i % 3)

    # Real logic: count increasing adjacent pairs
    for i in range(len(sequence) - 1):
        if sequence[i] < sequence[i + 1]:
            count += 1
            temp_sum += sequence[i]

    return count, temp_sum

def compute_aggregate(data, threshold):
    total_weight = 0.0
    adjustment_factor = 1.5
    dummy_pairs = list(combinations(data, 2))
    spike_count = 0

    # Misleading normalization attempt
    normalized_data = [x / max(data) * 100 for x in data]
    for val in normalized_data:
        if val > 90:
            spike_count += 1

    # Actual aggregation logic
    base_indices = []
    for idx, value in enumerate(data):
        if value > threshold:
            base_indices.append(idx)

    index_pairs = list(zip(base_indices[:-1], base_indices[1:]))
    for a, b in index_pairs:
        total_weight += (b - a) * adjustment_factor

    # Secondary contribution based on sum of high values
    high_values_sum = sum(v for v in data if v > threshold)
    total_weight += high_values_sum * 0.1

    # Dead code branch (never reached due to structure)
    if len(data) > 1000:
        fallback = 0
        for x in data:
            fallback += x ** 0.5
        total_weight = fallback

    return int(total_weight)

# Main execution
sensor_readings = [12, 7, 15, 23, 19, 31, 34, 27, 45, 41, 50]

count_analysis, partial_sum = analyze_pattern(sensor_readings)

# Key distraction: unused transformation chain
shifted_readings = [x - 5 for x in sensor_readings]
squared_shifts = [x**2 for x in shifted_readings if x > 10]

# Core computation with moderate interference
final_score = compute_aggregate(sensor_readings, threshold=20)

print(f"Result: {final_score}")