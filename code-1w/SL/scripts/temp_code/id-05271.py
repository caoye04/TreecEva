def normalize_values(raw_list):
    min_val = min(raw_list)
    max_val = max(raw_list)
    range_val = max_val - min_val or 1
    return [(x - min_val) / range_val for x in raw_list]

status_map = {'critical': 0, 'warning': 1, 'info': 2, 'debug': 3}

raw_metrics = [15, 30, 45, 60, 75]
adjusted_metrics = [x * 1.5 for x in raw_metrics if x > 20]
dummy_offset = sum([i**2 for i in range(3)])  # Irrelevant computation

normalized = normalize_values(adjusted_metrics)

stats = {}
stats['average'] = sum(normalized) / len(normalized)
stats['variance'] = sum((x - stats['average'])**2 for x in normalized) / len(normalized)
stats['threshold'] = 0.5

# Simulate data tagging
tagged_data = []
for val in normalized:
    if val > stats['threshold']:
        tagged_data.append({'value': val, 'tag': 'high'})
    elif val > stats['average']:
        tagged_data.append({'value': val, 'tag': 'medium'})
    else:
        tagged_data.append({'value': val, 'tag': 'low'})

# Misleading filter branch (dead logic path)
filter_mode = 'exclude_low'
temp_filtered = []
if filter_mode == 'exclude_debug':
    temp_filtered = [x for x in tagged_data if x['tag'] != 'debug']  # Never executed
else:
    dummy_counter = 0
    for item in tagged_data:
        dummy_counter += 1  # Distractor: counting without effect

processed_data = [x['value'] for x in tagged_data if x['tag'] in ['high', 'medium']]

# Auxiliary function with red herring parameters
def calculate_rating(data, weight_factor=0.8, debug_mode=False):
    base_rating = sum(data) * 100
    penalty = 0
    for i, val in enumerate(data):
        if val < 0.4:
            penalty += 10
        if i % 2 == 0:
            penalty += 2  # Extra penalty on even indices
    # Complex but irrelevant dictionary transformation
    lookup = {i: v * 1.1 for i, v in enumerate(data)}
    adjustment = len(lookup) * 0.5 if len(lookup) > 2 else 0
    return base_rating - penalty + adjustment

intermediate_result = calculate_rating(processed_data, debug_mode=True)

# Final redundant normalization step (does not affect outcome)
scaling_constant = 1.0
if len(processed_data) >= 3:
    scaling_constant *= 1.05  # Not actually applied

final_score = calculate_rating(processed_data)
print(f"Result: {final_score}")