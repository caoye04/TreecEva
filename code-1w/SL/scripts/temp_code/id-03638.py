def calculate_final_score(ranks, flags):
    base_score = len(ranks)
    adjustment = 0
    
    for i, flag in enumerate(flags):
        if flag and i in ranks:
            adjustment += i * 2
    
    if len(ranks) > 3:
        adjustment += 5
    
    return base_score + adjustment

# Simulate system performance evaluation
rank_set = {1, 2, 4, 5}
performance_flags = [False, True, False, True, True]
extra_data = [x**2 for x in range(6)]  # Irrelevant distractor list
unused_var = sum(extra_data)

final_score = calculate_final_score(rank_set, performance_flags)
print(f"Result: {final_score}")