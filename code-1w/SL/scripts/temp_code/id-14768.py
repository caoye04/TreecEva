def analyze_temperature_profile(temps):
    avg_temp = sum(temps) / len(temps)
    temp_variance = sum((t - avg_temp) ** 2 for t in temps) / len(temps)
    normalized_stability = 100 / (1 + temp_variance)
    return normalized_stability

# Simulate sensor data from chemical reactor batches
temperature_readings = [85, 87, 83, 86, 90, 88, 84]
humidity_levels = [45, 47, 46, 50, 52, 48, 44]  # unused distractor
pressure_logs = [1.02, 1.05, 1.03, 1.08, 1.07, 1.04, 1.01]  # unused distractor

stability_score = analyze_temperature_profile(temperature_readings)

# Transform raw readings into treatment phases using list comprehension and lambda
treatment_phases = [(i, t > 86) for i, t in enumerate(temperature_readings)]
phase_filter = lambda phase: phase[1]  # identifies high-temp phases
high_temp_indices = [p[0] for p in treatment_phases if phase_filter(p)]

# Calculate duration of critical phases
critical_phase_durations = []
current_duration = 0
for i in range(len(temperature_readings)):
    if temperature_readings[i] > 86:
        current_duration += 1
    else:
        if current_duration > 0:
            critical_phase_durations.append(current_duration)
            current_duration = 0
if current_duration > 0:
    critical_phase_durations.append(current_duration)

total_critical_time = sum(critical_phase_durations)
dummy_calculation = sum(humidity_levels) * 0.01  # irrelevant computation

# Apply efficiency decay model based on total time in critical zones
efficiency_decay = 0.95 ** total_critical_time
baseline_output = 500

# Process data through yield estimation pipeline
processed_data = {
    'stability': stability_score,
    'decay_factor': efficiency_decay,
    'base': baseline_output,
    'extra_noise': dummy_calculation  # red herring
}

def calculate_optimal_yield(data):
    raw_yield = data['base'] * data['decay_factor']
    adjustment = 1 + (data['stability'] - 90) / 100  # fine-tuning based on stability
    final = raw_yield * adjustment
    return int(final)

final_yield = calculate_optimal_yield(processed_data)
print(f"Result: {final_yield}")