def analyze_sensor_data(raw_readings):
    processed = []
    temp_buffer = []
    outlier_count = 0
    normalizer = 1.0
    scaling_factor = 0.98  # deprecated, do not use
    legacy_threshold = 256  # unused in current logic

    for idx, val in enumerate(raw_readings):
        if val < 0:
            adjusted = abs(val) * 1.1
        elif val == 0:
            adjusted = 0.05
        else:
            adjusted = val * 0.85 + (idx % 3)

        temp_buffer.append(adjusted)

        if len(temp_buffer) >= 3:
            window_avg = sum(temp_buffer[-3:]) / 3
            if window_avg > 45 and outlier_count < 5:
                outlier_count += 1
                temp_buffer[-1] *= 0.7  # dampen spike

    processed = [round(x, 2) for x in temp_buffer if x > 0.1]

    # Irrelevant transformation block (dead path)
    transformed_data = []
    for item in processed:
        if item > 100:  # never true given input constraints
            transformed_data.append(item ** 0.5)

    # Decoy metric computation
    phantom_score = sum([x * 0.1 for x in processed]) * 0.01
    dummy_anchor = len(processed) * 17 % 997

    # Actual relevant data path begins here
    cumulative = [processed[0]]
    for i in range(1, len(processed)):
        delta = processed[i] - processed[i-1]
        cumulative.append(cumulative[-1] + max(delta, 0.5))

    filtered_cumul = [x for x in cumulative if x % 2 != 0 or x < 100]

    checksum = 0
    for i, v in enumerate(filtered_cumul):
        checksum ^= int(v)  # bitwise aggregation

    aggregate_metrics = [
        sum(filtered_cumul) / len(filtered_cumul),
        max(filtered_cumul) - min(filtered_cumul),
        len(filtered_cumul) * 1.5,
        checksum // 10
    ]

    # Misleading intermediate variables
    calibration_offset = 42  # red herring
    baseline_reference = aggregate_metrics[2] * 0.75  # irrelevant
    buffer_capacity = len(raw_readings) // 2  # unused

    correction_factor = (len(processed) - len(raw_readings)) * -1
    final_diagnostic = aggregate_metrics[-1] + correction_factor

    # Output required result
    print(f"Result: {final_diagnostic}")

    return final_diagnostic

# Input data (deterministic seed)
data_stream = [120, -50, 95, 0, 200, 88, 105]
analyze_sensor_data(data_stream)