from collections import defaultdict

# Simulate user engagement metrics across platform segments
def analyze_engagement Trends(raw_clickstream):
    daily_visits = defaultdict(int)
    bounce_rates = {}
    avg_duration = 0

    for entry in raw_clickstream:
        day, clicks, duration, bounced = entry
        daily_visits[day] += clicks
        if bounced:
            bounce_rates[day] = bounce_rates.get(day, 0) + 1
        avg_duration += duration

    total_bounces = sum(bounce_rates.values())
    avg_duration /= len(raw_clickstream) if raw_clickstream else 1

    # Irrelevant transformation (distractor)
    normalized_scores = [round((v / (max(daily_visits.values()) or 1)) * 100) for v in daily_visits.values()]
    spike_days = [k for k, v in daily_visits.items() if v > 2 * (sum(daily_visits.values()) / len(daily_visits))]

    return dict(daily_visits), total_bounces, avg_duration

# Rank content based on adjusted performance
def rank_content_performance(metrics_log):
    base_ranks = {}
    penalty_map = defaultdict(float)

    cumulative_score = 0
    for idx, (content_id, views, shares, flags) in enumerate(metrics_log):
        base_ranks[content_id] = views + (shares * 2.5)
        if flags > 0:
            penalty_map[content_id] = flags * 0.8
        cumulative_score += base_ranks[content_id]

    # Apply decay for older entries (semi-relevant)
    decayed_ranks = {cid: score * (0.95 ** idx) for idx, (cid, score) in enumerate(base_ranks.items())}

    # Distractor: unused structure
    summary_report = {
        'total_entries': len(metrics_log),
        'average_base': cumulative_score / len(metrics_log),
        'peak_views': max(base_ranks.values())
    }

    return decayed_ranks, penalty_map

# Final scoring with adjustment factors
def calculate_final_score(rank_data, bonus_multiplier):
    raw_total = sum(rank_data.values())
    adjustment_factor = 1.0

    if raw_total > 500:
        adjustment_factor = 0.95
    elif raw_total < 100:
        adjustment_factor = 1.1

    # Add bonus based on multiplier (only some affect result)
    effective_bonus = 0
    for i in range(5):
        if i % 2 == 0:
            effective_bonus += bonus_multiplier / (i + 1)

    # Core computation
    preliminary = raw_total * adjustment_factor
    final_score = preliminary + (effective_bonus * 10)

    # Dead code path (distractor)
    debug_trace = []
    for k, v in rank_data.items():
        if v > 50:
            debug_trace.append(f"High:{k}")

    return int(final_score)

# Input data
user_sessions = [
    ('Mon', 120, 180, False),
    ('Tue', 150, 210, True),
    ('Wed', 130, 195, False),
    ('Thu', 170, 220, False),
    ('Fri', 160, 205, True)
]

content_metrics = [
    ('C01', 80, 12, 1),
    ('C02', 95, 18, 0),
    ('C03', 120, 25, 2),
    ('C04', 75, 10, 0),
    ('C05', 110, 22, 1)
]

# Execute analysis pipeline
visit_stats, total_rejections, duration_avg = analyze_engagement_Trends(user_sessions)
ranked_scores, penalties = rank_content_performance(content_metrics)
bonus_weight = len([v for v in visit_stats.values() if v > 140])

final_score = calculate_final_score(ranked_scores, bonus_weight)
print(f"Result: {final_score}")