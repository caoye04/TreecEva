def calculate_final_score(points, deductions):
    base = sum(points)
    penalty_total = max(deductions) if deductions else 0
    adjustment = len(points) * 0.5
    
    # Apply conditional bonus or penalty based on performance metrics
    performance_flag = 'high' if base > 80 else 'low'
    bonus = 10 if performance_flag == 'high' and len(points) >= 3 else 0
    
    raw_score = base - penalty_total + bonus - adjustment
    
    # Normalize score to range [0, 100] if needed
    final = max(0, min(100, raw_score))
    return int(final)

# Simulated assessment data
raw_points = [25, 18, 22, 15]
penalties = [5, 12, 8]

# Irrelevant auxiliary variables (minimal distraction - intervention level 5)
date_recorded = '2023-11-05'
assessment_type = 'cognitive'
temp_result = None

final_score = calculate_final_score(raw_points, penalties)
print(f"Result: {final_score}")