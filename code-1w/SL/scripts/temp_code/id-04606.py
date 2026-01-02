from collections import defaultdict, Counter
import math

# Simulated sensor data processing for environmental monitoring system
temperature_readings = [23.5, 24.1, 22.8, 25.0, 23.9, 24.4, 26.0, 23.7]
humidity_readings = [45, 48, 50, 55, 60, 62, 58, 53]
co2_levels = [400, 410, 415, 430, 450, 470, 500, 520]

# Irrelevant auxiliary data (distractor)
power_cycles = [1, 0, 1, 1, 0, 1, 1, 1]
uptime_seconds = [3600, 7200, 10800, 14400, 18000, 21600, 25200, 28800]
dummy_flags = [True, False, True, False, True, True, False, True]

# Data aggregation (relevant)
sensor_data = defaultdict(list)
for i in range(len(temperature_readings)):
    sensor_data['temp'].append(temperature_readings[i])
    sensor_data['humid'].append(humidity_readings[i])
    sensor_data['co2'].append(co2_levels[i])

# Misleading transformation chain (partially irrelevant)
normalized_humidity = [h / 100.0 for h in humidity_readings]
dew_point_estimates = [temp - ((100 - humid) / 5.0) for temp, humid in zip(temperature_readings, humidity_readings)]
adjusted_co2 = [(c - 400) * 1.2 for c in co2_levels if c > 420]  # filtered subset

# Decoy function with unused logic
def analyze_power_efficiency(cycles, uptime):
    efficiency_ratio = sum(cycles) / len(uptime)
    peak_utilization = max(uptime) / 86400
    return efficiency_ratio * 100 if peak_utilization > 0.5 else 0

# Another decoy: dead code path
temperature_anomalies = []
for t in temperature_readings:
    if t > 25 and t < 24:  # logically impossible
        temperature_anomalies.append(t)

# Real processing begins here
baseline = {
    'temp': 24.0,
    'humid': 50,
    'co2': 450
}

metrics = {}
metrics['temp_dev'] = sum(abs(t - baseline['temp']) for t in temperature_readings) / len(temperature_readings)
metrics['humid_dev'] = sum(abs(h - baseline['humid']) for h in humidity_readings) / len(humidity_readings)
metrics['co2_dev'] = sum(abs(c - baseline['co2']) for c in co2_levels) / len(co2_levels)

# Complex conditional weighting (key logic)
def calculate_stability_factor(deviations):
    base = 1.0
    if deviations['temp_dev'] < 1.0:
        base *= 1.2
    if deviations['humid_dev'] < 5.0:
        base *= 1.15
    if deviations['co2_dev'] < 50.0:
        base *= 1.25
    return base

# Secondary distraction: unused complex list comprehension
entropy_signals = [
    -p * math.log(p) for p in [
        Counter([int(x) for x in co2_levels]).get(val, 0) / len(co2_levels) + 1e-9 
        for val in set(int(x) for x in co2_levels)
    ] if p > 0
]

# Real evaluation function
def evaluate_performance(met, base):
    # Initialize score
    raw_score = 0
    weights = {'temp_dev': 0.4, 'humid_dev': 0.3, 'co2_dev': 0.3}
    
    for key, weight in weights.items():
        deviation = met[key]
        contribution = (100 - min(deviation * 10, 95)) * weight
        raw_score += contribution
    
    # Apply stability multiplier
    stability_multiplier = calculate_stability_factor(met)
    adjusted_score = raw_score * stability_multiplier
    
    # Apply arbitrary floor and ceiling
    final = max(20, min(adjusted_score, 100))
    
    # Red herring: unused transformation
    normalized_final = round((final - 20) / 80, 4)
    
    return int(round(final))

# Execution point of interest
final_score = evaluate_performance(metrics, baseline)

# Output result as required
print(f"Target result: {final_score}")