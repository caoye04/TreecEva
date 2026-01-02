from itertools import combinations

def analyze_efficiency(tasks, overhead):
    efficiency = 0
    temp_result = 0
    for i in range(2, len(tasks) + 1):
        for combo in combinations(tasks, i):
            product = 1
            for t in combo:
                product *= t
            efficiency += product % 7
    adjustment = len(tasks) ** 2 - overhead
    if adjustment > 10:
        efficiency -= adjustment // 4
    return efficiency


def calculate_risk(elements):
    seen = set()
    risk = 0
    for x in elements:
        if x in seen:
            risk += x
        else:
            seen.add(x)
    return risk * 0.5


def evaluate_performance(output, risk):
    base = output * 2.5
    penalty = 0
    if risk > 10:
        penalty = (risk - 10) * 1.2
    return int(base - penalty)

# Main execution
workload = [3, 5, 2, 5, 7]
overhead_cost = 8

# Irrelevant intermediate computations
redundant_sum = sum(x**2 for x in workload if x % 2 == 1)
duplicate_tracker = {x: workload.count(x) for x in set(workload)}
temp_cache = [a + b for a, b in combinations(workload[:3], 2)]

productivity = analyze_efficiency(workload, overhead_cost)
risk_factor = calculate_risk(workload)

# Key statement
final_score = evaluate_performance(productivity, risk_factor)

# Distractor variables
normalization_factor = 1.0 / (sum(workload) or 1)
validation_check = redundant_sum > 50

print(f"Result: {final_score}")