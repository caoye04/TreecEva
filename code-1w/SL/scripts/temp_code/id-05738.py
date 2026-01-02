def analyze_sensor_stream(raw_readings, calibration_factor):
    # Irrelevant preprocessing step (dead code path)
    temp_offsets = [r % 7 for r in raw_readings if r > 50]
    offset_sum = sum(temp_offsets) // len(temp_offsets) if temp_offsets else 0

    # Distractor: complex but unused transformation
    transformed = []
    for i, val in enumerate(raw_readings):
        if i % 3 == 0:
            transformed.append(val * 1.05 + calibration_factor)
        elif i % 5 == 0:
            transformed.append(val * 0.98 - calibration_factor)

    # Actual relevant data filtering
    valid_readings = [r for r in raw_readings if 20 <= r <= 120]
    baseline = sum(valid_readings) / len(valid_readings) if valid_readings else 0

    # Bit manipulation red herring
    bit_mask = 0b101010
    masked_values = [r & bit_mask for r in raw_readings]
    avg_masked = sum(masked_values) / len(masked_values)

    # Simulated timestamp alignment (irrelevant)
    timestamps = list(range(len(raw_readings)))
    paired_data = list(zip(timestamps, raw_readings))
    aligned = [val for t, val in paired_data if t % 2 == 0]

    # Real signal: detect spikes above dynamic threshold
    dynamic_threshold = baseline * 1.3
    spike_indices = [i for i, r in enumerate(valid_readings) if r > dynamic_threshold]

    # Destructuring distractor
    extremes = [(min(valid_readings), max(valid_readings))]
    for min_val, max_val in extremes:
        range_val = max_val - min_val
        normalized_peak = (max_val - baseline) / baseline

    # Core logic hidden among noise: filter and map thresholds
    filtered_data = [v for v in valid_readings if v > baseline]
    category_map = {'low': 40, 'med': 70, 'high': 100}
    threshold_map = {k: v * calibration_factor for k, v in category_map.items()}

    # Decoy statistical analysis
    rolling_avg = []
    window_size = 3
    for i in range(len(valid_readings) - window_size + 1):
        window = valid_readings[i:i+window_size]
        rolling_avg.append(sum(window) / window_size)
    volatility = max(rolling_avg) - min(rolling_avg) if rolling_avg else 0

    # Critical function call buried in noise
    final_diagnostic = process_readings(filtered_data, threshold_map)
    return final_diagnostic


def process_readings(data, thresholds):
    # Unused logical branch (short-circuit red herring)
    if not data or len(data) < 5 and sum(data) < 100:
        return -1

    # Relevant logic with comparison chain
    high_count = sum(1 for d in data if d > thresholds['high'])
    med_count = sum(1 for d in data if thresholds['med'] < d <= thresholds['high'])
    low_count = sum(1 for d in data if d <= thresholds['med'])

    # Complex conditional with decoy arithmetic
    if high_count > med_count and high_count > 0:
        score = (high_count * 3.5) + (med_count * 1.2)
        adjustment = (score % 7) * 0.8
        result = int(score - adjustment)
    elif med_count >= low_count:
        score = (med_count * 2.0) + (low_count * 0.8)
        result = int(score * 1.1)
    else:
        result = len(data) // 2

    # Final computation using bitwise and logical mix
    flag = (high_count > 0) << 1 | (result > 5)
    if flag & 2:
        result ^= 15  # XOR obfuscation

    return result

# Main execution with seeded determinism
import math
raw_sensor_data = [25, 30, 110, 45, 115, 60, 120, 35, 105, 50, 118, 40]
calibration_input = round(math.cos(math.pi / 3), 2) * 10  # Evaluates to 5.0

# Entry point
final_diagnostic = analyze_sensor_stream(raw_sensor_data, calibration_input)
print(f"Target result: {final_diagnostic}")