def calculate_final_score(ranks, bonuses):
    base_scores = {}
    adjustments = []
    temp_sum = 0

    # Initialize base scores using enumeration
    for idx, rank in enumerate(ranks):
        base_scores[idx] = (idx + 1) * rank

    # Apply bonus multipliers using dictionary lookup
    for key, value in bonuses.items():
        if key in base_scores:
            base_scores[key] *= value

    # Compute adjustment offsets (some irrelevant computation)
    for i in range(len(base_scores)):
        if i % 2 == 0:
            adjustments.append(i * 0.5)
        else:
            adjustments.append(-i * 0.1)

    # Accumulate sum with conditional logic
    running_total = 0
    for i, score in enumerate(base_scores.values()):
        if score > 10:
            running_total += score * 0.9
        else:
            running_total += score * 1.1

    # Dummy loop to increase cognitive load (irrelevant to final result)
    dummy_accumulator = 0
    for x in range(3):
        for y in range(3):
            dummy_accumulator += x * y

    # Final score calculation based on weighted sum
    scaling_factor = 1.05
    final_score = int(running_total * scaling_factor)

    # Unused variable - red herring
    metadata_log = {"processed": len(base_scores), "version": "2.1"}

    return final_score

# Input data
rank_data = [4, 5, 6, 3]
bonus_map = {1: 2, 3: 1}  # Only indices 1 and 3 get bonuses

# Key execution point
final_score = calculate_final_score(rank_data, bonus_map)
print(f"Target result: {final_score}")