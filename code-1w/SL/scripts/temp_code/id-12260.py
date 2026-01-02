from collections import Counter

# Simulate player rankings from tournament rounds
def evaluate_tournament_performance(players, rounds):
    rank_history = []
    for r in rounds:
        rank_history.extend(r['ranking'])
    
    # Count how many times each player was ranked
    rank_counts = Counter(rank_history)
    
    # Base scores derived from average performance
    base_scores = {player: (ord(player[0]) - ord('A') + 1) * 1.5 for player in players}
    
    # Irrelevant debug variable (minor distraction - intervention level 5)
    debug_mode = False
    
    # Calculate final score based on frequency and base value
    def calculate_final_score(counts, base_vals):
        score = 0
        for player, count in counts.items():
            if player in base_vals:
                bonus = 5 if count >= 3 else 2
                score += base_vals[player] * count + bonus
        return score

    total_score = calculate_final_score(rank_counts, base_scores)
    
    # Additional unrelated metric (minimal interference)
    avg_rank = len(rank_history) / len(players)
    
    return total_score

# Tournament data
participants = ['Alice', 'Bob', 'Charlie']
recent_rounds = [
    {'round': 'quarter', 'ranking': ['Alice', 'Bob']},
    {'round': 'semi',   'ranking': ['Charlie', 'Alice', 'Bob']},
    {'round': 'final',  'ranking': ['Alice', 'Charlie']}
]

result = evaluate_tournament_performance(participants, recent_rounds)
print(f"Result: {result}")