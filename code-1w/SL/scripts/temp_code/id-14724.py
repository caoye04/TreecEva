def evaluate_performance(output, risk_profile):
    base_score = 0
    penalty = 0
    bonus = 0

    # Preliminary metrics (some are distractions)
    efficiency = output * 1.5 if output > 50 else output * 0.8
    overhead_cost = output * 0.1
    idle_cycles = 100 - output

    # Real logic begins: assess performance using set overlap as proxy for risk alignment
    target_set = {x for x in range(10, 100, 2)}  # Even numbers from 10 to 98
    risk_intersection = target_set & risk_profile
    alignment_ratio = len(risk_intersection) / len(risk_profile) if risk_profile else 0

    # Secondary distraction: unused function call
    def calculate_stress_level(val):
        return val ** 0.5 * 2.5
    
    # Unused variable - red herring
    stress_estimate = calculate_stress_level(output)

    # Core scoring logic
    if alignment_ratio >= 0.6:
        bonus = 25
    elif alignment_ratio >= 0.3:
        bonus = 10
    else:
        penalty = 15

    # Additional logic branch with conditional expression
    risk_flag = 'high' if len(risk_profile - target_set) > len(risk_profile & target_set) else 'low'
    if risk_flag == 'high':
        penalty += 10

    # Final score computation
    base_score = output + bonus - penalty

    # Distraction: irrelevant loop
    temp_val = 0
    for i in range(3):
        for j in range(2):
            temp_val += (i * j)  # Adds 0+0+1+0+2 = 3 total, but unused elsewhere

    return int(base_score)

# Main execution context
productivity = 78
risk_factors = {12, 15, 18, 25, 30, 45, 50, 60, 72}

# Extraneous variable assignments
baseline_threshold = 65
adjustment_factor = 1.05
projection_window = "Q4"

# Key statement
final_score = evaluate_performance(productivity, risk_factors)

# Output result
print(f"Target result: {final_score}")