from itertools import compress, cycle

def analyze_efficiency(raw_data, thresholds):
    filtered = [x for x in raw_data if x > thresholds[0]]
    squared = [x ** 2 for x in filtered]
    adjusted = [s - thresholds[1] for s in squared]
    return [a for a in adjusted if a > 0]

def normalize_sequence(seq):
    total = sum(seq)
    return [round(v / total, 5) for v in seq] if total != 0 else seq

def evaluate_performance(weights, contributions):
    product_pairs = [weights[i] * contributions[i] for i in range(len(weights))]
    weighted_sum = sum(product_pairs)
    penalty = 0.1 if len(contributions) > 3 else 0
    return round(weighted_sum - penalty, 4)

def main():
    # Simulated departmental KPIs (distraction: some are unused later)
    marketing_kpis = [85, 90, 78, 88]
    engineering_kpis = [92, 87, 95, 85, 90]
    sales_kpis = [76, 81, 85]

    # Core input data
    raw_productivity = [120, 135, 110, 140, 130, 150, 105]
    limits = [115, 10]

    # Step 1: Filter and process efficiency metrics
    efficiency_metrics = analyze_efficiency(raw_productivity, limits)
    
    # Distractor computation: irrelevant team averages
    team_sizes = [5, 7, 6]
    avg_per_member = [sum(engineering_kpis) / team_sizes[1], sum(sales_kpis) / team_sizes[2]]
    growth_projected = [round(avg * 1.08, 2) for avg in avg_per_member]

    # Step 2: Normalize the efficiency results for scoring
    normalized_contributions = normalize_sequence(efficiency_metrics)

    # Step 3: Define metric weights (aligned with normalized_contributions)
    base_weights = [0.4, 0.3, 0.2, 0.1]
    metric_weights = normalize_sequence(base_weights)  # Renormalized to sum to 1

    # Step 4: Introduce cycling pattern over normalized weights (semi-relevant)
    weight_cycle = list(zip(metric_weights, cycle([1]))[:len(normalized_contributions)])
    
    # Step 5: Compute final performance score
    final_score = evaluate_performance(metric_weights, normalized_contributions)
    
    # Irrelevant filtering path (dead code path)
    if any(x > 1000 for x in efficiency_metrics):
        final_score *= 1.1
    
    # Output result as required
    print(f"Result: {final_score}")

    return final_score

# Execute main function
result = main()