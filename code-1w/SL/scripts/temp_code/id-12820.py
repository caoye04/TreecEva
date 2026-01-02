def calculate_ranking(data):
    weight_func = lambda x: x * 1.5 if x > 7 else x * 0.8
    adjusted = [weight_func(val) for val in data]
    
    # Irrelevant distraction: unused variable
    baseline = sum(data) / len(data)
    
    if adjusted[0] > 10:
        bonus = 5
    else:
        bonus = 2
    
    total = sum(adjusted) + bonus
    return round(total, 3)

# Core metrics influencing final score
tech_metrics = (6, 8, 7, 9)
final_score = calculate_ranking(tech_metrics)
print(f"Result: {final_score}")