from collections import defaultdict

# Simulate user engagement metrics across platform sections
def analyze_engagement(events):
    counts = defaultdict(int)
    durations = []
    total_actions = 0
    temp_sum = 0  # distractor

    for event in events:
        section = event['section']
        duration = event['duration']
        action_type = event['action']

        counts[section] += 1
        durations.append(duration)
        total_actions += 1

        # Distractor computation - not used later
        if duration > 30:
            temp_sum += len(section) * 0.7

    avg_duration = sum(durations) / len(durations) if durations else 0
    return dict(counts), avg_duration, total_actions


def rank_sections(counts, base_weights):
    ranked = {}
    max_count = max(counts.values()) if counts else 1
    min_count = min(counts.values()) if counts else 0

    # Apply scaling with baseline decay
    for section, count in counts.items():
        normalized = (count - min_count) / (max_count - min_count) if max_count != min_count else 1
        weight = base_weights.get(section, 0.5)
        ranked[section] = normalized * weight * 100

        # Dead code path - misleading logic
        if normalized > 1:  # never happens
            ranked[section] *= 0.9

    return ranked


def calculate_final_score(rank_data, bonus_multiplier):
    raw_scores = []
    adjustment_factor = 0.85
    penalty = 0

    for score in rank_data.values():
        if score > 75:
            penalty += 2
        elif score < 25:
            penalty += 1

        # Core scoring logic
        adjusted = score * adjustment_factor
        raw_scores.append(adjusted)

    # Final aggregation
    base_avg = sum(raw_scores) / len(raw_scores) if raw_scores else 0
    applied_bonus = base_avg * bonus_multiplier
    final_score = base_avg + applied_bonus - penalty * 1.5

    # Extra unused transformation
    ceiling_adjusted = min(final_score, 95)  # distractor

    return int(round(final_score))

# Main execution
if __name__ == '__main__':
    user_events = [
        {'section': 'feed', 'duration': 45, 'action': 'scroll'},
        {'section': 'search', 'duration': 12, 'action': 'query'},
        {'section': 'feed', 'duration': 67, 'action': 'like'},
        {'section': 'profile', 'duration': 89, 'action': 'edit'},
        {'section': 'feed', 'duration': 23, 'action': 'share'},
        {'section': 'search', 'duration': 34, 'action': 'query'},
        {'section': 'notifications', 'duration': 10, 'action': 'tap'},
        {'section': 'feed', 'duration': 56, 'action': 'comment'}
    ]

    weights = {
        'feed': 1.2,
        'search': 0.9,
        'profile': 0.7,
        'notifications': 1.1
    }

    # Step 1: Analyze engagement
    count_map, avg_time, actions_total = analyze_engagement(user_events)

    # Step 2: Compute derived stats (some irrelevant)
    total_sections = len(count_map)
    peak_activity = max(count_map.values())
    rare_section_count = sum(1 for c in count_map.values() if c < 2)

    # Step 3: Rank sections by engagement
    ranked_results = rank_sections(count_map, weights)

    # Step 4: Introduce red herring calculation
    dummy_result = sum(len(k) * v for k, v in ranked_results.items() if 'x' in k)  # always 0

    # Step 5: Calculate final performance score
    multiplier = 0.2
    final_score = calculate_final_score(ranked_results, multiplier)

    # Output target result
    print(f"Result: {final_score}")