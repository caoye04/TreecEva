def calculate_performance(data_map):
    total_weight = 0
    cumulative_value = 0
    
    # Auxiliary tracking variables (some not used in final calculation)
    max_entry = float('-inf')
    min_entry = float('inf')
    entry_count = 0
    temp_sum = 0  # distractor: used only for side logging
    debug_flag = True  # misleading flag, never changed
    
    for key, value in data_map.items():
        if isinstance(value, dict) and 'score' in value and 'active' in value:
            if value['active']:
                weight = len(key) % 4 + 1  # weighting by key length mod
                total_weight += weight
                cumulative_value += value['score'] * weight
                
                # Update min/max for distraction
                if value['score'] > max_entry:
                    max_entry = value['score']
                if value['score'] < min_entry:
                    min_entry = value['score']
                entry_count += 1
                temp_sum += value['score']  # irrelevant accumulation
    
    # Simulated post-processing with red herring logic
    adjustment_factor = 0.0
    if entry_count > 5:
        adjustment_factor = 1.1
    elif entry_count == 3:
        adjustment_factor = 0.9
    else:
        adjustment_factor = 1.0  # neutral, distractor branch
    
    # Final score computation — only this matters
    final_result = cumulative_value / total_weight if total_weight != 0 else 0
    
    # Extra dead code path (never reached due to logic above)
    if debug_flag and adjustment_factor < 0.5:
        final_result *= 2
        
    return final_result

# Setup input data
raw_keys = ['alpha', 'beta', 'gamma', 'delta', 'epsilon']
processed_keys = [k.upper() + '_V2' for k in raw_keys]

# Build benchmark data using zip and enumerate (required features)
data_entries = []
for idx, name in enumerate(processed_keys):
    score_val = (idx + 1) * 17 % 13  # deterministic score generation
    active_status = idx % 2 == 0  # every even index is active
    data_entries.append((name, {'score': score_val, 'active': active_status}))

dataset = dict(data_entries)

# Add a few extra inactive entries to mislead
for tag in ['DEBUG_X1', 'STAGING_Y2']:
    dataset[tag] = {'score': 999, 'active': False}  # inactive, won't count

# Perform calculation
total_sum = sum(len(k) for k in dataset.keys())  # distractor summation
decoy_value = total_sum * 0.5  # unused beyond assignment

final_score = calculate_performance(dataset)
print(f"Result: {final_score}")