def analyze_productivity(logs):
    total_hours = 0
    idle_count = 0
    peak_moments = []

    for i, (hour, activity) in enumerate(logs):
        total_hours += hour
        if activity < 0.2:
            idle_count += 1
        elif activity > 0.8:
            peak_moments.append(i)

    efficiency = total_hours / len(logs) if logs else 0
    return efficiency, idle_count, peak_moments


def calculate_rating(contributions, impact_levels):
    base_score = 0
    bonus = 0
    penalty = 0

    # Misleading pre-processing
    temp_data = [x * 1.5 for x in impact_levels if x > 0]
    temp_sum = sum(temp_data) + 10  # Unused distraction

    for idx, (contribution, impact) in enumerate(zip(contributions, impact_levels)):
        if contribution <= 0:
            continue
        if impact >= 0.7:
            base_score += contribution * 2
            if idx % 3 == 0:
                bonus += 5
        elif impact < 0.3:
            penalty += contribution // 4

    # Secondary loop with partial relevance
    adjustment = 0
    for i in range(len(contributions)):
        if i % 4 == 0 and contributions[i] > 0:
            adjustment += 2

    final_rating = base_score + bonus - penalty + adjustment
    return int(final_rating)

# Simulated dataset
work_logs = [(1, 0.85), (2, 0.15), (3, 0.92), (4, 0.08), (5, 0.77)]
efficiency, _, _ = analyze_productivity(work_logs)

contributions = [10, 15, 0, 20, 25, 12]
impact_levels = [0.8, 0.75, 0.1, 0.9, 0.65, 0.85]

# Key statement
final_score = calculate_rating(contributions, impact_levels)

print(f"Target result: {final_score}")