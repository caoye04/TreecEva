import itertools

# Simulated system health monitoring with performance evaluation

def collect_diagnostics() -> dict:
    # Irrelevant diagnostic data (distractor)
    return {
        'cpu_load': [0.78, 0.82, 0.75, 0.91],
        'mem_usage': [85.3, 87.1, 84.9, 90.2],
        'disk_iops': [1200, 1150, 1300, 1250],
        'network_latency_ms': [23, 45, 31, 67]
    }

def compute_entropy(values):
    # Unused function - red herring
    import math
    total = sum(values)
    entropy = 0
    for v in values:
        p = v / total
        if p > 0:
            entropy -= p * math.log2(p)
    return entropy

def analyze_trend(data, threshold=0.8):
    # Another distractor: analyzes trend but not used in final calculation
    count_above = sum(1 for x in data if x > threshold)
    return count_above / len(data) > 0.6

def generate_combinations(elements):
    # Uses itertools - satisfies language feature requirement
    # Generates unused combinations as distraction
    combos = []
    for r in range(2, len(elements)+1):
        combos.extend(itertools.combinations(elements, r))
    return [combo for combo in combos if sum(combo) % 2 == 0]  # Filter even-sum combos (unused)

def normalize_scores(raw_scores):
    # Normalizes scores (used in main logic)
    min_val, max_val = min(raw_scores), max(raw_scores)
    if max_val == min_val:
        return [0.5] * len(raw_scores)
    return [(x - min_val) / (max_val - min_val) for x in raw_scores]

def filter_outliers(data, factor=1.5):
    # Interquartile range filtering - defined but not used directly
    sorted_data = sorted(data)
    q1 = sorted_data[len(sorted_data)//4]
    q3 = sorted_data[3*len(sorted_data)//4]
    iqr = q3 - q1
    lower_bound = q1 - factor * iqr
    upper_bound = q3 + factor * iqr
    return [x for x in data if lower_bound <= x <= upper_bound]

def validate_checksum(token: str) -> bool:
    # String method usage - satisfies language feature
    if not token.isalnum():
        return False
    digit_sum = sum(int(c) for c in token if c.isdigit())
    alpha_weight = sum(ord(c.lower()) - ord('a') + 1 for c in token if c.isalpha())
    return (digit_sum + alpha_weight) % 11 == 0

def evaluate_performance(metrics: list, base: dict) -> int:
    # Core logic embedded in complex context
    adjusted = [m * 1.1 for m in metrics]  # Boost each metric slightly
    capped = [min(val, 95.0) for val in adjusted]  # Cap at 95
    
    # Destructuring assignment (valid use)
    primary, secondary, tertiary, *extras = capped
    
    # Conditional branches with early exit red herring
    if primary < 80.0:
        temp_result = int(primary)
        temp_result += len(extras)  # Distraction
        return temp_result  # Not taken due to data
    
    # Actual path taken
    normalized = normalize_scores([primary, secondary, tertiary])
    
    # Bitwise manipulation on derived values (relevant)
    n1, n2, n3 = [int(x * 100) for x in normalized]
    combined = (n1 << 2) ^ (n2 >> 1) | n3  # Bit shifts and logic ops
    
    # Conditional expression influencing result
    penalty = 10 if tertiary < 88 else 0
    
    # Final computation
    raw_score = (combined // 7) - penalty
    
    # Multiple assignments (distraction)
    temp_a, temp_b = raw_score + 5, raw_score - 3
    temp_c = temp_a if temp_a > 100 else temp_b
    
    # Final score determined here
    final_score = raw_score + (1 if validate_checksum('A7B3X9') else -1)
    
    # Dead code branch - misleading
    if final_score % 13 == 0:
        backup_metrics = base.get('alt_metrics', [])
        fallback = sum(backup_metrics) // len(backup_metrics) if backup_metrics else 0
        final_score = fallback  # Never reached
    
    return final_score

# Orchestration block
if __name__ == '__main__':
    # Real input data
    raw_metrics = [88.2, 84.7, 91.3, 79.5, 86.1]
    
    # Irrelevant preprocessing (distractor)
    filtered_data = filter_outliers(raw_metrics)
    entropy_value = compute_entropy([int(x) for x in raw_metrics])
    
    # Unused combination generation
    indices = list(range(len(raw_metrics)))
    unused_combos = generate_combinations(indices)
    
    # Baseline configuration with decoy entries
    baseline_config = {
        'version': '2.3.1',
        'mode': 'aggressive',
        'thresholds': { 'critical': 95, 'warning': 85 },
        'alt_metrics': [70, 65, 75],  # Unused fallback
        'checksum_required': True
    }
    
    # Diagnostics called but not used
    diagnostics = collect_diagnostics()
    cpu_high = analyze_trend(diagnostics['cpu_load'], 0.8)
    
    # Key execution point
    final_score = evaluate_performance(raw_metrics, baseline_config)
    
    # Print required output
    print(f"Result: {final_score}")