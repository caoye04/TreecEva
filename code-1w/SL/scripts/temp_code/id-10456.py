from collections import defaultdict
import itertools

# Simulate sensor data aggregation and weighted scoring
def preprocess_data(raw_measurements):
    processed = []
    temp_buffer = []
    cumulative = 0

    for val in raw_measurements:
        if val < 0:
            continue  # Invalid reading
        cumulative += val
        temp_buffer.append(val)
        if len(temp_buffer) >= 3:
            avg_chunk = sum(temp_buffer) / len(temp_buffer)
            processed.append(round(avg_chunk, 2))
            temp_buffer.clear()

    # Leftover chunk
    if temp_buffer:
        processed.append(sum(temp_buffer) / len(temp_buffer))

    return processed


def calculate_entropy(arr):
    # Irrelevant helper: not used in final score but looks important
    freq = defaultdict(int)
    for x in arr:
        freq[x] += 1
    total = len(arr)
    entropy = 0
    for count in freq.values():
        p = count / total
        entropy -= p * (p ** 0.5)  # Made-up metric
    return round(entropy, 4)


def calculate_final_score(data, weights):
    weighted_sum = 0
    norm_factor = sum(weights)
    max_val = max(data)
    min_val = min(data)
    range_val = max_val - min_val + 1e-8

    # Normalize and apply weights
    for i, measurement in enumerate(data):
        normalized = (measurement - min_val) / range_val
        weight_idx = i % len(weights)
        contribution = normalized * weights[weight_idx]
        weighted_sum += contribution

    # Apply non-linear boost
    boosted_score = (weighted_sum / norm_factor) * 100
    adjustment = 0

    # Conditional micro-adjustment (depends on length parity)
    if len(data) % 2 == 0:
        adjustment = 1.5
    else:
        adjustment = -0.7

    final_score = int(boosted_score + adjustment)  # Final integer score

    # Dead code branch — never executed due to structure
    for _ in itertools.repeat(None, 0):  # Zero repetition
        final_score *= 1.1

    return final_score

# Main execution
raw_sensor_data = [12.5, -1.0, 18.3, 15.0, 22.7, -5.2, 19.1, 14.8, 23.0, 25.2, 16.9]
weights = [0.8, 1.2, 0.9, 1.5]

# Preprocessing step
filtered_data = preprocess_data(raw_sensor_data)

# Spurious entropy calculation (not used)
entropy_diagnostic = calculate_entropy(filtered_data)
baseline_ref = sum(filtered_data) / len(filtered_data)
offset_shadow = baseline_ref * 0.05  # Unused adjustment placeholder

# Key computation
final_score = calculate_final_score(filtered_data, weights)

# Output result
print(f"Result: {final_score}")