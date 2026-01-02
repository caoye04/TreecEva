import itertools

# Sensor simulation and diagnostic analysis system
def generate_synthetic_signal(baseline, noise_factor, length):
    return [baseline + (i % 10) * noise_factor for i in range(length)]

# Irrelevant helper - dead code path
def deprecated_filter(data):
    return [x for x in data if x > 0]

# Unused transformation
def frequency_shift(signal, shift):
    return [(x * shift) % 100 for x in signal]

# Core processing pipeline
processed_signals = {}
signal_pool = []

# Simulate multiple sensor inputs
temperature_stream = generate_synthetic_signal(36.5, 0.3, 8)
pressure_stream = generate_synthetic_signal(101.3, 0.15, 8)
humidity_stream = generate_synthetic_signal(45.0, 0.5, 8)

# Misleading intermediate aggregation
aggregate_snapshot = {
    'temp_avg': sum(temperature_stream) / len(temperature_stream),
    'pressure_avg': sum(pressure_stream) / len(pressure_stream),
    'humidity_peak': max(humidity_stream),
    'phantom_index': 3.14159  # Red herring
}

# Real processing begins here
for idx, (t, p, h) in enumerate(itertools.zip_longest(temperature_stream, pressure_stream, humidity_stream)):
    if idx % 2 == 0:
        # Only process even-indexed readings
        normalized_t = (t - 36.5) * 10
        adjusted_p = (p - 100) * 0.5
        
        # Complex conditional logic with decoy branches
        if normalized_t > 5:
            status_flag = 2
        elif normalized_t > 2:
            status_flag = 1
        else:
            status_flag = 0
            
        # Distractor: unused computation branch
        if adjusted_p > 1.0:
            correction_matrix = [1.1, 0.9, 1.2]  # Never used
        elif adjusted_p < 0:
            recovery_sequence = list(itertools.accumulate([1, -1, 2]))  # Dead code

        # Critical data structure update
        key = f"sensor_{idx}"
        processed_signals[key] = {
            'reading': normalized_t + adjusted_p,
            'flag': status_flag,
            'source': 'primary',
            'meta_noise': h * 0.01 if h else 0  # Minor influence
        }

# Another red herring function
def calculate_theoretical_limit(x):
    return (x ** 2 + 5 * x + 3) // 1.7

# Unused accumulator
cumulative_bias = 0
for i in range(4):
    cumulative_bias += i * 0.1  # Irrelevant to final result

# Signal pool population - partially redundant
for k, v in processed_signals.items():
    signal_pool.append(v['reading'])

# Decoy statistical summary
decoys = {
    'mean_reading': sum(signal_pool) / len(signal_pool),
    'variance_proxy': sum((x - 3) ** 2 for x in signal_pool) / len(signal_pool),
    'magic_offset': 42
}

# Core diagnostic logic
threshold_map = {0: 1.0, 1: 2.5, 2: 4.0}
def analyze_readings(signals_dict):
    total_score = 0.0
    flag_count = {0: 0, 1: 0, 2: 0}
    
    for entry in signals_dict.values():
        reading_val = entry['reading']
        flag_type = entry['flag']
        flag_count[flag_type] += 1
        
        # Conditional branching with compound logic
        if flag_type == 2 and reading_val > 3.0:
            total_score += reading_val * 1.3
        elif flag_type == 1:
            total_score += reading_val * 0.8
        else:
            total_score += max(reading_val - 1.0, 0)
    
    # Final adjustment based on flag distribution
    if flag_count[2] >= 2:
        total_score *= 1.25
    elif flag_count[1] >= 3:
        total_score *= 0.9
    
    return total_score

# Execution point of interest
final_diagnostic = analyze_readings(processed_signals)

# Print required output
print(f"Target result: {final_diagnostic}")