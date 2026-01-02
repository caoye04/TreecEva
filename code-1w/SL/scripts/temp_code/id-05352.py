import math

# Irrelevant helper function (dead code path)
def unused_calculate_entropy(values):
    return sum(-p * math.log2(p) for p in values if p > 0)

# Distractor: Unused transformation chain
def transform_x(x):
    return (x ** 2 + 3 * x + 1) % 107

def transform_y(y):
    return abs(y * 4 - 12) // 3

# Real processing components
def filter_valid(entries):
    return [e for e in entries if e.get('active') and e['value'] > 10]

def compute_weighted_sum(items, weights):
    return sum(item['value'] * weights[i] for i, item in enumerate(items))

def apply_threshold(val, thresh=50):
    return int(val * 1.5) if val > thresh else int(val * 0.8)

# Higher-order function with lambda - relevant
aggregator = lambda func, data: func(data)

# Misleading data structure (decoy)
legacy_system_state = {
    'version': '2.1',
    'checksum': 98765,
    'last_updated': '2021-08-01',
    'deprecated_flag': True
}

# Another red herring: Simulated cache with no usage
cache_lookup = {}
for i in range(15):
    cache_lookup[i] = (i * i + 3 * i + 7) % 101

# Main configuration with mixed relevant/irrelevant fields
config = {
    'mode': 'production',
    'debug_trace': False,
    'data_schema': 'v3',
    'scaling_factor': 2.5,  # Used later
    'max_iterations': 1000,
    'use_enhanced_logic': True  # Critical flag
}

# Input data with noise entries
raw_data = [
    {'id': 1, 'value': 15, 'active': True, 'meta': {'temp': 23}},
    {'id': 2, 'value': 8, 'active': True, 'meta': {'temp': 19}},
    {'id': 3, 'value': 22, 'active': True, 'meta': {'temp': 25}},
    {'id': 4, 'value': 5, 'active': False, 'meta': {'temp': 17}},
    {'id': 5, 'value': 30, 'active': True, 'meta': {'temp': 28}}
]

# Decoy transformation pipeline
pipeline_A = [
    lambda x: x + 100,
    lambda x: x // 2,
    lambda x: x + x % 7
]

# Actual logic hidden among distractions
data = filter_valid(raw_data)

weights = [0.1, 0.3, 0.4]  # Matches filtered data length

base_result = compute_weighted_sum(data, weights)

adjusted = apply_threshold(base_result, thresh=40)

# Conditional branching with non-trivial control flow
if config['use_enhanced_logic']:
    temp_val = adjusted * config['scaling_factor']
    if temp_val < 100:
        temp_val = math.sqrt(temp_val) * 8
    else:
        temp_val = math.floor(temp_val * 0.9)
    
    # Bit manipulation distraction (partially irrelevant)
    bit_fiddle = (int(temp_val) ^ 255) & 1023
    temp_val += bit_fiddle / 100
    
    # Dictionary-based remapping (only one case hits)
    multiplier_map = {0: 1.1, 1: 1.2, 2: 1.3}
    key = min(int(temp_val) % 3, 2)
    temp_val *= multiplier_map.get(key, 1.0)
    
    secondary_adjust = 0
    for i in range(1, 6):
        if i % 2 == 0:
            secondary_adjust += math.sin(math.pi * i / 4)
    temp_val += secondary_adjust  # Adds ~0.414

    final_output = int(round(temp_val))
else:
    # Dead fallback branch
    final_output = sum(len(cache_lookup[k]) for k in cache_lookup)  # Would fail

# Unused nested dictionary traversal
temporary_snapshot = {
    'layer1': {
        'layer2': {
            'layer3': {
                'checksum': 12345,
                'status': 'archived'
            }
        }
    }
}

# Output target result
print(f"Target result: {final_output}")