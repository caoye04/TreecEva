import itertools

# Simulated sensor fusion system for environmental monitoring
sensor_a_data = [0.85, 0.91, 0.76, 0.88, 0.90]
sensor_b_data = [0.79, 0.83, 0.80, 0.85, 0.87]
sensor_c_data = [0.92, 0.84, 0.78, 0.91, 0.82]

# Irrelevant auxiliary data (distractor)
aux_temperatures = [22.1, 23.5, 21.8, 24.0, 22.7]
elevation_zones = ['low', 'mid', 'high', 'mid', 'low']

# Preprocessing: normalize sensor readings using min-max scaling (relevant)
def normalize_sensor(readings):
    min_val, max_val = min(readings), max(readings)
    if max_val == min_val:
        return [0.5] * len(readings)
    return [(x - min_val) / (max_val - min_val) for x in readings]

normalized_a = normalize_sensor(sensor_a_data)
normalized_b = normalize_sensor(sensor_b_data)
normalized_c = normalize_sensor(sensor_c_data)

# Weight assignment based on historical reliability (relevant)
historical_reliability = {
    'sensor_a': 0.88,
    'sensor_b': 0.76,
    'sensor_c': 0.81
}

# Misleading weight adjustment with dead logic path (distractor)
adjusted_weights = {}
for sensor, score in historical_reliability.items():
    base_weight = score ** 1.1
    if base_weight > 1.0:
        adjusted_weights[sensor] = 1.0  # Clipping (never reached)
    else:
        adjusted_weights[sensor] = base_weight

# Corrected weights used in calculation (relevant)
metric_weights = [
    adjusted_weights['sensor_a'],
    adjusted_weights['sensor_b'],
    adjusted_weights['sensor_c']
]

# Simulate raw outcome scores from detection algorithms (relevant)
raw_outcomes = []
for i in range(5):
    composite = (
        normalized_a[i] * metric_weights[0] +
        normalized_b[i] * metric_weights[1] +
        normalized_c[i] * metric_weights[2]
    )
    raw_outcomes.append(composite)

# Dead function - looks important but unused (distractor)
def deprecated_fusion_method(data_list):
    transposed = list(itertools.zip_longest(*data_list))
    averages = [sum(filter(None, row)) / len(list(filter(None, row))) for row in transposed]
    return [round(avg, 3) for avg in averages]

# Unused slicing operation on irrelevant data (distractor)
temp_slice = aux_temperatures[1:4:2]
elev_subset = elevation_zones[::-1]

# Another decoy function with complex logic but no invocation (distractor)
def calculate_robustness_index(stream, window=3):
    indices = []
    for i in range(len(stream) - window + 1):
        window_vals = stream[i:i+window]
        variance = sum((x - sum(window_vals)/window)**2 for x in window_vals) / window
        index = 1 / (1 + variance)
        indices.append(index)
    return sum(indices) / len(indices) if indices else 0

# Real evaluation logic with multiple steps (core reasoning path)
def evaluate_performance(weights, outcomes):
    # Step 1: Apply geometric transformation to dampen extremes
    transformed = [x ** 1.5 for x in outcomes]
    
    # Step 2: Compute weighted moving average using circular convolution concept
    cum_sum = 0
    for i in range(len(transformed)):
        weight_idx = i % len(weights)
        cum_sum += transformed[i] * weights[weight_idx]
    
    # Step 3: Normalize by total weight mass
    total_weight = sum(weights)
    preliminary_score = cum_sum / total_weight
n    
    # Step 4: Apply final non-linear calibration using tanh-like compression
    calibrated = 500 * (1 + preliminary_score ** 0.5)  # Shift and scale
    
    # Step 5: Round to nearest integer as per system spec
    return int(round(calibrated))

# Execution point of interest
final_score = evaluate_performance(metric_weights, raw_outcomes)

# Red herring computation on fake data (distractor)
fake_stream = [x * 0.5 for x in sensor_a_data if x > 0.8]
fake_aggregate = sum(f for f in fake_stream) * len(elev_subset)

# Actual output (must print result)
print(f"Result: {final_score}")