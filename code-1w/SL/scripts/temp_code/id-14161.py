from collections import Counter
def calculate_final_score(scores, attendance):
    avg_score = sum(scores) / len(scores)
    bonus = 5 if attendance > 0.9 else 2
    weighted_exam = avg_score * 0.8
    attendance_points = 10 * attendance * 0.2
    final_score = weighted_exam + attendance_points + bonus
    return final_score

def analyze_performance(logs):
    count = Counter(logs)
    return count['pass']

# Irrelevant helper function (adds minimal interference)
def normalize_values(data):
    min_val, max_val = min(data), max(data)
    return [(x - min_val) / (max_val - min_val) for x in data]

# Main computation
exam_scores = [85, 90, 78, 92]
attendance_rate = 0.93
temp_data = [10, 20, 30]
normalized = normalize_values(temp_data)
result_count = analyze_performance(['pass', 'fail', 'pass'])
final_score = calculate_final_score(exam_scores, attendance_rate)
print(f"Result: {final_score}")