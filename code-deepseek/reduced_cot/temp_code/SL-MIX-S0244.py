student_scores = [85, 92, 78, 96, 88, 74, 95]
passing_threshold = 80
filtered_scores = [score for score in student_scores if score >= passing_threshold]
sorted_scores = sorted(filtered_scores)
score_range = max(filtered_scores) - min(filtered_scores)
final_score = max(filtered_scores) - min(filtered_scores)
print(f"Result: {final_score}")