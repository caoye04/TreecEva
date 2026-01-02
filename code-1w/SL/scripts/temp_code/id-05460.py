from collections import defaultdict

# Simulate student quiz scores with potential retries
def generate_scores():
    raw_data = [
        ('Alice', [85, 90]),
        ('Bob', [70, 75, 80]),
        ('Charlie', [60]),
        ('Alice', [88])
    ]
    scores = defaultdict(list)
    for name, attempts in raw_data:
        scores[name].extend(attempts)
    return scores

# Scoring logic: best attempt counts, then apply curve if average > 85
def calculate_final_score(scores_dict, student_name):
    attempts = scores_dict.get(student_name, [])
    if not attempts:
        return 0
    best_score = max(attempts)
    avg_score = sum(attempts) / len(attempts)
    # Curve logic: +5 points if average > 85, but cap at 100
    curved_score = best_score + 5 if avg_score > 85 else best_score
    final = min(curved_score, 100)
    return final

# Irrelevant utility function (mild distraction)
def format_report(name, score):
    return f"Student: {name}, Grade: {score:.1f}%"

# Main execution
data = generate_scores()
final_score = calculate_final_score(data, 'Alice')
Result: {final_score}