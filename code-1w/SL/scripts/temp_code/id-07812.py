def calculate_performance(data):
    # Preprocessing phase with some irrelevant transformations
    normalized = [x * 0.95 for x in data if x > 0]
    offset_values = list(map(lambda y: y + 10, [1, 2, 3]))  # Distractor: unused later

    # Key metrics calculation
    base_metric = sum(normalized) / len(normalized) if normalized else 0
    
    # Secondary metric with conditional expression
    adjustment_factor = 1.2 if base_metric > 50 else (0.8 if base_metric > 30 else 0.5)
    
    # Simulated efficiency score (partially relevant)
    efficiency_scores = {i: val ** 0.5 for i, val in enumerate(normalized)}
    avg_efficiency = sum(efficiency_scores.values()) / len(efficiency_scores) if efficiency_scores else 0

    # Dummy dictionary operations for distraction
    stats_summary = {
        'count': len(normalized),
        'peak': max(normalized, default=0),
        'floor': min(normalized, default=0)
    }
    stats_summary['range'] = stats_summary['peak'] - stats_summary['floor']
    stats_summary['grade'] = 'A' if stats_summary['range'] > 40 else 'B'

    # Core logic buried among distractions
    raw_incentive = 0
    for i, val in enumerate(normalized):
        if i % 2 == 0 and val > 40:
            raw_incentive += val * 0.1
        elif i % 3 == 0:
            raw_incentive -= val * 0.05

    # Final composition using multiple intermediate values
    stability_bonus = 5 if avg_efficiency > 6 else 0
    final_score = (base_metric * adjustment_factor) + raw_incentive + stability_bonus

    # Dead code path (never executed due to fixed condition)
    if False:
        fallback = sum(data) // len(data)
        final_score = max(final_score, fallback)

    return final_score

# Input data
benchmark_data = [42, -5, 68, 0, 73, 29, 81, 12]

# Execution point of interest
final_score = calculate_performance(benchmark_data)
print(f"Result: {final_score}")