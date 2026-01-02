def analyze_efficiency(metrics):
    threshold = 0.75
    adjusted = list(map(lambda x: x * 1.2 if x < threshold else x * 0.9, metrics))
    return [val for val in adjusted if val > 0.5]

productivity = [0.68, 0.72, 0.78, 0.61, 0.85]
overhead_costs = [23, 45, 12, 67, 34]  # Distractor: not used in final logic
baseline = sum([x**2 for x in productivity]) / len(productivity)  # Red herring computation

risk_factor = 0
for i, val in enumerate(productivity):
    if val < 0.7:
        risk_factor += 0.1
    elif val >= 0.7 and val < 0.8:
        risk_factor += 0.05
    else:
        risk_factor -= 0.02

# Simulate auxiliary analysis (distractor)
dummy_analysis = []
def helper_simulation(data):
    for x in data:
        dummy_analysis.append(x * 0.1 + 2.1)
helper_simulation(overhead_costs)  # Dead code path — no effect on result

# Core evaluation logic
def evaluate_performance(efficiency_scores, penalty):
    raw_total = sum(efficiency_scores)
    adjustment = raw_total * (1 - penalty)
    bonus = 0.0
    if adjustment > 3.0:
        bonus = 0.5
    elif adjustment > 2.5:
        bonus = 0.3
    else:
        bonus = 0.1
    return int((adjustment + bonus) * 100)  # Final score as integer

# Intermediate distraction: string processing with no impact
task_labels = "alpha,beta,gamma,delta".split(',')
processed_names = [name.upper() + '_X' for name in task_labels]
concat_result = ''.join(processed_names)

# Key statement
efficient_metrics = analyze_efficiency(productivity)
final_score = evaluate_performance(efficient_metrics, risk_factor)
print(f"Result: {final_score}")