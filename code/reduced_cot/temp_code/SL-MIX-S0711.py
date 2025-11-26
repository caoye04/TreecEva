def calculate_performance(base_score, adjustments, bonus_multiplier):
    temp_adjust = sum(x for x in adjustments if x > 0)
    unused_calc = len(adjustments) * 2.5
    
    processed_score = base_score + temp_adjust
    intermediate = processed_score * 1.1
    
    threshold_check = (lambda x: 'high' if x > 100 else 'low')(intermediate)
    bonus_points = 15 if threshold_check == 'high' else 5
    
    final_adjustment = bonus_points * bonus_multiplier
    final_score = intermediate + final_adjustment
    
    dummy_operation = [x**2 for x in range(1, 4)]
    result = final_score + bonus_points
    
    print(f"Target result: {final_score}")

base_score = 85
adjustments = [3, -2, 7, -1, 4]
bonus_multiplier = 1.5
calculate_performance(base_score, adjustments, bonus_multiplier)