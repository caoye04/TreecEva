def analyze_efficiency(logs):
    total_entries = len(logs)
    valid_records = [entry for entry in logs if entry > 0]
    avg_time = sum(valid_records) / len(valid_records) if valid_records else 0
    return avg_time

logs_data = [12, -5, 8, 0, 15, -3, 7, 9, 11]

# Irrelevant transformation (distractor)
transformed_logs = [x ** 2 for x in logs_data if x % 2 != 0]
dummy_metric = sum(transformed_logs) / 10 if transformed_logs else 0

avg_efficiency = analyze_efficiency(logs_data)

# Simulate productivity index using slicing and filtering
top_performers = logs_data[1:6]  # slice of mid-range data
productivity = sum(top_performers) // len(top_performers) if top_performers else 0

# Risk assessment via set operations and bitwise check
critical_flags = {12, 8, 15, 7}
observed_flags = set(logs_data)
matched_flags = critical_flags & observed_flags
risk_count = len(matched_flags)
risk_factor = risk_count << 1  # Left shift as weight

# Use lambda to compute conditional adjustment
adjustment_func = lambda x, y: x ^ y if x > 5 else x | y
adjusted_risk = adjustment_func(risk_factor, 3)

# Final performance evaluation with modular arithmetic
def evaluate_performance(p, r):
    base_score = p * 10
    penalty = (r ** 2) % 7
    bonus = 5 if p >= 8 else 0
    return base_score - penalty + bonus + (len(logs_data) % 3)

final_score = evaluate_performance(productivity, risk_factor)

# Additional irrelevant computations (dead code path)
if dummy_metric > 100:
    final_score *= 2

# Print result for verification
print(f"Result: {final_score}")