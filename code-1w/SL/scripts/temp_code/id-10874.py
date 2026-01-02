def analyze_efficiency(logs):
    total_ops = sum(logs)
    avg_op_time = sum([x**0.5 for x in logs]) / len(logs) if logs else 0
    efficiency_ratio = total_ops / (avg_op_time + 1)
    return efficiency_ratio

logs_data = [12, 8, 15, 6, 22, 14]

# Misleading preprocessing
normalized_logs = [x / max(logs_data) for x in logs_data]
decay_factor = 0.95
weighted_sum = sum([x * (decay_factor ** i) for i, x in enumerate(reversed(normalized_logs))])

# Real signal extraction
raw_efficiency = analyze_efficiency(logs_data)
productivity = int(raw_efficiency // 10)

# Simulate risk adjustment with distractors
temp_buffers = [i * productivity for i in range(3)]
buffer_utilization = sum(temp_buffers) % 7 if temp_buffers else 0

# Dummy risk logic
baseline_risk = 5
fluctuation_index = (len(logs_data) * buffer_utilization) % 4
risk_factor = baseline_risk - fluctuation_index

# Core evaluation logic
penalty_func = lambda p, r: p * 1.5 if r < 3 else p * 0.8
bonus_applied = False
if risk_factor > 2:
    productivity += 2
    bonus_applied = True

adjusted_productivity = penalty_func(productivity, risk_factor) if not bonus_applied else productivity * 1.1

# Final scoring with red herring computations
deprecated_metric = sum([i**(2) for i in range(1, 6)])  # Unused legacy calculation
scaling_constant = 3.14159
theoretical_max = scaling_constant * len(logs_data)

final_score = evaluate_performance(adjusted_productivity, risk_factor)

# Helper function defined after use (tests reasoning continuity)
def evaluate_performance(p, r):
    base = p * 10
    if r < 3:
        base -= 15
    elif r >= 4:
        base += 5
    else:
        base += 10
    # Additional logic to increase nesting and steps
    modifier = 2 if p > 20 else 1
    return int(base * modifier)

print(f"Result: {final_score}")