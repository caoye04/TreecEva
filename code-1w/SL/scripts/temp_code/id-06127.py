def analyze_metrics(values):
    total = 0
    count = 0
    for v in values:
        if v > 0:
            total += v ** 0.5
            count += 1
    return total / count if count else 0

# Irrelevant helper function (dead code path)
def unused_normalizer(x):
    return x / (1 + abs(x))

# Misleading intermediate computation
temp_offset = sum([i * 2 for i in range(5)]) - 10  # evaluates to 10, not used later

# Data preprocessing with distractor keys
data_map = {
    'readings': [16, 25, 36, 49],
    'weights': [0.1, 0.3, 0.4, 0.2],
    'flags': [True, False, True, False],
    'aux_data': [-999, 123, -456]  # clearly irrelevant
}

# Secondary distraction: complex-looking but unused calculation
aggregate_noise = 0
for k in data_map:
    if 'a' in k:
        aggregate_noise += len(k) * 10

# Core logic hidden among noise
def compute_weighted_average(readings, weights):
    return sum(r * w for r, w in zip(readings, weights))

# Logical operation chain with short-circuiting distraction
primary_valid = len(data_map['readings']) > 0
secondary_valid = data_map.get('config', {}).get('active', False)  # always False

is_processing_enabled = primary_valid and secondary_valid or (not secondary_valid)  # resolves to True

# Conditional execution that looks consequential but isn't
calibration_factor = 1.0
if 'calibration' in data_map:
    calibration_factor = data_map['calibration']
else:
    temp_result = [x for x in range(len(data_map['readings'])) if x % 2 == 0]
    calibration_factor = len(temp_result)  # would be 2, but not actually used

# Real work begins here — actual answer depends only on this path
def calculate_final_score(data):
    readings = data['readings']
    weights = data['weights']
    
    # Step 1: Compute geometric influence (sqrt of each reading)
    adjusted_readings = [r ** 0.5 for r in readings]
    
    # Step 2: Apply weight-based modulation
    modulated = [ar * w for ar, w in zip(adjusted_readings, weights)]
    
    # Step 3: Aggregate final score
    base_score = sum(modulated)
    
    # Step 4: Apply fixed bonus condition (non-short-circuited logic)
    all_flags_true = all(data['flags'])
    any_flag_true = any(data['flags'])
    bonus_eligible = not all_flags_true and any_flag_true  # True
    
    bonus = 5.0 if bonus_eligible else 0.0
    
    return base_score + bonus

# Key statement
final_score = calculate_final_score(data_map)
print(f"Result: {final_score}")