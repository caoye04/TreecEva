def analyze_student_performance():
    # Student performance analysis with set operations
    math_scores = [85, 92, 78, 95, 88, 90, 82]
    science_scores = [92, 88, 85, 79, 91, 87, 90]
    
    # Identify top performers in each subject (distractor calculation)
    math_threshold = sum(math_scores) / len(math_scores) + 5
    science_threshold = sum(science_scores) / len(science_scores) + 3
    
    top_math_students = set(score for score in math_scores if score > math_threshold)
    top_science_students = set(score for score in science_scores if score > science_threshold)
    
    # Intermediate calculations that don't affect final result
    math_high_count = len([s for s in math_scores if s > 90])
    science_high_count = len([s for s in science_scores if s > 90])
    total_high_scores = math_high_count + science_high_count
    
    # Primary analysis - consistent high performers
    primary_set = set(math_scores).intersection(set(science_scores))
    primary_set = {score for score in primary_set if score >= 85}
    
    # Secondary analysis - overall high achievers
    secondary_set = set()
    for i in range(len(math_scores)):
        if math_scores[i] > 85 and science_scores[i] > 85:
            secondary_set.add(math_scores[i])
            secondary_set.add(science_scores[i])
    
    # Final score calculation (the key variable)
    final_score = primary_set.intersection(secondary_set)
    final_score = sum(final_score) if final_score else 0
    
    # Print irrelevant statistics
    print(f"Math high performers: {math_high_count}")
    print(f"Science high performers: {science_high_count}")
    print(f"Target result: {final_score}")

analyze_student_performance()