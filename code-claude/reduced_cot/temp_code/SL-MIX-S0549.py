def calculate_weighted_score(records, weights):
    total_weighted = 0
    total_credits = 0
    
    # Create a lookup dictionary for faster access
    weight_lookup = {course: weight for course, weight in weights.items()}
    
    # Sort courses by name (unnecessary for calculation)
    sorted_courses = sorted(records.keys())
    
    # Track highest and lowest scores (not used in final result)
    highest_score = 0
    lowest_score = 100
    
    for course in records:
        grade = records[course]['grade']
        credits = records[course]['credits']
        
        # Update tracking variables (not used in final calculation)
        if grade > highest_score:
            highest_score = grade
        if grade < lowest_score:
            lowest_score = grade
        
        # Apply weight if available, otherwise use default weight of 1.0
        weight = weight_lookup.get(course, 1.0)
        
        # Calculate weighted contribution
        weighted_value = grade * credits * weight
        total_weighted += weighted_value
        total_credits += credits
    
    # Calculate potential bonus (not applied to final result)
    potential_bonus = (highest_score - lowest_score) / 10
    
    # Return weighted average rounded to 2 decimal places
    return round(total_weighted / total_credits, 2) if total_credits > 0 else 0

# Student course records with grades and credits
student_records = {
    'Math101': {'grade': 85, 'credits': 4},
    'Physics': {'grade': 78, 'credits': 3},
    'Chemistry': {'grade': 92, 'credits': 4},
    'English': {'grade': 88, 'credits': 2}
}

# Course weight factors
course_weights = {
    'Math101': 1.2,
    'Physics': 1.1,
    'History': 0.9  # Note: Student doesn't have this course
}

# Calculate the weighted grade point average
final_score = calculate_weighted_score(student_records, course_weights)

# Display result
print(f"Result: {final_score}")