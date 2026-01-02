def calculate_threshold(data):
    filtered = [x for x in data if x > 20]
    averages = [(filtered[i] + filtered[i+1]) / 2 for i in range(len(filtered)-1)]
    return sum(averages) / len(averages) if averages else 0

readings = [15, 25, 30, 18, 22, 40, 35]
temperature_baseline = 10
correction_factor = 1.05

# Irrelevant variable (minimal distraction)
temp_debug_log = [r * correction_factor for r in readings if r < 20]

energy_threshold = calculate_threshold(readings)
print(f"Target result: {energy_threshold}")