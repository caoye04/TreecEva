def analyze_efficiency(metrics):
    base_efficiency = sum([m * (i + 1) for i, m in enumerate(metrics)])
    adjustment = len(metrics) // 2
    return base_efficiency - adjustment

metrics_data = [3, 7, 2, 8, 5]

# Irrelevant transformation (distractor)
transformed = [x ** 2 for x in metrics_data if x % 2 == 1]
dummy_sum = sum(transformed)

# Semi-relevant preprocessing
normalized = [x / max(metrics_data) for x in metrics_data]
productivity = sum(normalized) * 10

# Risk assessment with slicing distraction
risk_window = normalized[1:4]
risk_factor = 0
for val in risk_window:
    if val > 0.5:
        risk_factor += val * 2

# Dead code path (irrelevant)
if len(metrics_data) > 10:
    fallback = analyze_efficiency(metrics_data)
    productivity -= fallback

# Core logic
intermediate_diagnostic = analyze_efficiency(metrics_data)
efficiency_flag = intermediate_diagnostic > 30

# Final evaluation
final_score = 0
def evaluate_performance(prod, risk):
    base = prod - risk
    if efficiency_flag:
        base += 5
    return int(base)

final_score = evaluate_performance(productivity, risk_factor)
print(f"Target result: {final_score}")