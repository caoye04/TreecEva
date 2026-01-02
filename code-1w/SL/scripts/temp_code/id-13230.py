import math

# Irrelevant constants (distractors)
BASE_VOLTAGE = 230
CALIBRATION_FACTOR = 0.987
REFERENCE_TEMP = 298.15
MAX_ITERATIONS = 1000
EPSILON = 1e-6

# Sensor metadata (mostly unused)
sensor_specs = {
    'model': 'TH-7X',
    'accuracy': 0.005,
    'update_rate': 100,
    'units': 'kW/m^3'
}

# Simulated logged sensor data (real input)
logged_data = [18, 24, 12, 30, 6, 36, 8, 28, 14, 22]

# Threshold for activation (used in logic)
threshold = 15

# Decoy function – looks important but unused
def normalize_readings(data):
    max_val = max(data)
    return [x / max_val for x in data]

# Another decoy: complex transformation never called
def transform_nonlinear(data):
    return [math.tanh(x * 0.1) * math.log(x + 1) for x in data]

# Auxiliary helper used indirectly
def is_stable(value, reference=20):
    return abs(value - reference) <= 5

# Core logic disguised among distractions
def evaluate_threshold_condition(x, limit):
    if x < limit:
        return x * 1.8
    else:
        return x * 0.7 + 3

def filter_and_map(data, treshold):
    # Note: deliberate typo in parameter name to obscure usage
    result = []
    for item in data:
        if item > treshold * 0.5:  # red herring condition
            temp = evaluate_threshold_condition(item, treshold)
            if temp > 20:  # additional filtering
                result.append(temp)
    return result

# Higher-order function with lambda abstraction (required feature)
apply_correction = lambda func, data, corr: [func(x) + corr for x in data]

# Data pipeline builder – some stages are irrelevant
pipeline = [
    lambda d: [x for x in d if x % 2 == 0],           # keep even numbers
    lambda d: filter_and_map(d, threshold),             # actual signal extraction
    lambda d: apply_correction(lambda y: y**0.5, d, 1.5), # add noise-like correction
    lambda d: d                                   # pass through
]

# Execute pipeline
processed = logged_data
for stage in pipeline:
    processed = stage(processed)

# Dead code path – looks like validation but not connected
if len(processed) > 10:
    processed = processed[:10]
else:
    shadow_copy = [p * 0.95 for p in processed]  # unused

# Secondary computation on original data – misleading intermediate
aggregate_metric = sum([x**2 for x in logged_data if x > 10]) / len(logged_data)
dummy_shift = aggregate_metric * 0.01  # looks significant, unused

# Real calculation buried in complexity
def calculate_efficiency(dataset, thresh):
    # Step 1: extract values above threshold
    active_nodes = [x for x in dataset if x > thresh]
    
    # Step 2: compute weighted contribution
    weights = [0.5 if x < 25 else 1.0 for x in active_nodes]
    
    # Step 3: apply dynamic scaling based on count
    scale_factor = 2.5 if len(active_nodes) >= 4 else 1.8
    
    # Step 4: use list comprehension with filtering (required feature)
    contributions = [
        (val * weight * scale_factor)
        for val, weight in zip(active_nodes, weights)
        if is_stable(val)
    ]
    
    # Step 5: add environmental offset (constant)
    base_offset = REFERENCE_TEMP * 0.001  # minor influence
    
    # Step 6: final aggregation
    total = sum(contributions) + base_offset
    
    # Step 7: conditional boost (never triggers here)
    if all(x > 30 for x in dataset):
        total *= 1.2
    
    # Step 8: round to simulate precision loss
    return round(total, 4)

# --- Key Statement ---
thermal_capacity = calculate_efficiency(logged_data, threshold)

# Output result as required
print(f"Result: {thermal_capacity}")