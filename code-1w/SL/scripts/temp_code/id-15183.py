def evaluate_performance(metrics, baseline):
    # Initialize tracking variables
    score = 0
    adjustments = []
    temp_offset = 0

    # Irrelevant statistical moment calculations (distractor)
    mean_val = sum(metrics) / len(metrics)
    variance = sum((x - mean_val) ** 2 for x in metrics) / len(metrics)
    skew_hint = (sum((x - mean_val) ** 3 for x in metrics)) / (len(metrics) * variance ** 1.5) if variance > 0 else 0

    # Core logic: assess each metric against baseline with set-based filtering
    high_performers = {i for i, m in enumerate(metrics) if m > baseline[i]}
    low_performers = {i for i, m in enumerate(metrics) if m < baseline[i]}
    stable_indices = {i for i, m in enumerate(metrics) if abs(m - baseline[i]) < 5}

    # Compute overlap between high performers and stable trends (semi-relevant)
    consistent_gains = high_performers & stable_indices

    # Scoring mechanism
    for i in range(len(metrics)):
        if i in high_performers:
            score += 3
        elif i in low_performers:
            score -= 2
        else:
            score += 1

        # Distractor: cumulative adjustment not used in final score
        temp_offset += abs(metrics[i] - baseline[i])
        adjustments.append(temp_offset)

    # Additional red herring: unused transformation
    transformed_metrics = [m * 1.1 for m in metrics if m > mean_val]

    # Final score computed from logical conditions on sets
    redundancy_check = len(high_performers | low_performers) == len(metrics)
    bonus = 10 if redundancy_check and len(consistent_gains) >= 2 else 0

    final_score = score + bonus
    return final_score

# Main execution context
if __name__ == '__main__':
    # Input data
    metrics = [88, 92, 75, 85, 95]
    baseline = [85, 80, 80, 88, 90]

    # Unused auxiliary arrays (distractors)
    historical_trends = [87, 85, 78, 84, 93]
    projected_growth = [89, 95, 70, 90, 97]

    # Key statement
    final_score = evaluate_performance(metrics, baseline)
    
    # Output result
    print(f"Result: {final_score}")