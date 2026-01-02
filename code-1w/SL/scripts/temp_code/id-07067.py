def main():
    # Simulate sensor readings with noise
    raw_readings = [12, 15, 10, 8, 20, 14, 16]
    noise_factor = 0.1
    adjusted_readings = [x + x * noise_factor for x in raw_readings]

    # Filter out anomalies using a lambda-based threshold
    threshold_filter = lambda val: val > 11.5
    filtered_readings = list(filter(threshold_filter, adjusted_readings))

    # Compute moving average as stability metric
    stability_window = []
    for i in range(len(filtered_readings) - 1):
        stability_window.append((filtered_readings[i] + filtered_readings[i+1]) / 2)

    # Misleading computation: energy consumption (not used)
    base_power = 2.3
    runtime_hours = 8
    energy_consumption = base_power * runtime_hours  # Distractor

    # State tracking variables for system health
    health_log = []
    for val in stability_window:
        if val > 13:
            health_log.append('OPTIMAL')
        elif val > 10:
            health_log.append('STABLE')
        else:
            health_log.append('CAUTION')

    # Count transitions in health state (semi-relevant)
    transitions = 0
    for i in range(len(health_log) - 1):
        if health_log[i] != health_log[i+1]:
            transitions += 1

    # Feedback loop simulation with nested conditionals
    feedback_loop = []
    for val in filtered_readings:
        if val > 15:
            feedback_loop.append(3)
        elif val > 12:
            feedback_loop.append(2)
        else:
            feedback_loop.append(1)

    # Dead code path: diagnostic trace (never used)
    diagnostic_trace = []
    for i, v in enumerate(feedback_loop):
        diagnostic_trace.append(f"Step {i}: Level {v}")

    # Core aggregation logic
    def aggregate_performance(levels):
        base_weight = 0.8
        bonus_multiplier = 1.2
        penalty_rate = 0.9

        total = 0
        for level in levels:
            if level == 3:
                total += 10 * bonus_multiplier
            elif level == 2:
                total += 10 * base_weight
            else:
                total += 5 * penalty_rate

        # Apply decay for system fatigue (simulated over cycles)
        cycle_count = len(levels)
        fatigue_decay = 0.98 ** cycle_count
        total *= fatigue_decay

        return int(total)  # Final quantized score

    final_score = aggregate_performance(feedback_loop)
    print(f"Result: {final_score}")

if __name__ == "__main__":
    main()