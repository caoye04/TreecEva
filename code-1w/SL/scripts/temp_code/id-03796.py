from collections import defaultdict

# Simulate employee task logs with metadata
task_logs = [
    {'employee': 'Alice', 'category': 'debug', 'time_spent': 120, 'errors': 1},
    {'employee': 'Bob', 'category': 'feature', 'time_spent': 200, 'errors': 0},
    {'employee': 'Alice', 'category': 'docs', 'time_spent': 60, 'errors': 0},
    {'employee': 'Charlie', 'category': 'debug', 'time_spent': 180, 'errors': 3},
    {'employee': 'Bob', 'category': 'debug', 'time_spent': 90, 'errors': 1},
    {'employee': 'Charlie', 'category': 'feature', 'time_spent': 240, 'errors': 2}
]

# Aggregate metrics by employee
metrics = defaultdict(lambda: {"total_time": 0, "total_errors": 0, "debug_count": 0})
for log in task_logs:
    emp = log['employee']
    metrics[emp]['total_time'] += log['time_spent']
    metrics[emp]['total_errors'] += log['errors']
    if log['category'] == 'debug':
        metrics[emp]['debug_count'] += 1

# Compute productivity scores (higher = more efficient)
productivity = {}
for emp, data in metrics.items():
    base_efficiency = data['total_time'] / (data['total_errors'] + 1)
    penalty = data['debug_count'] * 10
    productivity[emp] = base_efficiency - penalty

# Irrelevant helper: computes unused engagement metric
engagement_index = lambda x: sum(ord(c) for c in x) % 50
unused_engagement = {e: engagement_index(e) for e in metrics.keys()}

# Risk factor based on error rate and debug frequency
risk_assessment = {}
for emp, data in metrics.items():
    error_rate = data['total_errors'] / max(data['total_time'], 1) * 100
    debug_ratio = data['debug_count'] / len([l for l in task_logs if l['employee'] == emp])
    risk_assessment[emp] = error_rate * 2 + debug_ratio * 15

# Distractor: compute team averages that won't be used
avg_productivity = sum(productivity.values()) / len(productivity)
avg_risk = sum(risk_assessment.values()) / len(risk_assessment)
dummy_variance = sum((v - avg_productivity) ** 2 for v in productivity.values())

# Core evaluation logic
def evaluate_performance(prod_dict, risk_dict):
    weighted_sum = 0
    count = 0
    for emp in prod_dict:
        # Normalize and combine metrics
        normalized_prod = max(0, prod_dict[emp] / 50)
        normalized_risk = max(0, (10 - risk_dict[emp]))
        contribution = normalized_prod * (normalized_risk + 5)
        weighted_sum += contribution
        count += 1
    return int(weighted_sum // count) if count else 0

# Misleading intermediate calculation
phantom_score = sum(productivity.values()) - sum(risk_assessment.values())

# Key execution point
final_score = evaluate_performance(productivity, risk_assessment)

# Dead code path (never executed)
if False:
    final_score *= 2
    debug_snapshot = metrics.copy()

print(f"Result: {final_score}")