def analyze_pattern(sequence):
    # Irrelevant helper function (dead code path)
    return sum(x ** 2 for x in sequence if x % 3 == 0)

# Distractor data structures
temp_log = {'errors': [1, 5, 9], 'warnings': (2, 4), 'status': 'nominal'}
system_state = {'mode': 'debug', 'priority': 3, 'active': False}

# Real input data disguised among noise
raw_metrics = [3, 7, 2, 8, 5, 6, 4]

# Decoy transformation chain
shadow_copy = [x * 1.5 for x in raw_metrics if x > 4]
dummy_agg = list(map(lambda x: x + 2 if x < 7 else x - 1, shadow_copy))

# Actual logic begins here — buried under distractions
weight_map = {i: w for i, w in enumerate([1.1, 0.9, 1.2, 0.8, 1.0, 1.3, 0.7])}

metric_data = {}
for idx, val in enumerate(raw_metrics):
    if idx % 2 == 0:
        metric_data[f"sensor_{idx}"] = val * weight_map[idx]
    else:
        metric_data[f"sensor_{idx}"] = val / weight_map[idx]

# Secondary transformation with red herring condition
adjusted_values = []
for k, v in metric_data.items():
    if 'sensor_2' in k or 'sensor_5' in k:
        adjusted_values.append(v * 1.1)
    elif 'sensor_1' in k:
        adjusted_values.append(v * 0.95)  # unused branch due to later override
    else:
        adjusted_values.append(v)

# Conditional override that seems significant but only affects one element
if system_state['active']:
    adjusted_values[0] *= 0.8
else:
    adjusted_values[2] += 1.5  # This executes and matters

# Key computation hidden in lambda and dictionary operation
transform_fn = lambda x: round(x ** 0.5, 4) if x > 5 else round(x * 0.4, 4)
applied_trans = {i: transform_fn(val) for i, val in enumerate(adjusted_values)}

# Accumulation with filtering
filtered_sum = 0
for i, v in applied_trans.items():
    if i not in [1, 4]:  # Skip indices 1 and 4
        filtered_sum += v

bonus_factor = 1
if len(applied_trans) > 5 and sum(raw_metrics) % 2 == 0:
    bonus_factor = 1.2
else:
    bonus_factor = 1.1  # This branch taken

# Final scoring logic
base_score = filtered_sum * bonus_factor
penalty = 0
for val in temp_log['errors']:
    penalty += val * 0.1  # Minor impact, looks important

final_score = base_score - penalty

# Print required output
Target result: {final_score}