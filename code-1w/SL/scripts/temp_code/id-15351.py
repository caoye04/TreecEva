def calculate_final_score(results, threshold):
    filtered = [score for score in results if score >= threshold]
    adjusted = list(map(lambda x: round(x * 0.9 + 5), filtered))
    average = sum(adjusted) / len(adjusted) if adjusted else 0
    return int(average)

exam_results = [85, 72, 90, 48, 67, 88, 53]
passing_threshold = 55

# Irrelevant distraction variables
temp_data = [x ** 0.5 for x in exam_results][:3]
bonus_points = 3

final_score = calculate_final_score(exam_results, passing_threshold)
print(f"Result: {final_score}")