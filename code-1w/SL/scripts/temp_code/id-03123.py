def calculate_total(performance_list):
    base_multiplier = 2
    bonus_factor = 1.5
    total = 0
    
    # Irrelevant distraction: unused variable
    max_possible = 100
    
    for index, score in enumerate(performance_list):
        if index % 2 == 0:
            total += score * base_multiplier
        else:
            total += score * bonus_factor
    
    return int(total)

# Simulate student test performances
test_scores = [85, 90, 78, 92]
adjustment_map = {0: 1, 2: 1}  # Unused distraction

# Apply lambda to normalize scores above 80
cleaned_scores = list(map(lambda x: x if x >= 80 else 80, test_scores))

# Performance weighting based on position
final_score = calculate_total(cleaned_scores)

print(f"Result: {final_score}")