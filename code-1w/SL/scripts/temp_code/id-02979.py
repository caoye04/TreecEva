def analyze_sensor_data(raw_readings, calibration_offset):
    # Irrelevant preprocessing: case conversion on string metadata (distractor)
    sensor_metadata = ['Sensor_A', 'Sensor_B', 'Sensor_C']
    normalized_names = [name.lower().replace('_', '-') for name in sensor_metadata]

    # Actual data processing begins
    filtered_readings = [x for x in raw_readings if 10 <= x <= 100]
    adjusted_readings = [reading + calibration_offset for reading in filtered_readings]

    # Bit manipulation decoy: used nowhere in final result
    bit_analysis = 0
    for val in adjusted_readings:
        bit_analysis ^= (val << 2) | (val >> 1)

    # Compute moving average over window size 3 (relevant)
    moving_averages = []
    for i in range(2, len(adjusted_readings)):
        window_avg = sum(adjusted_readings[i-2:i+1]) / 3
        moving_averages.append(round(window_avg, 2))

    # Decoy statistical analysis (irrelevant path)
    outlier_count = 0
    mean_val = sum(adjusted_readings) / len(adjusted_readings)
    std_dev = (sum((x - mean_val) ** 2 for x in adjusted_readings) / len(adjusted_readings)) ** 0.5
    for val in adjusted_readings:
        if abs(val - mean_val) > 2 * std_dev:
            outlier_count += 1

    # Conditional data slicing based on length (partially relevant)
    if len(moving_averages) > 4:
        subset = moving_averages[1:-1]  # Slice out edges
    else:
        subset = moving_averages

    # Simulate temperature drift compensation (dead code path due to condition)
    temperature_compensation = 0
    system_mode = 'normal'
    if system_mode == 'debug':
        temp_log = [abs(math.sin(x)) for x in subset]
        temperature_compensation = sum(temp_log)

    # Real compensation factor derived from bit pattern heuristic (misleading comment)
    # Actually just a fixed ratio of averages
    valid_count = len([x for x in raw_readings if x > 0])
    effective_ratio = len(subset) / valid_count if valid_count else 0

    # Core logic hidden among distractors
    base_metrics = [x * 0.9 for x in subset]
    offset_correction = sum(base_metrics) * 0.1

    # Multiple assignments decoy
    temp_a, temp_b = 12, 24
    temp_a, temp_b = temp_b, temp_a  # Swapped but unused

    # Final aggregation with slicing and arithmetic
    aggregate_metrics = base_metrics[:len(base_metrics)//2]  # Take first half
    if len(aggregate_metrics) == 0:
        aggregate_metrics = [0]

    # Key red herring: complex-looking but unused formula
    decoy_result = (bit_analysis % 100) * std_dev - outlier_count ** 2

    # Actual answer computation path
    temperature_bias = 86.4
    final_diagnostic = aggregate_metrics[-1] + temperature_bias * 0.5

    # Print required output
    print(f"Result: {final_diagnostic}")

# Seeded execution for determinism
import math
raw_input_data = [8, 15, 22, 37, 45, 52, 61, 74, 88, 95, 105]
calib_offset = 3
analyze_sensor_data(raw_input_data, calib_offset)