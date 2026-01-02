from collections import defaultdict, Counter

# Simulate a tournament scoring system with multiple rounds and partial data
def analyze_tournament_performance(players_data):
    aggregated_stats = defaultdict(float)
    event_counts = Counter()
    temp_buffer = []

    for player, records in players_data.items():
        raw_scores = [r['score'] for r in records]
        bonus_awarded = len([s for s in raw_scores if s > 85]) > 1
        adjustment_factor = 1.1 if bonus_awarded else 1.0

        base_total = sum(raw_scores)
        capped_scores = [min(s, 95) for s in raw_scores]
        adjusted_total = sum(capped_scores) * adjustment_factor

        # Irrelevant aggregation (distractor)
        for score in raw_scores:
            if score > 90:
                temp_buffer.append((player, score))

        aggregated_stats[player] += adjusted_total
        event_counts[player] += len(records)

    return aggregated_stats, event_counts, temp_buffer

def compute_rank_distribution(ranks):
    rank_freq = defaultdict(int)
    for r in ranks:
        rank_freq[r] += 1
    sorted_ranks = sorted(rank_freq.items())
    return [f"{k}:{v}" for k, v in sorted_ranks]

def compute_final_score(rankings, weights):
    score = 0.0
    weight_sum = 0

    # Real computation path
    for i, r in enumerate(rankings):
        if r <= 5:
            score += weights[i] * (10 - r)
            weight_sum += weights[i]

    normalized = score / weight_sum if weight_sum != 0 else 0

    # Dead code branch (distractor)
    if len(rankings) > 100:
        fallback = sum(rankings) // len(rankings)
        return fallback

    # Additional red herring
    debug_info = [f"Pos {i}: {r}" for i, r in enumerate(rankings[:3])]
    return round(normalized, 4)

# Main execution
if __name__ == "__main__":
    # Input data: mock tournament results
    participants = {
        'Alice': [
            {'event': 'E1', 'score': 88},
            {'event': 'E2', 'score': 92},
            {'event': 'E3', 'score': 87}
        ],
        'Bob': [
            {'event': 'E1', 'score': 76},
            {'event': 'E2', 'score': 94},
            {'event': 'E3', 'score': 89},
            {'event': 'E4', 'score': 95}
        ],
        'Charlie': [
            {'event': 'E1', 'score': 90},
            {'event': 'E2', 'score': 91}
        ]
    }

    # Step 1: Analyze performance (uses real logic + distractors)
    stats, counts, buffer = analyze_tournament_performance(participants)

    # Extract rankings based on total adjusted score
    ranked_players = sorted(stats.items(), key=lambda x: x[1], reverse=True)
    rankings = [i + 1 for i in range(len(ranked_players))]  # Final ranking positions

    # Mock weights for final score calculation
    weights = [1.0, 1.5, 2.0]  # Only first three matter due to condition in compute_final_score

    # Critical statement
    final_score = compute_final_score(rankings, weights)

    # Output result
    print(f"Result: {final_score}")