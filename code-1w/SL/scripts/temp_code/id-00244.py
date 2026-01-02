def calculate_performance_rating(marks, threshold):
    avg = sum(marks) / len(marks)
    above_threshold = sum(1 for m in marks if m >= threshold)
    bonus = 10 if above_threshold >= 3 else 5
    adjustment = 0.5 if avg >= 85 else -0.5
    return int(avg + bonus + adjustment)

# Student test marks across 5 subjects
test_marks = (88, 92, 76, 85, 90)
threshold = 80
final_score = calculate_performance_rating(test_marks, threshold)
print(f"Result: {final_score}")