def compute_final_result(scores, threshold):
    valid_scores = [score for score in scores if score > threshold]
    average_score = sum(valid_scores) / len(valid_scores) if valid_scores else 0
    bonus_multiplier = 1.5 if average_score > 85 else 1.0
    final_result = average_score * bonus_multiplier
    return round(final_result, 2)

participant_scores = [78, 92, 85, 67, 94, 88, 76, 91]
threshold_value = 80
preliminary_result = sum(participant_scores) / len(participant_scores)
unused_data = [x for x in range(10)]

final_score = compute_final_result(participant_scores, threshold_value)
print(f"Target result: {final_score}")