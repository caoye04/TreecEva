def analyze_efficiency(metrics):
    adjusted_metrics = [m * 1.1 for m in metrics if m > 5]
    return sum(adjusted_metrics) // len(adjusted_metrics) if adjusted_metrics else 0

metrics_data = [3, 7, 8, 4, 9, 6, 10]
efficiency_score = analyze_efficiency(metrics_data)

productivity = 0
for val in metrics_data:
    if val >= 7:
        productivity += val * 2
temp_buffer = [x**2 for x in metrics_data]  # irrelevant computation
risk_factor = len([x for x in metrics_data if x < 5])

status_flags = {'high': 0, 'low': 0}
for m in metrics_data:
    if m > efficiency_score:
        status_flags['high'] += 1
    else:
        status_flags['low'] += 1

snapshot_log = [(i, metrics_data[i]) for i in range(len(metrics_data))]  # unused log

# Core evaluation logic
def evaluate_performance(prod, risk):
    base = prod // (risk + 1)
    penalty = 0
    if risk > 2:
        penalty = risk * 3
    return base - penalty

final_score = evaluate_performance(productivity, risk_factor)
Result: {final_score}