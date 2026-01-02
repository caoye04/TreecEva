def main():
    # Sensor metrics from environmental monitoring array
    raw_readings = [127, 83, 155, 46, 94, 133, 77, 101, 142]
    
    # Baseline calibration set (known stable conditions)
    baseline_set = {70, 77, 83, 89, 94, 101, 107}
    
    # Thresholds for anomaly detection
    lower_bound = 75
    upper_bound = 130

    # Irrelevant configuration: network parameters
    net_latency_ms = 42
    packet_size_b = 1500
    retries = 3
    timeout_flag = False

    # Signal processing: filter out noise outside operational range
    filtered_metrics = [x for x in raw_readings if lower_bound <= x <= upper_bound]

    # Dead code path: unused alternative filtering method
    def legacy_filter(data):
        return [x for x in data if x > 60 and x % 7 != 0]  # never called

    # Auxiliary tracking variables (distractors)
    sample_count = len(raw_readings)
    avg_raw = sum(raw_readings) / sample_count
    fluctuation_index = max(raw_readings) - min(raw_readings)

    # Bitmask analysis on selected readings (mixed paradigm)
    masked_values = []
    for val in filtered_metrics:
        processed = val & 0xFF  # Apply 8-bit mask (redundant here but looks important)
        if processed % 2 == 0:
            processed ^= 0x0F  # Flip lower nibble for even numbers
        masked_values.append(processed)
    
    # Secondary derived metric (unused)
    adjusted_sum = sum(masked_values) + 17

    # Control flow with conditional expression
    status_flag = 'active' if len(filtered_metrics) > 5 else 'standby'

    # Set operations: detect deviations from baseline
    observed_set = set(filtered_metrics)
    deviant_readings = observed_set - baseline_set  # readings not in baseline
    expected_missing = baseline_set - observed_set

    # Another red herring: energy consumption estimate
    energy_cost = 0.0
    for i, val in enumerate(masked_values):
        energy_cost += val * 0.03
        if i % 2 == 0:
            energy_cost -= 0.01  # arbitrary correction

    # Core diagnostic logic
    def analyze_readings(readings_list, baseline):
        readings_set = set(readings_list)
        match_count = len(readings_set & baseline)
        deviation_score = len(readings_set - baseline)
        
        # Conditional expression determining outcome
        severity = 1.5 if deviation_score >= 3 else (0.5 if deviation_score == 0 else 1.0)
        
        # Final computation combining arithmetic and set logic
        diagnostic_value = (match_count * 12) - (deviation_score * 8)
        
        # Introduce bit operation distraction (used in calculation)
        diagnostic_value ^= 0b1101  # XOR with binary constant
        diagnostic_value += (deviation_score & 0b111)  # Add bitwise AND result

        return int(diagnostic_value)

    # Execute critical statement
    final_diagnostic = analyze_readings(filtered_metrics, baseline_set)

    # Unused telemetry output
    telemetry_dump = {
        'raw_count': sample_count,
        'filtered_count': len(filtered_metrics),
        'deviations': len(deviant_readings),
        'energy': round(energy_cost, 3)
    }

    # Print target result
    print(f"Result: {final_diagnostic}")

if __name__ == '__main__':
    main()