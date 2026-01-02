from collections import defaultdict

# Simulate employee performance tracking across departments
def calculate_efficiency(metrics):
    base_efficiency = sum(metrics) / len(metrics)
    adjustment = 0.0
    if base_efficiency > 80:
        adjustment = 12.5
    elif base_efficiency > 60:
        adjustment = 5.0
    else:
        adjustment = -7.3
    return base_efficiency + adjustment

def analyze_trends(data_stream):
    trend_counter = defaultdict(int)
    for val in data_stream:
        trend_counter[val // 10] += 1
    peak_decade = max(trend_counter, key=lambda x: trend_counter[x])
    return peak_decade * 10

def evaluate_performance(output_log, risk_level):
    normalized_output = [x * (0.9 + risk_level * 0.1) for x in output_log]
    avg_output = sum(normalized_output) / len(normalized_output)
    efficiency_bonus = 1.0 if avg_output > 75 else 0.85
    penalty = 0
    if risk_level > 0.7:
        penalty = 15
    elif risk_level < 0.3:
        penalty = 5
    score = avg_output * efficiency_bonus - penalty
    return int(score)

# Simulated input data
metrics_data = [88, 76, 92, 81, 74]
dynamic_stream = [85, 91, 78, 94, 88, 90, 82, 87]
productivity = metrics_data + [analyze_trends(dynamic_stream)]
risk_factor = 0.65

# Irrelevant distraction: capacity forecasting (not used in final result)
capacity_model = [x * 1.2 for x in dynamic_stream if x > 85]
projected_headcount = len(capacity_model) * 3.5
utilization_rate = projected_headcount / 12

interim_efficiency = calculate_efficiency(metrics_data)
temp_adjustment = interim_efficiency * 0.05 if interim_efficiency > 85 else 0

# Key computation chain
scaled_productivity = [p * 1.1 for p in productivity]
smoothed_values = [val for val in scaled_productivity if val >= 70]
aggregated_metric = sum(smoothed_values) / len(smoothed_values)

final_score = evaluate_performance(productivity, risk_factor)
print(f"Result: {final_score}")