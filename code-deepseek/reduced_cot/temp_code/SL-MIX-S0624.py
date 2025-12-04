data_points = [(3, 'low'), (7, 'medium'), (5, 'high'), (2, 'low')]
weight_multiplier = lambda priority: {'low': 1, 'medium': 2, 'high': 3}[priority]
base_score = 0
for value, priority in data_points:
    base_score += value * weight_multiplier(priority)
bonus_points = 8
adjusted_data = base_score * 0.75
final_score = adjusted_data + bonus_points
print(f"Result: {final_score}")