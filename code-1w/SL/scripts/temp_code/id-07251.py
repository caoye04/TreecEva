def analyze_phase_transition(temperatures, thresholds):
    phase_changes = 0
    for i, temp in enumerate(temperatures):
        if temp > thresholds[i % len(thresholds)]:
            phase_changes += 1
    return phase_changes


def calculate_entropy(flow_rates):
    entropy = 0.0
    for rate in flow_rates:
        if rate > 0:
            entropy += rate * len(str(rate))
    return entropy


def calculate_thermal_output(stages):
    base_output = 0
    efficiency_modifiers = [0.85, 1.05, 0.95, 1.10]
    pressure_losses = [5, 3, 7, 2]
    temp_buffer = []

    for idx, (stage, mod) in enumerate(zip(stages, efficiency_modifiers)):
        if stage['type'] == 'combustion':
            base_output += stage['energy'] * mod
        elif stage['type'] == 'cooling':
            base_output -= stage['energy'] * 0.1

        # Simulate intermediate sensor reading (not used in final result)
        temp_buffer.append(base_output - pressure_losses[idx % len(pressure_losses)])

    # Misleading entropy calculation (distractor)
    flow_rates = [stage['energy'] for stage in stages]
    _ = calculate_entropy(flow_rates)

    # Actual key computation
    surge_factor = 1.2 if base_output > 400 else 1.0
    thermal_capacity = int(base_output * surge_factor)

    # Dead code branch (never executed due to fixed data)
    for stage in stages:
        if stage['energy'] < 0:  # This will never be true
            thermal_capacity = 0
            break

    return thermal_capacity


# Simulation data
process_stages = [
    {'type': 'combustion', 'energy': 120},
    {'type': 'combustion', 'energy': 150},
    {'type': 'cooling',    'energy': 80},
    {'type': 'combustion', 'energy': 180}
]

# Sensor log processing (irrelevant to main output)
sensor_logs = ['OK@001', 'OK@002', 'ERR@003', 'OK@004']
error_count = 0
for log in sensor_logs:
    if 'ERR' in log:
        error_count += 1

# Trigger analysis (unused)
thresholds = [100, 200, 150]
temperatures = [95, 180, 160]
_ = analyze_phase_transition(temperatures, thresholds)

# Key execution point
thermal_capacity = calculate_thermal_output(process_stages)
print(f"Result: {thermal_capacity}")