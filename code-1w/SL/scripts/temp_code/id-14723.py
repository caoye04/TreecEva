def analyze_efficiency(metrics):
    baseline = sum(metrics) / len(metrics)
    adjusted = [x * 0.9 + 1.1 for x in metrics if x > baseline]
    return sum(adjusted) if adjusted else baseline


def calculate_stress_level(workload, breaks):
    stress_index = workload / (breaks + 1)
    penalty = 5 if workload > 40 else 0
    return stress_index + penalty

productivity = [85, 90, 78, 92, 88]
risk_factor = 3
temporary_weights = [1.1, 0.9, 1.05, 0.95, 1.0]

# Irrelevant transformation chain
distorted_productivity = [p * w for p, w in zip(productivity, temporary_weights)]
shifted_values = distorted_productivity[1:] + [distorted_productivity[0]]
avg_shifted = sum(shifted_values) / len(shifted_values)

# Misleading intermediate calculation
effective_load = sum(p * 1.05 for p in productivity if p < 88)
phantom_threshold = 80 if avg_shifted > 85 else 70

# Conditional expression with slicing
peak_phase = productivity[-3:] if sum(productivity[-3:]) > 250 else productivity[:3]
concentration = sum(peak_phase) / len(peak_phase)

# Dummy dictionary for distraction
diagnostic_log = {
    'phases': len(productivity),
    'max': max(productivity),
    'flagged': any(p < 80 for p in productivity),
    'ignored_metric': calculate_stress_level(45, 2)
}

# Key logic hidden among distractors
def evaluate_performance(output, risk):
    efficiency = analyze_efficiency(output)
    bonus = 10 if concentration > 85 else 5
    # Nested conditionals and logical operations
    adjustment = risk * (-1 if efficiency < 85 else 1)
    raw_score = efficiency + bonus + adjustment
    # Final adjustment using conditional expression and slicing
    final_boost = raw_score * 1.1 if output[::-1][:2][0] > 80 else raw_score * 0.95
    return int(final_boost)

# Execution point of interest
final_score = evaluate_performance(productivity, risk_factor)
print(f"Target result: {final_score}")