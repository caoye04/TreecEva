def calculate_final_score(results):
    passing_threshold = 50
    bonus_factor = 1.1
    
    # Compute adjusted scores using list comprehension and lambda
    adjust_score = lambda x: x * bonus_factor if x >= passing_threshold else x
    adjusted = [adjust_score(score) for score in results]
    
    # Calculate average with integer division and rounding
    total = sum(adjusted)
    count = len(adjusted)
    average = round(total // count)
    
    # Apply final adjustment based on performance tier
    if average >= 75:
        final = average + 5
    elif average >= 60:
        final = average + 3
    else:
        final = average
        
    return final

# Irrelevant auxiliary variable (minor distraction, intervention level 4)
dummy_weight = 0.9

exam_results = [85, 70, 55, 90, 68]
final_score = calculate_final_score(exam_results)
print(f"Result: {final_score}")