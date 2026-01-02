def evaluate_performance(output, risk):
    base_score = 100
    efficiency_bonus = 0
    penalty = 0

    if output > 80:
        efficiency_bonus += 25
    elif output > 60:
        efficiency_bonus += 15
    else:
        efficiency_bonus += 5

    # Simulate complex risk adjustment with red herring variables
    risk_tiers = ['low', 'moderate', 'high']
    risk_index = min(int(risk / 30), 2)
    tier_multiplier = [1.1, 1.0, 0.7][risk_index]

    # Distractor: unused health_check calculation
    health_check = sum([i * 2 for i in range(5)]) + output % 10

    # Actual penalty logic
    if risk > 75:
        penalty += 30
    elif risk > 50:
        penalty += 15
    else:
        penalty += 5

    # Misleading intermediate score (not final)
    preliminary_score = (base_score + efficiency_bonus) * tier_multiplier - penalty

    # Additional distractor: irrelevant loop
    temp_values = []
    for i in range(3):
        temp_values.append((i + 1) * 100)

    # Final adjustment based on hidden rule: if output divisible by 5, add bonus
    final_score = int(preliminary_score)
    if output % 5 == 0:
        final_score += 10

    return final_score

# Main execution
productivity = 85
risk_factor = 57
aux_data = {'timestamp': 12345, 'version': '2.1'}  # Unused metadata

# Irrelevant preprocessing
processed_inputs = [x * 2 for x in [10, 20, 30] if x > 15]

final_score = evaluate_performance(productivity, risk_factor)
print(f"Result: {final_score}")