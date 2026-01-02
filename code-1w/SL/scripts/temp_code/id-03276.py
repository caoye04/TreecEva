import math

# Simulated system performance metrics over time
def collect_metrics():
    raw_data = [120, 85, 90, 110, 95]
    timestamps = [1, 2, 3, 4, 5]
    status_flags = [True, False, True, True, False]
    
    # Irrelevant transformation (distractor)
    processed = []
    for x in raw_data:
        processed.append(int(math.sqrt(x) * 2))
    
    # Actual meaningful data structure
    metrics_log = {}
    for i in range(len(raw_data)):
        key = f"metric_{i+1}"
        metrics_log[key] = {
            'value': raw_data[i],
            'weight_factor': 0.2,
            'active': status_flags[i],
            'timestamp': timestamps[i]
        }
    
    # Dead code path - never used (red herring)
    def analyze_outliers(data):
        mean_val = sum(data) / len(data)
        return [x for x in data if abs(x - mean_val) > 20]
    
    # Unused variable (distraction)
    outlier_report = analyze_outliers(raw_data)
    
    return metrics_log

# Legacy function for backward compatibility (never called)
def legacy_evaluate(data_dict):
    total = 0
    for k in data_dict:
        if 'flag' in k:
            total += data_dict[k] * 0.1
    return total

# Weight configuration (some irrelevant entries)
def get_weights():
    weights = {
        'metric_1': 0.3,
        'metric_2': 0.1,
        'metric_3': 0.2,
        'metric_4': 0.25,
        'metric_5': 0.15,
        'placeholder_x': 0.0,  # unused
        'backup_flag': False   # unused
    }
    
    # Superfluous sorting operation (distraction)
    sorted_keys = sorted(weights.keys())
    temp_dict = {}
    for k in sorted_keys:
        temp_dict[k] = weights[k]
    
    # Return original anyway
    return weights

# Core evaluation logic
def apply_correction(value, base_weight):
    if value > 100:
        return base_weight * 1.1
    elif value < 90:
        return base_weight * 0.9
    else:
        return base_weight

def adjust_for_activity(metric_entry, weight_map):
    base_weight = weight_map[metric_entry['key']]
    adjusted_weight = apply_correction(metric_entry['value'], base_weight)
    if not metric_entry['active']:
        adjusted_weight *= 0.5  # penalty for inactive
    return adjusted_weight

def compute_contribution(value, effective_weight):
    # Complex but deterministic contribution formula
    raw_contrib = value * effective_weight
    capped = min(raw_contrib, 25.0)
    floored = max(capped, 5.0)
    return round(floored, 4)

def evaluate_performance(metrics_log, weights):
    contributions = []
    debug_values = []  # logged but unused
    
    for key, entry in metrics_log.items():
        # Build extended entry with redundant field (misleading)
        extended = {
            'key': key,
            'value': entry['value'],
            'active': entry['active'],
            'timestamp': entry['timestamp'],
            'weight_factor': entry['weight_factor']
        }
        
        # Real computation path
        effective_weight = adjust_for_activity(extended, weights)
        contrib = compute_contribution(extended['value'], effective_weight)
        contributions.append(contrib)
        
        # Store misleading intermediate (distractor)
        debug_values.append({
            'raw': entry['value'] * weights[key],
            'corrected': contrib,
            'factor': effective_weight
        })
    
    # Final aggregation
    base_total = sum(contributions)
    
    # Secondary adjustment based on pattern recognition (actual use)
    active_count = sum(1 for e in metrics_log.values() if e['active'])
    if active_count >= 3:
        base_total *= 1.05
    
    # Red herring: potential bonus logic (never triggered here)
    peak_value = max(entry['value'] for entry in metrics_log.values())
    if peak_value > 115:
        bonus = 10.0
    else:
        bonus = 0.0  # dead branch
    
    final_score = round(base_total + bonus, 4)
    
    # Critical print statement
    print(f"Result: {final_score}")
    return final_score

# Orphaned utility function (decoy)
def normalize_dataset(data_list):
    min_val = min(data_list)
    max_val = max(data_list)
    return [(x - min_val) / (max_val - min_val) for x in data_list]

# Unused list transformation (irrelevant)
temp_series = [x**2 for x in range(5)]
squared_filtered = [x for x in temp_series if x > 10]

# Main execution flow
metrics_data = collect_metrics()
weight_config = get_weights()

# Key statement
final_score = evaluate_performance(metrics_data, weight_config)