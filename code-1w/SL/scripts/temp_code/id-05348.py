def analyze_sensor_array(raw_readings, calibration_factor):
    # Irrelevant preprocessing block (dead path)
    temp_offsets = [0.1 * i for i in range(len(raw_readings))]
    adjusted_offsets = [x * 1.5 for x in temp_offsets if x > 0.3]

    # Distractor: complex but unused transformation
    encoded_stream = ''
    for val in raw_readings:
        encoded_stream += hex(int(val) ^ 255)[-2:]

    # Real processing begins: filter valid readings
    valid_indices = []
    filtered_data = []
    for i, val in enumerate(raw_readings):
        if val > 50 and val < 950:
            valid_indices.append(i)
            filtered_data.append(val + calibration_factor)

    # Misleading statistical decoy
    mean_val = sum(filtered_data) / len(filtered_data) if filtered_data else 0
    variance_proxy = sum((x - mean_val) ** 2 for x in filtered_data) / len(filtered_data) if filtered_data else 0

    # Unused recursive red herring
    def recursive_transform(n):
        if n <= 1:
            return 1
        return n * recursive_transform(n - 2)

    # Another distraction: dictionary-based mapping not fully used
    status_flags = {i: 'OK' if v > 100 else 'LOW' for i, v in enumerate(filtered_data)}
    flag_count = {'OK': 0, 'LOW': 0}
    for flag in status_flags.values():
        flag_count[flag] += 1

    # Actual threshold logic embedded in noise
    threshold_map = {}
    for idx, reading in enumerate(filtered_data):
        base_threshold = 75 + (idx % 4) * 10
        dynamic_adj = (reading * 0.02) if idx % 3 == 0 else 0
        threshold_map[idx] = base_threshold + dynamic_adj

    # Critical function buried in complexity
    def process_readings(data, thresholds):
        result = 0
        for i, val in enumerate(data):
            if i in thresholds:
                if val >= thresholds[i]:
                    result += int(val // (i + 1))  # Avoid division by zero
                else:
                    result -= i * 2
        return abs(result)  # Ensure positive output

    # Decoy list comprehension with zip and enumerate (partially irrelevant)
    paired_diagnostics = [
        f"{i}:{a:.0f}-{b:.0f}" 
        for i, (a, b) in enumerate(zip(filtered_data, adjusted_offsets + [0]*len(filtered_data)))
        if i % 4 == 0
    ]

    # Unused bitwise analysis
    bit_analysis = 0
    for val in filtered_data:
        bit_analysis ^= int(val) & 255
        bit_analysis = (bit_analysis << 1) | (bit_analysis >> 7)

    # Key execution point
    final_diagnostic = process_readings(filtered_data, threshold_map)

    # Print required output
    print(f"Result: {final_diagnostic}")
    return final_diagnostic

# Simulate input data
import math
simulated_readings = [
    int(100 * math.sin(i) + 500) for i in range(1, 18)
] + [888, 45, 902]

# Execute main function
analyze_sensor_array(simulated_readings, calibration_factor=12)