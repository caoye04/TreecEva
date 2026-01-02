def transform_data(entries):
    processed = []
    for entry in entries:
        if len(entry) > 3:
            processed.append(entry.upper()[::-1])
        else:
            processed.append(entry.lower())
    return processed

# Irrelevant data transformation (red herring)
dummy_logs = ['err', 'ok', 'fail', 'pass']
transformed_logs = transform_data(dummy_logs)

# Core system parameters (some are decoys)
system_mode = 'advanced'
base_threshold = 42
scaling_factor = 1.5

# Real input data
raw_metrics = [85, 90, 78, 92]
weight_map = {'w1': 0.2, 'w2': 0.3, 'w3': 0.25, 'w4': 0.25}

# Distractor: unused alternative weights
temporal_weights = [0.1, 0.4, 0.3, 0.2]  # never used

# Simulated preprocessing with string manipulation distraction
def preprocess_strings(data_list):
    cleaned = []
    for item in data_list:
        item = item.strip().replace('_', '').title()
        if 'X' in item:
            continue
        cleaned.append(item[:3].upper())
    return cleaned

config_tags = ['cfg_main', 'cfg_aux', 'cfg_X_override']
filtered_tags = preprocess_strings(config_tags)

# Real logic begins here — metric evaluation
def apply_weighting(values, weights):
    weighted_sum = 0.0
    for i in range(len(values)):
        weighted_sum += values[i] * list(weights.values())[i]
    return weighted_sum

# Secondary scoring model (dead path)
def calculate_legacy_score(vals):
    score = 0
    for v in vals:
        if v > 80:
            score += v * 0.1
    return score  # never called

# Main evaluation engine
def evaluate_performance(weight_dict, raw_vals):
    total = 0.0
    keys = sorted(weight_dict.keys())
    
    # Nested conditional + arithmetic chain
    for idx, key in enumerate(keys):
        val = raw_vals[idx]
        weight = weight_dict[key]
        
        if val >= 80:
            adjusted = (val ** 0.5) * weight * scaling_factor
        else:
            adjusted = val * weight / scaling_factor
        
        # Bitwise red herring
        magic_offset = (idx ^ 5) & 3  # looks important, not actually used
        
        total += adjusted
    
    # Complex post-processing with slicing distraction
    history_buffer = [70, 75, 80, 85, 90]
    recent_trend = history_buffer[-3:]  # [80, 85, 90]
    trend_boost = sum(recent_trend) / 100  # 2.55
    
    # Final adjustment using case conversion decoy
    mode_flag = system_mode.upper()  # 'ADVANCED'
    flag_value = len(mode_flag)  # 8, irrelevant
    
    total += trend_boost
    
    # This is the real answer computation
    final_norm = round(total * 100) / 100
    return final_norm

# Trigger execution
evaluation_data = [85, 90, 78, 92]
metric_weights = {'w1': 0.2, 'w2': 0.3, 'w3': 0.25, 'w4': 0.25}
raw_results = evaluation_data

# Dead code path
if base_threshold < 40:
    fallback = apply_weighting(raw_results, weight_map)
else:
    temp_result = None  # unused

# Key statement
final_score = evaluate_performance(metric_weights, raw_results)

print(f"Result: {final_score}")