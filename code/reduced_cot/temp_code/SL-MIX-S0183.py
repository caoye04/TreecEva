def calculate_student_scores():
    student_names = ['alice', 'BOB', 'Charlie', 'Diana', 'edward']
    raw_scores = [85, 92, 78, 96, 88]
    
    # Process names and scores using enumerate and zip
    processed_data = []
    temp_storage = []
    
    for idx, (name, score) in enumerate(zip(student_names, raw_scores)):
        normalized_name = name.lower()
        adjusted_score = score + (idx % 2)
        processed_data.append((normalized_name, adjusted_score))
        temp_storage.append(score * 2)  # Distractor operation
    
    # Calculate final results with some intermediate calculations
    bonus_points = [5, 3, 7, 2, 6]
    processed_results = []
    
    for name_score_tuple, bonus in zip(processed_data, bonus_points):
        base_score = name_score_tuple[1]
        intermediate_val = base_score * 0.1  # Distractor calculation
        final_score_entry = base_score + bonus
        processed_results.append(final_score_entry)
    
    # Final assignment with nested indexing
    final_score = processed_results[-1]
    print(f"Result: {final_score}")

calculate_student_scores()