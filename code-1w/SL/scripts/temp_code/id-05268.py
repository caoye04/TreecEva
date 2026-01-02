def analyze_efficiency(values):
    filtered = [v for v in values if v > 0]
    squared = [x ** 2 for x in filtered]
    avg = sum(squared) / len(squared) if squared else 0
    return avg

productivity = [3, -1, 4, 1, 5, -2, 9]
overhead_costs = [10, 20, 30]  # Irrelevant data
baseline = sum([x // 2 for x in productivity if x % 2 == 0])

# Simulate resource allocation (distraction)
allocations = {}
for i in range(len(productivity)):
    if i % 2 == 0:
        allocations[i] = productivity[i] * 1.5
    else:
        allocations[i] = productivity[i] * 0.8

# Risk modeling using set operations
risk_factors = {1, 3, 5, 7, 9}
tolerance_level = {2, 4, 6, 8}
risk_set = risk_factors - tolerance_level  # Only odd risks retained
exposure = len(risk_set & set(productivity))

# Auxiliary calculation with no impact
phantom_sum = 0
for val in overhead_costs:
    phantom_sum += val * 0.1

# Core evaluation logic
performance_boost = analyze_efficiency(productivity)
penalty = len(risk_set.intersection({1, 2})) * 2.5

# Key statement
final_score = evaluate_performance(productivity, risk_set)

# Helper function defined after use (testing parsing robustness)
def evaluate_performance(p, r):
    base = sum(x for x in p if x in r)
    modifier = len(r) - min(r) if r else 0
    temp_result = base * modifier
    # Additional distraction: unused branching
    if temp_result < 0:
        temp_result = abs(temp_result)
    return int(temp_result + 0.5)

print(f"Result: {final_score}")