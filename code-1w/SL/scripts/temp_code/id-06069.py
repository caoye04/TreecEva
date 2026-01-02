from collections import Counter

def calculate_final_score(standings):
    points = Counter()
    
    # Simulate round results
    rounds = [
        ['Alice', 'Bob', 'Charlie', 'Alice'],
        ['Bob', 'Alice', 'Alice', 'Charlie'],
        ['Charlie', 'Alice', 'Bob', 'Bob']
    ]
    
    for round_result in rounds:
        winner = round_result[0]
        runner_up = round_result[1]
        
        points[winner] += 3
        points[runner_up] += 1
    
    # Bonus for most wins
    max_wins = max(points.values())
    for player, win_count in points.items():
        if win_count == max_wins:
            points[player] += 2  # Consistency bonus
            break
    
    total_score = 0
    for player in standings:
        if player in points:
            total_score += points[player]
    
    return total_score

# Irrelevant auxiliary variable (minor distraction)
unused_threshold = 5

leaderboard = ['Alice', 'Bob']
final_score = calculate_final_score(leaderboard)
print(f"Result: {final_score}")