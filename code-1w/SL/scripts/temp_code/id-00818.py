from itertools import compress

def calculate_final_score(raw_marks, extra_bonus):
    # Normalize marks to percentage
    normalized = [min(max(mark, 0), 100) for mark in raw_marks]
    
    # Determine passing status using conditional expression
    passing = all(score >= 40 for score in normalized)
    
    # Apply curve only if average is below 75 and passing
    average = sum(normalized) / len(normalized)
    curved = [score * 1.1 for score in normalized] if average < 75 and passing else normalized
    
    # Compute base total
    base_total = sum(curved)
    
    # Bonus logic using lambda filtering
    significant_scores = list(filter(lambda x: x > 90, curved))
    bonus_points = len(significant_scores) * 5
    
    # Final adjustment with optional bonus activation
    final_adjustment = bonus_points if extra_bonus else 0
    
    return int(base_total + final_adjustment)

# Input data
marks = [68, 72, 65, 80]
bonus_activated = True

# Key computation
final_score = calculate_final_score(marks, bonus_activated)
print(f"Result: {final_score}")