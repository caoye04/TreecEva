import math

# Irrelevant helper function (dead code path)
def legacy_transform(x):
    return (x ** 2 + 3 * x + 1) % 7

# Misleading computation with decoy results
decoynum = 56
for i in range(3):
    decoynum = (decoynum * 7) % 101

# Unused data structure - red herring
dummy_cache = {f'key_{i}': (i**3 - 2*i + 1) for i in range(10)}

# Actual relevant constants
PRIME_MODULUS = 997
SHIFT_OFFSET = 13

# Simulated sensor buffer with initial values
data_buffer = [18, 24, 67, 83, 41, 92]

# Configuration map with multiple distracting keys
config_map = {
    'version': '2.1.9',
    'debug_mode': False,
    'threshold': 45.0,
    'scaling_factor': 2.5,
    'padding_value': 999,  # unused
    'max_retries': 3,       # unused
    'active_filters': ['A', 'C'],
    'mask_sequence': [1, 1, 0, 1, 0],  # used in irrelevant branch
    'transform_key': 7      # critical for final step
}

# Decoy loop with no side effects on main logic
intermediate = 0
for _ in range(5):
    intermediate += sum([i * 2 for i in range(7)]) // 3

# Auxiliary function that appears important but is never called
def validate_checksum(arr):
    total = 0
    for val in arr:
        total = (total * 31 + val) % PRIME_MODULUS
    return total > 500

# Another unused utility
last_result = None
def store_final(val):
    global last_result
    last_result = val * 1.5  # misleading transformation

# Core processing function with embedded logic and distractors
def process_pipeline(data, config):
    result = 0
    scaling = config['scaling_factor']
    key = config['transform_key']
    threshold = config['threshold']

    # Bit manipulation mix - only some steps matter
    masked_values = []
    for val in data:
        temp = val ^ key                    # meaningful
        temp = (temp << 2) & 255            # meaningful
        temp = temp | SHIFT_OFFSET         # meaningful
        if temp > threshold * 2:           # conditional filtering (relevant)
            masked_values.append(temp)
        else:
            masked_values.append(temp // 2)  # alternate path (some used)

    # Dictionary-based state tracking (core concept)
    stats = {
        'sum_raw': 0,
        'count_above': 0,
        'processed_entries': [],
        'dummy_metric_x': len(masked_values) * 3  # irrelevant
    }

    accumulator = 0
    index = 0
    for v in masked_values:
        if index % 2 == 0:
            transformed = int((v * scaling) % PRIME_MODULUS)
        else:
            # This branch looks complex but contributes linearly
            shifted = v >> 1
            adjusted = (shifted + index) % 100
            transformed = (adjusted ** 2) % PRIME_MODULUS

        accumulator = (accumulator + transformed) % PRIME_MODULUS
        stats['processed_entries'].append(transformed)

        if v > 100:
            stats['count_above'] += 1  # rarely triggered

        index += 1

    # Critical modular arithmetic chain
    final_step = accumulator * 2
    final_step = (final_step + 5) % PRIME_MODULUS
    final_step = (final_step * config['transform_key']) % PRIME_MODULUS  # depends on config

    # Red herring: unused conditional block
    if len(stats['processed_entries']) > 10:
        final_step = (final_step + 100) % PRIME_MODULUS

    # Final non-linear adjustment using dictionary lookup simulation
    lookup_sim = {i: (i * i + i) % 50 for i in range(20)}
    adjustment_key = (final_step % 19) + 1
    adjustment = lookup_sim.get(adjustment_key, 0)

    result = final_step + adjustment

    # Dead assignment - does not affect output
    stats['sum_raw'] = sum(data) + result // 10

    return result

# Execution point of interest
final_output = process_pipeline(data_buffer, config_map)

# Print required output
print(f"Target result: {final_output}")