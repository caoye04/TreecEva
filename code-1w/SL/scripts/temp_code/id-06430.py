def analyze_efficiency(metrics):
    base_efficiency = sum([m * (i + 1) for i, m in enumerate(metrics)])
    adjustment = len(metrics) ** 0.5
    return base_efficiency / adjustment if adjustment != 0 else 0

metrics_data = [0.8, 0.9, 0.75, 0.88, 0.92]

# Irrelevant calculation - distractor
historical_avg = sum(metrics_data) / len(metrics_data)
trend_deviation = (metrics_data[-1] - metrics_data[0]) ** 2

# Semi-relevant transformation
normalized_metrics = [round(m * 100) for m in metrics_data]
efficiency_rating = analyze_efficiency(metrics_data)

# Simulate risk factors using set operations
risk_profiles = {1: 'low', 2: 'medium', 3: 'high'}
current_risks = {1, 2}
risk_factor = len(risk_profiles.intersection(current_risks)) * 0.1

# Productivity computation with tuple unpacking
daily_logs = [(8, 0.85), (7, 0.91), (9, 0.78)]
total_hours, avg_focus = 0, 0.0
for hours, focus in daily_logs:
    total_hours += hours
    avg_focus += focus
avg_focus /= len(daily_logs)

productivity = total_hours * avg_focus

# Secondary unused metric - dead code path
projected_output = productivity * (1 + risk_factor)

# Core evaluation logic
status_codes = {200: 'active', 404: 'inactive', 500: 'critical'}
activation_status = status_codes.get(200, 'unknown')

def evaluate_performance(prod, risk):
    if prod > 50 and risk < 0.3:
        return int(prod - (risk * 100))
    elif prod <= 50:
        return int(prod / (risk + 1))
    else:
        return int((prod * 0.8) - (risk * 50))

final_score = evaluate_performance(productivity, risk_factor)

# Extraneous logging - irrelevant
debug_info = {"timestamp": 1678886400, "source": "module_x", "cached": True}
metadata_summary = [len(str(val)) for val in debug_info.values()]

print(f"Result: {final_score}")