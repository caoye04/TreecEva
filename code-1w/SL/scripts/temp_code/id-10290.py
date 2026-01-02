def calculate_final_score(data, weights):
    # Preprocessing: clean and normalize string-based rank entries
    normalized = {}
    for key, val in data.items():
        if isinstance(val, str):
            cleaned = val.strip().lower().replace('rank_', '')
            try:
                normalized[key] = int(cleaned)
            except ValueError:
                normalized[key] = 0
        else:
            normalized[key] = max(1, min(10, abs(val)))  # clamp to 1-10

    # Irrelevant distraction: process unused metadata
    total_chars = 0
    for k in data.keys():
        total_chars += len(k)  # unused computation
    avg_length = total_chars / len(data) if data else 0
    scaling_factor = 1.0 + (avg_length % 3) * 0.1  # dead end

    # Core logic: weighted aggregation with conditional boost
    base_score = 0
    boost_count = 0
    weight_sum = 0

    for i, (k, v) in enumerate(normalized.items()):
        weight = weights.get(k, 1.0)
        base_score += v * weight
        weight_sum += weight
        
        # Conditional logic: boost if high rank early in iteration
        if v <= 3 and i < 4:  # top 3 rank in first 4 items
            boost_count += 1

    if boost_count >= 2:
        base_score *= 1.25  # significant multiplier

    # Distractor: complex dictionary restructuring (unused)
    summary = {f"item_{i}": {'name': k, 'raw': data[k], 'norm': v} 
               for i, (k, v) in enumerate(normalized.items())}
    summary['stats'] = {'size': len(summary), 'boosts': boost_count}

    # Final adjustment based on sorted order (real dependency)
    sorted_ranks = sorted(normalized.values())
    median_rank = sorted_ranks[len(sorted_ranks)//2]
    final_adjustment = 10 - median_rank  # higher if median is low

    final_score = int(base_score // 1) + final_adjustment

    return final_score

# Main execution
rank_data = {
    'player_a': 'rank_2',
    'player_b': 8,
    'player_c': 'rank_1',
    'player_d': 5,
    'player_e': 'rank_3',
    'player_f': 11  # clamped to 10
}

bonus_weights = {
    'player_a': 1.5,
    'player_c': 2.0,
    'player_e': 1.8,
    'player_x': 3.0  # irrelevant key
}

interim_result = sum(len(name) for name in rank_data.keys()) % 7  # red herring

final_score = calculate_final_score(rank_data, bonus_weights)
print(f"Result: {final_score}")