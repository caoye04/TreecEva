student_names = ['Alice', 'Bob', 'Charlie', 'Diana']
quiz_scores = [85, 92, 78, 96]
score_pairs = list(zip(student_names, quiz_scores))
score_sum = sum(quiz_scores)
enumerated_scores = [i * score for i, score in enumerate(quiz_scores)]
final_score = sum(enumerated_scores)
print(f"Result: {final_score}")