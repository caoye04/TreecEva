def analyze_efficiency(metrics):
    base_efficiency = sum([m * (i + 1) for i, m in enumerate(metrics)])
    adjustment = len(metrics) % 3
    if adjustment > 0:
        base_efficiency -= adjustment * 2
    return base_efficiency

productivity = [7, 5, 9, 3, 8]
overhead_costs = [2, 4, 1]  # Unused distractor list
waste_factor = 0
for cost in overhead_costs:
    waste_factor += cost ** 2  # Irrelevant computation

risk_levels = {1: 'low', 2: 'medium', 3: 'high'}
risk_set = set(risk_levels.keys())
risk_set.add(4)
risk_set.discard(1)

# Semi-relevant transformation
risk_index = sum(risk_set) % 5

# Dummy function that isn't used
def dummy_util(val):
    return val * val + 1

# Character counting distraction
project_name = "OptimaPrime"
duplicate_chars = len(project_name) - len(set(project_name))

scaling_factor = 1.5
raw_efficiency = analyze_efficiency(productivity)

# Multiple assignments with some irrelevant ones
intermediate_a, intermediate_b = raw_efficiency // 4, raw_efficiency % 7
intermediate_c = intermediate_a ^ intermediate_b  # Bitwise red herring

safety_margin = 3
risk_factor = max(risk_index, safety_margin)

# Core logic embedded among noise
adjusted_productivity = raw_efficiency - (risk_factor * 2)

def evaluate_performance(p, r):
    base = p + 10
    if r > 4:
        base *= 0.8
    else:
        base *= 1.1
    bonus = 5 if p > 30 else 0  # Dead code path (p unlikely >30)
    return int(base)

final_score = evaluate_performance(productivity, risk_factor)
print(f"Result: {final_score}")