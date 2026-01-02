def analyze_sensor_array(raw_readings, baseline):
    temp_log = []
    alert_flags = []
    cumulative_shift = 0
    for idx, reading in enumerate(raw_readings):
        adjusted = reading - baseline
        if adjusted > 50:
            alert_flags.append((idx, 'HIGH'))
        elif adjusted < -50:
            alert_flags.append((idx, 'LOW'))
        temp_log.append(adjusted ** 2)
        cumulative_shift += abs(adjusted) // 7

    # Irrelevant transformation: dead code path
    inverted_map = {i: val for i, val in enumerate(reversed(temp_log))}
    outlier_candidates = [v for v in temp_log if v > 1000]

    # Actual signal filtering
    filtered_indices = [i for i, r in enumerate(raw_readings) if 10 <= r <= 85]
    filtered_data = [raw_readings[i] for i in filtered_indices]

    # Decoy statistical analysis (not used later)
    mean_temp = sum(temp_log) / len(temp_log) if temp_log else 0
    variance_proxy = sum((x - mean_temp) ** 2 for x in temp_log) / len(temp_log) if temp_log else 0

    # Red herring: complex but unused bit manipulation
    bit_analysis = 0
    for val in raw_readings:
        bit_analysis ^= (val << 2) & 0xFF
        bit_analysis |= (val >> 1) & 0x0F

    # Real processing begins: use of zip and slicing
    paired_offsets = list(zip(filtered_data[:-1], filtered_data[1:]))
    differential_gaps = [b - a for a, b in paired_offsets if a != 0]

    # Misleading intermediate calculation
    stability_score = len([dg for dg in differential_gaps if -5 <= dg <= 5])
    decay_pattern = [filtered_data[i] * 0.95**i for i in range(len(filtered_data))]

    # Critical calibration factor derived from safe index access
    fallback_bases = [3, 7, 11]
    calibration_index = (len(filtered_data) + cumulative_shift) % 3
    calibration_factor = fallback_bases[calibration_index] + 0.1 * (sum(differential_gaps) % 10)

    def process_readings(data, factor):
        if not data:
            return -999
        # Core logic with slicing and arithmetic chain
        segment_a = data[:len(data)//2]
        segment_b = data[len(data)//2:]
        
        # Use of enumerate in meaningful computation
        weighted_sum = 0
        for i, val in enumerate(segment_b):
            weighted_sum += val * (0.8 ** i)
        
        # Composite transformation
        transformed = [abs(x - factor) * 1.1 for x in segment_a]
        base_metric = sum(transformed) / len(transformed) if transformed else 0
        secondary_metric = weighted_sum / len(segment_b)
        
        # Final non-linear combination
        return int((base_metric + secondary_metric * 2) ** 1.5) // 3

    # Unused recursive red herring
    def predict_decay(values, depth):
        if depth == 0 or len(values) < 2:
            return values[-1] if values else 0
        new_vals = [(values[i] + values[i+1]) / 2 for i in range(len(values)-1)]
        return predict_decay(new_vals, depth - 1)

    # Dead assignment: misleading diagnostic
    legacy_diagnostic = predict_decay(raw_readings, 5) * 2.5

    # Key execution point
    final_diagnostic = process_readings(filtered_data, calibration_factor)
    
    # Output requirement
    print(f"Result: {final_diagnostic}")

# Input setup
sensor_input = [12, 67, 88, 45, 34, 76, 90, 23, 56, 61, 18]
baseline_offset = 40

# Execute
analyze_sensor_array(sensor_input, baseline_offset)