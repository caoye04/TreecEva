def transform_value(x, mode='basic'):
    if mode == 'advanced':
        return (x ** 2 + 3 * x + 1) % 97
    elif mode == 'experimental':
        return x ^ (x >> 4)
    else:
        return (x * 7) % 53

# Irrelevant helper (distractor)
def unused_helper(data):
    return sum(d ** 2 for d in data if d % 3 == 0)

# Decoy function that looks important but isn't called
def decrypt_sequence(seq):
    result = 0
    for i, val in enumerate(seq):
        result += val * (i + 1)
    return result % 1000

# Another decoy — simulates complex logic
mock_registry = {}
for i in range(10):
    mock_registry[f'key_{i}'] = (i * i * (i + 1)) % 89

# Real transformation pipeline
lambda_transform = lambda a, b: (a + b) * 2 if (a + b) % 2 == 0 else (a + b) // 2

config = {
    'threshold': 42,
    'mode': 'advanced',
    'scale': 3.5,
    'flags': [True, False, True],
    'weights': [0.5, 1.5, 2.0, 0.1]
}

# Misleading data initialization
shadow_data = [i * 3 + 2 for i in range(15) if i % 2 == 1]
data = [12, 19, 25, 34, 41]

# Dead code path — looks like it modifies data but doesn't
if len(data) > 10:
    data = [x * 2 for x in data]
elif config['threshold'] < 40:
    data = [x + 5 for x in data]
else:
    temp_buffer = []
    for x in data:
        temp_buffer.append(x % 7)
    # Result unused

# Simulated preprocessing (some steps are red herrings)
processed = []
for val in data:
    if val < config['threshold']:
        transformed = transform_value(val, mode=config['mode'])
        processed.append(transformed)
    else:
        # This branch is taken only once
        backup_val = (val + 7) % 61
        processed.append(backup_val)

# Linear search with side computation (only index matters)
search_target = 41
found_index = -1
for idx, val in enumerate(data):
    if val == search_target:
        found_index = idx
        break

# Dummy dictionary operations to distract
stats = {
    'count': len(data),
    'sum': sum(data),
    'max_prime': max([p for p in data if all(p % i != 0 for i in range(2, int(p**0.5)+1)) or p == 2]),
    'flag_sum': sum(int(f) for f in config['flags'])
}

# Real pipeline logic
ext_weight = config['weights'][found_index % len(config['weights'])]
intermediate = 0
for i, p_val in enumerate(processed):
    intermediate = lambda_transform(intermediate, p_val)

# Introduce bit manipulation as distraction
bit_fiddle = 0
for i in range(5):
    bit_fiddle ^= (intermediate >> i) & 1

# Core calculation uses stats and intermediate
core_base = stats['max_prime'] * ext_weight
aux_shift = transform_value(int(core_base), mode='basic')

# Final composition
final_output = (intermediate + aux_shift) % 100000

# Critical output print
print(f"Result: {final_output}")