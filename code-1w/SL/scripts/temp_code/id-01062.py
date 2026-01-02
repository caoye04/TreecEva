import math

# Irrelevant helper function (dead code path)
def unused_utility(x):
    return sum([i ** 2 for i in x if i % 3 == 0])

# Misleading metric calculator (partially used, mostly distraction)
def false_metric(seq):
    acc = 0
    for i in range(len(seq)):
        if seq[i] % 4 == 0:
            acc += seq[i] // 4
    return acc * 1.5

# Core transformation pipeline
def transform_entry(val, key_multiplier):
    shifted = val ^ key_multiplier  # Bitwise red herring
    adjusted = abs(shifted) % 1000
    if adjusted > 500:
        adjusted -= 250
    return int(math.sqrt(adjusted + 1))

# Data normalization with decoy logic
def normalize_stream(raw):
    filtered = [x for x in raw if x > 0]  # Remove negatives (some are irrelevant)
    magnitude = sum(filtered) / len(filtered) if filtered else 0
    scaled = [x / (magnitude + 1e-8) for x in filtered]
    return [round(s * 100) for s in scaled[:10]]  # Truncate to first 10

# Real processing function obscured by complexity
def process_metrics(data, cfg):
    threshold = cfg['limit']
    boost = cfg['amplify']
    temp_result = 0

    # Complex conditional with misleading branches
    for idx, item in enumerate(data):
        if idx % 2 == 0:
            temp_result += int(math.log(item + 2) * boost)
        elif item > threshold:
            temp_result += item % 7
        else:
            temp_result -= int(math.sin(item) * 10)  # Negligible effect due to small values

    # Final adjustment using lambda (critical python feature)
    modifier = lambda x: x + 10 if x < 100 else x - 5
    return modifier(temp_result)

# Decoy data structure (distractor)
legacy_system_cache = {
    'checksums': [113, 244, 307, 412],
    'flags': [True, False, True],
    'unused_score': 87
}

# Primary input data (real source)
raw_sensor_readings = [23, 45, 67, 89, 12, 34, 56, 78, 90, 11, 22, 33]

# Configuration with irrelevant fields
config = {
    'active': True,
    'limit': 40,
    'amplify': 3,
    'version': '2.1.0',
    'debug_mode': False,
    'timeout': 5000,
    'metadata_keys': ['id', 'ts', 'src']
}

# Step 1: Normalize raw sensor data
normalized_readings = normalize_stream(raw_sensor_readings)

# Step 2: Transform each entry using bitwise-aware logic
transformed_data = [transform_entry(val, 7) for val in normalized_readings]

# Step 3: Process metrics through main logic chain
final_diagnostic = process_metrics(transformed_data, config)

# Print final result as required
print(f"Result: {final_diagnostic}")