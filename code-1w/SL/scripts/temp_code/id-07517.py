def analyze_signal(samples, threshold):
    magnitude = sum(abs(s) for s in samples)
    normalized = magnitude / len(samples) if samples else 0
    return normalized > threshold

# Irrelevant signal processing functions (dead code path)
def filter_noise(data):
    return [x for x in data if abs(x) > 0.1]

def compute_envelope(signal):
    return max(signal) - min(signal)

# Unused constants and decoy variables
time_slice = 0.025
sampling_rate = 44100
decoy_matrix = [[i ^ j for j in range(8)] for i in range(8)]
scaling_factor = 3.14159  # unused in logic

# Core diagnostic logic with distractors
def evaluate_system_health(sensor_data, config):
    baseline = config.get('baseline', 100)
    tolerance = config.get('tolerance', 0.15)
    critical_level = baseline * (1 + tolerance)

    # Distractor: irrelevant aggregation
    temp_aggr = sum(v ** 0.5 for v in sensor_data.values() if v > 0) / len(sensor_data)

    # Real logic path begins
    active_sensors = 0
    total_power = 0
    for k, v in sensor_data.items():
        if k.startswith('sensor_'):
            bit_status = (v ^ 15) & 7  # Bit manipulation red herring
            if v > critical_level:
                active_sensors += 1
            total_power += v

    efficiency_ratio = (total_power / (baseline * len(sensor_data))) if baseline else 0
    return active_sensors, efficiency_ratio

# Complex data transformation with conditional expressions
def transform_readings(raw_readings):
    processed = []
    for val in raw_readings:
        adjusted = val * 1.05 if val < 50 else (val * 0.97 if val < 100 else val * 0.92)
        processed.append(int(adjusted) + (val & 3))  # bitwise add-on, partially relevant
    return processed

# Main diagnostic engine
def process_metrics(metrics_dict, threshold=1.0):
    # Unrelated list comprehension distraction
    _ = [i * i for i in range(10) if i % 2 == 0]

    score_a = metrics_dict.get('score_a', 0)
    score_b = metrics_dict.get('score_b', 0)
    
    # Conditional expression mix
    base_score = score_a if score_a > threshold else (score_b * 1.5 if score_b > threshold * 0.8 else 0)

    # Irrelevant nested dictionary traversal
    aux_data = {
        'meta': {
            'version': '2.1',
            'nodes': [{'id': i, 'state': 'active'} for i in range(3)]
        }
    }

    # Real computation path
    adjustment = 0
    for k, v in metrics_dict.items():
        if 'flag' in k:
            adjustment += v ^ 5  # XOR operation with constant
    
    # Key logic step: final calculation
    intermediate = (base_score + adjustment) * 100
    final_value = int(intermediate) & 0xFFFF  # Clamp to 16-bit

    # Dead code branch — never executed due to logic
    if final_value < 0:
        fallback = sum(len(str(val)) for val in metrics_dict.values())
        final_value = fallback % 1000

    return final_value

# Setup input data with misleading entries
diagnostic_map = {
    'score_a': 42.5,
    'score_b': 38.2,
    'flag_critical': 12,
    'flag_backup': 7,
    'flag_legacy': 3,
    'temp_diagnostic': 999,  # distractor
    'unused_metric': 42.0
}

activation_threshold = 40.0

# Execute core logic
system_data = {'sensor_1': 110, 'sensor_2': 95, 'sensor_3': 130, 'sensor_aux': 45}
config_params = {'baseline': 100, 'tolerance': 0.2}

# Irrelevant preprocessing chain
raw_samples = [12, -7, 25, 18, -3, 41]
filtered_samples = transform_readings(raw_samples)
analyzed = analyze_signal(filtered_samples, 10)

# Critical execution point
final_diagnostic = process_metrics(diagnostic_map, activation_threshold)

print(f"Result: {final_diagnostic}")