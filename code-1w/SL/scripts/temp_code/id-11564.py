def analyze_efficiency(metrics):
    efficiency_list = []
    for i, val in enumerate(metrics):
        if i % 2 == 0:
            efficiency_list.append(val * 1.5)
        else:
            efficiency_list.append(val * 0.8)
    return efficiency_list

metrics_data = [12, 18, 24, 30, 42]
efficiency_results = analyze_efficiency(metrics_data)

# Misleading computation with dead weight
temp_multiplier = 1.05
weighted_sum = 0
for x in efficiency_results:
    weighted_sum += x * temp_multiplier  # Not used later

baseline = sum(efficiency_results) / len(efficiency_results)
adjusted_metrics = [x for x in efficiency_results if x > baseline]

# Simulate risk profile using set operations
risk_factors = {14.4, 19.2, 27.0, 36.0, 48.0}
high_risk_threshold = 25.0
risk_set = {x for x in risk_factors if x < high_risk_threshold}

productivity = 0
for i, val in enumerate(adjusted_metrics):
    productivity += val * (i + 1)

# Unused helper variables to increase cognitive load
shadow_productivity = productivity * 0.95
dummy_scale = len(risk_factors) - len(risk_set)

scaling_factor = len(adjusted_metrics) / (len(risk_set) + 1)

# Key function with conditional logic and string-based filtering
def evaluate_performance(prod, risks):
    penalty = 0
    performance_class = ""
    
    if prod > 100:
        performance_class = "high"
        if len(risks) >= 3:
            penalty = 15
        elif len(risks) == 2:
            penalty = 10
        else:
            penalty = 5
    else:
        performance_class = "medium"
        penalty = 20
    
    # Use of string method in logic (real but subtle use)
    if "h" in performance_class.upper():
        bonus = 10
    else:
        bonus = 0
    
    # Final score calculation
    raw_score = prod - penalty + bonus
    normalized = raw_score * (0.1 + scaling_factor)  # Uses outer scope
    return int(normalized)

final_score = evaluate_performance(productivity, risk_set)
print(f"Target result: {final_score}")