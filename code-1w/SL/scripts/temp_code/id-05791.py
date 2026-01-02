employee_ratings = {'alice': 4.2, 'bob': 3.8, 'charlie': 4.5, 'diana': 4.0}
base_scores = [85, 76, 92, 88]
weights = [0.4, 0.3, 0.2, 0.1]

total_score = 0
for i, (name, rating) in enumerate(zip(employee_ratings.keys(), employee_ratings.values())):
    base = base_scores[i]
    weighted_rating = rating * weights[i] * 10
    performance_bonus = 0
    if rating >= 4.0:
        performance_bonus = 5
    total_score += weighted_rating
    total_score += performance_bonus

Result: total_score