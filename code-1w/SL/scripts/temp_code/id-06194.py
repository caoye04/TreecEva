from collections import defaultdict, Counter

# Simulated tournament ranking system with weighted performance metrics
def calculate_rank_metrics(players):
    rank_map = {}
    for idx, player in enumerate(players):
        rank_map[player['name']] = len(players) - idx  # Higher index = better rank
    return rank_map

def compute_consistency_score(records):
    consistency = defaultdict(int)
    for name, record in records.items():
        win_streak = 0
        max_streak = 0
        for outcome in record:
            if outcome == 'W':
                win_streak += 1
                max_streak = max(max_streak, win_streak)
            else:
                win_streak = 0
        consistency[name] = max_streak
    return consistency

def filter_eligible_players(roster, min_tournaments):
    # Irrelevant filtering path - not used in final computation
    eligible = []
    for entry in roster:
        if entry['tournaments'] >= min_tournaments:
            eligible.append(entry['name'])
    return eligible

def analyze_head_to_head(results):
    # Dead function - collects data but never used
    h2h_matrix = defaultdict(lambda: defaultdict(int))
    for p1, p2, winner in results:
        if winner == p1:
            h2h_matrix[p1][p2] += 1
        else:
            h2h_matrix[p2][p1] += 1
    return h2h_matrix

def adjust_for_variance(scores, factor=0.85):
    # Distractor transformation - looks important but unused
    adjusted = {}
    for k, v in scores.items():
        adjusted[k] = round(v * (1 + factor / 10), 4)
    return adjusted

def derive_impact_multiplier(counts):
    multiplier = {}
    total_events = sum(counts.values())
    for event, count in counts.items():
        multiplier[event] = round(count / total_events, 3) if total_events > 0 else 0
    return multiplier

def extract_key_performances(metrics, cutoff=2):
    # Another red herring - processes data not used downstream
    highlights = []
    for player, score in metrics.items():
        if score >= cutoff:
            highlights.append(f'{player}:{score}')
    return sorted(highlights)

def aggregate_performance(ranks, weights):
    # Core logic buried among distractions
    base_total = 0
    bonus = 0
    tier_bonus = {1: 25, 2: 15, 3: 10}  # Bonus for top 3 ranks
    for name, rank in ranks.items():
        weight = weights.get(name, 1.0)
        base_total += round(rank * weight * 1.1, 2)
        if rank <= 3:
            bonus += tier_bonus[rank]
    
    # Secondary calculation using slicing and counting
    names = list(ranks.keys())
    mid_section = names[1:-1]  # Exclude first and last
    counter = Counter(mid_section)
    diversity_factor = len(counter) * 2
    
    # Final composition
    raw_score = int(base_total + bonus)
    adjustment = sum(diversity_factor for _ in range(1))  # Simple but obscured
    return raw_score + adjustment

# Main execution block
if __name__ == '__main__':
    # Player data
    participants = [
        {'name': 'Alice', 'seed': 5, 'region': 'north'},
        {'name': 'Bob', 'seed': 1, 'region': 'south'},
        {'name': 'Charlie', 'seed': 3, 'region': 'east'},
        {'name': 'Diana', 'seed': 2, 'region': 'west'},
        {'name': 'Evan', 'seed': 4, 'region': 'central'}
    ]

    match_records = {
        'Alice': ['W', 'L', 'W', 'W'],
        'Bob': ['L', 'W', 'W', 'W', 'W'],
        'Charlie': ['W', 'L', 'W', 'L'],
        'Diana': ['W', 'W', 'W', 'W'],
        'Evan': ['L', 'L', 'W', 'W']
    }

    registration_roster = [
        {'name': 'Alice', 'tournaments': 4},
        {'name': 'Bob', 'tournaments': 5},
        {'name': 'Charlie', 'tournaments': 3},
        {'name': 'Diana', 'tournaments': 6},
        {'name': 'Evan', 'tournaments': 2}
    ]

    head_to_head_results = [
        ('Alice', 'Bob', 'Bob'),
        ('Charlie', 'Diana', 'Diana'),
        ('Alice', 'Evan', 'Alice')
    ]

    # Step 1: Compute rankings from participant order
    player_names = [p['name'] for p in participants]
    performance_ranks = calculate_rank_metrics(participants)  # {'Alice':5, 'Bob':4, ...}

    # Step 2: Consistency scores (partially relevant)
    consistency = compute_consistency_score(match_records)

    # Step 3: Irrelevant eligibility check
    qualified_players = filter_eligible_players(registration_roster, 4)

    # Step 4: Unused head-to-head analysis
    h2h_stats = analyze_head_to_head(head_to_head_results)

    # Step 5: Derive impact multipliers from fictitious event counts
    event_counts = {'regional': 3, 'national': 2, 'friendly': 4}
    impacts = derive_impact_multiplier(event_counts)  # {'regional': 0.333, ...}

    # Step 6: Adjust ranks with dummy weights
    base_weights = {}
    for name in player_names:
        base_weight = 1.0
        if consistency.get(name, 0) >= 3:
            base_weight += 0.25
        if name in ['Alice', 'Diana']:
            base_weight *= 1.1
        base_weights[name] = round(base_weight, 2)

    # Step 7: Extract performance highlights (unused)
    key_perfs = extract_key_performances(consistency, cutoff=3)

    # Step 8: Adjust for variance (dead end)
    skewed_scores = adjust_for_variance(performance_ranks)

    # Step 9: Critical statement - compute final score
    final_score = aggregate_performance(performance_ranks, base_weights)

    # Output result
    print(f"Result: {final_score}")