import math

# Simulated system metrics for performance analysis
timestamps = [1623456000, 1623456060, 1623456120, 1623456180]
raw_data_points = [45, 67, 89, 52, 73, 91, 48, 64]

# Irrelevant auxiliary data (distractor)
user_preferences = {
    'theme': 'dark',
    'auto_save': True,
    'notifications': False,
    'retry_limit': 3
}

# Benchmark configuration with red herring parameters
benchmark_config = {
    'threshold': 60,
    'weight_a': 0.4,
    'weight_b': 0.6,
    'decay_factor': 0.95,
    'padding_offset': 17,
    'dummy_flag': True,
    'version': '2.1.0'
}

# Preprocess raw data with irrelevant transformations (some are distractors)
processed_values = []
for val in raw_data_points:
    if val > 50:
        processed_values.append(int(math.sqrt(val) * 3))
    else:
        processed_values.append(val + 10)

# Decoy function that is never called (dead code path)
def deprecated_analysis(data):
    return sum(x ** 0.5 for x in data if x % 2 == 0)

# Auxiliary transformation with partial relevance
shifted_data = [v ^ 15 for v in processed_values]  # Bitwise XOR (partial relevance)

# Log creation with mixed content
metrics_log = {}
for i, ts in enumerate(timestamps):
    key = f"entry_{ts}"
    chunk = shifted_data[i*2:(i+1)*2]
    avg = sum(chunk) / len(chunk)
    status = 'pass' if avg > benchmark_config['threshold'] else 'fail'
    metrics_log[key] = {
        'average': avg,
        'status': status,
        'raw_count': len(chunk),
        'checksum': chunk[0] * 2 + chunk[1]  # unused field (distractor)
    }

# Secondary irrelevant computation (misleading intermediate result)
total_weight = 0
for k in benchmark_config:
    if 'weight_' in k:
        total_weight += benchmark_config[k]
adjustment_factor = total_weight * 100  # looks important but unused later

# Core logic buried in distractions
def apply_decay(value, steps):
    for _ in range(steps):
        value *= benchmark_config['decay_factor']
    return value

def evaluate_performance(log, config):
    base_scores = []
    for entry in log.values():
        raw_avg = entry['average']
        if entry['status'] == 'pass':
            # Apply decay based on dummy_flag which is always True (red herring)
            steps = 2 if config.get('dummy_flag') else 1
            adjusted = apply_decay(raw_avg, steps)
            base_scores.append(adjusted)
    # Real calculation hidden among noise
    composite = sum(base_scores) * config['weight_a']
    
    # Spurious alternate path (never taken due to data)
    fallback = math.log(len(log) + 1) * 100 if len(base_scores) == 0 else 0
    
    # Final score depends only on composite
    result = int(composite + 0.5)  # round to nearest integer
    
    # Additional decoy operations (no effect)
    result ^= 255
    result += benchmark_config['padding_offset']
    result %= 1000000
    return result

# Critical statement
final_score = evaluate_performance(metrics_log, benchmark_config)

# Print result as required
print(f"Target result: {final_score}")