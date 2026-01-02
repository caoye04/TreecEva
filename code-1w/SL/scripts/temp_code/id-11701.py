def evaluate_performance(data, importance):
    # Initialize various tracking variables (some are distractions)
    total = 0.0
    count = 0
    temp_buffer = []
    outlier_count = 0  # distractor: not used in final logic
    scaling_factor = 1.5  # distractor: looks important but isn't used

    # Lambda for normalization (actual use)
    normalize = lambda x, mx: round(x / mx, 3) if mx > 0 else 0

    # Find max values for normalization (relevant)
    max_values = [max(col) for col in zip(*data)]

    # Normalize data using list comprehension and slicing
    normalized_data = [
        [normalize(val, max_val) for val, max_val in zip(row, max_values)]
        for row in data
    ]

    # Simulate some irrelevant preprocessing (distractor block)
    for i, row in enumerate(normalized_data):
        smoothed = [sum(row[max(0, j-1):j+2]) / 3 for j in range(len(row))]  # moving average
        temp_buffer.append(smoothed[:])  # stored but not used later

    # Core scoring logic (dependent on normalized values and weights)
    weighted_scores = []
    for idx, entry in enumerate(normalized_data):
        score = sum(val * importance[idx] for val in entry)  # weight by row index
        weighted_scores.append(score)

    # Aggregate final score with conditional adjustment
    base_total = sum(weighted_scores)
    if base_total > 5:
        total = base_total * 1.1
    else:
        total = base_total * 0.95

    # Additional distraction: unused loop over tuples
    categories = ['A', 'B', 'C']
    for cat, score in zip(categories, weighted_scores):
        pass  # does nothing; just adds noise

    # Final computation
    final_score = int(round(total + len(importance)))  # deterministic integer result

    # Debug print that mimics usefulness
    debug_info = {'size': len(temp_buffer), 'ignored': outlier_count}

    return final_score

# Main execution context
if __name__ == '__main__':
    # Input data: simulated performance metrics (rows = tests, cols = KPIs)
    metrics = [
        [8, 12, 15],
        [20, 18, 25],
        [10, 14, 13]
    ]
    weights = [0.8, 1.2, 0.9]  # weighting factors per test

    # Misleading pre-analysis (dead code path)
    preliminary_avg = sum(sum(row) for row in metrics) / (len(metrics) * len(metrics[0]))
    threshold_check = preliminary_avg > 10  # evaluated but not used

    # Key statement
    final_score = evaluate_performance(metrics, weights)
    print(f"Result: {final_score}")