def analyze_efficiency(metrics):
    adjusted_metrics = [m * 1.1 for m in metrics if m > 5]
    return sum(adjusted_metrics) // len(adjusted_metrics) if adjusted_metrics else 0

productivity = [8, 7, 6, 9, 4, 10]
overhead_costs = [200, 150, 300]  # Irrelevant distractor list
baseline = 7

efficiency_rating = analyze_efficiency(productivity)

# Simulate risk assessment with string-based flags
risk_flags = ['low', 'medium', 'high']
operation_status = 'nominal'
risk_index = len(risk_flags) - 1

if efficiency_rating >= baseline:
    risk_factor = risk_index * 0.5
    temp_buffer = [x for x in productivity if x % 2 == 0]  # Semi-relevant: not used later
else:
    risk_factor = risk_index * 0.8

# Use slicing and set operations for data refinement (some redundant)
refined_data = productivity[1:4]
distinct_values = set(refined_data)
distinct_count = len(distinct_values)

# Apply conditional logic with logical operations
is_optimal = efficiency_rating > baseline and distinct_count >= 3
penalty_rate = 0.9 if not is_optimal else 1.0

# Core computation chain
base_performance = sum(productivity) / len(productivity)
scaled_risk = risk_factor ** 2
final_score = 0

# Key statement
final_score = evaluate_performance(base_performance, risk_factor)

# Helper function defined after use (adds cognitive load)
def evaluate_performance(perf, risk):
    stability_adjustment = 10 if perf >= 7.0 else 5
    risk_penalty = 20 * risk
    raw_score = perf * 10 + stability_adjustment - risk_penalty
    return int(raw_score * penalty_rate)  # Final score influenced by earlier branch

# Dead code path (distractor)
if operation_status == 'critical':
    final_score += 100

print(f"Result: {final_score}")