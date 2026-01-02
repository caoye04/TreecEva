from collections import defaultdict

def calculate_final_score(ranks, multiplier):
    base_points = defaultdict(int)
    for category, rank in ranks.items():
        if rank <= 3:
            base_points[category] += 10 - (rank * 2)
        elif rank <= 6:
            base_points[category] += 5
    adjustment = len(base_points) // 2
    total = sum(base_points.values())
    total //= 2  # Integer division to scale down
    if total > 20:
        total += multiplier * 3
    return total + adjustment

# Irrelevant auxiliary variable (minimal distraction)
current_phase = "evaluation"
bonus_multiplier = 4
rank_data = {
    "ux_design": 2,
    "performance": 5,
    "security": 1,
    "compatibility": 7,
    "accessibility": 3
}
initial_flag = True
final_score = calculate_final_score(rank_data, bonus_multiplier)
print(f"Result: {final_score}")