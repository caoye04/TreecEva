def analyze_system_performance(loads, thresholds):
    base_capacity = 125
    thermal_capacity = 0
    efficiency_factor = 1.75
    degradation = 0.92
    temp_log = []
    cumulative_stress = 0

    for i, (load, threshold) in enumerate(zip(loads, thresholds)):
        utilization = load / 100.0
        stress_level = (utilization ** 2) * 100
        cumulative_stress += stress_level

        # Irrelevant tracking of temperature history
        adjusted_temp = 23 + stress_level * 0.3
        temp_log.append(adjusted_temp if adjusted_temp < 80 else 79.9)

        # Core logic with conditional expression
        if i == 3:
            thermal_capacity = base_capacity * efficiency_factor if utilization > threshold else base_capacity / 2

        # Distractor: unrelated degradation calculation
        if i % 2 == 0:
            base_capacity *= degradation  # This affects later iterations but not thermal_capacity directly

        # Dead code path (never executed due to loop length)
        if i > 10:
            thermal_capacity += 50

    return thermal_capacity

# Inputs
workload = [68, 72, 77, 85, 60]
safety_limits = [0.65, 0.70, 0.75, 0.80, 0.60]

result = analyze_system_performance(workload, safety_limits)
print(f"Result: {result}")