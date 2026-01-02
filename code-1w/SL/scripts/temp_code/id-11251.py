from itertools import combinations

# Simulated sensor array data from environmental monitoring station
temperature_readings = [23.4, 24.1, 22.9, 25.3, 26.0, 24.8, 23.7]
humidity_readings = [45, 47, 50, 52, 48, 55, 60]
pressure_readings = [1013, 1015, 1012, 1010, 1008, 1009, 1011]

# Irrelevant transformation - red herring
shifted_temps = [t - 273.15 for t in [x + 273.15 for x in temperature_readings]]

# Misleading intermediate: normalized but unused
normalized_humidity = [h / max(humidity_readings) for h in humidity_readings]

# Dummy function that looks important but isn't used in final calculation
def calculate_entropy(values):
    total = sum(values)
    return sum(-(v/total) * (v/total) for v in values if v > 0)

# Another decoy: frequency analysis with no impact
duplicate_count = 0
seen = set()
for h in humidity_readings:
    if h in seen:
        duplicate_count += 1
    seen.add(h)

# Real processing begins: detect anomalies in temperature
anomalies = []
for i, temp in enumerate(temperature_readings):
    if abs(temp - sum(temperature_readings)/len(temperature_readings)) > 1.0:
        anomalies.append(i)

# Cross-reference anomalies with pressure fluctuations using zip
anomaly_pressure_pairs = list(zip(anomalies, [pressure_readings[i] for i in anomalies]))
anomaly_magnitude = sum(p % 10 for _, p in anomaly_pressure_pairs)

# Distractor: complex but unused combinatorial analysis
valid_triplets = 0
for combo in combinations(pressure_readings, 3):
    if abs(combo[0] - combo[1]) < 3 and abs(combo[1] - combo[2]) < 3:
        valid_triplets += 1

# Decoy dictionary construction - looks diagnostic but unused
diagnostic_summary = {}
for idx, (t, h) in enumerate(zip(temperature_readings, humidity_readings)):
    status = 'stable' if t < 25 and h < 55 else 'elevated'
    diagnostic_summary[f'sensor_{idx}'] = status

# Real signal: count how many sensors report elevated temp or humidity
elevated_conditions = 0
for t, h in zip(temperature_readings, humidity_readings):
    if t > 24.5 or h > 50:
        elevated_conditions += 1

# Fake correction path - never executed
correction_applied = False
if len(anomalies) > 5:
    elevated_conditions *= 0.9
    correction_applied = True

# Core logic disguised among distractors
baseline_score = len(anomalies) * 100
aggregate_score = baseline_score + elevated_conditions * 10

# Hidden dependency on set operations
unique_pressure_anomalies = set(p % 7 for p in pressure_readings)
reference_set = {1, 2, 3, 4}
overlap = unique_pressure_anomalies & reference_set
anomaly_flag = 1 if len(overlap) >= 2 else 0

correction_factor = 0
for i, p in enumerate(pressure_readings):
    if i in anomalies and p < 1010:
        correction_factor += 50

# Critical execution point
final_diagnostic = aggregate_score + anomaly_flag * correction_factor

# Dead code path - looks like validation but doesn't affect result
if final_diagnostic < 0:
    final_diagnostic = abs(final_diagnostic)
    raise RuntimeError("Invalid diagnostic")

print(f"Result: {final_diagnostic}")