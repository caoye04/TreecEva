from collections import defaultdict

# Simulate employee performance analytics with noise and intermediate metrics
def analyze_productivity(hours_worked, tasks_completed):
    if not hours_worked:
        return 0.0
    base_rate = sum(tasks_completed) / len(hours_worked)
    efficiency = base_rate / (sum(hours_worked) / len(hours_worked))
    penalty = 0.0
    for h in hours_worked:
        if h > 12:
            penalty += 0.5
    adjusted_efficiency = efficiency - penalty / len(hours_worked)
    return max(adjusted_efficiency, 0.1)

# Risk assessment based on overtime and task complexity
def calculate_risk_profile(overtime_hours, error_count):
    risk_map = defaultdict(int)
    for i, oh in enumerate(overtime_hours):
        risk_map[i] += oh * 2
        if i % 3 == 0:
            risk_map[i] += 1  # arbitrary bias for every third record
    total_risk = sum(risk_map.values()) + sum(error_count)
    normalization_factor = len(overtime_hours) or 1
    return total_risk / normalization_factor

# Core evaluation logic combining productivity and risk
def evaluate_performance(prod_log, risk_log):
    productivity = analyze_productivity([8, 9, 10], [4, 5, 6])
    temp_result = productivity * 100
    temp_result += 10  # red herring adjustment not used later

    risk_factor = calculate_risk_profile([3, 5, 2], [1, 0, 1])
    volatility_index = 0.0
    for _ in range(2):
        volatility_index += risk_factor * 0.1  # side computation with no impact

    # Actual final calculation
    raw_score = productivity * 85
    adjustment = 15 if risk_factor < 10 else -10
    final_score = int(raw_score + adjustment)

    # Distractor block: unused health metrics
    health_audit = []
    for val in prod_log:
        if isinstance(val, str):
            health_audit.append(len(val))
        else:
            health_audit.append(val * 2)  # dead code path since all are integers

    return final_score

# Execution trace
productivity_metrics = [8, 9, 10]
task_log = [4, 5, 6]
overtime_data = [3, 5, 2]
error_history = [1, 0, 1]

# Intermediate variables with mixed relevance
baseline = analyze_productivity(productivity_metrics, task_log)
risk_assessment = calculate_risk_profile(overtime_data, error_history)

# Key statement
final_score = evaluate_performance(productivity_metrics, risk_assessment)
print(f"Target result: {final_score}")