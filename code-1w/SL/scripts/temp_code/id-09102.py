def calculate_thermal_metric(log, stress):
    base_rating = sum(log) / len(log) if log else 0
    adjustment = 1.5 if stress > 0.7 else 0.8
    return round(base_rating * adjustment, 4)

# System diagnostics simulation
temperature_readings = [23.5, 24.1, 22.9, 25.3, 26.0, 24.8]
efficiency_log = [0.88, 0.91, 0.85, 0.93, 0.87, 0.90]

# Irrelevant signal processing (distractor)
signal_strength = 4.2
filtered_data = [x * 0.95 for x in temperature_readings if x > 24]
smoothed = [filtered_data[i] + 0.1 for i in range(len(filtered_data))]

# Stress factor calculation (semi-relevant)
stress_threshold = 25.0
high_stress_periods = len([t for t in temperature_readings if t >= stress_threshold])
stress_factor = high_stress_periods / len(temperature_readings)

# Redundant health check (dead code path)
system_health = "stable" if stress_factor < 0.5 else "degraded"
health_score = 100 - (stress_factor * 50) if system_health == "stable" else 50

# Core computation with conditional expression
baseline_efficiency = sum(efficiency_log) / len(efficiency_log)
performance_bonus = 0.05 if baseline_efficiency > 0.88 else 0.0
adjusted_efficiency = [e + performance_bonus for e in efficiency_log]

# Key assignment with distractors
interim_diagnostic = min(adjusted_efficiency) * max(temperature_readings)
diagnostic_flag = True if interim_diagnostic > 20 else False

# Critical statement
thermal_capacity = calculate_thermal_metric(efficiency_log, stress_factor)

# Additional irrelevant metric (distraction)
peak_load_ratio = (max(temperature_readings) - min(temperature_readings)) / baseline_efficiency

# Output result
print(f"Result: {thermal_capacity}")