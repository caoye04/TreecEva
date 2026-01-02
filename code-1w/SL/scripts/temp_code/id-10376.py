def compute_efficiency(base, hours, threshold=40):
    overtime_ratio = (hours - threshold) / threshold if hours > threshold else 0
    return base * (1 + overtime_ratio)

productivity = [85, 90, 78, 92]
weights = [0.2, 0.3, 0.15, 0.35]

weighted_avg = sum(p * w for p, w in zip(productivity, weights))

base_rating = 75
hours_worked = 45

# Key computation chain
initial_effort = compute_efficiency(base_rating, hours_worked)
stress_factor = max(weighted_avg - 80, 0) / 10

apply_bonus = lambda x: 1.05 + 0.02 * min(x, 3)
final_adjustment = apply_bonus(stress_factor)
efficiency_score = initial_effort * final_adjustment

Result: efficiency_score