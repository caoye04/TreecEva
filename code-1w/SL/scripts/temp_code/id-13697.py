from collections import defaultdict

# Simulate a tournament ranking system with weighted scoring
def main():
    player_data = [
        ('Alice', [85, 90, 78, 88]),
        ('Bob', [76, 85, 82, 93]),
        ('Charlie', [92, 88, 85, 87]),
        ('Diana', [87, 92, 80, 90])
    ]

    # Irrelevant aggregation: average per round (not used in final score)
    round_averages = []
    for i in range(4):
        total = 0
        for data in player_data:
            total += data[1][i]
        round_averages.append(total / 4)

    # Extract rankings per player based on total performance
    raw_totals = {name: sum(scores) for name, scores in player_data}
    sorted_players = sorted(raw_totals.keys(), key=lambda x: raw_totals[x], reverse=True)
    rankings = {player: idx + 1 for idx, player in enumerate(sorted_players)}

    # Misleading normalization (unused)
    max_total = max(raw_totals.values())
    normalized_scores = {p: raw_totals[p] / max_total for p in raw_totals}

    # Weight vector for scoring: recent rounds more important
    weights = [0.1, 0.2, 0.3, 0.4]

    # Calculate individual weighted scores (used in final calculation)
    weighted_scores = {}
    for name, scores in player_data:
        weighted_sum = sum(score * weight for score, weight in zip(scores, weights))
        weighted_scores[name] = weighted_sum

    # Secondary ranking based on weighted scores
    weighted_ranking = sorted(weighted_scores.keys(), key=lambda x: weighted_scores[x], reverse=True)
    weighted_ranks = {p: i+1 for i, p in enumerate(weighted_ranking)}

    # Distractor: track rank changes (not used)
    rank_shifts = {p: abs(rankings[p] - weighted_ranks[p]) for p in rankings}

    # Final score calculation: combine base rank and weighted consistency
    def calculate_final_score(base_ranks, weight_vector):
        consistency_check = 0
        for name, scores in player_data:
            # Compute variance proxy (centered around mean)
            mean_score = sum(scores) / len(scores)
            variance_proxy = sum((s - mean_score)**2 for s in scores)
            if variance_proxy < 20:
                consistency_check += 1

        # Bonus logic: players with low variance get rank advantage
        adjusted_rank_sum = 0
        for player, base_rank in base_ranks.items():
            effective_rank = base_rank
            player_mean = sum([s for s in dict(player_data)[player]]) / 4
            if player_mean >= 85:
                # High average performers get slight bump
                effective_rank = max(1, base_rank - 1)
            adjusted_rank_sum += effective_rank

        # Key distractor computation (unused)
        phantom_score = 0
        for i, w in enumerate(weight_vector):
            if i % 2 == 0:
                phantom_score += w * 100
            else:
                phantom_score -= w * 50

        # Actual answer depends only on adjusted_rank_sum and consistency_check
        return (adjusted_rank_sum * 10) + (consistency_check * 5)

    final_score = calculate_final_score(rankings, weights)
    print(f"Result: {final_score}")

if __name__ == "__main__":
    main()