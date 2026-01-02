def analyze_system_stability(readings):
    baseline = sum(readings) / len(readings)
    variance = sum((x - baseline) ** 2 for x in readings) / len(readings)
    adjusted_readings = [x * 0.9 + baseline * 0.1 for x in readings]

    # Irrelevant transformation (distractor)
    normalized = [max(0, min(100, (x - baseline) / (variance ** 0.5 + 1e-5))) for x in readings]
    decay_factor = 0.95
    trend = 0
    for i in range(len(adjusted_readings)):
        trend += adjusted_readings[i] * (decay_factor ** i)
    
    return adjusted_readings, trend

# Simulate sensor data from a thermodynamic system
temperature_data = [23.5, 24.1, 22.8, 25.3, 26.0, 24.7, 23.9, 25.1]

# Initial processing with side effects
adjusted_temps, temporal_trend = analyze_system_stability(temperature_data)

# Additional irrelevant computations (distractors)
smoothing_window = 3
smoothed = []
for i in range(len(adjusted_temps)):
    start = max(0, i - smoothing_window + 1)
    smoothed.append(sum(adjusted_temps[start:i+1]) / (i - start + 1))

# Hidden signal extraction (semi-relevant)
peak_activity = max(adjusted_temps) - min(adjusted_temps)
signal_strength = peak_activity * len([x for x in adjusted_temps if x > sum(adjusted_temps)/len(adjusted_temps)])

# Core recursive energy flow simulation
def simulate_decay(value, steps):
    return value * 0.5 if steps == 0 else simulate_decay(value * 1.1, steps - 1)

energy_flow = [simulate_decay(temp, 2) for temp in adjusted_temps]

# Feedback loop modeling with conditional expression
feedback_magnitude = 1.2 if sum(energy_flow) > 100 else 0.8
feedback_loops = [\n    fb * feedback_magnitude if idx % 2 == 0 else fb * 0.75 \n    for idx, fb in enumerate(energy_flow)\n]

# Central calculation buried among distractions
def calculate_equilibrium(energy_levels, feedbacks):
    net_influence = sum(energy_levels[i] * feedbacks[i] for i in range(len(energy_levels)))
    damping = len(energy_levels) / (1 + abs(feedback_magnitude - 1))
    return int(net_influence / damping)  # Final quantized equilibrium score

equilibrium_score = calculate_equilibrium(energy_flow, feedback_loops)

# Print result as required
print(f"Result: {equilibrium_score}")