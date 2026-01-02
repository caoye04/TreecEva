from itertools import combinations

# Simulate employee performance evaluation across teams
def calculate_synergy(team):
    return sum([a * b for a, b in combinations(team, 2)])

# Auxiliary function to compute workload distribution index
def compute_wdi(tasks, employees):
    if len(employees) == 0:
        return 0
    avg_tasks = tasks / len(employees)
    variance = sum((t - avg_tasks) ** 2 for t in employees)
    return variance / len(employees)

# Main productivity model with distraction paths
productivity = [85, 90, 78, 92, 88]
risk_factor = [0.1, 0.3, 0.2, 0.4, 0.25]
workloads = [20, 22, 18, 24, 21]
dummy_matrix = [[i * j for j in range(4)] for i in range(4)]  # Irrelevant matrix computation

# Dead code path - never executed but looks important
def deprecated_eval(data):
    return [x ** 0.5 for x in data if x > 80]

# Misleading intermediate calculations
temporal_weights = [0.95 ** i for i in range(len(productivity))]
weighted_productivity = sum(p * w for p, w in zip(productivity, temporal_weights))
adjusted_risk = sum(risk_factor) * 1.15  # Unused adjustment

# Real processing begins here
synergy_score = calculate_synergy([p // 10 for p in productivity])
base_performance = sum(productivity) / len(productivity)
penalty = 0
for i, r in enumerate(risk_factor):
    if r > 0.2:
        penalty += productivity[i] * r * 0.1

# Simulate false branch that doesn't affect outcome
if base_performance < 80:
    final_boost = 10
else:
    final_boost = 0  # Not actually used

# Core logic hidden among distractions
aggregate_risk = sum(risk_factor[i] ** 2 for i in range(len(risk_factor)))
final_score = base_performance - penalty + synergy_score

# Print result as required
print(f"Result: {final_score}")