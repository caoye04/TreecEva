def analyze_performance(metrics):
    # Irrelevant transformation (distractor)
    normalized = {k: v / max(metrics.values()) for k, v in metrics.items()}
    adjusted = {}
    
    for key, value in metrics.items():
        if value > 80:
            adjusted[key] = value * 1.1
        elif value > 60:
            adjusted[key] = value * 1.05
        else:
            adjusted[key] = value
    
    # Semi-relevant aggregation (only total_count matters later)
    total_score = sum(adjusted.values())
    total_count = len([v for v in metrics.values() if v >= 70])  # Only this is used
    avg_adjusted = total_score / len(adjusted)

    return total_count, avg_adjusted


def filter_outliers(data):
    mean_val = sum(data) / len(data)
    variance = sum((x - mean_val) ** 2 for x in data) / len(data)
    std_dev = variance ** 0.5
    # Dead code path — never used
    cleaned = [x for x in data if abs(x - mean_val) <= 2 * std_dev]
    return data  # Returns original anyway


def calculate_final_score(results, multiplier):
    # Core logic begins
    base_set = {i for i in range(len(results)) if results[i] >= 75}
    penalty_set = {i for i in range(len(results)) if results[i] < 60}
    effective_indices = base_set - penalty_set
    
    raw_total = sum(results[i] for i in effective_indices)
    
    # Conditional expression used
    adjustment_factor = 1.2 if len(effective_indices) >= 3 else 0.9
    
    # Red herring computation
    _ = [x * 1.5 for x in results if x < 50]  # unused list comprehension
    temp_offset = sum(1 for r in results if r > 90) * 2
    
    intermediate = raw_total * adjustment_factor + temp_offset
    
    # Another conditional expression
    bonus = intermediate * 0.1 if len(penalty_set) == 0 else 0
    
    final_value = intermediate + bonus
    
    return int(final_value * multiplier)

# Main execution flow
if __name__ == "__main__":
    # Input data
    performance_metrics = {'task1': 85, 'task2': 92, 'task3': 78, 'task4': 63, 'task5': 96}
    
    # Distractor function calls
    count_eligible, _ = analyze_performance(performance_metrics)
    filtered_data = filter_outliers(list(performance_metrics.values()))
    
    # Misleading variable
    outlier_count = len(performance_metrics) - len(filtered_data)
    
    # Key data structure
    results = [88, 76, 91, 58, 95]  # One below 60 (index 3)
    
    # Unused helper (dead code)
    def get_rank(score):
        if score > 90: return 'S'
        elif score > 80: return 'A'
        elif score > 70: return 'B'
        else: return 'C'
    
    # Bonus only applied if no penalties, but there is one → bonus = 0
    bonus_multiplier = 1.05
    
    # Critical statement
    final_score = calculate_final_score(results, bonus_multiplier)
    
    print(f"Result: {final_score}")