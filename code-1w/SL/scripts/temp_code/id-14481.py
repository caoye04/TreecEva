def calculate_final_score(data):
    base_score = data['points'] + data['bonus']
    penalty_factor = 0.9 if data['faults'] < 3 else 0.7
    
    # Irrelevant computation - distractor
    temp_adjustment = (data['level'] ** 2) % 5
    level_multiplier = 1.1 + (data['level'] * 0.05)
    
    # Simulate historical performance (unused in final logic)
    historical_peaks = []
    for i in range(1, data['level']):
        historical_peaks.append((i * data['points']) // (i + 1))
    
    # Conditional bonus based on efficiency
    efficiency = data['points'] / (data['attempts'] or 1)
    if efficiency > 8:
        base_score += 10
    elif efficiency > 5:
        base_score += 5
    else:
        base_score += 2
    
    # Apply multiplier and penalty
    adjusted_score = base_score * level_multiplier * penalty_factor
    
    # Rounding logic based on experience (some distraction)
    experience_mod = data['experience_years'] // 10
    adjusted_score += experience_mod
    
    # Dead code branch - never executed due to fixed condition
    if False and data['experience_years'] > 20:
        adjusted_score *= 1.2
    
    # Final clamping and rounding
    final_score = int(round(adjusted_score))
    return final_score

# Player data dictionary with multiple fields
player_data = {
    'points': 85,
    'bonus': 15,
    'faults': 2,
    'level': 6,
    'attempts': 10,
    'experience_years': 8,
    'category': 'intermediate',
    'region': 'north'
}

# Extra unused variables - interference
baseline_ref = 100
scaling_factor_z = 0.03
offset_buffer = [1, 2, 3]

# Key statement
final_score = calculate_final_score(player_data)
print(f"Result: {final_score}")