def main():
    # System load data from sensors (in arbitrary units)
    sensor_readings = [14, 18, 22, 19, 25, 30, 12]
    baseline_offset = 5
    adjusted_readings = [x + baseline_offset for x in sensor_readings]

    # Historical peak tracking (distractor: not used in final calculation)
    historical_peaks = set()
    for val in sensor_readings:
        if val > 20:
            historical_peaks.add(val)

    # Current cluster load computed as moving average of last 3 readings
    recent_load = sum(adjusted_readings[-3:]) / 3
    cluster_load = int(recent_load)

    # Threshold function for efficiency calculation (lambda used)
    threshold_func = lambda x: x > 25

    # Auxiliary metric: stability index (dead code path)
    stability_deltas = []
    for i in range(1, len(adjusted_readings)):
        delta = abs(adjusted_readings[i] - adjusted_readings[i-1])
        stability_deltas.append(delta)
    stability_index = sum(stability_deltas) / len(stability_deltas)

    # Efficiency depends on how many high-load components exceed dynamic threshold
    def calculate_efficiency(load, predicate):
        # Simulate component bank with derived values
        components = [load * 0.8, load * 0.9, load * 1.0, load * 1.1, load * 1.2]
        active_components = list(filter(predicate, components))
        inactive_count = len(components) - len(active_components)

        # Secondary adjustment based on inactive count (irrelevant to final result)
        fallback_modes = []
        for i in range(inactive_count):
            fallback_modes.append(f"Mode_{i}")

        # Actual efficiency formula
        if len(active_components) == 0:
            return 0.0
        efficiency_score = sum(active_components) / len(active_components)
        return efficiency_score * 0.75

    # Key computation step
    thermal_capacity = 0
    thermal_capacity = calculate_efficiency(cluster_load, threshold_func)

    # Final output
    print(f"Result: {thermal_capacity}")

if __name__ == "__main__":
    main()