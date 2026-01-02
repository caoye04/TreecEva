def evaluate_performance(metrics, base):
    # Irrelevant transformation (distractor)
    temp_normalized = [round((x - min(metrics)) / (max(metrics) - min(metrics)) * 100) for x in metrics]
    
    # Actual logic starts here
    above_base = set()
    for m in metrics:
        if m > base:
            above_base.add(m)
    
    # Secondary metric: count of unique high performers
    high_performers = {m for m in above_base if m >= 90}
    
    # Compute weighted contribution
    raw_sum = sum(metrics)
    base_penalty = len([x for x in metrics if x < base]) * 5
    bonus = len(high_performers) * 10

    # Misleading complex calculation that isn't used
    phantom_score = (raw_sum / (base + 1)) ** 0.5 if base != -1 else 0
    temp_result = (raw_sum - base_penalty + bonus)  # This is important

    # Simulate conditional adjustment
    adjustments = 0
    if len(above_base) >= 3:
        adjustments += 15
    elif len(above_base) == 2:
        adjustments += 5
    else:
        adjustments -= 10

    # Another red herring: unused function call
    def calculate_entropy(data):
        from math import log
        total = sum(data)
        if total == 0:
            return 0
        entropy = 0
        for x in data:
            p = x / total
            if p > 0:
                entropy -= p * log(p)
        return entropy

    unused_entropy = calculate_entropy(metrics)  # Dead code path

    # Final computation
    final_score = temp_result + adjustments

    # Print result as required
    print(f"Result: {final_score}")
    return final_score

# Main execution
metric_data = [85, 92, 78, 96, 88]
baseline = 85
noise_filter = [x for x in metric_data if x % 2 == 0]  # Distractor list
offset_correction = sum(noise_filter) / len(noise_filter) if noise_filter else 0

# Key statement
final_score = evaluate_performance(metric_data, baseline)