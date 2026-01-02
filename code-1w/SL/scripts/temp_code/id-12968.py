def analyze_productivity(hours_worked, breaks_taken):
    efficiency = 0
    stress_factor = 0
    for hour in hours_worked:
        if hour > 8:
            efficiency += 4
            stress_factor += 1.5
        elif hour >= 6:
            efficiency += 6
        else:
            efficiency += 3
    
    # Distractor: Unused computation
    phantom_load = sum([h**2 for h in hours_worked if h < 5])
    normalization_shift = len(breaks_taken) * 0.2

    return efficiency

# Simulated team data
team_hours = [7, 9, 6, 8]
team_breaks = [2, 1, 3, 2]

base_efficiency = analyze_productivity(team_hours, team_breaks)

# Feedback levels from peer reviews
peer_feedback = ["excellent", "good", "good", "average", "poor"]
feedback_weights = {"excellent": 1.5, "good": 1.2, "average": 1.0, "poor": 0.5}

# Irrelevant transformation (distractor)
decay_rate = 0.95
adjusted_feedback = list(map(lambda fb: feedback_weights[fb] * decay_rate, peer_feedback))

# Key processing step with distractors
temp_offset = 0
for w in feedback_weights.values():
    temp_offset += w / len(feedback_weights)

# Actual aggregation logic
feedback_levels = [feedback_weights[fb] for fb in peer_feedback]
smoothing_factor = 1.1

# Dead code path (never executed)
if False:
    smoothing_factor *= 1.5
    base_efficiency -= 10

aggregate_performance = lambda levels: int(smoothing_factor * sum(levels) * (base_efficiency / 10))

# Critical execution point
final_score = aggregate_performance(feedback_levels)

# Print result as required
print(f"Result: {final_score}")