from itertools import combinations

# Simulate employee performance metrics across departments
def analyze_department_efficiency(base_rate, overtime_hours):
    efficiency = base_rate * (1 + 0.05 * overtime_hours)
    penalty = 0.0
    if overtime_hours > 10:
        penalty = 0.1 * (overtime_hours - 10)
    adjusted_efficiency = efficiency - penalty
    return adjusted_efficiency

# Calculate team synergy score based on pairwise compatibility
def compute_synergy(team_members):
    if len(team_members) < 2:
        return 0.0
    total_compatibility = 0.0
    compat_pairs = list(combinations(team_members, 2))
    for a, b in compat_pairs:
        total_compatibility += (a % 3) * (b % 4) / 8.0
    return round(total_compatibility, 4)

# Core evaluation function with mixed logic paths
def evaluate_performance(output_log, risk_factor):
    base_score = 0
    adjustment = 0.0
    spike_count = 0

    for val in output_log:
        if val > 80:
            spike_count += 1
            adjustment += 0.05
        elif val < 20:
            adjustment -= 0.02

    # Apply non-linear transformation using lambda
    transform = lambda x: x ** 0.5 if x > 0 else 0
    transformed_spike = int(transform(spike_count * 4))

    # Dummy tracking variables (not used in final result)
    anomaly_flags = [0] * len(output_log)
    for i, v in enumerate(output_log):
        if v < 10 or v > 90:
            anomaly_flags[i] = 1

    # Irrelevant statistical moment calculation (dead computation)
    mean_val = sum(output_log) / len(output_log)
    variance_proxy = sum((x - mean_val) ** 2 for x in output_log) / len(output_log)
    skewness_like = sum((x - mean_val) ** 3 for x in output_log) / (len(output_log) * (variance_proxy ** 1.5) or 1)

    # Key logic branch with conditional override
    if risk_factor > 0.7 and spike_count >= 3:
        base_score = 65
    elif risk_factor < 0.3:
        base_score = 85
    else:
        base_score = 75

    # Final score depends only on base_score, transformed_spike, and fixed offset
    final_component = base_score + transformed_spike * 5 - int(risk_factor * 10)
    return final_component

# Simulated input data
productivity = [85, 12, 92, 45, 88, 96, 18, 77]
risk_level = 0.68

# Auxiliary calculations with limited impact
dept_efficiency = analyze_department_efficiency(0.85, 12)
synergy_score = compute_synergy([2, 5, 7, 9])
temp_diagnostic = [x for x in productivity if x > 50]

# Critical execution point
final_score = evaluate_performance(productivity, risk_level)
print(f"Result: {final_score}")