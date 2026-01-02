from collections import defaultdict

def calculate_performance(flags, scores):
    total = 0
    penalty_map = defaultdict(int, {'flag_x': 3, 'flag_y': 5})
    
    for i, score in enumerate(scores):
        if i >= len(flags):
            break
        if not flags[i]:
            total -= penalty_map[f'flag_{i}']
            continue
        total += score * 2 if score > 70 else score
    
    adjustment = 10 if sum(flags) >= 3 else 0
    return total + adjustment

# Base data
base_scores = [85, 45, 90, 60, 75]
bouns_flags = [True, False, True, True, False]  # Note: intentional typo to test attention, but not used
bonus_flags = [True, False, True, True, False]

# Calculation
final_score = calculate_performance(bonus_flags, base_scores)
print(f"Target result: {final_score}")