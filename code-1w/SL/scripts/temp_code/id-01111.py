def calculate_performance(records):
    passing_threshold = 70
    bonus_factor = 1.2
    
    # Extract scores above threshold and apply bonus
    passed = [int(score * bonus_factor) for score in records if score >= passing_threshold]
    
    base_count = len(records)
    passed_count = len(passed)
    
    # Compute weighted performance score
    if passed_count > 0:
        average_bonus = sum(passed) / passed_count
    else:
        average_bonus = 0
    
    # Irrelevant distraction: unused variable (minimal interference)
    max_possible = 100 * bonus_factor
    
    result = (passed_count * average_bonus) // base_count
    return result

# Assessment data from student quizzes
assessments = [65, 72, 88, 91, 67, 76]

dummy_data = [x**2 for x in range(5)]  # Unused list comprehension (low interference)

final_score = calculate_performance(assessments)
print(f"Result: {final_score}")