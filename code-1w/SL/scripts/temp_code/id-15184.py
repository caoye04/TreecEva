from collections import defaultdict, Counter

# Simulate user interaction logs with action counts
def generate_interaction_counts(actions):
    count_map = defaultdict(int)
    for action in actions:
        count_map[action] += 1
    return count_map

# Analyze sequence patterns for repeated behavior
def detect_repeats(logs):
    repeats = 0
    for i in range(len(logs) - 2):
        if logs[i] == logs[i+1] == logs[i+2]:
            repeats += 1
    return repeats

# Core scoring logic with combinatorial weighting
def calculate_combinations(n, r):
    if r > n or r < 0:
        return 0
    # Simple combinatorics using factorial reduction
    result = 1
    for i in range(min(r, n - r)):
        result = result * (n - i) // (i + 1)
    return result

# Main score calculation with multiple factors
def calculate_final_score(ranks, weights):
    base_score = 0
    combo_score = 0
    adjustment_factor = 0.0

    # Irrelevant helper: counts rank frequencies but only some are used
    rank_freq = Counter(ranks)
    rare_ranks = [r for r, cnt in rank_freq.items() if cnt < 2]

    # Real computation: sum top 3 ranks
    sorted_ranks = sorted(ranks, reverse=True)
    for i in range(3):
        base_score += sorted_ranks[i]

    # Bonus from combination logic
    unique_ranks = len(set(ranks))
    combo_score = calculate_combinations(unique_ranks, 2)

    # Red herring: complex weight mapping that's only partially used
    weighted_sum = 0
    temp_debug = []
    for idx, w in enumerate(weights):
        temp_debug.append(w * (idx + 1))  # dead computation
        if idx % 2 == 0:
            weighted_sum += w

    # Adjustment uses only odd indices sum
    odd_weight_sum = sum(weights[1::2])
    if odd_weight_sum > 0:
        adjustment_factor = combo_score / odd_weight_sum

    # Final composition
    final_score = base_score + int(adjustment_factor)

    # Dead code: tracking unused stats
    debug_stats = defaultdict(list)
    debug_stats['actions'].append('processed')
    debug_stats['stages'].extend(['init', 'mid', 'final'])

    return final_score

# Simulated input data
rank_data = [8, 12, 5, 12, 3, 7, 8]
bonus_weights = [4, 6, 2, 8, 1]

# Misleading pre-processing (not affecting final outcome)
action_log = ['click', 'hover', 'click', 'scroll', 'click', 'keypress']
interaction_counts = generate_interaction_counts(action_log)
repeated_patterns = detect_repeats(action_log)

# Key execution point
final_score = calculate_final_score(rank_data, bonus_weights)
print(f"Result: {final_score}")