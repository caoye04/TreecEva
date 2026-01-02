def calculate_final_score(raw_data, multiplier):
    # Initialize tracking variables
    base_points = 0
    penalty_offset = 0
    temp_result = 0
    
    # Irrelevant statistical tracking (distractor)
    value_frequencies = {}
    for val in raw_data['values']:
        value_frequencies[val] = value_frequencies.get(val, 0) + 1
    
    # Core logic: process thresholds and apply bitwise weight adjustments
    threshold_met = 0
    for i, val in enumerate(raw_data['values']):
        if val > 50:
            base_points += val // 3
            # Bitwise influence on high performers
            base_points ^= (i & 3)  # XOR with index mod 4
        else:
            penalty_offset += (val % 7)

    # Secondary adjustment using dictionary lookup (semi-relevant)
    level_map = {'low': 1, 'mid': 2, 'high': 5}
    level_bonus = level_map.get(raw_data['level'], 0)
    
    # Dummy loop that recalculates unused metric
    cumulative_sum = 0
    for x in range(len(raw_data['values']) + 2):
        cumulative_sum += x * x  # Dead computation

    # Actual formula construction
    intermediate = (base_points - penalty_offset) * level_bonus
    if intermediate > 100:
        intermediate = intermediate // 2
    
    # Final scaling with external multiplier
    result = intermediate + (multiplier << 1)  # Add multiplier left-shifted by 1
    
    return result

# Main execution context
config = {
    'debug_mode': True,
    'version': '2.1',
    'threshold_cap': 999
}

auxiliary_data = [8, 12, 16]
data = {
    'values': [65, 42, 77, 55, 81],
    'level': 'high',
    'timestamp': 1712345678
}
bonus_multiplier = 7

# Trigger key computation
total_aggregate = sum([x * 2 for x in auxiliary_data])  # Distractor accumulation
final_score = calculate_final_score(data, bonus_multiplier)

print(f"Result: {final_score}")