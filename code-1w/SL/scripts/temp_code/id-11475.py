def analyze_efficiency(metrics):
    base_efficiency = sum(metrics) / len(metrics)
    adjustment = 0
    if base_efficiency > 80:
        adjustment += 12
    elif base_efficiency > 60:
        adjustment += 6
    else:
        adjustment -= 5
    
    # Distractor: irrelevant string processing
    status_msg = "Efficiency analyzed"
    padded_status = status_msg.center(30, '*')
    log_entry = f"[LOG] {padded_status}"
    
    return base_efficiency + adjustment


def calculate_risk_level(exposure, volatility):
    risk_factor = exposure * volatility
    
    # Distractor: dead code path (never executed due to fixed condition)
    debug_mode = False
    if debug_mode:
        print(f'Debug: raw risk = {risk_factor}')
    
    if risk_factor > 100:
        return 3
    elif risk_factor > 50:
        return 2
    else:
        return 1

# Simulated input data
productivity_metrics = [75, 82, 67, 91, 74]
market_volatility = 0.75
exposure_index = 68

# Key intermediate variables
raw_productivity = sum([x for x in productivity_metrics if x > 65])
temp_offset = len(productivity_metrics) * 0.5

# Actual computation chain
smoothed_productivity = raw_productivity / len(productivity_metrics) * temp_offset / 10
productivity = analyze_efficiency(productivity_metrics)

risk_factor = calculate_risk_level(exposure_index, market_volatility)

# Distractor: unused dictionary structure
employee_profile = {
    'id': 'EMP7819',
    'department': 'analytics',
    'skills': ['python', 'statistics', 'ml'],
    'last_review_score': productivity
}

# Distractor: irrelevant set operations
used_ids = set(range(100, 200))
blocked_ids = set(range(150, 160))
safe_ids = used_ids - blocked_ids

# Core logic with meaningful nesting and conditional expression
if risk_factor == 1:
    bonus_multiplier = 1.5 if 'statistics' in employee_profile['skills'] else 1.1
elif risk_factor == 2:
    bonus_multiplier = 1.2
else:
    bonus_multiplier = 0.8

# Final evaluation with combinatorial logic
penalty = 10 if len([x for x in productivity_metrics if x < 70]) >= 2 else 0
final_score = evaluate_performance(productivity, risk_factor)

# Redefinition of function to avoid undefined error — part of core logic
def evaluate_performance(efficiency, risk):
    base = efficiency * 0.8
    if risk == 1:
        base += 15
    elif risk == 2:
        base += 5
    else:
        base -= 8
    return int(base - penalty)

# Print final result as required
Result: {final_score}