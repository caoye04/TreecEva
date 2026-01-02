def analyze_performance(stats):
    # Irrelevant transformation (distractor)
    temp_boost = sum([v * 0.1 for v in stats.values()])
    enhanced_stats = {k: v + temp_boost for k, v in stats.items()}

    # Real logic begins: compute efficiency ratio
    attempts = stats['shots'] + stats['passes'] + stats['tackles']
    successes = stats['shots'] * 0.3 + stats['passes'] * 0.85 + stats['tackles'] * 0.6
    efficiency = successes / attempts if attempts > 0 else 0

    # Distraction: unused branching
    if efficiency > 0.7:
        tier = 'elite'
    elif efficiency > 0.5:
        tier = 'average'
    else:
        tier = 'development'
        adjustment = -0.1  # Dead code path variable

    return efficiency


def count_alphabetic(text):
    # Distractor function: not directly used in final score but looks relevant
    return sum(1 for c in text if c.isalpha())


def calculate_final_score(data):
    raw_score = 0
    bonus = 0

    # Use of dictionary operations (required)
    for game, stats in data.items():
        performance = analyze_performance(stats)
        raw_score += performance

        # Conditional bonus based on game context (semi-relevant)
        if 'championship' in game.lower():
            bonus += 5

        # Early termination based on threshold (suggested paradigm)
        if raw_score > 2.0:
            break  # Simulates early return logic

    # Final aggregation with misleading intermediate steps
    normalized = raw_score * 10
    penalty = 0
    for stat_dict in data.values():
        total_actions = sum(stat_dict.values())
        if total_actions > 100:
            penalty += 1  # Minor penalty for high volume, rarely triggered

    final_score = int(normalized - penalty + bonus)

    # Print required output format
    print(f"Target result: {final_score}")
    return final_score

# Main execution
player_data = {
    'friendly_match': {'shots': 5, 'passes': 40, 'tackles': 3},
    'league_game': {'shots': 8, 'passes': 75, 'tackles': 6},
    'championship_final': {'shots': 12, 'passes': 90, 'tackles': 8}
}

final_score = calculate_final_score(player_data)