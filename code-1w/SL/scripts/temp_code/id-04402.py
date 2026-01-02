from itertools import combinations

def analyze_trends(data, threshold):
    trend_count = 0
    temp_result = []
    for i in range(2, len(data) + 1):
        for subset in combinations(data, i):
            if sum(subset) / len(subset) > threshold:
                trend_count += 1
                temp_result.append(sum(subset))
    return trend_count

def validate_entry(value, codes):
    if value < 0:
        return False
    code_str = str(value)
    for c in codes:
        if str(c) in code_str:
            return True
    return False

def compute_weighted_sum(elements, weights):
    total = 0.0
    norm_weights = [w / sum(weights) for w in weights]
    scaling_factor = 1.0
    if sum(elements) > 100:
        scaling_factor = 0.9
    for e, w in zip(elements, norm_weights):
        total += e * w * scaling_factor
    return total

def evaluate_performance(metrics, baseline):
    adjusted_metrics = [m * 0.95 for m in metrics if m > baseline]
    outlier_check = set([m for m in metrics if m > 2 * baseline])
    consistency_flag = len(outlier_check) < 3
    
    # Distractor: irrelevant computation on string transformations
    temp_names = ['metric_A', 'metric_B', 'metric_C']
    upper_names = [name.upper() for name in temp_names]
    flipped_names = [name[::-1] for name in upper_names if 'A' not in name]
    
    # Key logic branch based on set size
    penalty = 0
    if len(outlier_check) >= 1:
        penalty = 5
    
    # Another distractor: unused itertools combination
    all_pairs = list(combinations(adjusted_metrics, 2))
    pair_summation = sum([abs(a - b) for a, b in all_pairs]) if all_pairs else 0
    
    raw_score = sum(adjusted_metrics) - penalty
    final_score = int(raw_score * 0.8) if consistency_flag else int(raw_score * 0.6)
    
    # Irrelevant state tracking
    log_entry = {
        'timestamp': 'ignored',
        'final_value': final_score,
        'debug': pair_summation
    }
    
    return final_score

# Main execution block
baseline = 20
metrics = [25, 30, 15, 40, 5, 60]

# Dead code path (unused function call)
def unused_helper(x): return x ** 2 + 1

# Unused variables
max_limit = 1000
temp_cache = {}

# Trigger key evaluation
final_score = evaluate_performance(metrics, baseline)
print(f"Target result: {final_score}")