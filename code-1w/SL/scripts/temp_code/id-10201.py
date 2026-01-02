def process_results(data):
    # Irrelevant transformation (distractor)
    normalized = [round(x * 0.95 + 2.5, 2) for x in data if x > 0]
    
    # Semi-relevant preprocessing
    filtered = list(filter(lambda x: x >= 50, data))
    adjustments = []
    
    for val in filtered:
        if val < 75:
            adjustments.append(val * 1.1)
        elif val < 90:
            adjustments.append(val * 1.05)
        else:
            adjustments.append(val * 0.98)  # Minor penalty for overfitting
    
    # Dummy statistic tracking (dead code path)
    avg_adjustment = sum(adjustments) / len(adjustments) if adjustments else 0
    adjustment_variance = sum((x - avg_adjustment) ** 2 for x in adjustments) / len(adjustments) if adjustments else 0

    # Core logic: weighted contribution based on performance bands
    high_performer_count = len([x for x in data if x >= 90])
    mid_performer_count = len([x for x in data if 75 <= x < 90])
    low_performer_count = len([x for x in data if 50 <= x < 75])

    # Bonus calculation with string-based condition (uses string method)
    performance_flag = "high_volume" if len(data) > 6 else "standard"
    volume_bonus = 10 if performance_flag.endswith("volume") else 0

    # Actual score computation
    base_score = sum(adjustments)
    complexity_penalty = len(data) * 0.5
    final_score = base_score - complexity_penalty + volume_bonus

    # Unused diagnostic info (irrelevant)
    diagnostic_report = f"Processed {len(data)} entries with {high_performer_count} high performers."
    report_hash = sum(ord(c) for c in diagnostic_report) % 1000

    return int(round(final_score))

# Simulated assessment data from system diagnostics
test_metrics = [88, 92, 76, 95, 83, 73, 91, 87]
dummy_padding_value = 42  # unused in logic
placeholder_buffer = [0] * 5  # dead storage

result_tracker = []
result_tracker.append("start")

# Key execution point
final_score = process_results(test_metrics)

result_tracker.append("complete")

print(f"Result: {final_score}")