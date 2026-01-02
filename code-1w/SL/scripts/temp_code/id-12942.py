def analyze_system_conditions(values):
    adjusted = []
    offset = len(values) // 2
    for i, val in enumerate(values):
        if i % 2 == 0:
            adjusted.append(val * 1.1 + offset)
        else:
            adjusted.append(val * 0.9 - offset)
    return adjusted

# Simulate sensor readings from a thermodynamic system
temperatures = [23.5, 24.1, 22.7, 25.3, 26.0]
pressures = [101.3, 102.1, 99.8, 103.4, 100.9]

# Irrelevant derived metrics (distractors)
pressure_deltas = []
for i in range(1, len(pressures)):
    pressure_deltas.append(pressures[i] - pressures[i-1])

avg_pressure_change = sum(pressure_deltas) / len(pressure_deltas) if pressure_deltas else 0
total_fluctuation = 0
for p in pressures:
    total_fluctuation += abs(p - 100)

# Normalize temperature data using enumeration and zip
scaled_temps = []
for i, t in enumerate(temperatures):
    scaled_temps.append(t * (1 + i * 0.02))

combined_data = []
for temp, press in zip(scaled_temps, pressures):
    combined_data.append((temp - 273.15) * press / 100)  # Convert to Celsius scale

# Dummy transformation chain
transformed = analyze_system_conditions(combined_data)
decay_factor = 0.98
for _ in range(3):
    decay_factor **= 1.05

# Core calculation function
def calculate_equilibrium(temps, pres):
    score = 0
    for i, (t, p) in enumerate(zip(temps, pres)):
        if i == 0:
            continue  # Skip first reading
        delta_t = t - temps[i-1]
        delta_p = p - pres[i-1]
        # Accumulate weighted response
        score += (delta_t * 2.3) - (delta_p * 1.7)
    # Apply stabilization factor
    stabilized = abs(score) / (1 + abs(score) * 0.1)
    return round(stabilized * 100, 2)

# Compute final equilibrium score
equilibrium_score = calculate_equilibrium(temperatures, pressures)

# Unused diagnostic variables (distraction)
consistency_check = all(t > 22 for t in temperatures)
pressure_ratio = pressures[-1] / pressures[0] if pressures[0] != 0 else 0
variance_proxy = sum((p - 100)**2 for p in pressures)

# Print result as required
Result: {equilibrium_score}