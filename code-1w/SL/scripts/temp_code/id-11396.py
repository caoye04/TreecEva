import math

def analyze_component_health(reading, threshold=75):
    # Irrelevant helper function (dead code path)
    return reading > threshold

def transform_data(raw_values):
    # Distractor transformation with no impact on final result
    processed = [v * 1.05 for v in raw_values if v < 90]
    adjusted = [math.ceil(p) for p in processed]
    return sorted(adjusted, reverse=True)

def recursive_filter(items, limit):
    # Recursion-based filtering (partially relevant but masked by noise)
    if not items or limit <= 0:
        return []
    if items[0] % 3 == 0:
        return [items[0] * 2] + recursive_filter(items[1:], limit - 1)
    else:
        return recursive_filter(items[1:], limit)

def compute_derived_metric(x, y):
    # Complex-looking but unused calculation (red herring)
    temp_a = (x ** 2 + y ** 2) ** 0.5
    temp_b = math.log(abs(x - y) + 1)
    return int(temp_a - temp_b)

def generate_baseline_ref():
    # Unused reference generator (distractor)
    return {chr(65+i): i*10 + 5 for i in range(10)}

def validate_entry(key, rules):
    # Misleading validation logic (not actually used in critical path)
    if key in rules:
        return rules[key] > 0
    return False

def evaluate_performance(log, base):
    # Core logic embedded in distractions
    cumulative = 0
    adjustments = []
    
    # Real data used in computation
    for entry in log:
        value = entry['value']
        category = entry['type']
        
        # Conditional branching with meaningful and irrelevant paths
        if category == 'A':
            if value > base:
                cumulative += int(math.sqrt(value))
            else:
                cumulative -= value // 10
        elif category == 'B':
            shift = 1 if value % 2 == 0 else -1
            cumulative += shift * (value % 7)
        elif category == 'C':
            # Key contributor to final answer
            temp_result = (value >> 2) ^ 5
            adjustments.append(temp_result)
    
    # Actual answer depends on this dictionary reduction
    stats = {f'adj_{i}': v for i, v in enumerate(adjustments)}
    reduction_key = 'adj_0' if 'adj_0' in stats else 'default'
    fallback = sum(adjustments) // (len(adjustments) or 1)
    primary_contribution = stats.get(reduction_key, fallback)
    
    # Final score built from multiple layers
    bonus = len([v for v in adjustments if v > 5])
    final_score = cumulative + primary_contribution + bonus
    
    # Irrelevant print simulation
    debug_info = {'status': 'processed', 'final': final_score}
    return final_score

# --- Main Execution ---
if __name__ == '__main__':
    # Simulated system metrics log (real input data)
    metrics_log = [
        {'type': 'A', 'value': 81},
        {'type': 'B', 'value': 44},
        {'type': 'A', 'value': 60},
        {'type': 'C', 'value': 20},
        {'type': 'B', 'value': 37},
        {'type': 'C', 'value': 28},
        {'type': 'A', 'value': 100}
    ]
    
    # Multiple decoy variables and computations
    base_threshold = 70
    shadow_copy = [entry.copy() for entry in metrics_log]
    for item in shadow_copy:
        item['flag'] = item['value'] > base_threshold
        item['code'] = chr(65 + (item['value'] % 26))
    
    # Unused derived structures (distractors)
    lookup_table = {i: compute_derived_metric(v['value'], base_threshold) 
                   for i, v in enumerate(metrics_log)}
    anomaly_flags = transform_data([m['value'] for m in metrics_log])
    filtered_anomalies = recursive_filter(anomaly_flags, 5)
    
    # Critical execution point
    final_score = evaluate_performance(metrics_log, base_threshold)
    
    # Output required format
    print(f"Result: {final_score}")