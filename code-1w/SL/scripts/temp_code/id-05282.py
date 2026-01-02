import itertools

def analyze_pattern(sequence):
    count = 0
    trend = []
    for i in range(1, len(sequence)):
        if sequence[i] > sequence[i-1]:
            trend.append(1)
        elif sequence[i] < sequence[i-1]:
            trend.append(-1)
        else:
            trend.append(0)
    
    # Irrelevant computation: analyzing flat segments (not used later)
    flat_segments = 0
    for t in trend:
        if t == 0:
            flat_segments += 1

    # Real logic: count direction changes
    changes = 0
    for i in range(1, len(trend)):
        if trend[i] != trend[i-1] and trend[i] != 0:
            changes += 1

    return changes


def compute_entropy(values):
    from math import log2
    freq = {}
    total = len(values)
    for v in values:
        freq[v] = freq.get(v, 0) + 1
    
    entropy = 0.0
    for f in freq.values():
        p = f / total
        entropy -= p * log2(p) if p > 0 else 0
    
    # Dead code: normalized entropy never used
    if entropy > 0:
        normalized = entropy / log2(total) if total > 1 else 1
    
    return entropy


def process_metrics(data, config):
    # Extract relevant series
    time_series = [x['value'] for x in data if x['active']]
    categories = [x['category'] for x in data if x['active']]
    
    # Compute auxiliary metrics (some irrelevant)
    avg = sum(time_series) / len(time_series) if time_series else 0
    deviations = [abs(x - avg) for x in time_series]
    stability = sum(1 for d in deviations if d < config['stability_threshold'])

    # Dummy dictionary aggregation (partially irrelevant)
    category_stats = {}
    for cat in set(categories):
        category_stats[cat] = {
            'count': categories.count(cat),
            'weight': config['weights'].get(cat, 1.0)
        }
    
    # Unused nested structure
    meta_analysis = {
        'dimensions': len(category_stats),
        'distribution': {k: v['count'] for k, v in category_stats.items()},
        'flags': [False, True, False]
    }

    # Core logic begins
    pattern_complexity = analyze_pattern(time_series)
    info_content = compute_entropy(time_series)
    
    # Key intermediate (used later)
    base_score = len(time_series) * config['base_multiplier']
    adjustment = 0
    
    # Conditional logic with nesting
    if stability > len(time_series) // 2:
        if pattern_complexity < 4:
            adjustment += config['bonus_low_complexity']
        else:
            adjustment -= config['penalty_high_complexity']
    else:
        adjustment -= len(set(categories)) * 2

    # Bitwise masking for state encoding (real use)
    state_flag = 0
    state_flag |= int(stability > 5) << 1
    state_flag |= int(pattern_complexity % 2) << 2
    state_flag ^= int(info_content * 10) & 7  # XOR with truncated entropy part

    # Final computation
    final_score = base_score + adjustment
    final_score += (state_flag & 7) * config['flag_multiplier']  # Only lower 3 bits matter

    # Print result as required
    print(f"Result: {final_score}")
    return final_score

# Main execution
if __name__ == "__main__":
    raw_data = [
        {'value': 10, 'category': 'A', 'active': True},
        {'value': 12, 'category': 'B', 'active': True},
        {'value': 11, 'category': 'A', 'active': True},
        {'value': 15, 'category': 'C', 'active': True},
        {'value': 14, 'category': 'B', 'active': True},
        {'value': 14, 'category': 'A', 'active': True},
        {'value': 18, 'category': 'D', 'active': True},
        {'value': 17, 'category': 'A', 'active': False},  # Inactive
        {'value': 20, 'category': 'B', 'active': True}
    ]

    settings = {
        'stability_threshold': 3.0,
        'base_multiplier': 7,
        'bonus_low_complexity': 15,
        'penalty_high_complexity': 10,
        'flag_multiplier': 4,
        'weights': {'A': 1.1, 'B': 0.9, 'C': 1.0, 'D': 1.2}
    }

    final_score = process_metrics(raw_data, settings)
