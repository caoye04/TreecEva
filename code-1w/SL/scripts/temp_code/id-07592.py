from collections import defaultdict, Counter
from itertools import cycle

# Simulated sensor data for thermal regulation system
temperature_readings = [23.5, 24.1, 22.8, 25.6, 26.7, 24.3, 23.9, 25.1, 26.4, 27.2, 25.8]
humidity_levels = [45, 47, 44, 50, 52, 48, 46, 51, 53, 49, 47]
pressure_logs = [1013, 1015, 1012, 1018, 1020, 1016, 1014, 1019, 1021, 1017, 1015]

# Irrelevant transformation: normalize humidity (unused later)
normalized_humidity = [h / max(humidity_levels) for h in humidity_levels]

# Misleading capacity calculation based on pressure (dead end)
baseline_pressure = sum(pressure_logs) / len(pressure_logs)
phantom_capacity = int(baseline_pressure - 1000) * 5  # Looks important but unused

# Data alignment using cycling (over-engineered)
sensor_cycle = cycle(['temp', 'hum', 'pres'])
reading_sequence = [next(sensor_cycle) for _ in range(len(temperature_readings))]

# Real processing begins: detect thermal anomalies
anomalies = []
for i, temp in enumerate(temperature_readings):
    if temp > 25.0:
        anomalies.append(i)

# Compute derived thermal load with polynomial response curve
thermal_loads = []
for t in temperature_readings:
    adjusted = (t - 20) ** 2 + 3 * (t - 20)  # Quadratic thermal model
    thermal_loads.append(adjusted)

# Decoy statistical analysis (never used)
stats_summary = defaultdict(float)
stats_summary['mean_temp'] = sum(temperature_readings) / len(temperature_readings)
stats_summary['variance'] = sum((t - stats_summary['mean_temp']) ** 2 for t in temperature_readings) / len(temperature_readings)
stats_summary['skew'] = len(anomalies) / len(temperature_readings)  # Fake skew metric

# Spurious list of thresholds (distractor)
thresholds = [30, 50, 75, 100, 120, 150]
classified_loads = []
for load in thermal_loads:
    assigned = False
    for th in thresholds:
        if load < th:
            classified_loads.append(th)
            assigned = True
            break
    if not assigned:
        classified_loads.append(200)

# Another decoy: frequency count of classifications (looks diagnostic)
load_distribution = Counter(classified_loads)

# Core logic buried among distractions
baseline_thermal = sum(thermal_loads) / len(thermal_loads)
efficiency_factor = 0.87

# Key assignment with multiple dependencies
peak_capacity = max(thermal_loads) * efficiency_factor

# Fake optimization pass (dead code)
optimized = False
def optimize_system():
    global optimized
    optimized = True
    return False  # Never called

# Red herring: simulate pressure drift (irrelevant)
pressure_drift = 0
for i in range(1, len(pressure_logs)):
    pressure_drift += abs(pressure_logs[i] - pressure_logs[i-1])

# Final result output
Result: {peak_capacity}