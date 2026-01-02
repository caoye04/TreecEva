def process_leaderboard(entries):
    # Irrelevant preprocessing: normalize names
    normalized = [name.strip().title() for name in entries.keys()]
    temp_scores = {}
    for name, data in entries.items():
        raw_score = data['base'] * data['multiplier']
        if raw_score > 100:
            raw_score = 95  # artificial cap (not used later)
        temp_scores[name] = raw_score + 5

    # Real computation begins: extract rankings based on adjusted metric
    ranking_data = []
    for name, data in entries.items():
        adjusted = data['base'] + (data['bonus'] * 0.1)
        ranking_data.append((name, adjusted))
    
    # Sort by adjusted score descending
    ranking_data.sort(key=lambda x: x[1], reverse=True)
    
    # Assign ranks with tie consideration (unused)
    rank_dict = {}
    prev_score = None
    rank = 1
    for i, (name, score) in enumerate(ranking_data):
        if score != prev_score:
            rank = i + 1
        rank_dict[name] = rank
        prev_score = score

    # Compute frequency of letter 'a' in all names (distraction)
    total_a_count = sum(name.lower().count('a') for name in entries.keys())
    adjustment_factor = total_a_count % 4 + 1
    
    # Build final rankings with red herring transformations
    rankings = {}
    for idx, (name, score) in enumerate(ranking_data):
        # This transformation is irrelevant but looks important
        noise = (idx * adjustment_factor) % 3
        rankings[name] = score - noise + len(name)

    # Define weighting schema (some weights are misleading)
    weights = {
        'base_contribution': 0.6,
        'length_bonus': 0.2,  # unused in actual calc
        'position_penalty': 0.1,  # unused
        'rank_adjustment': 0.1
    }

    return rankings, weights


def calculate_rating(ranks, w):
    # Actual rating formula uses only specific components
    names = list(ranks.keys())
    total = 0.0
    for i, name in enumerate(names):
        base_val = ranks[name]
        # Only base and rank order matter
        position_weight = 1 - (i * 0.05)  # decreases by 5% per rank
        total += base_val * position_weight
    
    # Apply fixed scaling
    scaled = total * 0.85
    
    # Dead code: complex dictionary manipulation that does nothing
    stats = {}
    parts = [str(int(scaled)), str(scaled % 1).split('.')[1]]
    joined = ''.join(parts)
    segments = [joined[i:i+2] for i in range(0, len(joined), 2)]
    for s in segments:
        if len(s) == 2:
            stats[s] = int(s) ** 2
    
    # Final irrelevant smoothing
    if len(stats) > 5:
        smoothed = sum(v % 10 for v in stats.values()) / 10
        scaled += smoothed  # minor bump, but not impactful in this case

    return int(scaled)

# Main execution
contestants = {
    'alice jennings': {'base': 88, 'multiplier': 1.1, 'bonus': 12},
    'brian tao': {'base': 92, 'multiplier': 1.0, 'bonus': 8},
    'clara mendez': {'base': 85, 'multiplier': 1.2, 'bonus': 15},
    'daniel park': {'base': 90, 'multiplier': 1.05, 'bonus': 10}
}

# Trigger processing
rankings, weights = process_leaderboard(contestants)
final_score = calculate_rating(rankings, weights)

print(f"Result: {final_score}")