def evaluate_performance(metrics, limit):
    high_performers = {x for x in metrics if x > limit}
    low_performers = {x for x in metrics if x <= limit}
    adjustment_factor = 0.85
    
    # Irrelevant computation - distractor
    temp_sum = sum([i**2 for i in range(len(metrics))])
    avg_metric = sum(metrics) / len(metrics) if metrics else 0
    
    # Semi-relevant transformation
    normalized = [round(x * adjustment_factor) for x in metrics]
    normalized_set = set(normalized)
    
    # Another distraction: counting pairs with sum above average
    count_pairs = 0
    for i in range(len(metrics)):
        for j in range(i+1, len(metrics)):
            if metrics[i] + metrics[j] > avg_metric:
                count_pairs += 1

    # Core logic: performance score based on high performers and penalties
    base_score = len(high_performers) * 10
    penalty = 0
    for val in low_performers:
        if val < limit - 5:
            penalty += 3
    
    # Additional irrelevant state tracking
    history_log = []
    for val in metrics:
        status = "high" if val > limit else "low"
        history_log.append(f"{status}-{val}")

    intermediate_result = base_score - penalty
    final_adjustment = len(normalized_set.intersection(high_performers))
    
    result = intermediate_result + final_adjustment
    return result

# Main execution
productivity_data = [8, 12, 5, 17, 9, 4, 11]
threshold = 10
baseline_check = [x for x in productivity_data if x >= threshold]

# Unused helper function - dead code path
def calculate_bonuses(data, rate=0.1):
    return [int(x * rate) for x in data]

noise_value = sum([x % 3 for x in productivity_data])  # Distractor variable

final_score = evaluate_performance(productivity_data, threshold)

# Print result as required
print(f"Target result: {final_score}")