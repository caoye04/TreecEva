from collections import Counter
def analyze_assessment_types(assessments):
    type_counter = Counter([item['type'] for item in assessments])
    return type_counter

def calculate_final_score(assessments):
    weights = {'quiz': 0.2, 'homework': 0.3, 'exam': 0.5}
    total_score = 0.0
    for item in assessments:
        contribution = item['score'] * weights[item['type']]
        total_score += contribution
    return round(total_score, 3)

# Irrelevant utility function (adds minor distraction)
def format_timestamp(ts):
    return f"Timestamp: {ts}"

assessments = [
    {'type': 'quiz', 'score': 78, 'date': '2023-09-01'},
    {'type': 'homework', 'score': 94, 'date': '2023-09-05'},
    {'type': 'exam', 'score': 85, 'date': '2023-09-10'},
    {'type': 'quiz', 'score': 88, 'date': '2023-09-08'}
]

# Analysis call (not used in final score calculation - mild distractor)
assessment_breakdown = analyze_assessment_types(assessments)

# Key statement
total_score = calculate_final_score(assessments)

print(f"Result: {total_score}")