def calculate_quality_scores(items):
    base_score = 0
    adjustment_factor = 1.5
    temp_calc = []
    
    for idx, item in enumerate(items):
        quality_check = len(item) % 3
        temp_val = quality_check * adjustment_factor
        temp_calc.append(temp_val)
        
        if quality_check == 0:
            base_score += 5
        elif quality_check == 1:
            base_score += 3
        else:
            base_score += 1
    
    # Distractor operations that don't affect final result
    unused_sum = sum(temp_calc)
    average_temp = unused_sum / len(temp_calc) if temp_calc else 0
    
    # Key logic that determines final score
    bonus_points = 0
    for score in temp_calc:
        if score > 2.0:
            bonus_points += 2
    
    # Additional unused calculation
    unused_product = base_score * adjustment_factor
    
    final_score = base_score + bonus_points
    result = final_score
    print(f"Target result: {result}")

# Execute the function
items_list = ["apple", "banana", "cherry", "date", "elderberry"]
calculate_quality_scores(items_list)