def calculate_weighted_score():
    # Simulate a scoring system with weights and thresholds
    points = [85, 90, 78, 92, 88]
    multipliers = [1, 2, 1, 3, 2]
    threshold = 80
    bonus_applied = False
    total_score = 0

    for i in range(len(points)):
        if points[i] < threshold:
            continue
        total_score += points[i] * multipliers[i]
        if points[i] > 90 and not bonus_applied:
            total_score += 10
            bonus_applied = True

    # Irrelevant tracking variable (minimal distraction)
    final_length = len(points)

    print(f"Result: {total_score}")

calculate_weighted_score()