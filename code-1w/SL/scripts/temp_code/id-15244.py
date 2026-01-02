def analyze_trends(data, thresholds):
    trend_stats = {}
    temp_accumulator = 0
    spike_count = 0

    for key, values in data.items():
        if len(values) == 0:
            trend_stats[key] = 0
            continue
        avg_val = sum(values) / len(values)
        max_val = max(values)
        min_val = min(values)
        
        # Irrelevant transformation
        normalized = [(v - min_val) / (max_val - min_val + 1e-5) for v in values]
        temp_accumulator += sum(normalized)

        if max_val > thresholds.get(key, 100):
            spike_count += 1

        trend_stats[key] = avg_val * (spike_count + 1)

    # Dead code path - never used later
    if temp_accumulator < 0:
        trend_stats['error'] = -1

    return trend_stats


def calculate_risk_factor(trend_stats, base_risk=1.0):
    risk = base_risk
    adjustment = 0.0

    for val in trend_stats.values():
        if val > 50:
            adjustment += 0.1
        elif val < 10:
            adjustment -= 0.05

    # Complex but irrelevant bitwise manipulation
    masked_risk = int(risk * 100) ^ 255 & 1023
    adjusted_risk = (masked_risk / 100.0) + adjustment

    return adjusted_risk


def evaluate_performance(feedback, metrics):
    consistency = 0
    total_feedback = 0
    weight_map = {'high': 3, 'medium': 2, 'low': 1}

    for category, entries in feedback.items():
        for entry in entries:
            sentiment = entry['sentiment']
            level = entry['priority']
            total_feedback += 1
            
            if sentiment == 'positive':
                consistency += weight_map[level]
            elif sentiment == 'negative':
                consistency -= weight_map[level] // 2

    # Semi-relevant computation that doesn't affect final result
    raw_consistency = consistency / max(total_feedback, 1)
    decayed = raw_consistency * (0.95 ** len(feedback))

    base_value = metrics.get('base', 10)
    multiplier = metrics.get('multiplier', 2)
    offset = metrics.get('offset', 5)

    # Final score calculation - this is the key line
    final_score = (base_value + raw_consistency) * multiplier + offset

    # Red herring: unused complex dictionary operation
    summary_snapshot = {k: len(v) for k, v in feedback.items()}
    summary_snapshot['total_processed'] = total_feedback
    summary_snapshot['flagged'] = [k for k, v in summary_snapshot.items() if v > 10]

    return final_score

# Main execution block
if __name__ == '__main__':
    user_data = {
        'usability': [8, 12, 15, 7],
        'performance': [20, 22, 18],
        'security': [5, 6, 4, 5, 7]
    }

    threshold_config = {
        'usability': 10,
        'performance': 15,
        'security': 8
    }

    # Irrelevant preprocessing
    processed_data = {k: [v*1.1 for v in vals] for k, vals in user_data.items()}

    stats = analyze_trends(user_data, threshold_config)

    risk_level = calculate_risk_factor(stats, base_risk=1.2)

    base_metrics = {
        'base': 25,
        'multiplier': 3,
        'offset': 10,
        'extra': 999  # unused field
    }

    feedback_dict = {
        'interface': [
            {'sentiment': 'positive', 'priority': 'high'},
            {'sentiment': 'positive', 'priority': 'medium'},
            {'sentiment': 'negative', 'priority': 'low'}
        ],
        'workflow': [
            {'sentiment': 'positive', 'priority': 'high'},
            {'sentiment': 'negative', 'priority': 'medium'}
        ]
    }

    final_score = evaluate_performance(feedback_dict, base_metrics)
    print(f"Result: {final_score}")