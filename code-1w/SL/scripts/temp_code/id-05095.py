from collections import defaultdict, Counter

# Simulate tournament results with team performance tracking
def simulate_tournament_results():
    teams = ['alpha', 'beta', 'gamma', 'delta', 'epsilon']
    points = [120, 98, 105, 110, 92]
    penalties = [15, 8, 12, 10, 20]
    bonus_awarded = [True, False, True, False, True]

    # Irrelevant stats (distractor)
    total_matches = len(teams) * (len(teams) - 1) // 2
    avg_duration = 45.5  # minutes

    # Compute net scores
    net_scores = {}
    for i, team in enumerate(teams):
        base = points[i] - penalties[i]
        if bonus_awarded[i]:
            base += 7
        net_scores[team] = base

    # Ranking based on net score
    sorted_teams = sorted(net_scores.keys(), key=lambda x: net_scores[x], reverse=True)
    rankings = {}
    for rank, team in enumerate(sorted_teams, 1):
        rankings[team] = rank

    # Use of enumerate and zip (required features)
    rank_list = list(enumerate(sorted_teams, start=1))
    penalty_map = dict(zip(sorted_teams, [penalties[teams.index(t)] for t in sorted_teams]))

    # Set operations to find high performers (distractor computation)
    high_scorers = {t for t, s in net_scores.items() if s >= 100}
    penalized_heavily = {t for t in teams if penalties[teams.index(t)] > 10}
    borderline = high_scorers ^ penalized_heavily  # Symmetric difference (irrelevant)

    # Weight assignment using defaultdict
    weights = defaultdict(float)
    for idx, team in enumerate(sorted_teams):
        weights[team] = round(0.9 - (idx * 0.1), 1)

    # Another distractor: frequency count of penalty tiers
    penalty_tiers = ['low', 'medium', 'high']
    tier_mapping = {}
    for p in penalties:
        if p < 10:
            tier_mapping[p] = 'low'
        elif p <= 15:
            tier_mapping[p] = 'medium'
        else:
            tier_mapping[p] = 'high'
    tier_counts = Counter(tier_mapping.values())

    # Critical function call
    final_score = calculate_final_score(rankings, weights)
    
    # Print result as required
    print(f"Result: {final_score}")
    return final_score


def calculate_final_score(ranks, wts):
    score = 0.0
    adjustment_factor = 1.5

    # Use of items() and logic across multiple concepts
    for team, rank in ranks.items():
        weight = wts[team]
        # Composite calculation: rank contribution scaled by weight
        contribution = (11 - rank) * weight  # higher rank → more points
        if rank <= 3:
            contribution *= adjustment_factor  # boost top 3
        score += contribution
    
    # Dead code path (distractor)
    if False:
        backup = sum(wts.values()) * 10
        score = max(score, backup)

    # Final transformation
    score = round(score, 3)
    return score

# Execute simulation
result = simulate_tournament_results()