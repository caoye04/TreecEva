import math

# Simulated sensor fusion system for environmental monitoring
def collect_sensor_data():
    raw_values = [127, 255, 64, 192, 32]
    timestamps = [1623456000, 1623456060, 1623456120, 1623456180, 1623456240]
    metadata = {'location': 'Zone-A', 'version': '2.1'}
    # Irrelevant transformation
    scaled = [x * 0.1 for x in raw_values]
    return list(zip(raw_values, timestamps))

def filter_outliers(data, limit=200):
    filtered = []
    outlier_count = 0
    for val, ts in data:
        if val > limit:
            outlier_count += 1
        else:
            filtered.append((val, ts))
    # Dead code path (never used)
    if outlier_count == 0:
        status = 'CLEAN'
    else:
        status = 'DIRTY'
    return filtered

def transform_coordinates(x):
    # Unused geometric transformation
    angle = math.radians(45)
    rotated_x = x * math.cos(angle)
    return int(rotated_x)

def generate_lookup():
    # Distractor: builds unused mapping
    keys = ['A', 'B', 'C']
    values = [transform_coordinates(i) for i in range(3)]
    return dict(zip(keys, values))

def normalize_readings(sensor_data):
    normalized = []
    base = sensor_data[0][0] if sensor_data else 1
    for val, ts in sensor_data:
        norm_val = val / base
        normalized.append((norm_val, ts))
    return normalized

def calculate_entropy(data_list):
    # Red herring function: looks important but not used in main flow
    total = sum(d[0] for d in data_list)
    probs = [d[0]/total for d in data_list]
    entropy = -sum(p * math.log2(p) for p in probs if p > 0)
    return round(entropy, 4)

def aggregate_metrics(normalized):
    metrics = {}
    values = [x[0] for x in normalized]
    metrics['mean'] = sum(values) / len(values)
    metrics['peak'] = max(values)
    metrics['stability'] = metrics['mean'] / metrics['peak']
    
    # Bit manipulation for checksum (partially relevant)
    checksum = 0
    for v in values:
        iv = int(v * 10) & 0xFF
        checksum ^= iv
    metrics['checksum'] = checksum
    
    # Unused statistical measures
    variance = sum((x - metrics['mean'])**2 for x in values) / len(values)
    metrics['z_score_peak'] = (metrics['peak'] - metrics['mean']) / (variance**0.5) if variance > 0 else 0
    
    return metrics

# Higher-order function with lambda - Python feature
threshold_func = lambda x: x > 1.5

# Set operations - Python feature
reference_set = {1.0, 1.25, 1.5, 2.0}

processed_data = []
def analyze_readings(data, threshold_strategy):
    global processed_data
    
    # Unpack and filter
    readings = [x[0] for x in data]
    timestamp_range = (data[0][1], data[-1][1])
    
    # Create auxiliary set (distractor)
    nearby_values = {r + delta for r in readings for delta in [-0.1, 0, 0.1]}
    overlap = reference_set & nearby_values  # Interesting but unused
    
    # Main processing branch
    high_readings = list(filter(threshold_strategy, readings))
    
    # Complex conditional logic with nesting depth 4
    if len(high_readings) > 0:
        if len(high_readings) % 2 == 0:
            factor = 1.75
            if high_readings[0] > 1.75:
                if sum(high_readings) > 5.0:
                    factor = 2.1
                else:
                    factor = 1.9
            adjustment = math.log(factor)
        else:
            adjustment = 0.5
        score = len(high_readings) * adjustment * 100
    else:
        score = 50
    
    # Data transformation chain
    processed_data = [(r * 1.1, t) for r, t in data]
    
    # Decoy computation
    shadow_score = 0
    for i, r in enumerate(readings):
        if i % 3 == 0:
            shadow_score += r * 0.25
    
    # Final diagnostic depends on multiple paths
    final_diagnostic = int(score + len(overlap) * 10)
    
    # Early return red herring
    if final_diagnostic < 0:
        return -999  # Never reached
    
    return final_diagnostic

# Execution sequence
raw = collect_sensor_data()
denoised = filter_outliers(raw)
normalized_batch = normalize_readings(denoised)
metrics_summary = aggregate_metrics(normalized_batch)
# calculate_entropy(normalized_batch)  # Commented out dead call
lookup_table = generate_lookup()  # Unused structure
final_diagnostic = analyze_readings(normalized_batch, threshold_func)
print(f"Result: {final_diagnostic}")