def evaluate_performance(output, risk_profile):
    base_score = 0
    adjustment_factor = 0.0
    
    # Initial scoring based on output levels
    if output > 80:
        base_score += 40
    elif output > 60:
        base_score += 30
    else:
        base_score += 15
    
    # Irrelevant computation: team morale simulation (distractor)
    team_morale = [3.2, 4.1, 3.9, 4.0]
    avg_morale = sum(team_morale) / len(team_morale)
    performance_bonus = 0
    if avg_morale > 3.5:
        performance_bonus = 10  # Not used in final logic
    
    # Risk adjustment using set operations
    high_risk_flags = {1, 3, 5, 7, 9}
    medium_risk_flags = {2, 4, 6, 8}
    critical_risks = high_risk_flags & risk_profile  # Intersection
    potential_risks = medium_risk_flags & risk_profile
    
    # Distractor: unused risk analysis
    low_risk_count = len(risk_profile - high_risk_flags - medium_risk_flags)
    if low_risk_count > 0:
        adjustment_factor -= 0.5  # Has no real impact
    
    # Real risk penalty application
    critical_count = len(critical_risks)
    if critical_count >= 3:
        adjustment_factor -= 5.0
    elif critical_count >= 1:
        adjustment_factor -= 2.0
    
    # Additional distraction: legacy system compatibility check
    legacy_mode = False
    compatibility_matrix = {'v1': True, 'v2': False, 'v3': True}
    if compatibility_matrix.get('v2'):
        legacy_mode = True  # Dead code path
    
    # Final score accumulation with distractor variables
    temp_score = base_score + performance_bonus  # Bonus not actually valid
    final_adjusted = temp_score + int(adjustment_factor)
    
    # Key state tracking: efficiency tier
    efficiency_tier = ""
    if output > 75 and len(potential_risks) == 0:
        efficiency_tier = "optimal"
        final_adjusted += 5
    else:
        efficiency_tier = "standard"
    
    return final_adjusted

# Main execution context
productivity = 68
risk_exposure = {2, 4, 5, 9}  # Contains both medium and high risk
misc_data = [x ** 2 for x in range(5)]  # Irrelevant list comprehension

# Unused function call placeholder (distractor)
def log_activity(data):  
    timestamp = 1234567890
    entry = f"Log at {timestamp}: {len(data)} items"
    return entry

log_activity(misc_data)  # Execution has no side effect

interim_result = productivity * 1.5  # Computed but not crucial

# Critical execution point
final_score = evaluate_performance(productivity, risk_exposure)

print(f"Result: {final_score}")