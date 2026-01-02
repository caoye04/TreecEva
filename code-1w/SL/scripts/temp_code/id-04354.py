import math

# Simulated sensor diagnostics from industrial turbine array
turbine_ids = [101, 102, 103, 104, 105]
sensor_readings = {
    101: [89, 92, 85, -1, 95, 88],
    102: [76, -1, -1, 81, 74, 79],
    103: [94, 90, 93, 91, -1, 89],
    104: [67, 70, -1, 65, 68, -1],
    105: [85, 87, 89, -1, 86, 88]
}

# Irrelevant auxiliary mapping (distractor)
status_codes = {'OK': 200, 'WARN': 300, 'ERR': 500}

# Historical baseline data – not used in final computation (dead path)
historical_averages = {tid: sum(vals) / len(vals) for tid, vals in sensor_readings.items()}

# Compute raw averages including noise (misleading intermediate)
raw_averages = {}
for tid, readings in sensor_readings.items():
    valid_readings = [r for r in readings if r != -1]
    raw_averages[tid] = sum(valid_readings) / len(valid_readings) if valid_readings else 0

# Identify turbines with more than 1 failed sensor (seemingly relevant but unused)
degraded_turbines = [tid for tid, readings in sensor_readings.items() if readings.count(-1) > 1]

# Generate diagnostic codes based on threshold (distractor logic)
diagnostic_flags = {}
for tid, avg in raw_averages.items():
    if avg >= 85:
        diagnostic_flags[tid] = 'OPTIMAL'
    elif avg >= 75:
        diagnostic_flags[tid] = 'STABLE'
    else:
        diagnostic_flags[tid] = 'CRITICAL'

# Unused transformation – list comprehension red herring
restructured_data = [
    {'turbine': tid, 'diagnostics': [r for r in readings if r != -1 and r > 70]}
    for tid, readings in sensor_readings.items()
]

# Core logic begins here — extract all non-negative readings above threshold
all_diagnostics = []
for readings in sensor_readings.values():
    all_diagnostics.extend([r for r in readings if r != -1])

# Apply domain-specific filter: only high-confidence readings
high_confidence = [x for x in all_diagnostics if x >= 85]

# Further filter by occurrence frequency (set operation distraction)
frequency_set = set([x for x in high_confidence if high_confidence.count(x) >= 2])
filtered_diagnostics = [x for x in high_confidence if x in frequency_set]

# Introduce irrelevant mathematical transformation (bitwise decoy)
transformed_values = [val ^ 17 for val in filtered_diagnostics]

# Critical statement: compute integer average of filtered high-confidence diagnostics
if filtered_diagnostics:
    filtration_score = sum(filtered_diagnostics) // len(filtered_diagnostics)
else:
    filtration_score = 0

# Print result as required
print(f"Result: {filtration_score}")