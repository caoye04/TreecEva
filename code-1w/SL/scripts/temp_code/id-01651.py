from collections import defaultdict

# Simulate developer contribution analysis with noise and red herrings
def analyze_developer_activity():
    # Core data
    contributions = [12, 8, 15, 6, 22, 14, 9]
    review_scores = [4.2, 3.8, 4.5, 4.0, 4.7, 4.3, 3.9]
    commit_frequency = [3, 5, 4, 2, 6, 4, 3]

    # Irrelevant metrics (distractors)
    ui_clicks = [102, 88, 134, 77, 201, 95, 83]  # Not used in final logic
    session_duration = [12.5, 8.3, 15.1, 6.7, 20.2, 11.8, 9.4]  # Dead code path
    temp_cache = set()
    for x in session_duration:
        temp_cache.add(round(x % 5))

    # Penalty system based on infrequent commits
    penalty_map = defaultdict(int)
    for i, freq in enumerate(commit_frequency):
        if freq < 3:
            penalty_map[i] += 3
        elif freq < 4:
            penalty_map[i] += 1

    # Noise: unused transformation
    normalized_contrib = [c / max(contributions) for c in contributions]
    weighted_review = [(i, score * 0.8) for i, score in enumerate(review_scores)]

    # Auxiliary tracking (semi-relevant)
    streak_counter = 0
    max_streak = 0
    for val in contributions:
        if val > 10:
            streak_counter += 1
            max_streak = max(max_streak, streak_counter)
        else:
            streak_counter = 0

    # Red herring function call
    def compute_entropy(data):
        from math import log
        total = sum(data)
        if total == 0:
            return 0.0
        entropy = 0.0
        for x in data:
            p = x / total
            if p > 0:
                entropy -= p * log(p)
        return round(entropy, 4)
    _ = compute_entropy(ui_clicks)  # Computation has no effect

    # Core calculation obscured by context
    base_score = sum(contributions)
    adjustment = 0
    for idx, contrib in enumerate(contributions):
        if idx in penalty_map:
            adjustment -= penalty_map[idx] * 2

    performance_bonus = 5 if max_streak >= 3 else 0

    # Final rating computation
    def calculate_rating(contribs, penalties):
        raw = sum(contribs)
        deduction = 0
        for k, v in penalties.items():
            deduction += v * 2
        bonus = 5 if raw > 50 else 0
        return raw - deduction + bonus

    final_score = calculate_rating(contributions, penalty_map)
    print(f"Result: {final_score}")

analyze_developer_activity()