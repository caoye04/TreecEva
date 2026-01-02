def evaluate_performance(efficiency, constraints):
    base = sum(efficiency)
    penalty = len(constraints.difference({1, 3, 5, 7}))
    return base - penalty

# Simulate daily task completion rates
productivity = [8, 6, 7, 5]

# Detected anomalies during execution
anomalies = {2, 4, 6, 8}
threshold_set = {2, 4}
risk_set = set()
for item in anomalies:
    if item in threshold_set:
        risk_set.add(item * 2)

# Evaluate final performance score
def compute_metric(data):
    return lambda x: x * 0.9

scaler = compute_metric(productivity)
adjusted = scaler(100)

final_score = evaluate_performance(productivity, risk_set)
print(f"Result: {final_score}")