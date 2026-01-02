def evaluate_performance(efficiency, hazards):
    # Core metrics
    critical_tasks = {x for x in efficiency if x > 70}
    avoided_risks = {x for x in hazards if x < 30}
    
    # Intermediate calculations with some distractions
    total_effort = sum(efficiency)  # Used only for logging
    avg_risk_level = sum(hazards) / len(hazards)
    compliance_rate = len(avoided_risks) / len(hazards) * 100
    
    # Distractor: Irrelevant transformation
    normalized = [round((x - min(efficiency)) / (max(efficiency) - min(efficiency)) * 100) for x in efficiency]
    enhanced_normalized = [n + 5 for n in normalized if n < 80]  # Dead code path
    
    # Key logic: performance score based on overlap
    synergy_elements = critical_tasks.intersection(set(hazards))
    penalty = len(synergy_elements) * 2
    base_score = len(critical_tasks) * 10
    adjustment = 0
    
    # Conditional adjustment based on risk behavior
    if compliance_rate > 50:
        adjustment += 15
    else:
        adjustment -= 10
    
    # Final computation
    final_score = base_score - penalty + adjustment
    
    # Additional red herring: unused dictionary aggregation
    stats_summary = {
        'peak_efficiency': max(efficiency),
        'min_hazard': min(hazards),
        'risk_distribution': {i: hazards.count(i) for i in set(hazards) if i < 40},
        'phantom_metric': sum(enhanced_normalized) // len(enhanced_normalized) if enhanced_normalized else 0
    }
    
    return final_score

# Input data
productivity_data = [65, 72, 78, 85, 60, 90, 44]
risk_exposure = [25, 35, 28, 90, 78, 22, 88]

# Execution point of interest
final_score = evaluate_performance(productivity_data, risk_exposure)
print(f"Result: {final_score}")