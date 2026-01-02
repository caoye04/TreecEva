def calculate_final_score(scores, deductions):
    base_total = sum(scores)
    adjusted_total = base_total * 0.9
    penalty_set = {i for i in deductions if i > 0}
    reduction = len(penalty_set) * 5
    if reduction > 20:
        reduction = 20
    return int(adjusted_total - reduction)

raw_scores = [85, 92, 78, 96, 88]
penalties = [10, -5, 15, 0, 25]
initial_total = sum(raw_scores)
extra_buffer = raw_scores[2:4]
final_score = calculate_final_score(raw_scores, penalties)
print(f"Target result: {final_score}")