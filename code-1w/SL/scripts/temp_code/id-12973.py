from collections import defaultdict, Counter

# Simulate processing of tournament results with scoring adjustments
def main():
    player_results = [
        ('Alice', 'win', 'fast'),
        ('Bob', 'loss', 'slow'),
        ('Charlie', 'win', 'fast'),
        ('Alice', 'win', 'slow'),
        ('David', 'win', 'fast'),
        ('Bob', 'win', 'fast'),
        ('Charlie', 'loss', 'slow'),
        ('David', 'loss', 'slow')
    ]

    # Irrelevant aggregation: count all outcomes by speed (not used in final logic)
    speed_count = defaultdict(int)
    for _, result, speed in player_results:
        speed_count[speed] += 1

    # Relevant: count wins per player
    win_count = defaultdict(int)
    for name, result, _ in player_results:
        if result == 'win':
            win_count[name] += 1

    # Distractor: complex but unused combo counter
    performance_grid = Counter((name, result) for name, result, _ in player_results)

    # Compute base rank score using win counts
    ranked_players = sorted(win_count.items(), key=lambda x: x[1], reverse=True)
    rank_score = {}
    for idx, (name, wins) in enumerate(ranked_players):
        rank_score[name] = 10 - idx  # Higher rank = higher base score

    # Bonus logic based on consistency of performance
    consistency_score = {}
    for name in win_count:
        total_entries = len([r for r in player_results if r[0] == name])
        win_streaks = 0
        current_streak = 0
        for _, result, _ in player_results:
            if result == 'win':
                current_streak += 1
                win_streaks = max(win_streaks, current_streak)
            else:
                current_streak = 0
        consistency_score[name] = win_streaks * 2

    # Unused distractor: average performance gap
    total_gaps = 0
    for i in range(len(ranked_players) - 1):
        total_gaps += ranked_players[i][1] - ranked_players[i+1][1]
    avg_gap = total_gaps / len(ranked_players) if ranked_players else 0

    # Critical data structure for final calculation
    rank_data = []
    for name, wins in ranked_players:
        base = rank_score[name]
        bonus = consistency_score[name]
        rank_data.append({'player': name, 'base': base, 'bonus': bonus})

    bonus_multiplier = 1.5

    # Key statement
    final_score = calculate_final_score(rank_data, bonus_multiplier)
    
    print(f"Result: {final_score}")

    return final_score


def calculate_final_score(data, mult):
    total = 0
    for entry in data:
        # Only top 3 contribute to final score
        if entry['base'] > 7:  
            contribution = entry['base'] + (entry['bonus'] * mult)
            total += int(contribution)  # Truncate any fractional part
    return total

if __name__ == "__main__":
    main()