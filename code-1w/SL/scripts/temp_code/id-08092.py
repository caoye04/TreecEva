def calculate_final_score(students):
    passing_threshold = 50
    bonus_factor = 1.1
    
    # Extract scores of students who passed, using list comprehension
    passed_scores = [score for name, score in students if score >= passing_threshold]
    
    # Apply conditional expression to add bonus only if average is below 75
    raw_average = sum(passed_scores) / len(passed_scores) if passed_scores else 0
    adjusted_average = raw_average * bonus_factor if raw_average < 75 else raw_average
    
    # Compute final score as ceiling-equivalent using simple arithmetic
    final_score = int(adjusted_average + 0.999)
    
    # Irrelevant distraction: counting student names with more than 5 letters
    long_names_count = len([name for name, _ in students if len(name) > 5])
    
    return final_score

# Dataset of student records
students_data = [
    ('Alice', 85),
    ('Bob', 42),
    ('Charlie', 67),
    ('Diana', 70),
    ('Eve', 58)
]

# Execution point
final_score = calculate_final_score(students_data)
print(f"Result: {final_score}")