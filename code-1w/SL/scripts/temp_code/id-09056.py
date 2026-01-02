from collections import defaultdict

# Simulate user engagement analytics with scoring logic
def analyze_engagement(logs):
    event_count = defaultdict(int)
    temporal_trend = []
    total_interactions = 0

    for entry in logs:
        event_type = entry['type']
        duration = entry['duration']
        event_count[event_type] += 1
        total_interactions += 1

        if duration > 50:
            temporal_trend.append(1)
        else:
            temporal_trend.append(0)

    high_dur_count = sum(temporal_trend)
    ratio = high_dur_count / total_interactions if total_interactions else 0

    return event_count, ratio, total_interactions


def calculate_contribution(count_dict, base_weight):
    contribution = 0
    weights = {'click': 1, 'hover': 0.5, 'scroll': 0.7, 'input': 2}
    scaling_factor = 1.5  # arbitrary scaling

    for event, count in count_dict.items():
        if event in weights:
            contribution += count * weights[event] * base_weight

    # Dead code branch - never reached due to structure
    if False:
        contribution *= scaling_factor

    return contribution


def calculate_final_score(ranks, flags):
    base_score = 0
    penalty = 0
    flag_bonuses = 0

    # Scoring based on rank positions (lower index = higher rank)
    for i, rank in enumerate(ranks):
        if rank <= 10:
            base_score += (11 - rank) * 2
        if i % 3 == 0 and rank <= 5:
            base_score += 3

    # Bonus logic with set operations
    valid_indices = {i for i, r in enumerate(ranks) if r <= 7}
    premium_flags = {2, 5, 8}
    overlap = valid_indices & premium_flags
    flag_bonuses = len(overlap) * 5

    # Irrelevant tracking variable
    debug_trace = [0] * len(ranks)
    for idx in range(len(ranks)):
        debug_trace[idx] = ranks[idx] * 0.1

    # Spurious computation that does nothing
    temp_aggregate = 0
    for x in debug_trace:
        if x > 0.5:
            temp_aggregate += x ** 2

    # Final adjustments
    if len(ranks) > 8:
        penalty -= 2  # bonus for large dataset

    final = base_score + flag_bonuses + penalty

    # Additional distraction: unused transformation
    normalized = [round(f / sum(ranks), 3) for f in ranks if f > 0]

    return int(final)

# Main execution
if __name__ == '__main__':
    # Input data
    access_logs = [
        {'type': 'click', 'duration': 65},
        {'type': 'hover', 'duration': 45},
        {'type': 'scroll', 'duration': 70},
        {'type': 'input', 'duration': 30},
        {'type': 'click', 'duration': 80},
        {'type': 'hover', 'duration': 55},
        {'type': 'scroll', 'duration': 40},
        {'type': 'click', 'duration': 90}
    ]

    # Extract analytics
    counts, trend_ratio, total_events = analyze_engagement(access_logs)

    # Secondary processing
    influence = calculate_contribution(counts, base_weight=1.2)

    # Critical ranking data
    rank_data = [3, 7, 1, 12, 5, 4, 9, 6, 2, 11]
    bonus_flags = [True, False, True, False, True, True, False, True, False, True]

    # Key statement
    final_score = calculate_final_score(rank_data, bonus_flags)

    print(f"Result: {final_score}")