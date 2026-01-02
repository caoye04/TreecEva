def calculate_efficiency(profile, decay):
    base = sum(map(lambda x: x ** 0.5, filter(lambda x: x > 0, profile)))
    adjustment = min(decay) * 1.5 if any(d < 0 for d in decay) else max(decay) / 2
    penalty = len([p for p in profile if p < 30]) * 0.1
    return round(base - penalty + adjustment, 4)

# Simulated sensor data from turbine array
turbine_output = [45, 67, 23, 89, 12, 78, 56, 34]
noise_floor = [-0.3, 1.2, 0.8, -0.9, 2.1]
baseline_shift = [x * 0.95 for x in turbine_output]

# Irrelevant intermediate calculations (distractors)
avg_output = sum(turbine_output) / len(turbine_output)
deviation_map = {i: abs(turbine_output[i] - avg_output) for i in range(len(turbine_output))}
threshold_count = len([v for v in deviation_map.values() if v > 20])

# Data preprocessing with string-based flag filtering (using string method)
status_codes = ['OK', 'LOW', 'OK', 'CRIT', 'LOW', 'OK', 'OK', 'LOW']
valid_indices = [i for i, code in enumerate(status_codes) if code.strip().upper() == 'OK']
filtered_output = [turbine_output[i] for i in valid_indices]

# Secondary noise correction (semi-relevant but not used in final path)
corrected_noise = [abs(n) ** 0.5 for n in noise_floor if n != 0]
smoothing_factor = sum(corrected_noise) / len(corrected_noise) if corrected_noise else 0.0

# Core computation inputs
energy_profile = [x * 1.05 for x in filtered_output]  # Apply gain correction
losses = [abs(noise_floor[i % len(noise_floor)]) + 0.1 for i in range(len(energy_profile))]

# Red herring: unused complex structure
turbine_health = {
    'sensors': len(turbine_output),
    'faulty': status_codes.count('CRIT'),
    'maintenance_due': False
}
turbine_health['diagnostics'] = ' '.join(['PASS' if s == 'OK' else 'FAIL' for s in status_codes])

# Key statement
thermal_efficiency = calculate_efficiency(energy_profile, losses)

print(f"Result: {thermal_efficiency}")