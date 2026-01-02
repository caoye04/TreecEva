def analyze_efficiency(metrics):
    if not metrics:
        return 0
    avg = sum(metrics) / len(metrics)
    adjusted = [m * 1.1 for m in metrics if m > avg]
    return len(adjusted)

productivity = [85, 90, 78, 92, 88]
overhead_costs = [23, 45, 12, 67, 34]  # Distractor variable
baseline = 80

efficiency_benchmark = analyze_efficiency(productivity)
dummy_calc = sum(overhead_costs) * 0.05  # Irrelevant computation

risk_set = {x for x in productivity if x < baseline}  # Set comprehension
risk_factor = len(risk_set) + (1 if efficiency_benchmark >= 3 else 0)

# Slicing and conditional expression used together
trend = productivity[-3:]  # Last three periods
recent_trend = 'up' if sum(trend) > sum(productivity[:3]) else 'down'

boost = 1.5 if recent_trend == 'up' else 0.8

# Core logic with distraction from dead computations above
def evaluate_performance(perf_data, risk):
    base_score = sum(perf_data) / len(perf_data)
    penalty = risk * 5
    bonus = 10 if base_score >= 85 else 0
    return int(base_score - penalty + bonus)

intermediate_result = efficiency_benchmark * dummy_calc  # Dead path, no impact
final_score = evaluate_performance(productivity, risk_factor)

print(f"Result: {final_score}")