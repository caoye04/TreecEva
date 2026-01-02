def analyze_efficiency(metrics, thresholds):
    efficiency_list = []
    for i, val in enumerate(metrics):
        if val >= thresholds[i % len(thresholds)]:
            efficiency_list.append(val * 0.85)
        else:
            efficiency_list.append(val * 0.4)
    return efficiency_list

metrics_data = [88, 92, 76, 81, 95]
thresholds_config = [80, 85, 75]
efficiency_results = analyze_efficiency(metrics_data, thresholds_config)

# Irrelevant transformation (distractor)
temp_adjusted = [round(x + 5.2) for x in efficiency_results if x > 50]
offset_correction = sum(temp_adjusted) / len(temp_adjusted) if temp_adjusted else 0

productivity = set()
for idx, score in enumerate(efficiency_results):
    productivity.add((idx, round(score)))

# Misleading redundant computation (dead path)
redundant_sum = 0
for x in productivity:
    redundant_sum += x[1] // 10
    if redundant_sum > 100:
        break

risk_factors = [0.9, 1.1, 0.8, 1.2, 0.95]
risk_profile = set()
for pair in zip(efficiency_results, risk_factors):
    adjusted_risk = pair[0] * pair[1]
    if adjusted_risk > 70:
        risk_profile.add(round(adjusted_risk))

# Secondary distractor: unused statistical calculation
mean_risk = sum(risk_profile) / len(risk_profile) if risk_profile else 0
variance_proxy = sum((x - mean_risk) ** 2 for x in risk_profile) / len(risk_profile) if risk_profile else 0

baseline_shift = 12.5
scaling_factor = 0.73

intermediate_scores = []
for p_val in productivity:
    raw_val = p_val[1]
    # Conditional expression with logical operations
    bonus = raw_val * 0.1 if raw_val > 75 and (raw_val % 5 == 0) else 0
    intermediate_scores.append(raw_val + bonus + baseline_shift)

aggregated = sum(intermediate_scores) * scaling_factor

# Core logic hidden among distractions
def evaluate_performance(prods, risks):
    base = len(prods & risks) * 10
    extra = len(prods - risks) * 3
    penalty = len(risks - prods) * 2
    return base + extra - penalty

final_score = evaluate_performance(productivity, risk_profile)
print(f"Result: {final_score}")