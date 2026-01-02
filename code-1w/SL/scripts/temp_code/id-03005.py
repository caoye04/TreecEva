from collections import defaultdict

# Simulate student exam results with subject-wise scores
def generate_exam_data():
    data = [
        ('Alice', 'Math', 85),
        ('Bob', 'Math', 78),
        ('Alice', 'Physics', 92),
        ('Charlie', 'Math', 88),
        ('Bob', 'Physics', 81),
        ('Charlie', 'Chemistry', 95),
        ('Alice', 'Chemistry', 87)
    ]
    return data

# Aggregate scores by student using defaultdict
def aggregate_scores(exam_data):
    scores = defaultdict(list)
    for student, subject, mark in exam_data:
        scores[student].append(mark)
    return scores

# Calculate average score per student
average = lambda lst: round(sum(lst) / len(lst), 2)

# Determine final composite score using top N averaged subjects
def calculate_final_score(raw_results):
    aggregated = aggregate_scores(raw_results)
    avg_scores = {s: average(scores) for s, scores in aggregated.items()}
    
    # Sort students by average score descending
    ranked = sorted(avg_scores.items(), key=lambda x: x[1], reverse=True)
    
    # Boost top performer's score by 5%
    boosted_scores = [
        score * 1.05 if idx == 0 else score
        for idx, (student, score) in enumerate(ranked)
    ]
    
    # Final score is the mean of boosted rankings
    final_mean = sum(boosted_scores) / len(boosted_scores)
    return round(final_mean, 3)

# Irrelevant utility (minor distraction, intervention level 5)
def unused_helper():
    return "This function is not used"

# Main execution flow
exam_results = generate_exam_data()
final_score = calculate_final_score(exam_results)
print(f"Result: {final_score}")