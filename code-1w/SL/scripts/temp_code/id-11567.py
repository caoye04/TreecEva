def main():
    # System parameters
    base_frequency = 4800
    voltage_levels = [1.1, 1.25, 1.35, 1.4]
    thermal_threshold = 75.5

    # Simulated sensor readings over time (timestamp, temp, load)
    telemetry_log = [
        (1623456780, 68.2, 0.45), (1623456785, 69.1, 0.52), (1623456790, 71.0, 0.61),
        (1623456795, 72.8, 0.58), (1623456800, 74.9, 0.73), (1623456805, 76.3, 0.81)
    ]

    # Extract recent high-load samples
    high_load_samples = [entry for entry in telemetry_log if entry[2] > 0.6]

    # Misleading intermediate calculations (distractors)
    avg_temp = sum([x[1] for x in telemetry_log]) / len(telemetry_log)
    peak_load = max([x[2] for x in telemetry_log])
    temp_variance = sum([(x[1] - avg_temp) ** 2 for x in telemetry_log]) / len(telemetry_log)
    cumulative_power_estimate = 0
    for i in range(len(voltage_levels)):
        cumulative_power_estimate += voltage_levels[i] * base_frequency * 0.1  # Not used later

    # Critical data processing
    process_data = {
        'samples': high_load_samples,
        'baseline': base_frequency,
        'scaling_factor': 0.87
    }

    # Helper lambda for dynamic adjustment
    adjust_fn = lambda x, f: round(x * f * process_data['scaling_factor'], 3)

    def calculate_efficiency(data):
        raw_samples = data['samples']
        baseline = data['baseline']
        factor = data['scaling_factor']

        # Internal distractor variables
        total_duration = raw_samples[-1][0] - raw_samples[0][0] if raw_samples else 1
        dummy_weights = [0.9 + i*0.05 for i in range(len(raw_samples))]
        weighted_load_sum = sum([raw_samples[i][2] * dummy_weights[i] for i in range(len(raw_samples))])

        # Core logic: compute effective frequency under load
        load_values = [sample[2] for sample in raw_samples]
        adjusted_frequency = baseline
        for load in load_values:
            if load > 0.7:
                adjusted_frequency *= 0.92
            elif load > 0.5:
                adjusted_frequency *= 0.98

        # Efficiency formula: scaled performance per unit load
        avg_load = sum(load_values) / len(load_values) if load_values else 1
        efficiency = (adjusted_frequency / baseline) / avg_load

        # Final transformation using lambda
        efficiency = adjust_fn(efficiency, 1000)  # Scale to meaningful range

        return int(efficiency)

    # Execution point of interest
    efficiency_score = calculate_efficiency(process_data)

    # Dead code path (never executed)
    if False:
        backup_calc = sum([int(x[1]) for x in telemetry_log])
        efficiency_score = max(efficiency_score, backup_calc)

    print(f"Result: {efficiency_score}")

if __name__ == "__main__":
    main()