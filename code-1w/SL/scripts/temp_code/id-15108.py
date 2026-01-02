from itertools import compress

def evaluate_performance(marks, thresholds):
    # Convert marks to boolean pass/fail based on threshold
    passing_status = [mark >= threshold for mark, threshold in zip(marks, thresholds)]
    
    # Calculate raw pass count
    pass_count = sum(passing_status)
    
    # Weighted score calculation (higher weight for earlier components)
    weights = [1.5, 1.3, 1.2, 1.0, 0.8]
    weighted_score = sum(mark * weight for mark, weight in zip(marks, weights))
    
    # Bonus logic: perfect threshold match in any category gives bonus
    exact_match_bonus = sum(1 for mark, threshold in zip(marks, thresholds) if mark == threshold)
    
    # Final score combines weighted performance and bonuses
    final_score = weighted_score + (pass_count * 2) + (exact_match_bonus * 3)
    return final_score

# Irrelevant auxiliary data (mild distraction)
student_names = ['Alice', 'Bob', 'Charlie']
course_credits = [3, 4, 3, 2, 3]

# Key data
marks = [85, 78, 90, 88, 76]
thresholds = [80, 75, 90, 85, 70]

# Execution point
final_score = evaluate_performance(marks, thresholds)
print(f"Result: {final_score}")