from collections import defaultdict
import math

# Simulate user interaction logs with feature usage counts
def analyze_user_engagement(logs):
    feature_count = defaultdict(int)
    temporal_weights = [0.85 ** i for i in range(len(logs))][::-1]
    decayed_interactions = 0

    for idx, entry in enumerate(logs):
        feature = entry['feature']
        feature_count[feature] += 1
        decayed_interactions += entry['duration'] * temporal_weights[idx]  # Weighted by recency

    # Distractor computation: total sessions (not directly used)
    total_sessions = sum(1 for log in logs if log['action'] == 'start')

    return dict(feature_count), decayed_interactions

# Assess feedback patterns and derive correction metrics
def process_feedback(reports):
    sentiment_analysis = {'positive': 0, 'negative': 0, 'neutral': 0}
    priority_flags = []

    for report in reports:
        sentiment = report['sentiment']
        urgency = report['urgency']
        sentiment_analysis[sentiment] += 1
        if urgency > 0.7:
            priority_flags.append(True)

    # Misleading intermediate: unused in final logic
    avg_urgency = sum(report['urgency'] for report in reports) / len(reports) if reports else 0

    return sentiment_analysis, len(priority_flags)

# Core evaluation logic combining engagement and feedback
def evaluate_performance(counter, factor):
    base_metric = sum(counter.values())
    adjustment = factor * 0.95
    if base_metric > 10:
        adjustment += 1.5
    elif base_metric < 5:
        adjustment -= 2.0
    return int(base_metric * adjustment + 3)

# Auxiliary function to compute derived analytics (mostly irrelevant)
def compute_derived_metrics(data):
    stats = {}
    values = [len(str(v)) for v in data.values()]
    stats['max_digits'] = max(values) if values else 0
    stats['digit_variance'] = sum((x - sum(values)/len(values))**2 for x in values) / len(values) if values else 0
    return stats

# Main execution flow
if __name__ == "__main__":
    # Input data: user interaction logs
    activity_log = [
        {'feature': 'search', 'action': 'start', 'duration': 120},
        {'feature': 'filter', 'action': 'interact', 'duration': 45},
        {'feature': 'search', 'action': 'refine', 'duration': 60},
        {'feature': 'export', 'action': 'start', 'duration': 30},
        {'feature': 'filter', 'action': 'update', 'duration': 25},
        {'feature': 'dashboard', 'action': 'view', 'duration': 200}
    ]

    feedback_reports = [
        {'sentiment': 'positive', 'urgency': 0.3},
        {'sentiment': 'neutral', 'urgency': 0.5},
        {'sentiment': 'negative', 'urgency': 0.8},
        {'sentiment': 'negative', 'urgency': 0.9}
    ]

    # Step 1: Analyze engagement (returns relevant and irrelevant data)
    feature_usage, time_score = analyze_user_engagement(activity_log)
    
    # Step 2: Process feedback for flags (semi-relevant)
    sentiments, high_priority_count = process_feedback(feedback_reports)
    
    # Step 3: Compute meaningless derived metrics (distractor)
    fake_stats = compute_derived_metrics(feature_usage)
    
    # Step 4: Determine adjustment factor using partial sentiment data
    negative_feedback = sentiments['negative']
    adjustment_factor = 4.0
    if negative_feedback >= 2:
        adjustment_factor *= 0.7
    else:
        adjustment_factor *= 1.1

    # Step 5: Key execution point - evaluate final performance score
    final_score = evaluate_performance(feature_usage, adjustment_factor)

    # Print result as required
    print(f"Target result: {final_score}")