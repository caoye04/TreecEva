def preprocess_entries(entries):
    cleaned = {}
    temp_sum = 0
    for k, v in entries.items():
        if len(k) % 2 == 0 and v > 0:
            cleaned[k.upper()] = v * 2
            temp_sum += v
        else:
            cleaned[k.lower()] = v
    return cleaned

# Irrelevant helper that's defined but barely used
def validate_key(key):
    return isinstance(key, str) and key.isalpha()

# Data transformation with distractors
raw_data = {'alpha': 5, 'beta': -3, 'gamma': 8, 'delta': 12}
filtered_data = {k: v for k, v in raw_data.items() if v != -3}  # filters out beta

processed = preprocess_entries(filtered_data)

# Misleading intermediate calculations
offset = sum([v for v in raw_data.values() if v > 0]) - 10  # irrelevant adjustment
shift = len(processed.keys()) * 2  # used later, but not critical

# Simulate feature weights (some are unused)
weights = {
    'FACTOR_X': 1.5,
    'FACTOR_Y': 0.8,
    'FACTOR_Z': 2.0  # never actually used
}

scaling_factor = weights['FACTOR_X'] if shift > 5 else weights['FACTOR_Y']

# Aggregation with red herring variables
aggregate = 0
max_val = float('-inf')
for val in processed.values():
    if val > max_val:
        max_val = val
    aggregate += val

# Dead code path - never executed
if False:
    aggregate *= 0.5

# Auxiliary structure - looks important but only minor role
flags = set()
for k in processed:
    if 'A' in k:
        flags.add('HIGH')
    else:
        flags.add('LOW')

bonus = 10 if 'HIGH' in flags else 5

# Core computation buried in noise
def calculate_final_score(data_map):
    base = sum(data_map.values())
    penalty = 0
    for v in data_map.values():
        if v % 4 == 0:
            penalty += 2
    return int((base - penalty) * scaling_factor + bonus)

# Key statement
final_score = calculate_final_score(processed)

print(f"Result: {final_score}")