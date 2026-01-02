from collections import defaultdict

# Simulate user engagement analytics across platform features
def analyze_engagement_metrics(raw_logs):
    feature_hits = defaultdict(int)
    total_events = 0
    temporal_weights = [1.0, 0.9, 0.7, 0.4, 0.2]

    for log in raw_logs:
        parts = log.split('|')
        feature = parts[1]
        timestamp = int(parts[0])
        event_type = parts[2]

        if event_type == 'click':
            weight = temporal_weights[min(timestamp // 10000, 4)]
            feature_hits[feature] += int(weight * 100)
            total_events += 1

    return feature_hits, total_events

# Rank features by weighted engagement
def generate_feature_ranking(hit_data):
    sorted_features = sorted(hit_data.items(), key=lambda x: (-x[1], x[0]))
    ranking = {}
    decay_factor = 1.0

    for idx, (feature, score) in enumerate(sorted_features):
        rank = idx + 1
        adjusted_score = score * decay_factor
        ranking[feature] = (rank, adjusted_score)
        decay_factor *= 0.95  # Diminishing influence for lower ranks

    return ranking

# Calculate composite performance score with bonus logic
def calculate_final_score(rank_map, multiplier):
    base_value = 0
    penalty_offset = 0
    temp_result = 0

    for feat, (r, adj_score) in rank_map.items():
        if r <= 5:
            base_value += adj_score / r
        else:
            penalty_offset += 0.5 * (r - 5)

        # Irrelevant intermediate calculation (distractor)
        temp_result += len(feat) * 0.1

    # Red herring computation (not used in final result)
    outlier_check = temp_result > 100
    adjustment_factor = 1.1 if outlier_check else 1.0

    raw_score = base_value - penalty_offset
    final_score = int(raw_score * multiplier * adjustment_factor)  # adjustment_factor always 1.0

    return final_score

# Simulated log data (timestamp|feature|event_type)
logs = [
    "10000|search|click",
    "20000|profile|view",
    "25000|feed|click",
    "30000|search|click",
    "35000|feed|click",
    "40000|notifications|click",
    "45000|feed|impression",
    "50000|search|click",
    "55000|settings|click",
    "60000|feed|click",
    "65000|search|click",
    "70000|feed|click",
    "75000|profile|click",
    "80000|feed|click",
    "90000|search|click"
]

# Extract engagement data
hit_analysis, event_count = analyze_engagement_metrics(logs)

# Generate ranking map
rankings = generate_feature_ranking(hit_analysis)

# Bonus multiplier based on system-wide performance
bonus_multiplier = 1.25

# Compute final score
final_score = calculate_final_score(rankings, bonus_multiplier)

print(f"Target result: {final_score}")