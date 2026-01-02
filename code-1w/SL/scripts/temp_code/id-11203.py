def evaluate_performance(data, limits):
    # Irrelevant transformation: normalize unrelated features
    normalized = [round((x - min(data)) / (max(data) - min(data)) * 100) for x in data]
    adjusted = [n + 5 for n in normalized if n < 85]  # Partial processing, not used later

    # Core logic: count how many metrics exceed their corresponding thresholds
    exceeded = 0
    for i in range(len(data)):
        if data[i] > limits[i]:
            exceeded += 1

    # Secondary check: find first significant drop in consecutive values
    drops = []
    for i in range(1, len(data)):
        if data[i] < data[i-1] * 0.9:  # More than 10% drop
            drops.append(i)
    first_drop = drops[0] if drops else -1

    # Determine base score from threshold exceedances
    base_score = exceeded * 10

    # Apply penalty if early drop exists
    penalty = 0
    if first_drop != -1 and first_drop < 5:
        penalty = 15

    # Bonus calculation based on bitwise pattern in index sum
    index_sum = sum(i for i, x in enumerate(data) if x > 50)
    bonus_flag = (index_sum & 7) == 0  # Check if last 3 bits are 0 (divisible by 8)
    bonus = 20 if bonus_flag else 0

    # Final score computation
    final_score = base_score - penalty + bonus

    # Dead code: unused health summary
    health = set(['stable'] * len(data))
    health.add('degraded' if first_drop != -1 else 'stable')

    return final_score

# Main execution
metric_data = [80, 75, 90, 60, 45, 85, 95]
thresholds = [70, 80, 85, 65, 50, 80, 90]

# Setup intermediate variables (some irrelevant)
baseline_avg = sum(metric_data) // len(metric_data)
deviations = [abs(x - baseline_avg) for x in metric_data]
adjusted_thresholds = [t * 0.95 for t in thresholds]  # Unused adjustment

# Key statement
final_score = evaluate_performance(metric_data, thresholds)

print(f"Result: {final_score}")