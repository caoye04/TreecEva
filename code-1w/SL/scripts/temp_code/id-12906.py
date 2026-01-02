def calculate_total(scores):
    bonus = 10
    penalty = 2
    base = sum(scores.values())
    if base > 50:
        base += bonus
    else:
        base -= penalty
    return base

# Student performance tracking
task_weights = {'hw': 0.25, 'quiz': 0.25, 'project': 0.5}
raw_points = {'hw': 20, 'quiz': 18, 'project': 45}

points_map = {}
for k, v in raw_points.items():
    points_map[k] = int(v * task_weights[k])

# Adjust for participation
points_map['participation'] = 5

final_score = calculate_total(points_map)
print(f"Result: {final_score}")