from collections import Counter
def calculate_final_score(points_str, faults):
    # Convert string of points to list of integers
    points = [int(p) for p in points_str.split(',') if p.strip()]
    total_points = sum(points)
    
    # Apply penalty deduction: 5 points per fault
    adjusted_score = total_points - (faults * 5)
    
    # Bonus logic based on case pattern in input string
    upper_count = sum(1 for c in points_str if c.isupper())
    lower_count = sum(1 for c in points_str if c.islower())
    
    # Conditional expression for bonus
    bonus = 10 if upper_count > lower_count else 5
    
    # Final score calculation
    final_result = adjusted_score + bonus
    return final_result

# Simulated input data
raw_points = "8,12,15,7,20"
penalty_count = 3

# Irrelevant counter for character frequency (minimal distraction)
count_stats = Counter(raw_points)

# Key computation step
current_status = "ACTIVE" if penalty_count < 5 else "INACTIVE"
final_score = calculate_final_score(raw_points, penalty_count)

print(f"Result: {final_score}")