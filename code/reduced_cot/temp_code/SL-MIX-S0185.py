student_scores = {85, 92, 78, 96, 88, 91}
threshold = 90
filter_scores = lambda scores, min_val: [score for score in scores if score >= min_val]
filtered_scores = filter_scores(student_scores, threshold)
scoring_boost = 1.5
final_score = filtered_scores[1] * scoring_boost
print(f"Target result: {final_score}")