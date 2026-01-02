def analyze_performance(metrics):
    base_score = 0
    bonus_multiplier = 1.0
    temp_adjustment = 0

    for i, (metric, value) in enumerate(metrics.items()):
        if i % 2 == 0 and value > 50:
            base_score += value * 0.1
        if 'response' in metric:
            temp_adjustment += value // 10
        elif 'error' in metric:
            bonus_multiplier *= 0.9

    # Irrelevant tracking variables
    debug_log = [f'{k}:{v}' for k, v in metrics.items() if v > 0]
    snapshot = {k: v * 0.01 for k, v in metrics.items()}

    return int(base_score), bonus_multiplier


def calculate_ranking(raw_points, deductions):
    ranking = 0
    offset = len(deductions) % 4

    for idx, (p, d) in enumerate(zip(raw_points, deductions)):
        adjustment = (p - d) % 7
        if adjustment == 0:
            adjustment = 1
        
        # Core computation
        contribution = (p // (d + 1)) * adjustment
        ranking += contribution
        
        # Distractor computations
        shadow_buffer = [i**2 for i in range(idx + 1)]
        dummy_mask = sum(1 for x in shadow_buffer if x % 2 == 0)

    # Secondary influence
    modifier = 1 if len(raw_points) > len(deductions) else 0.5
    ranking = int(ranking * modifier)

    # Final threshold logic
    if ranking < 50:
        ranking += 10
    
    return ranking

# Main execution block
metrics_data = {
    'response_time_avg': 65,
    'error_rate_peak': 30,
    'throughput_jun': 80,
    'retries_count': 15,
    'latency_p95': 70
}

points = [85, 90, 78, 92, 88]
deductions = [5, 12, 3, 14, 6]

# Dead code path (never executed)
if False:
    fallback_scores = [x * 0.5 for x in points]
    points = fallback_scores

interim_result = analyze_performance(metrics_data)

# Key statement
final_score = calculate_ranking(points, deductions)

print(f"Result: {final_score}")