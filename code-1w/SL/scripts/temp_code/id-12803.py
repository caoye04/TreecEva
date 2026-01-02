def analyze_sensor_data(raw_readings, calibration_offset=0.73):
    # Irrelevant pre-processing: normalize readings (not actually used in final path)
    normalized = [round((x - min(raw_readings)) / (max(raw_readings) - min(raw_readings)) * 100, 2) for x in raw_readings]
    
    # Distractor: complex-looking but unused transformation
    transformed = []
    for i, val in enumerate(raw_readings):
        if i % 2 == 0:
            transformed.append(val ** 0.5 * (i + 1))
        else:
            transformed.append(val / (i + 1) ** 0.3)

    # Dead code path: function defined but not called
    def deprecated_filter(data):
        return [d for d in data if d > sum(data) / len(data)]

    # Unused intermediate: statistical decoy
    mean_val = sum(raw_readings) / len(raw_readings)
    variance_proxy = sum((x - mean_val) ** 2 for x in raw_readings) / len(raw_readings)
    entropy_approx = -sum((x / sum(raw_readings)) * __import__('math').log2(x / sum(raw_readings)) for x in raw_readings if x > 0)

    # Real logic begins: extract positions and values where reading > threshold
    high_signal_indices = [i for i, x in enumerate(raw_readings) if x > 40]
    indexed_signals = list(zip(high_signal_indices, [raw_readings[i] for i in high_signal_indices]))
    
    # Accumulate weighted score based on position and magnitude
    base_accumulator = 0
    for pos, val in indexed_signals:
        if val % 2 == 0:
            base_accumulator += pos * 1.5
        else:
            base_accumulator += val // 3

    # Secondary distractor: string-based red herring
    status_log = "System nominal" if len(raw_readings) > 5 else "Review needed"
    diagnostic_codes = {"A1": "OK", "B2": "CHECK", "C3": "HOLD"}
    active_flags = [k for k, v in diagnostic_codes.items() if v == "CHECK"]

    # Conditional expression with meaningful outcome
    adjustment = calibration_offset if len(high_signal_indices) > 2 else 0.0
    
    # Key computation chain
    temp_offset = 0
    for i in range(len(raw_readings)):
        if i in high_signal_indices and raw_readings[i] % 5 == 0:
            temp_offset += 3
    
    # Another irrelevant bit manipulation sequence
    bit_fiddle = raw_readings[0] ^ raw_readings[-1]
    bit_fiddle = (bit_fiddle << 2) | (bit_fiddle >> 1)
    
    # Core logic: summation of even-positioned high signals
    even_indexed_energy = sum(raw_readings[i] for i in high_signal_indices if i % 2 == 0)
    
    # Final calculation components
    aggregate_score = base_accumulator + even_indexed_energy
    correction_factor = adjustment * temp_offset
    
    # Critical execution point
    final_diagnostic = aggregate_score + correction_factor
    
    # Print result for observable output
    print(f"Result: {final_diagnostic}")

# Execute with fixed input
analyze_sensor_data([12, 45, 60, 33, 72, 41, 28])