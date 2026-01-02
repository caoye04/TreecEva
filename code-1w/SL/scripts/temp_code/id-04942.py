from collections import defaultdict

# Simulate a tournament ranking system with weighted scoring
def main():
    player_data = [
        ('Alice', [85, 90, 78]),
        ('Bob', [92, 88, 85]),
        ('Charlie', [76, 85, 90]),
        ('Diana', [94, 91, 89])
    ]

    # Extract rankings based on average performance
    averages = {}
    for name, scores in player_data:
        avg = sum(scores) / len(scores)
        averages[name] = round(avg, 2)

    # Sort players by average score (descending)
    sorted_players = sorted(averages.keys(), key=lambda x: averages[x], reverse=True)
    rankings = {player: idx + 1 for idx, player in enumerate(sorted_players)}

    # Misleading: irrelevant normalization process
    total_avg = sum(averages.values())
    normalized_averages = {k: v / total_avg for k, v in averages.items()}  # Not used later

    # Weight vector for ranking positions (more weight to top ranks)
    weights = [10, 7, 4, 2]  # Decreasing importance

    # Distractor: unused alternative weighting
    alt_weights = [w * 1.1 for w in weights]
    temp_sum = sum(alt_weights)  # Dead computation

    # Auxiliary function to compute final score based on rank and weights
    def calculate_final_score(ranks, w):
        score_map = defaultdict(float)
        for player, rank in ranks.items():
            if rank <= len(w):  # Only top 4 get scores
                score_map[player] += w[rank - 1] * 0.8  # Apply multiplier

        # Secondary adjustment based on alphabetical order (minor effect)
        sorted_names = sorted(ranks.keys())
        bonus_accumulator = 0.0
        for i, name in enumerate(sorted_names):
            if i % 2 == 0:
                bonus_accumulator += 0.3
                score_map[name] += bonus_accumulator  # Small incremental bonus

        # Final aggregation
        total_score = 0.0
        for val in score_map.values():
            total_score += val

        return round(total_score, 4)

    # Execute calculation
    final_score = calculate_final_score(rankings, weights)

    # Red herring: complex but unused list comprehension
    _ = [[(i, j) for j in range(3) if j != i] for i in range(3)]

    # Output result
    print(f"Result: {final_score}")

if __name__ == "__main__":
    main()