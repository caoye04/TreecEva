def calculate_final_score(participants):
    total_score = 0
    base_multiplier = 2
    bonus_factor = 1.5
    penalty_offset = 10

    for idx, (name, score, active) in enumerate(participants):
        if not active:
            continue
        
        normalized_score = score / (idx + 1)
        adjustment = int(normalized_score * base_multiplier)
        
        if idx % 2 == 0:
            adjustment = int(adjustment * bonus_factor)
        else:
            adjustment -= penalty_offset

        total_score += adjustment
        
        # Irrelevant tracking variable (minor distraction)
        status_log = f'Processed {name} at index {idx}'

    return total_score

# Input data
participants_data = [
    ('Alice', 80, True),
    ('Bob', 90, False),
    ('Charlie', 70, True),
    ('Diana', 60, True)
]

total_score = calculate_final_score(participants_data)
print(f'Result: {total_score}')