from itertools import compress, cycle

def evaluate_performance(metrics, thresholds):
    # Normalize metrics using min-max scaling (irrelevant for final result but adds distraction)
    normalized = [(m - min(metrics)) / (max(metrics) - min(metrics) + 1e-8) for m in metrics]
    
    # Weighted sum of metrics (distractor computation)
    weights = [0.1, 0.2, 0.3, 0.2, 0.1, 0.1]
    weighted_sum = sum(m * w for m, w in zip(metrics, weights))
    
    # Actual logic: count how many metrics exceed their corresponding threshold
    above_threshold = [m >= t for m, t in zip(metrics, thresholds)]
    count_passed = sum(above_threshold)
    
    # Use itertools.compress to extract passing metric values (semi-relevant)
    passing_values = list(compress(metrics, above_threshold))
    
    # Dummy conditional branch based on even/odd count (dead code path)
    adjustment = 0
    if count_passed % 2 == 0:
        adjustment = 10
    else:
        temp_seq = list(cycle([1, 2]))[:count_passed]
        adjustment = sum(temp_seq)
    
    # Key logic: final score is the product of count_passed and the middle value of sorted metrics
    sorted_metrics = sorted(metrics)
    median_value = sorted_metrics[len(sorted_metrics) // 2]  # Middle element via slicing proxy
    final_score = count_passed * median_value
    
    # Irrelevant dictionary construction (distractor)
    report = {
        'total': len(metrics),
        'passed': count_passed,
        'values': passing_values,
        'adjustment': adjustment
    }
    
    return final_score

# Input data
metrics = [12, 15, 8, 20, 9, 14]
thresholds = [10, 13, 7, 18, 10, 12]

# Execution point
final_score = evaluate_performance(metrics, thresholds)
print(f"Result: {final_score}")