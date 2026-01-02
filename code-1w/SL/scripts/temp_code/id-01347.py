from collections import defaultdict
from itertools import combinations

# Simulate sensor data with noise and redundancy
def generate_sensor_readings():
    base_values = [24, 25, 23, 26, 24, 25, 22]
    readings = defaultdict(list)
    for i, val in enumerate(base_values):
        readings['sensor_a'].append(val + (i % 3))
        readings['sensor_b'].append(val - (i % 2))
        readings['auxiliary'].append((val * 2) % 7)  # Irrelevant data
    return readings

# Process and filter valid measurements
def process_readings(raw):
    cleaned = []
    temp_offsets = []
    total_aux = 0

    for i in range(len(raw['sensor_a'])):
        a_val = raw['sensor_a'][i]
        b_val = raw['sensor_b'][i]
        offset = abs(a_val - b_val)
        temp_offsets.append(offset)

        if offset <= 2:
            cleaned.append((a_val + b_val) // 2)

        # Distractor: accumulate auxiliary but not used later
        total_aux += raw['auxiliary'][i]

    # Compute moving average to smooth
    smoothed = []
    for i in range(1, len(cleaned) - 1):
        avg_val = round((cleaned[i-1] + cleaned[i] + cleaned[i+1]) / 3)
        smoothed.append(avg_val)

    # Extra distraction: generate unused pairs
    unused_pairs = list(combinations(smoothed, 2))
    pair_xor_sum = 0
    for x, y in unused_pairs:
        pair_xor_sum ^= (x ^ y)  # Computation with no impact

    return smoothed

# Calculate final diagnostic score
def calculate_final_score(data):
    peak = max(data)
    trough = min(data)
    spread = peak - trough
    adjustment_factor = 0.8

    # Some intermediate irrelevant calculations
    squared_deltas = [d ** 2 for d in data if d % 2 == 0]
    avg_square = sum(squared_deltas) / len(squared_deltas) if squared_deltas else 0

    # Core logic
    raw_sum = sum(data)
    count = len(data)
    mean_val = raw_sum / count if count else 0

    # Apply adjustment based on spread
    if spread > 3:
        adjustment_factor *= 0.9
    elif spread < 2:
        adjustment_factor *= 1.1

    score = (mean_val * adjustment_factor) + (spread * 1.5)
    return int(score)

# Main execution flow
raw_data = generate_sensor_readings()
processed_data = process_readings(raw_data)
final_score = calculate_final_score(processed_data)
print(f"Result: {final_score}")