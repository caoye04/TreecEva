def evaluate_performance(output, risk):
    base_efficiency = 85
    adjustment = 0
    
    # Distractor: Historical metrics not used in final calculation
    historical_avg = [78, 83, 80, 86]
    peak_performance = max(historical_avg)
    decay_rate = 0.95
    projected_next = peak_performance * decay_rate
    
    # Real logic begins
    if output > 90:
        adjustment += 12
    elif output >= 80:
        adjustment += 7
    else:
        adjustment -= 5

    # Risk adjustment using lambda
    risk_penalty = (lambda r: 10 if r > 7 else (5 if r > 4 else 0))(risk)
    adjustment -= risk_penalty

    # Use of set operations to filter noise
    valid_outputs = {80, 85, 90, 95, 100}
    if output in valid_outputs:
        adjustment += 3

    # List comprehension for secondary metric (unused but plausible)
    recent_trends = [x * 1.05 for x in historical_avg if x > 80]
    trend_boost = len(recent_trends) * 0.5  # Not actually used

    # Conditional branch affecting result
    if output >= 85 and risk < 5:
        adjustment += 4

    final_rating = base_efficiency + adjustment
    return final_rating

# Simulated inputs
productivity = 92
risk_factor = 6
monitoring_log = {'status': 'active', 'interval': 5}
baseline_threshold = 75  # Unused parameter

# Key computation
final_score = evaluate_performance(productivity, risk_factor)

# Dead code path - misleading control flow
if monitoring_log['status'] == 'inactive':
    final_score *= 0.9

Result: {final_score}