from collections import defaultdict, Counter
from itertools import combinations

# Simulated sensor network data processing with decoy analysis paths
def analyze_sensor_network():
    raw_readings = [145, 278, 93, 201, 117, 305, 88, 192, 255, 167, 134, 209]
    calibration_factor = 0.92
    base_threshold = 150
    temporal_weights = [0.8, 1.0, 1.2, 0.9, 1.1, 1.3, 0.85, 0.95, 1.15, 0.75, 1.05, 1.25]

    # Irrelevant frequency analysis (decoy)
    frequency_map = defaultdict(int)
    for val in raw_readings:
        frequency_map[val // 10 * 10] += 1

    # Misleading transformation chain (dead path)
    transformed_readings = []
    for i, val in enumerate(raw_readings):
        adjusted = int((val * calibration_factor) + (i % 3))
        if adjusted > 200:
            transformed_readings.append(adjusted // 2)
        else:
            transformed_readings.append(adjusted)

    # Unused smoothing function (red herring)
    def smooth(data, window=3):
        smoothed = []
        for i in range(len(data)):
            start = max(0, i - window // 2)
            end = min(len(data), i + window // 2 + 1)
            smoothed.append(sum(data[start:end]) / (end - start))
        return smoothed

    # Distractor: false anomaly detection
    anomalies = []
    for i in range(1, len(raw_readings)):
        if abs(raw_readings[i] - raw_readings[i-1]) > 100:
            anomalies.append((i, raw_readings[i]))

    # Real processing begins here — non-obvious due to noise
    weighted_readings = []
    for i, val in enumerate(raw_readings):
        weighted_val = val * temporal_weights[i % len(temporal_weights)]
        weighted_readings.append(int(weighted_val))

    # Filter based on dynamic condition
    dynamic_offset = len([x for x in raw_readings if x > base_threshold]) * 2
    effective_threshold = base_threshold - dynamic_offset

    filtered_data = [v for v in weighted_readings if v > effective_threshold]

    # Decoy statistical analysis
    mean_val = sum(filtered_data) / len(filtered_data) if filtered_data else 0
    variance = sum((x - mean_val) ** 2 for x in filtered_data) / len(filtered_data) if filtered_data else 0

    # Irrelevant combinatorial check (distractor)
    significant_pairs = []
    for pair in combinations(filtered_data, 2):
        if abs(pair[0] - pair[1]) > 80:
            significant_pairs.append(pair)

    # Threshold map construction — actually used later
    category_bounds = {'low': (0, 120), 'medium': (121, 200), 'high': (201, 350)}
    threshold_map = {}
    for cat, (low, high) in category_bounds.items():
        count_in_range = len([v for v in filtered_data if low <= v <= high])
        threshold_map[cat] = count_in_range * (high - low + 1) // (base_threshold // 10)

    # Fake optimization loop (dead code)
    optimized = []
    for _ in range(3):
        temp = 0
        for j in range(5):
            temp += (j * j) % 7
        optimized.append(temp)

    # Core logic buried in abstraction
    def process_readings(data, thresholds):
        result = 0
        for val in data:
            if val < 100:
                result += thresholds['low']
            elif val < 200:
                result += thresholds['medium']
            else:
                result += thresholds['high']
        # Additional transformation based on bit properties
        binary_ones = bin(result).count('1')
        trailing_zeros = 0
        temp_result = result
        while temp_result & 1 == 0 and temp_result != 0:
            temp_result >>= 1
            trailing_zeros += 1
        return result + binary_ones - (trailing_zeros * 2)

    # Critical execution point
    final_diagnostic = process_readings(filtered_data, threshold_map)

    # Output required format
    print(f"Result: {final_diagnostic}")

    # Unused checksum verification (distractor)
    checksum = sum(filtered_data[i] * (i+1) for i in range(len(filtered_data))) % 1024
    expected = 512
    status = "VERIFIED" if checksum == expected else "FAILED"

    return final_diagnostic

# Execute
analyze_sensor_network()