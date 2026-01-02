def evaluate_performance(output, risk):
    base_efficiency = output * 0.85
    adjusted_risk = max(1.0, 10 - risk)
    bonus = 10 if output > 50 else 5
    penalty = 20 if risk > 8 else 0
    
    # Distractor: Historical metrics not used in final calculation
    historical_avg = 72.3
    compliance_check = True if output % 2 == 0 else False
    shadow_metric = (output + risk) // 3

    # Real computation path
    raw_score = base_efficiency * adjusted_risk + bonus - penalty
    
    # Conditional expression usage
    multiplier = 1.2 if output > 40 and risk < 6 else 1.0
    enhanced_score = raw_score * multiplier
    
    # Set operations as red herring
    departments = {'A', 'B', 'C'}
    active_departments = {'B', 'C'}
    idle_count = len(departments - active_departments)
    
    # Final adjustment using conditional expression
    final_value = enhanced_score + (10 if idle_count == 1 else 0)
    return int(final_value)

# Simulated input data
productivity = 60
risk_factor = 7
auxiliary_data = [3, 6, 9]
deprecated_flag = False

# Irrelevant loop (dead code path)
intermediate_results = []
for x in auxiliary_data:
    temp = x ** 2 - 1
    if temp > 10:
        intermediate_results.append(temp)

# Key execution point
final_score = evaluate_performance(productivity, risk_factor)
print(f"Result: {final_score}")