import math

# System health monitoring simulation with red herrings
def monitor_system_load(base_load, temperature):
    if temperature > 75:
        return base_load * 1.8
    elif temperature > 60:
        return base_load * 1.4
    else:
        return base_load * 1.1

# Irrelevant audio processing function (dead code path)
def process_audio_sample(sample, rate=44100):
    fft_size = 1024
    windowed = [sample[i] * 0.5 for i in range(len(sample))]
    return sum(windowed) / len(windowed)

# Unused network latency simulator
def simulate_latency(packets, jitter_factor):
    delays = []
    for p in packets:
        delay = (p % 17) * jitter_factor
        if delay > 100:
            delays.append(100)
        else:
            delays.append(delay)
    return delays

# Core diagnostic engine with distractors
def generate_diagnostics(node_id, readings, thresholds, mode='advanced'):
    diagnostics = {}
    temp_offset = 0
    
    # Real computation embedded in noise
    for i, val in enumerate(readings):
        key = f"sensor_{i}"
        diagnostics[key] = {
            'raw': val,
            'threshold': thresholds.get(key, 50),
            'exceeded': val > thresholds.get(key, 50),
            'flag': (val % 7) > 3
        }
        
        if val > 80:
            temp_offset += 2
        elif val > 60:
            temp_offset += 1
    
    # Distractor: unused image resolution map
    resolutions = {
        'low': (640, 480),
        'medium': (1280, 720),
        'high': (1920, 1080),
        'ultra': (3840, 2160)
    }
    
    # Another red herring: video frame counter
    frame_count = 0
    for res in resolutions.values():
        frame_count += res[0] // 320
    
    diagnostics['meta'] = {
        'node': node_id,
        'offset': temp_offset,
        'checksum': sum([v['raw'] for v in diagnostics.values() if isinstance(v, dict)]) % 100
    }
    
    return diagnostics

# Weighting algorithm mixed with irrelevant logic
def calculate_weights(fail_counts, priority_map):
    weights = {}
    total_failures = sum(fail_counts)
    
    # Real weight calculation
    for sensor, base_prio in priority_map.items():
        adjustment = 1.0
        if total_failures > 5:
            adjustment = 1.5
        weights[sensor] = base_prio * adjustment
    
    # Irrelevant timezone offset calculations
    timezones = ['UTC', 'EST', 'PST', 'CET', 'IST']
    tz_offsets = {tz: (i * -3) % 12 for i, tz in enumerate(timezones)}
    
    # Dummy compression simulation
    def compress_data_chunk(chunk_size):
        level = 0
        while chunk_size > 1024:
            chunk_size /= 2.1
            level += 1
        return level
    
    _ = compress_data_chunk(8192)
    
    return weights

# Main aggregation with critical logic buried in noise
def aggregate_metrics(diagnostics, weights):
    # Extract relevant sensor data
    valid_sensors = [k for k in diagnostics.keys() if k.startswith('sensor_')]
    
    # Real metric accumulation
    weighted_sum = 0.0
    weight_total = 0.0
    
    for sensor in valid_sensors:
        entry = diagnostics[sensor]
        raw_val = entry['raw']
        threshold = entry['threshold']
        exceeded = entry['exceeded']
        
        # Actual contribution logic
        base_score = raw_val / threshold if threshold != 0 else 0
        if exceeded:
            base_score *= 1.7
        
        sensor_weight = weights.get(sensor, 1.0)
        weighted_sum += base_score * sensor_weight
        weight_total += sensor_weight
    
    # Normalization factor with decoy intermediate steps
    normalization_factor = 1.0
    if diagnostics['meta']['checksum'] > 50:
        normalization_factor = 0.9
    elif diagnostics['meta']['checksum'] < 20:
        normalization_factor = 1.1
    
    # Red herring: unused matrix operation
    matrix_a = [[i + j for j in range(4)] for i in range(4)]
    matrix_b = [[(i * j) % 3 for j in range(4)] for i in range(4)]
    matrix_product = [
        [sum(matrix_a[i][k] * matrix_b[k][j] for k in range(4))
         for j in range(4)]
        for i in range(4)
    ]
    
    # Decoy statistical analysis
    all_raw_values = [diagnostics[s]['raw'] for s in valid_sensors]
    mean_val = sum(all_raw_values) / len(all_raw_values)
    variance = sum((x - mean_val) ** 2 for x in all_raw_values) / len(all_raw_values)
    std_dev = math.sqrt(variance)
    
    # Final result with conditional scaling (actual answer path)
    raw_result = weighted_sum / weight_total if weight_total != 0 else 0
    final_score = raw_result * normalization_factor
    
    # Critical assignment
    final_diagnostic = int(round(final_score * 100))
    
    # Unused cryptographic hash simulation
    def simulate_hash(data_str):
        acc = 0
        for c in data_str:
            acc = (acc * 31 + ord(c)) % (10**8)
        return acc
    
    _ = simulate_hash(f"diagnostic_{final_diagnostic}")
    
    return final_diagnostic

# Execution flow with setup and call
if __name__ == "__main__":
    # Input data
    sensor_readings = [68, 72, 58, 85, 45, 92]
    
    # Threshold configuration (real inputs)
    limits = {
        'sensor_0': 60,
        'sensor_1': 65,
        'sensor_2': 55,
        'sensor_3': 80,
        'sensor_4': 50,
        'sensor_5': 90
    }
    
    # Priority levels (used in weighting)
    priorities = {
        'sensor_0': 1.2,
        'sensor_1': 1.5,
        'sensor_2': 1.0,
        'sensor_3': 1.8,
        'sensor_4': 0.9,
        'sensor_5': 2.0
    }
    
    # Failure history (influences weight adjustment)
    failure_history = [3, 1, 4, 2, 0, 5]
    
    # Generate real diagnostics
    diagnostics = generate_diagnostics("NODE_X9", sensor_readings, limits)
    
    # Calculate weights (some used, some not)
    weights = calculate_weights(failure_history, priorities)
    
    # Execute key statement
    final_diagnostic = aggregate_metrics(diagnostics, weights)
    
    # Print result
    print(f"Target result: {final_diagnostic}")