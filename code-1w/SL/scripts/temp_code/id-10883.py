from itertools import groupby

def analyze_training_cycle():
    # Simulated employee training performance data
    raw_scores = [78, 85, 92, 67, 88, 73, 94, 81, 77, 85, 90, 82]
    attendance_rate = [0.95, 0.87, 0.99, 0.76, 0.93, 0.81, 0.97, 0.89, 0.84, 0.91, 0.96, 0.83]
    peer_reviews = [3.4, 4.1, 4.8, 2.9, 4.5, 3.7, 4.9, 4.0, 3.8, 4.3, 4.6, 3.9]

    # Irrelevant transformation: normalize reviews to arbitrary scale (not used in final logic)
    adjusted_reviews = [round((pr - 2) * 10 / 3, 2) for pr in peer_reviews]

    # Determine performance bands based on raw scores
    performance_band = []
    for score in raw_scores:
        if score >= 90:
            performance_band.append('excellent')
        elif score >= 80:
            performance_band.append('good')
        elif score >= 70:
            performance_band.append('fair')
        else:
            performance_band.append('poor')
    
    # Misleading intermediate calculation: average attendance by band (computed but not used)
    zipped_data = list(zip(performance_band, attendance_rate))
    sorted_data = sorted(zipped_data, key=lambda x: x[0])
    for key, group in groupby(sorted_data, key=lambda x: x[0]):
        avg_attendance = sum(item[1] for item in group) / len(list(group))
        # This result is never stored or used further

    # Generate feedback levels using conditional expressions based on multiple criteria
    feedback_levels = []
    for i in range(len(raw_scores)):
        level = 'high' if raw_scores[i] >= 85 and attendance_rate[i] > 0.85 else \
                  'medium' if raw_scores[i] >= 75 and attendance_rate[i] > 0.75 else 'low'
        feedback_levels.append(level)
    
    # Dead code path: hypothetical escalation (never executed due to condition)
    escalation_risk = 0
    if False:  # Simulate unused contingency logic
        for j, lvl in enumerate(feedback_levels):
            if lvl == 'low' and peer_reviews[j] < 3.5:
                escalation_risk += 1

    # Core logic: aggregate performance from feedback levels
    counts = {'high': 0, 'medium': 0, 'low': 0}
    for fl in feedback_levels:
        counts[fl] += 1
    
    # Final scoring formula: weighted combination
    base_score = counts['high'] * 10 + counts['medium'] * 5 - counts['low'] * 2
    penalty_factor = len([s for s in raw_scores if s < 70])  # extra low performers
    final_score = base_score - penalty_factor * 3
    
    # Output target result
    print(f"Target result: {final_score}")

    # Return unused metrics to increase cognitive load
    return final_score, adjusted_reviews, escalation_risk

# Execute function
result = analyze_training_cycle()