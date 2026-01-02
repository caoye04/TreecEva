def evaluate_performance(log, kpi_threshold):
    # Extract recent feedback entries
    recent_entries = log[-5:]
    
    # Irrelevant computation: analyze sentiment (not used in final score)
    sentiment_scores = []
    for entry in log:
        positive_words = len([w for w in entry.split() if w.lower() in ['great', 'good', 'excellent']])
        negative_words = len([w for w in entry.split() if w.lower() in ['bad', 'poor', 'terrible']])
        sentiment_scores.append(positive_words - negative_words)
    
    # Compute performance metrics
    total_entries = len(recent_entries)
    compliance_count = 0
    feedback_length_total = 0
    
    for entry in recent_entries:
        feedback_length_total += len(entry)
        words = entry.lower().split()
        if 'compliant' in words or 'met' in words:
            compliance_count += 1

    avg_length = feedback_length_total / total_entries if total_entries > 0 else 0
    
    # Distractor: unused trend analysis
    trend_direction = []
    for i in range(1, len(sentiment_scores)):
        if sentiment_scores[i] > sentiment_scores[i-1]:
            trend_direction.append(1)
        elif sentiment_scores[i] < sentiment_scores[i-1]:
            trend_direction.append(-1)

    # Core logic: performance score based on compliance rate and average message length
    compliance_rate = compliance_count / total_entries
    length_bonus = 1.0 if avg_length > 50 else 0.5
    
    base_score = compliance_rate * 100
    adjusted_score = base_score * length_bonus
    
    # Apply KPI threshold multiplier
    kpi_multiplier = 1.2 if compliance_rate >= kpi_threshold else 0.8
    final_score = adjusted_score * kpi_multiplier
    
    # Red herring: modify string content without impact
    summary = ''.join([entry[0] for entry in recent_entries]).upper()
    checksum = sum(ord(c) for c in summary) % 100
    
    return int(final_score)

# Simulated feedback log from team meetings
feedback_log = [
    "Great progress this week, all tasks met expectations",
    "Good effort but some delays in deployment",
    "Excellent teamwork, fully compliant with protocols",
    "Met most goals, minor issues with documentation",
    "Compliant with security policies, well done",
    "Poor communication during sprint",
    "Terrible outage due to misconfiguration"
]

target_kpi = 0.6

# Key execution point
final_score = evaluate_performance(feedback_log, target_kpi)
print(f"Result: {final_score}")