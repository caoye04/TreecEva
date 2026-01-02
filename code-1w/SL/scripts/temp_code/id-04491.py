def analyze_efficiency(metrics):
    adjusted = [m * 1.1 for m in metrics if m > 5]
    return sum(adjusted) // len(adjusted) if adjusted else 0

productivity = [8, 7, 9, 4, 6]
overhead_costs = [200, 350, 180, 400]  # Distractor: not used
risk_levels = {'alpha': 0.8, 'beta': 0.5, 'gamma': 0.9}
baseline = 7.0

# Simulate intermediate analysis with red herring computation
temp_analysis = []
for val in productivity:
    if val >= baseline:
        temp_analysis.append(val ** 2)
dummy_aggregate = sum(temp_analysis) * 0.1  # Irrelevant aggregation

# Real signal extraction
efficiency = analyze_efficiency(productivity)
flags = [1 for x in productivity if x < 5]
trigger_count = len(flags)  # Used only if risk is high

# Risk assessment using dictionary lookup and conditional expression
risk_factor = risk_levels['gamma'] if trigger_count > 0 else risk_levels['alpha']

# Auxiliary calculation (distraction)
simulated_loss = 0
for i in range(len(overhead_costs)):
    simulated_loss += overhead_costs[i] * 0.01
simulated_loss = round(simulated_loss, 2)

# Core logic: performance evaluation
penalty = 10 if efficiency < 8 else 0
bonus = 5 if efficiency >= 8 and risk_factor < 0.8 else 0

# Key statement
final_score = evaluate_performance(productivity, risk_factor)

# Helper function defined after use (adds cognitive load)
def evaluate_performance(p, r):
    base = sum(p) / len(p)
    adjustment = 1 - abs(r - 0.7)
    # Combinatorics-inspired weight: number of pairs above threshold
    high_performers = len([i for i in p if i >= 7])
    combinatorial_weight = (high_performers * (high_performers - 1)) // 2 if high_performers > 1 else 0
    return int(base * adjustment + combinatorial_weight - penalty + bonus)

print(f"Result: {final_score}")