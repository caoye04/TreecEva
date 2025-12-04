def analyze_student_data(raw_scores, student_names):
    # Convert scores to integers and handle potential errors
    processed_scores = []
    for score in raw_scores:
        try:
            processed_scores.append(int(score))
        except ValueError:
            processed_scores.append(0)
    
    # Track statistics (some not used in final calculation)
    min_score = min(processed_scores) if processed_scores else 0
    max_score = max(processed_scores) if processed_scores else 0
    total_students = len(student_names)
    
    # Create sets for tracking special cases
    uppercase_names = {name for name in student_names if name.isupper()}
    lowercase_names = {name for name in student_names if name.islower()}
    mixed_case_count = total_students - len(uppercase_names) - len(lowercase_names)
    
    # Process student data with enumeration
    score_multipliers = [1.0, 1.5, 0.8, 1.2, 1.0]
    adjusted_scores = []
    name_score_pairs = list(zip(student_names, processed_scores))
    
    for idx, (name, score) in enumerate(name_score_pairs):
        # Apply multiplier based on position
        multiplier = score_multipliers[idx % len(score_multipliers)]
        
        # Apply bonus for uppercase names (not used in final result)
        if name in uppercase_names:
            bonus = 5
        else:
            bonus = 0
            
        # Calculate adjusted score
        adjusted = score * multiplier
        adjusted_scores.append(adjusted)
    
    # Filter scores based on thresholds
    threshold = sum(processed_scores) / len(processed_scores) if processed_scores else 0
    valid_scores = [score for score in adjusted_scores if score > threshold - 10]
    
    # Calculate the filtered score (this is our target value)
    filtered_score = sum(valid_scores)
    
    # Additional calculations that don't affect the result
    avg_score = filtered_score / len(valid_scores) if valid_scores else 0
    score_range = max_score - min_score
    
    return filtered_score

# Test data
test_scores = ['85', '92', '78', '90', '88']
test_names = ['Alice', 'BOB', 'charlie', 'Diana', 'evan']

# Execute the function
result = analyze_student_data(test_scores, test_names)
print(f"Result: {result}")