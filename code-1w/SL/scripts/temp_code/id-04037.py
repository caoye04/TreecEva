from collections import defaultdict

# Simulate analytics processing for a tournament ranking system
def preprocess_ranks(raw_scores):
    rank_data = defaultdict(int)
    temp_counts = defaultdict(lambda: 0)

    for score in raw_scores:
        if score > 50:
            rank_data['high'] += 1
        elif score > 25:
            rank_data['medium'] += 1
        else:
            rank_data['low'] += 1
        
        # Distractor: tracking even/odd for no reason
        temp_counts['even' if score % 2 == 0 else 'odd'] += 1

    # Irrelevant transformation
    adjustment_factor = sum(temp_counts.values()) / (rank_data['medium'] + 1)
    adjusted_high = rank_data['high'] * (1 + adjustment_factor * 0.1)

    return dict(rank_data), adjusted_high

def compute_statistics(values):
    # Unused helper function (dead code path)
    mean = sum(values) / len(values)
    variance = sum((x - mean) ** 2 for x in values) / len(values)
    return mean, variance

def calculate_final_score(rank_distribution, multiplier):
    base = 0
    # Logical weighting with conditional boosts
    if rank_distribution['high'] > rank_distribution['low']:
        base += 10 * rank_distribution['high']
    else:
        base += 5 * rank_distribution['medium']

    # Additional logic step: combinatorics-inspired weighting
    combo_weight = 0
    for k in rank_distribution:
        if k == 'high':
            combo_weight += rank_distribution[k] * 2
        elif k == 'medium':
            combo_weight += rank_distribution[k] * 1
        else:
            combo_weight -= rank_distribution[k]  # penalty for low

    # Apply multiplier and combine
    intermediate_result = base + combo_weight
    scaling_shift = (intermediate_result % 7) / 10.0  # minor decimal influence
    final_value = intermediate_result * multiplier + scaling_shift

    # Distractor calculation
    dummy_sequence = [i ** 2 for i in range(1, 6) if i % 2 == 1]
    dummy_sum = sum(x for x in dummy_sequence if x < 20)

    return int(final_value)  # deterministic integer output

# Main execution flow
raw_input_scores = [85, 42, 67, 23, 91, 58, 16, 77, 34, 49]
bonus_multiplier = 1.3

# Preprocessing step with side results
rank_info, adjusted_high_count = preprocess_ranks(raw_input_scores)

# Auxiliary analysis (not used in final path)
count_high_peaks = sum(1 for s in raw_input_scores if s >= 80)
even_ratio = len([s for s in raw_input_scores if s % 2 == 0]) / len(raw_input_scores)

# Core computation
final_score = calculate_final_score(rank_info, bonus_multiplier)

# Output result as required
print(f"Result: {final_score}")