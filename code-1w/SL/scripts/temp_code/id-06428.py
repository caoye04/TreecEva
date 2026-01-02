def analyze_efficiency(workload, downtime):
    if workload <= 0:
        return 0
    efficiency = (workload - downtime) / workload
    return efficiency if efficiency > 0 else 0

productivity = 0
risk_factor = 0
baseline = [80, 95, 70, 100]
metrics = {"stress": [], "output": []}

for i in range(len(baseline)):
    adjusted = baseline[i] * (1.1 if i % 2 == 0 else 0.9)
    decay = (i + 1) * 2
    processed = adjusted - decay
    
    # Distractor: irrelevant tracking
    metrics["output"].append(processed * 0.95)
    metrics["stress"].append((processed / 10) ** 2)
    
    temp_efficiency = analyze_efficiency(adjusted, decay)
    
    # Real signal mixed with noise
    score_boost = 10 if processed > 85 else 0
    risk_penalty = 5 if decay > 4 else 0
    
    productivity += temp_efficiency * 25 + score_boost
    risk_factor += risk_penalty * (i + 1)

# Misleading complex-looking but unused calculation
total_stress = sum(metrics["stress"])
avg_output = sum(metrics["output"]) / len(metrics["output"]) if metrics["output"] else 0
phantom_weight = (total_stress / (avg_output + 1)) * 0.01 if avg_output > 0 else 0

# Conditional expression used appropriately
critical_threshold = 75
is_high_load = len(baseline) > 3 and max(baseline) >= critical_threshold

scaling_factor = 1.25 if is_high_load else 0.8

# Final computation chain
intermediate_result = productivity * scaling_factor - (risk_factor * 2.5)

# Key statement
final_score = evaluate_performance(productivity, risk_factor)

# Supporting function defined late to obscure flow
def evaluate_performance(output, risk):
    base = output * 0.75
    adjustment = base * (0.1 if risk > 10 else -0.05)
    return int(base - adjustment + (5 if risk % 2 == 1 else 0))

print(f"Result: {final_score}")