import math

# Simulated sensor data processing with diagnostic analysis
def collect_samples(size):
    return [i * 0.5 + (2 ** (i % 4)) for i in range(size)]

def filter_noise(data, limit=100):
    # Irrelevant filtering path (not used)
    return [x for x in data if abs(x) < limit]

def transform_scale(value, mode='linear'):
    if mode == 'log':
        return math.log(abs(value) + 1)
    else:
        return value * 1.5

def accumulate_trend(data):
    trend = 0
    for val in data:
        trend += transform_scale(val, 'linear') % 7
    return trend

def compute_entropy(data):
    # Dead function - looks important but unused
    total = sum(abs(x) for x in data)
    if total == 0:
        return 0
    return -sum((abs(x)/total) * math.log(abs(x)/total + 1e-9) for x in data)

def extract_features(raw):
    # Real feature extraction happens here
    magnitude = sum(abs(x) for x in raw)
    peak = max(abs(x) for x in raw)
    count = len(raw)
    avg = magnitude / count if count else 0
    
    # Distractor computations
    dummy_score = (peak * 3.14) % 100
    temp_buffer = [math.sin(x/10) for x in raw[:10]]
    checksum = sum(temp_buffer) * 1000  # Unused
    
    return {
        'mag': magnitude,
        'pk': peak,
        'avg': avg,
        'len': count,
        'dummy': dummy_score  # Red herring
    }

def evaluate_stability(features):
    base = features['avg']
    penalty = 0
    if features['pk'] > 50:
        penalty += 15
    if features['len'] < 30:
        penalty += 10
    return base - penalty

def generate_baseline(n):
    # Misleading baseline generation
    return [math.cos(i * 0.1) * 5 for i in range(n)]

def process_chunk(chunk_data):
    # Nested transformation with conditional expression
    adjusted = [x * (1.1 if x > 10 else 0.9) for x in chunk_data]
    enhanced = [transform_scale(y, 'linear') for y in adjusted]
    return sum(enhanced) % 1000

def analyze_signal(diag_data, thresh):
    # Core logic embedded in complex structure
    if not diag_data:
        return 0
    
    # Key signal metric
    signal_power = diag_data.get('mag', 0)
    noise_floor = diag_data.get('avg', 0) * 2
    signal_to_noise = (signal_power / noise_floor) if noise_floor > 0 else 0
    
    # Secondary checks with distractors
    quality_flag = 1 if diag_data.get('pk') > 20 else 0
    
    # Hidden key calculation: depends only on mag and avg
    primary_metric = int(diag_data['mag']) + int(diag_data['avg'] * 2)
    
    # Decoy metrics
    synthetic_index = (quality_flag * 100) + (compute_entropy([1,2,3]) * 10)  # compute_entropy called with fake data
    stability_score = evaluate_stability(diag_data)
    
    # Conditional expression determining final output
    result = primary_metric if signal_to_noise >= thresh else -1
    
    # Unused debugging trace
    debug_dump = {
        'input_len': len(str(diag_data)),
        'timestamp': 1678886400,
        'version': '2.1a'
    }
    
    return result

# Main execution flow
raw_sensor_stream = collect_samples(64)

# Irrelevant preprocessing branch
baseline_ref = generate_baseline(len(raw_sensor_stream))
comparison_diff = [a - b for a, b in zip(raw_sensor_stream, baseline_ref)]

# Real processing begins
processed_data = extract_features(raw_sensor_stream)

# Distractor: accumulation that isn't used later
historical_trend = accumulate_trend(comparison_diff)
archive_checksum = process_chunk(comparison_diff)  # Dead end

# Threshold computation with red herring
dynamic_ceiling = max(raw_sensor_stream)
temp_adjustment = math.floor(dynamic_ceiling / 10)
threshold = 3.0 if temp_adjustment > 2 else 2.5  # Actual value used

# Critical statement
final_diagnostic = analyze_signal(processed_data, threshold)

print(f"Result: {final_diagnostic}")