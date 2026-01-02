def analyze_performance(marks):
    avg = sum(marks) / len(marks)
    passing = [m for m in marks if m >= 50]
    above_avg = [m for m in passing if m > avg]
    sorted_ranks = sorted(above_avg, reverse=True)
    filtered_data = [x for x in sorted_ranks if x % 2 == 1]
    threshold_score = filtered_data[-1] if filtered_data else 0
    outlier_check = [x for x in marks if x < 30]
    return threshold_score

exam_marks = [65, 72, 50, 88, 45, 91, 60, 74]
result = analyze_performance(exam_marks)
print(f"Result: {result}")