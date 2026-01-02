def evaluate_performance(data, importance):
    base = sum(x * y for x, y in zip(data, importance))
    adjustment = 0
    
    # Irrelevant preprocessing: normalizing data (not used in final computation)
    normalized = [x / max(data) for x in data]
    temp_sum = sum(normalized)
    dummy_calc = temp_sum * 0.1
    
    # Semi-relevant logic: conditional bonus based on threshold
    threshold = 50
    performance_flags = [1 if x >= threshold else 0 for x in data]
    bonus = 5 if sum(performance_flags) >= 2 else 0
    
    # Distractor: unused helper function
    calculate_risk = lambda vals: sum(v ** 0.5 for v in vals) / len(vals)
    risk_metric = calculate_risk(data)  # Computed but not used
    
    # Another red herring: tracking a state that doesn't affect outcome
    status_log = []
    for i, val in enumerate(data):
        if val > 60:
            status_log.append(f"High at {i}")
        elif val < 30:
            status_log.append(f"Low at {i}")
    
    # Core logic with modular arithmetic twist
    modifier = 0
    for i in range(len(data)):
        if data[i] % 10 == 0 and importance[i] > 0.2:
            modifier += 2
    
    # Final score calculation
    final_score = base + bonus + modifier
    return final_score

# Main execution
metrics = [45, 60, 30]
weights = [0.4, 0.5, 0.1]

# Intermediate distraction: unused weight analysis
weight_analysis = list(map(lambda w: round(w * 100), weights))
disparity = max(weight_analysis) - min(weight_analysis)

# Key statement
final_score = evaluate_performance(metrics, weights)
print(f"Result: {final_score}")