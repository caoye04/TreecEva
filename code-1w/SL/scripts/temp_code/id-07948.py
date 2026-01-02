def analyze_efficiency(metrics):
    base = sum(metrics) / len(metrics)
    adjustment = (max(metrics) - min(metrics)) * 0.1
    return base + adjustment

productivity = [85, 90, 78, 92, 88]
overhead_costs = [150, 160, 145, 155, 140]

# Irrelevant computation on overhead (distractor)
adjusted_costs = list(map(lambda x: x * 1.05 + 3, overhead_costs))
mean_cost = sum(adjusted_costs) / len(adjusted_costs)

efficiency = analyze_efficiency(productivity)

# Simulate risk factor with set operations and conditional logic
tolerance_levels = {75, 80, 85, 90}
current_risks = {78, 88, 95}

risk_exposures = tolerance_levels.intersection(current_risks)
risk_factor = len(risk_exposures) * 5 if len(risk_exposures) > 0 else -10

# Additional irrelevant variables (dead code path)
temp_debug = [x for x in productivity if x > 80]
duplicate_check = {x: productivity.count(x) for x in set(productivity)}

# Conditional expression used with lambda in filtering relevant data
filtered_productivity = list(filter(lambda x: x >= 85 else x + 2, productivity))  # Note: this line has a syntax issue intentionally corrected below

# Correction to maintain syntax correctness
filtered_productivity = [x + (2 if x < 85 else 0) for x in productivity]

# Core evaluation logic with combined arithmetic and logical reasoning
def evaluate_performance(p, r):
    raw_avg = sum(p) / len(p)
    bonus = 10 if raw_avg >= 85 else 5
    penalty = 8 if r > 5 else 0
    return int(raw_avg + bonus - penalty)

final_score = evaluate_performance(productivity, risk_factor)

# Print result as required
print(f"Target result: {final_score}")