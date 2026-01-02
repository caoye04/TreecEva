def evaluate_performance(output, risk):
    base_score = 100
    adjustment = 0

    # Complex productivity scoring using lambda
    productivity_index = (lambda x: x ** 0.5 if x > 0 else 0)(output)

    # Distraction: irrelevant calculation for energy_consumption
    energy_consumption = 0
    for hour in range(1, 8):
        energy_consumption += hour * 1.5
        if hour % 3 == 0:
            energy_consumption -= 0.5  # minor correction

    # Real logic: adjust score based on productivity and risk
    if output >= 50:
        adjustment += 20
        if risk < 0.5:
            adjustment += 30
        elif risk >= 0.7:
            adjustment -= 40
    else:
        adjustment -= 10
        if risk > 0.8:
            adjustment -= 25

    # Bonus mechanism based on hidden rule
    compliance_flags = {'audit_passed': True, 'review_cycle': 3}
    if compliance_flags['audit_passed'] and compliance_flags['review_cycle'] > 2:
        adjustment += 15

    # Use of dictionary operation to map tier bonuses
    tier_bonus = {'high': 25, 'medium': 10, 'low': 0}
    volume_tier = 'high' if output > 75 else 'medium' if output > 40 else 'low'
    adjustment += tier_bonus[volume_tier]

    # Final computation
    final_score = base_score + productivity_index + adjustment

    # Dead code path - never executed due to fixed flags
    if compliance_flags.get('suspended', False):
        final_score = 0  # overridden only if suspended

    return final_score

# Main execution
productivity = 65
risk_factor = 0.3
irrelevant_list = [i**2 for i in range(10) if i % 2 == 0]  # distraction
auxiliary_sum = sum(irrelevant_list)  # unused sum

final_score = evaluate_performance(productivity, risk_factor)
print(f"Result: {final_score}")