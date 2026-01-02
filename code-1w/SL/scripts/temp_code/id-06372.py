from collections import defaultdict

# Simulate player rankings across multiple tournaments
tournament_results = [
    ['Alice', 'Bob', 'Charlie'],
    ['Bob', 'Alice', 'Diana'],
    ['Charlie', 'Diana', 'Alice'],
    ['Alice', 'Bob', 'Eve']
]

rank_counts = defaultdict(int)
participation_bonus = 0.0

# Accumulate rank positions (lower is better)
for result in tournament_results:
    for idx, player in enumerate(result):
        rank_counts[player] += idx + 1  # 1st place = 1 point, etc.

# Minor distraction: count total participants (not directly used in final score)
total_participants = len(rank_counts)

# Compute final score: inverse of average rank, higher is better
def calculate_final_score(rank_count_map):
    scores = {}
    for player, total_rank in rank_count_map.items():
        avg_rank = total_rank / 4  # 4 tournaments
        scores[player] = round(100 / avg_rank, 3)  # Scale for readability
    return max(scores.values())  # Best player's scaled score

final_score = calculate_final_score(rank_counts)
print(f"Target result: {final_score}")