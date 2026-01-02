from collections import defaultdict

# Simulate daily user engagement scores with decay factors
engagement = [12, 15, 10, 8, 20]
decay_factors = [0.9, 0.85, 0.8, 0.75, 0.7]
penalty_points = [2, 3, 1, 4, 2]

# Irrelevant auxiliary tracking (minor distraction)
counter = defaultdict(int)
for score in engagement:
    counter[score > 10] += 1

# Main computation: weighted total score with progressive penalties
total_score = 0
for i in range(len(engagement)):
    adjusted = engagement[i] * decay_factors[i]
    total_score += adjusted
    if i % 2 == 0:
        total_score -= 1  # Small correction on even days
    total_score += penalty_points[i] * (i + 1)

Result: total_score