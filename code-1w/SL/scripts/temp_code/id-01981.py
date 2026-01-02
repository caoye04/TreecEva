import itertools

# Simulated sensor data for wind turbine diagnostics
turbine_readings = [
    [107, 115, 99, 120, 108],
    [205, 210, 198, 215, 207],
    [301, 297, 303, 295, 306],
    [410, 415, 405, 420, 412]
]

# Fault thresholds (indexed by sensor type)
fault_thresholds = {
    'vibration': 110,
    'pressure': 200,
    'temperature': 300,
    'rpm': 400
}

# Irrelevant calibration constants (distractor)
calib_constants = {
    'gain': 1.02,
    'offset': -0.5,
    'scale_factor': 0.99
}

# Decoy function that looks important but is never called
def analyze_vibration_patterns(data):
    return sum(x ** 0.5 for x in data if x > 100) / len(data)

# Misleading intermediate computation (unused)
baseline_avg = sum(itertools.chain.from_iterable(turbine_readings)) / 20

# Auxiliary transformation map (some entries are red herrings)
sensor_transform = {
    0: lambda x: x + 5 if x < 110 else x - 3,
    1: lambda x: (x * 1.05) // 1,
    2: lambda x: x,
    3: lambda x: (x + 10) % 310,
    4: lambda x: x * 0.95
}

# Dead code path: simulated backup thresholds (not used in logic)
backup_fault_levels = [
    {'type': 'vib', 'limit': 105},
    {'type': 'pres', 'limit': 195},
    {'type': 'temp', 'limit': 290},
    {'type': 'rot', 'limit': 390}
]

# Real-time anomaly counter (distraction: updated but not used)
anomaly_count = 0
for readings in turbine_readings:
    for val in readings:
        if val > 300:
            anomaly_count += 1

# Core diagnostic logic
mapped_sensors = ['vibration', 'pressure', 'temperature', 'rpm']

# Apply transformations and extract key metrics
def process_turbine_data(raw_data, transform_map):
    processed = []
    for i, row in enumerate(raw_data):
        transformed_row = [transform_map[j](val) for j, val in enumerate(row)]
        processed.append(transformed_row)
    return processed

# Heavily obfuscated filter using lambda and itertools (some parts irrelevant)
filtered_diagnostics = list(filter(
    lambda record: sum(record) > 500,
    itertools.starmap(
        lambda a, b, c, d: [a*1.1, b*0.9, c+2, d-1],
        process_turbine_data(turbine_readings, sensor_transform)
    )
))

# Secondary analysis with decoy conditionals
flagged_readings = 0
for entry in filtered_diagnostics:
    if any(x > 450 for x in entry):  # This condition always false due to scaling
        flagged_readings += 1

# Critical function: computes final diagnostic score
# Combines arithmetic, dictionary lookup, list comprehension, and conditional logic
def aggregate_metrics(data, thresholds):
    scores = []
    for idx, sensor_type in enumerate(mapped_sensors):
        raw_series = [row[idx] for row in data]
        base_threshold = thresholds[sensor_type]
        
        # Compute deviation ratio using modular arithmetic and exponentiation
        avg_val = sum(raw_series) / len(raw_series)
        deviation = abs(avg_val - base_threshold)
        stability_score = (1000 / (1 + deviation))  # Inverse relationship
        
        # Conditional bonus based on pattern consistency (uses bitwise check)
        variation = max(raw_series) - min(raw_series)
        consistency_bonus = 10 if (int(variation) & 1) == 0 else 0  # Even variation?
        
        # Red herring: unused complex calculation
        entropy_proxy = sum(x * x for x in raw_series) / (avg_val * len(raw_series) + 1)
        
        final_component = stability_score + consistency_bonus
        scores.append(final_component)
    
    # Final aggregation with weighted sum (weights appear arbitrary but are fixed)
    weights = [0.2, 0.3, 0.3, 0.2]
    weighted_sum = sum(w * s for w, s in zip(weights, scores))
    
    # Additional adjustment based on length (constant in this case)
    adjustment = len(scores) * 0.5
    
    return int(weighted_sum + adjustment)

# Execute main pipeline
turbine_data = process_turbine_data(turbine_readings, sensor_transform)
final_diagnostic = aggregate_metrics(turbine_data, fault_thresholds)

# Output result as required
print(f"Result: {final_diagnostic}")