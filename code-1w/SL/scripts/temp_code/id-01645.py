def calculate_final_score(entries, limits):
    base_score = 0
    penalty_adjustment = 0
    bonus_tracker = []
    temp_result = 0

    # Irrelevant pre-processing (distractor)
    max_entry_value = max([e['value'] for e in entries])
    if max_entry_value > 100:
        temp_result += 10

    # Real logic begins: score accumulation with conditional adjustments
    for i, entry in enumerate(entries):
        category = entry['category']
        value = entry['value']
        
        # Conditional expression used with enumerate
        adjustment_factor = 1.5 if category == 'priority' else 0.8
        
        # Accumulate base score with factor
        base_score += value * adjustment_factor
        
        # Track bonuses for high-value entries
        if value > limits[category]:
            bonus_tracker.append((i, value // 10))

    # Apply bonus from tracker
    for idx, bonus in bonus_tracker:
        if idx % 2 == 0:
            base_score += bonus * 3

    # Bitwise check on accumulated score (semi-relevant)
    if base_score & 1:  # if odd
        penalty_adjustment -= 5

    # Dummy loop with zip (distraction) - iterates over unrelated pairs
    statuses = ['active', 'inactive', 'pending', 'verified']
    ids = [101, 205, 307, 409]
    for sid, status in zip(ids, statuses):
        if 'active' in status:
            temp_result += sid % 7

    # Final score computation
    final_score = int(base_score + penalty_adjustment)
    
    return final_score

# Input data
thresholds = {'standard': 50, 'priority': 75}
data = [
    {'category': 'priority', 'value': 80},
    {'category': 'standard', 'value': 60},
    {'category': 'priority', 'value': 90},
    {'category': 'standard', 'value': 40},
    {'category': 'priority', 'value': 70}
]

# Execution
final_score = calculate_final_score(data, thresholds)
print(f"Target result: {final_score}")