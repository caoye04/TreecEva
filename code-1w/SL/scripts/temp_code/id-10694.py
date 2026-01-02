def calculate_final_score(ranks, flags):
    base_score = len(ranks)
    bonus = 0
    
    if 'high_performance' in flags and 'reliable' in flags:
        bonus += 15
    elif 'high_performance' in flags:
        bonus += 5

    adjustment = 0
    if ranks.intersection({1, 2, 3}):
        adjustment += 10
    if len(ranks) > 4:
        adjustment -= 2
    
    temp_debug_value = 999  # Irrelevant debug variable (minimal distraction)
    
    return base_score + bonus + adjustment

# Simulate system evaluation
rank_set = {1, 4, 5, 7}
performance_flags = {'high_performance', 'reliable'}
initial_threshold = 3.5  # Unused parameter (low interference)

final_score = calculate_final_score(rank_set, performance_flags)
print(f"Result: {final_score}")