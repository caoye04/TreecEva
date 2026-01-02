from collections import defaultdict

# Simulate round-based scoring with weighted multipliers
def calculate_tournament_score():
    rounds = [3, 5, 2, 4, 6]
    bonuses = {2: -1, 4: 2}
    points = defaultdict(int)
    
    for i, score in enumerate(rounds):
        base = score if score % 2 == 0 else score + 1
        points[i] = base + bonuses.get(score, 0)
    
    total_score = 0
    multiplier_tracker = []
    
    for i in range(len(points)):
        if points[i] <= 0:
            continue
        total_score += points[i] * (i + 1)
        multiplier_tracker.append(i + 1)
    
    # Irrelevant debugging line (minimal interference)
    debug_info = f"Applied multipliers: {multiplier_tracker}"
    
    print(f"Result: {total_score}")

calculate_tournament_score()