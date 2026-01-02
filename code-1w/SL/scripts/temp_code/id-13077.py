import itertools

# System health monitoring simulation with diagnostic computation

# Sensor input data (simulated)
temperature_readings = [23.5, 24.1, 22.9, 25.3, 26.0, 24.8, 23.7]
pressure_readings = [101.3, 102.1, 99.8, 103.4, 100.2, 101.8, 102.5]
humidity_readings = [45, 47, 50, 44, 48, 52, 46]

# Irrelevant transformation: rolling average filter (unused in final calculation)
def smooth_signal(signal):
    return [(signal[i-1] + signal[i] + signal[i+1]) / 3 
            for i in range(1, len(signal)-1)]

# Distractor function: analyzes pressure trends but not used
def analyze_pressure_trend(pressures):
    trend_changes = 0
    for i in range(1, len(pressures)):
        if (pressures[i] - pressures[i-1]) * (pressures[i-1] - pressures[i-2] if i > 1 else 0) < 0:
            trend_changes += 1
    return trend_changes

# Decoy diagnostic score based on humidity only (misleading)
humidity_risk_score = 0
for h in humidity_readings:
    if h > 50:
        humidity_risk_score += 3
    elif h > 45:
        humidity_risk_score += 1

# Unused data fusion attempt with itertools (red herring)
combined_pairs = list(itertools.product(temperature_readings[::2], pressure_readings[::2]))
product_sum = sum(a * b for a, b in combined_pairs[:3])

# Real processing path begins here
valid_temps = [t for t in temperature_readings if 22 <= t <= 25]
adjusted_pressure = [p - 100 for p in pressure_readings]

# Compute thermal variance (used later)
mean_temp = sum(valid_temps) / len(valid_temps)
thermal_variance = sum((t - mean_temp) ** 2 for t in valid_temps) / len(valid_temps)

# Primary diagnostic components
base_stability_index = len(valid_temps) * 10
fluctuation_penalty = int(sum(abs(p - adjusted_pressure[i-1]) for i, p in enumerate(adjusted_pressure) if i > 0))

# Hidden correction logic: find dominant cycle in sensor sampling
indices = list(range(len(temperature_readings)))
cycle_patterns = []
for size in range(2, 5):
    cycles = [indices[i:i+size] for i in range(0, len(indices), size) if len(indices[i:i+size]) == size]
    if cycles:
        cycle_patterns.append(len(cycles[-1]))
mode_cycle_length = max(set(cycle_patterns), key=cycle_patterns.count) if cycle_patterns else 3

# Critical intermediate result (obscured by context)
aggregate_score = base_stability_index - fluctuation_penalty

correction_factor = 1.75  # Calibrated from historical data
offset_value = thermal_variance * mode_cycle_length

# UNUSED: complex bit manipulation on sensor IDs (dead code path)
sensor_id = 0b11010110
shifted_a = (sensor_id >> 3) & 0b1111
shifted_b = (sensor_id << 2) & 0b11110000
xor_fuse = shifted_a ^ shifted_b
inverted = ~xor_fuse & 0b1111

# Final diagnostic computation (key statement)
final_diagnostic = aggregate_score * correction_factor + offset_value

# Irrelevant sorting operation (distractor)
sorted_diagnostic = sorted([final_diagnostic, product_sum, humidity_risk_score])

# Additional decoy: early return simulation that doesn't trigger
ever_triggered = False
if final_diagnostic < 0:
    final_diagnostic = -1
    ever_triggered = True

print(f"Result: {final_diagnostic}")