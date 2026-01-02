import math

# Irrelevant helper function (dead code path)
def unused_helper(x):
    return (x ** 2 + 3 * x + 1) % 7

# Misleading signal generator with decoy logic
def generate_noise(length):
    signal = []
    for i in range(length):
        if i % 5 == 0:
            signal.append((i * 0.7) ** 1.5)
        else:
            signal.append(math.sin(i) * math.cos(i / 2))
    return signal

# Unused transformation chain
def legacy_transform(data):
    return [d * 1.05 for d in data if d > 0.5]

# Real processing begins here
initial_config = {
    'threshold': 0.65,
    'gain': 1.8,
    'mode': 'adaptive',
    'history': [],
    'counter': 0
}

# Simulated sensor input (irrelevant values mixed with relevant ones)
sensor_feed = [
    0.12, 0.34, 0.56, 0.78, 0.89, 0.23, 0.45, 0.67, 0.77, 0.88
]

# Distractor: complex but unused filter bank
filter_bank = {}
for key in ['low', 'mid', 'high']:
    filter_bank[key] = []
    for j in range(10):
        filter_bank[key].append((j * len(key)) % 4)

# Actual data pipeline setup
current_state = {
    'buffer': [],
    'active_filters': 0,
    'stats': {
        'max_val': -1.0,
        'min_val': 1.0,
        'avg': 0.0
    }
}

# Populate buffer and compute stats (partially relevant)
running_sum = 0.0
valid_count = 0
for val in sensor_feed:
    if val >= initial_config['threshold']:
        current_state['buffer'].append(val)
        running_sum += val
        valid_count += 1
        if val > current_state['stats']['max_val']:
            current_state['stats']['max_val'] = val
        if val < current_state['stats']['min_val']:
            current_state['stats']['min_val'] = val

if valid_count > 0:
    current_state['stats']['avg'] = running_sum / valid_count

# Transform step with red herring operations
temp_offset = 0.11
transformed_data = []
for x in current_state['buffer']:
    # Complex-looking but deterministic transformation
    shifted = x + temp_offset
    scaled = shifted * initial_config['gain']
    # Apply non-linear correction only if above threshold (redundant check)
    if scaled > 0.7:
        corrected = scaled * (1.0 + 0.1 * math.sin(x))
    else:
        corrected = scaled
    transformed_data.append(round(corrected, 6))

# Additional irrelevant dictionary manipulation
diagnostic_log = {}
for idx, entry in enumerate(transformed_data):
    hex_key = f"entry_{idx:02x}"
    diagnostic_log[hex_key] = {
        'raw': entry,
        'flagged': entry > 1.5,
        'checksum': int(entry * 100) % 17
    }

# Real configuration used in final step
config = {
    'amplification': 2.5,
    'offset_correction': -0.35,
    'enable_enhancement': True
}

# Core recursive reducer (simple recursion with distractors)
def recursive_reduce(data_list, index=0, acc=0.0):
    if index >= len(data_list):
        return acc
    current_value = data_list[index]
    enhanced = current_value * 1.1 if config['enable_enhancement'] else current_value
    new_acc = acc + (enhanced + config['offset_correction'])
    return recursive_reduce(data_list, index + 1, new_acc)

# Secondary processing with case conversion red herring
processing_modes = ['NORMALIZE', 'AMPLIFY', 'FILTER']
mapped_actions = {}
for mode in processing_modes:
    lower_mode = mode.lower()
    action_code = sum([ord(c) for c in lower_mode]) % 5
    mapped_actions[mode] = action_code

# Actual signal processor
def process_signal(signal_data, settings):
    base_result = recursive_reduce(signal_data)
    amplified = base_result * settings['amplification']
    
    # Add artificial bias from misleading source
    fake_bias = 0.0
    for k in diagnostic_log:
        if '01' in k or '03' in k:
            fake_bias += diagnostic_log[k]['raw'] * 0.01  # negligible contribution
    
    final = amplified + fake_bias
    
    # Inject unused intermediate that looks important
    summary_report = {
        'input_size': len(signal_data),
        'total_drift': sum([abs(d - 1.0) for d in signal_data]),
        'peak_adjustment': max(signal_data) * 0.02
    }
    
    return round(final, 6)

# Execution point of interest
final_output = process_signal(transformed_data, config)
print(f"Target result: {final_output}")