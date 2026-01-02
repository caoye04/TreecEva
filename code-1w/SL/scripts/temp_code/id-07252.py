from itertools import combinations

# Simulate employee productivity and risk metrics across departments
def calculate_efficiency(base, load):
    return base * (1.5 - load / 10)

def analyze_stability(record):
    return sum(1 for x in record if x < 3) > len(record) // 2

def generate_risk_profile(data):
    high_alerts = 0
    for item in data:
        if item > 8:
            high_alerts += 1
    return high_alerts / len(data) if data else 0

def filter_outliers(values):
    mean_val = sum(values) / len(values)
    return [v for v in values if abs(v - mean_val) <= 2]

def evaluate_performance(productivity, risk_factor):
    if risk_factor > 0.5:
        return int(productivity * 0.7)
    elif productivity > 40:
        return int(productivity * 1.1)
    else:
        return int(productivity)

# Departmental data
base_productivity = 38
workload = 4
historical_errors = [2, 1, 4, 2, 5, 3]
daily_metrics = [7, 9, 6, 10, 8, 7, 9]

# Irrelevant distraction: unused team roles
team_roles = {'A': 'Lead', 'B': 'Dev', 'C': 'QA', 'D': 'Ops'}
task_distribution = {role: len(name) for name, role in team_roles.items()}

# Compute intermediate metrics
productivity = calculate_efficiency(base_productivity, workload)
is_stable = analyze_stability(historical_errors)
risk_data = generate_risk_profile(daily_metrics)
clean_metrics = filter_outliers(daily_metrics)

# Create synthetic pairs (unused distractor)
pairwise_combinations = list(combinations(clean_metrics, 2))
valid_pairs = [p for p in pairwise_combinations if p[0] + p[1] > 15]

# Set operations to demonstrate python idiom (partially relevant)
unique_metrics = set(daily_metrics)
filtered_set = set(clean_metrics)
overlap_count = len(unique_metrics & filtered_set)

# Final performance calculation
risk_factor = risk_data if not is_stable else risk_data * 1.2
final_score = evaluate_performance(productivity, risk_factor)

print(f"Result: {final_score}")