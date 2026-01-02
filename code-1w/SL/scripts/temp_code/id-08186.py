from collections import defaultdict

# Simulate student quiz data with multiple attempts
def calculate_final_score(students):
    scores = defaultdict(list)
    for name, quiz_attempts in students.items():
        for score in quiz_attempts:
            if score >= 50:  # Only count passing attempts
                scores[name].append(score)
    
    final_scores = {}
    for name, passing in scores.items():
        final_scores[name] = max(passing) if passing else 0
    
    avg_high_score = sum(final_scores.values()) / len(final_scores) if final_scores else 0
    
    bonus = 10 if avg_high_score > 75 else 5
    
    # Aggregate total performance
    total = sum(final_scores.values())
    final_score = int(total + bonus)
    
    return final_score

# Irrelevant auxiliary variable (minor distraction)
dummy_weights = [0.5, 1.5, 2.0]

students_data = {
    'alice': [68, 72, 55],
    'bob': [45, 80, 85],
    'charlie': [90, 70, 60],
    'diana': [75, 85]
}

final_score = calculate_final_score(students_data)
print(f"Result: {final_score}")