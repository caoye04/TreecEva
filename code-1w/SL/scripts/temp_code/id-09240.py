def analyze_risk_profile(inputs):
    risk_scores = []
    for i, val in enumerate(inputs):
        if i % 2 == 0:
            risk_scores.append(val ** 2)
        else:
            risk_scores.append(val + 5)
    return risk_scores

# Environmental simulation parameters
exposure_levels = [3, 7, 2, 8, 4]
stress_factors = [1, -2, 3, -1, 2]
baseline_offset = 10

# Irrelevant intermediate transformation (distractor)
dummy_weights = [x * 0.5 for x in exposure_levels]
weighted_sum = sum(dummy_weights)  # unused

# Simulate feedback loops with conditional logic
adjusted_levels = []
for idx, (exp, stress) in enumerate(zip(exposure_levels, stress_factors)):
    adjustment = 0
    if exp > 5:
        adjustment += baseline_offset // 2
    if stress < 0:
        adjustment -= abs(stress) * 3
    adjusted_levels.append(exp + adjustment)

# Secondary distraction: modeling unrelated decay process
decay_curve = []
for i in range(len(exposure_levels)):
    decay = exposure_levels[i] * (0.9 ** i)
    decay_curve.append(round(decay, 3))
unused_metric = sum(decay_curve)  # dead-end computation

# Core logic: evaluate system yield under combined factors
def harvest_results(x_levels, s_factors):
    total_yield = 0
    penalty_tracker = 0
    
    for i, (level, factor) in enumerate(zip(x_levels, s_factors)):
        base_yield = level * 10
        
        # Conditional bonus based on index and stress interaction
        if factor > 0 and i % 3 == 0:
            base_yield += 15
        
        # Penalty logic with bitwise condition (modular arithmetic + XOR)
        if (level + factor) % 4 == 0 or (i ^ factor) == 1:
            penalty_tracker += 1
            base_yield -= 20
        
        total_yield += base_yield
    
    # Final adjustment independent of penalty_tracker but uses same variable
    total_yield -= penalty_tracker * 5
    return total_yield

# Execute core evaluation
temp_diagnostic = analyze_risk_profile(exposure_levels)  # distractor call
final_yield = harvest_results(adjusted_levels, stress_factors)
print(f"Result: {final_yield}")