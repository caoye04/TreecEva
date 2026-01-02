import math

# Simulated sensor data processing with red herrings and distractions
def legacy_normalize(x):
    # Obsolete function - never called
    return (x - min(x)) / (max(x) - min(x))

def deprecated_hash(data):
    # Dead code path - unused
    acc = 0
    for c in data:
        acc = (acc * 31 + ord(c)) % 10007
    return acc

def transform_signal(raw):
    # Actual relevant transformation
    shifted = [x << 1 for x in raw]  # Bit shift left by 1
    filtered = [x for x in shifted if x > 100]
    return [x ^ 255 for x in filtered]  # XOR with mask

def evaluate_stability(risk_score, threshold=75):
    # Distractor logic with misleading intermediate values
    if risk_score < threshold:
        status = 'stable'
        correction_factor = 0.9
    else:
        status = 'unstable'
        correction_factor = 1.2  # Never actually used
    confidence = (100 - risk_score) / 100
    return {'status': status, 'confidence': confidence}

# Irrelevant data structures
user_preferences = {
    'theme': 'dark',
    'language': 'fr',
    'notifications': True,
    'timeout': 300
}

system_logs = [
    {'timestamp': '2023-01-01T10:00:00Z', 'event': 'boot', 'level': 'INFO'},
    {'timestamp': '2023-01-01T10:05:00Z', 'event': 'poll', 'level': 'DEBUG'}
]

# Real input data
sensor_readings = [45, 67, 89, 105, 120]

# Step 1: Transform signal using bit manipulation
transformed_data = transform_signal(sensor_readings)

# Step 2: Apply conditional filtering based on length
if len(transformed_data) >= 3:
    subset = transformed_data[1:]
else:
    subset = [0] * 3

# Step 3: Compute derived metrics
magnitude = sum([math.ceil(x / 10) for x in subset])
divergence = abs(subset[0] - subset[-1])

# Step 4: Simulate configuration with decoy fields
config = {
    'version': '2.1.0',
    'debug_mode': False,
    'data_format': 'hex',
    'retries': 3,
    'threshold_primary': 200,
    'threshold_backup': None
}

# Step 5: Core metric aggregation using lambda and set operations
core_values = list(set([x & 127 for x in subset]))  # Bitwise AND to mask
weight_fn = lambda v: v * 1.05 if v > 100 else v * 0.95
weighted_sum = sum(weight_fn(v) for v in core_values)

# Step 6: Conditional adjustment
if magnitude > 50:
    magnitude -= 10

# Step 7: String-based flag processing (distractor)
flags = ['CALIBRATED', 'VERIFIED']
flag_summary = '; '.join(flags).lower()
summary_length = len(flag_summary.replace(';', '').replace(' ', ''))

# Step 8: Main processing function
def process_metrics(data, cfg):
    base = sum(data)
    offset = len(data) * 15
    adjustment = 0
    
    # Nested logic with red herring branches
    if cfg['debug_mode']:
        adjustment += 100  # Not triggered
    elif 'format' in cfg and cfg['data_format'] == 'bin':
        adjustment -= 50   # Not applicable
    else:
        adjustment += 25   # This branch taken
    
    # Complex but relevant calculation
    temp_result = (base + offset + adjustment) * 0.85
    
    # Final nonlinear correction
    final_value = int(math.floor(temp_result))
    
    # Decoy computation
    _ = [x ** 2 for x in range(5) if x % 2 == 0]  # Unused list comp
    
    return final_value

# Critical execution point
final_diagnostic = process_metrics(transformed_data, config)

# Output result as required
print(f"Result: {final_diagnostic}")