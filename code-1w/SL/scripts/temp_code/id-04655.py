def calculate_final_score(data, thresholds):
    base_score = 0
    bonus_points = 0
    penalty = 0
    temp_result = 0  # distractor variable
    intermediate_sum = 0  # semi-relevant for debugging only

    for i, (value, flag) in enumerate(data):
        if i % 3 == 0:
            base_score += value % 7
        if flag and value > thresholds['high']:
            bonus_points += 2
        elif not flag and value < thresholds['low']:
            penalty += 1

    # Distractor computation: unrelated to final score
    for j in range(len(data)):
        temp_result += j * 0.5
    
    # Semi-relevant aggregation
    for idx, (val, _) in enumerate(zip(data, data[1:])):
        intermediate_sum += val[0] // (idx + 1) if idx != 0 else 0

    # Core logic with modular arithmetic and conditional adjustment
    raw_total = base_score + bonus_points - penalty
    adjustment = (raw_total * 3) % 5
    
    # Final decision using integer division and threshold check
    if raw_total > thresholds['medium']:
        final_score = (raw_total // 2) + adjustment
    else:
        final_score = raw_total + (adjustment * 2)
    
    return final_score

# Input setup
data = [(8, True), (3, False), (12, True), (5, True), (9, False)]
thresholds = {'low': 4, 'medium': 10, 'high': 10}

# Execution
final_score = calculate_final_score(data, thresholds)
print(f"Target result: {final_score}")