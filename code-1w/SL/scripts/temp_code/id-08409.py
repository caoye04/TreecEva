from itertools import compress

def analyze_performance():
    # Employee performance data
    employees = ['Alice', 'Bob', 'Charlie', 'Diana']
    base_scores = [85, 90, 78, 92]
    attendance_rate = [0.95, 0.87, 0.90, 0.96]
    
    # Bonus logic based on attendance
    bonus_eligibility = [rate >= 0.9 for rate in attendance_rate]
    performance_bonus = list(compress([5, 8, 3, 10], bonus_eligibility))
    
    # Apply bonus to base scores for eligible employees
    adjusted_scores = base_scores.copy()
    bonus_iter = iter(performance_bonus)
    for i, eligible in enumerate(bonus_eligibility):
        if eligible:
            adjusted_scores[i] += next(bonus_iter)
    
    # Categorize performance
    performance_category = {}
    for idx, score in enumerate(adjusted_scores):
        if score >= 95:
            performance_category[employees[idx]] = 'Outstanding'
        elif score >= 85:
            performance_category[employees[idx]] = 'Good'
        else:
            performance_category[employees[idx]] = 'Satisfactory'
    
    # Final rating adjustment using dictionary mapping
    category_multiplier = {'Outstanding': 1.1, 'Good': 1.05, 'Satisfactory': 1.0}
    final_ratings = {}
    for emp, score in zip(employees, adjusted_scores):
        category = performance_category[emp]
        multiplier = category_multiplier[category]
        final_ratings[emp] = round(score * multiplier)
    
    total_score = sum(final_ratings.values())
    print(f"Result: {total_score}")

analyze_performance()