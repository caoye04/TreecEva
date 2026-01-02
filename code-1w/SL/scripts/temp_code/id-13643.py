def calculate_final_score(records, limits):
    base_score = 0
    penalty_adjustment = 0
    temp_sum = 0
    overflow_flag = False
    
    for i, (key, value) in enumerate(records.items()):
        if i % 2 == 0 and value > limits['max_even']:
            base_score += value // 3
        elif value > limits['min_odd']:
            base_score += value % 7
            
        # Distractor: irrelevant tracking
        temp_sum += value * 2
        if temp_sum > 1000:
            overflow_flag = True
            temp_sum = 0  # Reset, but never used again

    # Semi-relevant transformation
    transformed = [v ** 0.5 for k, v in records.items() if v > 0]
    bonus = sum(1 for x in transformed if x > 2.0)

    # Another distractor loop: dead computation
    hypotheticals = []
    for x in range(len(transformed)):
        hypotheticals.append(x * bonus - 1)
    avg_hypothetical = sum(hypotheticals) / len(hypotheticals) if hypotheticals else 0

    # Real logic step: bitwise adjustment
    bit_mask = 7
    masked_bonus = bonus & bit_mask

    # Final score depends only on base_score and masked_bonus
    final_score = base_score + masked_bonus
    
    # Irrelevant state check
    if avg_hypothetical < 5 and not overflow_flag:
        final_score -= 1  # Minor red herring, condition won't trigger due to reset

    return final_score

# Main execution
config = {
    'max_even': 25,
    'min_odd': 8
}

data = {
    'alpha': 30,
    'beta': 12,
    'gamma': 50,
    'delta': 3,
    'epsilon': 18
}

intermediate_total = 0
for val in data.values():
    intermediate_total += val * 0.1  # Distractor accumulation

final_score = calculate_final_score(data, config)
print(f"Target result: {final_score}")