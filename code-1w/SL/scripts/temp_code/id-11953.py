scores = {'alice': 85, 'bob': 90, 'charlie': 95, 'diana': 88}
weights = {'exam': 0.6, 'project': 0.4}

# Base performance calculation
weighted_avg = (scores['bob'] * weights['exam']) + (scores['diana'] * weights['project'])

# Performance categorization
cutoff = 87.5
is_above_cutoff = weighted_avg > cutoff

performance_level = 'high' if is_above_cutoff else 'medium'

high_performers = ['high']
apply_bonus = True if performance_level in high_performers else False

bonus = 50 if apply_bonus else 0
base_salary = 4500

final_score = base_salary + bonus
print(f"Result: {final_score}")