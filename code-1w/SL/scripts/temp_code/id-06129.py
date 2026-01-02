import math

def analyze_pattern(sequence):
    trend = []
    for i in range(1, len(sequence)):
        trend.append(sequence[i] - sequence[i-1])
    return trend

# Simulate sensor readings with noise filtering
data_stream_a = [3, 5, 9, 15, 23]
data_stream_b = [2, 4, 8, 14, 22]

# Irrelevant transformation (distractor)
transformed_noise = [x ** 2 for x in data_stream_a if x % 2 == 1]
noise_floor = sum(transformed_noise) / len(transformed_noise) if transformed_noise else 0

# Extract patterns from both streams
trend_a = analyze_pattern(data_stream_a)
trend_b = analyze_pattern(data_stream_b)

delta_comparison = [abs(a - b) for a, b in zip(trend_a, trend_b)]
consistency_metric = sum(delta_comparison)

# Simulated calibration offset (not used in final computation, distractor)
calibration_offset = math.sin(math.pi / 4) * 100
offset_buffer = [calibration_offset * i for i in range(3)]

# Combine trends using set logic to eliminate duplicates
unique_trends = list(set(trend_a + trend_b))
sorted_trends = sorted(unique_trends)

# Apply combinatorial weighting based on position and frequency
weights = [len(sorted_trends) - i for i in range(len(sorted_trends))]
frequency_map = {x: sorted_trends.count(x) for x in sorted_trends}
weighted_sum = sum(trend * weights[i] * frequency_map[trend] for i, trend in enumerate(sorted_trends))

# Normalize using logarithmic scale (base e)
normalization_factor = math.log(weighted_sum) if weighted_sum > 0 else 1
combined_data = int(weighted_sum / normalization_factor) if normalization_factor != 0 else 0

# Final scoring function
def calculate_final_score(score):
    base = score * 0.8
    bonus = 10 if score > 100 else 5
    penalty = 2 if consistency_metric > 0 else 0
    return int(base + bonus - penalty)

final_score = calculate_final_score(combined_data)
print(f"Target result: {final_score}")