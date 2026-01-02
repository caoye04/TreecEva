def evaluate_efficiency(index, score_map):
    return sum([v ** 0.5 for k, v in score_map.items() if k % index == 0])

# Irrelevant helper function (decoy)
def validate_allocation(config):
    total = 0
    for k, v in config.items():
        if isinstance(v, dict):
            total += len(v) * k
    return total > 5

# Unused data structure (red herring)
test_config = {
    1: {'mode': 'A', 'active': True},
    2: {'mode': 'B', 'active': False},
    3: {'mode': 'C', 'active': True}
}

# Simulate sensor readings (distractor block)
sensor_data = [12, 15, 9, 22, 11]
avg_sensor = sum(sensor_data) / len(sensor_data)
sensor_variance = sum((x - avg_sensor) ** 2 for x in sensor_data) / len(sensor_data)

# Core logic disguised among distractions
resource_map = {
    'A': [6, 8, 10],
    'B': [3, 7],
    'C': [12],
    'D': [4, 5, 6, 7]
}

# Secondary map used in computation
efficiency_scale = {0: 1.0, 1: 0.9, 2: 0.85, 3: 0.75, 4: 0.6}

def transform_resources(data):
    result = {}
    for key, values in data.items():
        # Meaningful transformation
        processed = [x for x in values if x % 2 == 0]
        if len(processed) > 0:
            result[key] = sum(processed) / len(processed)
        else:
            result[key] = 0
    return result

# Another decoy function with misleading name
def predict_failure_risk(data_dict):
    risk_score = 0
    for k, v in data_dict.items():
        if 'error' in k.lower():
            risk_score += v * 2
    return risk_score  # never actually used

# Unused intermediate calculation
baseline_offset = 0.15 * sum(len(lst) for lst in resource_map.values())

# Real processing begins here
normalized = transform_resources(resource_map)

# Mapping keys to indices for later use
key_index = {k: i for i, k in enumerate(resource_map.keys())}

# Dummy loop with no effect on final result
for _ in range(2):
    temp_val = 0
    for v in normalized.values():
        temp_val += v * 0.1

# Score map used in evaluate_efficiency (critical)
score_map = {i+1: len(items)*2 for i, items in enumerate(resource_map.values())}

# This call is unused but looks important (dead path)
evaluate_efficiency(2, score_map)

# Actual core logic hidden in plain sight
def calculate_optimal_distribution(resources):
    transformed = transform_resources(resources)
    total_units = 0
    efficiency_factor = 1.0
    
    for idx, (key, val) in enumerate(transformed.items()):
        total_units += val
        # Use score_map from outer scope
        scale_key = score_map.get(idx + 1, 1)
        if scale_key in efficiency_scale:
            efficiency_factor *= efficiency_scale[scale_key]
        
        # Extra distraction inside critical function
        if val > 7 and key in ['A', 'D']:
            efficiency_factor *= 0.95  # minor penalty
    
    # Additional logic that seems complex but is deterministic
    adjustment = 1.0
    if len(resources) >= 4:
        adjustment = 0.98
    
    # Final computation
    raw_yield = total_units * efficiency_factor * adjustment
    
    # Red herring: irrelevant rounding attempt
    _ = round(raw_yield + 0.001, 4)
    
    return raw_yield

# Key execution point
final_yield = calculate_optimal_distribution(resource_map)

print(f"Result: {final_yield}")