def analyze_productivity(hours_worked, break_hours):
    total_hours = sum(hours_worked)
    effective_hours = total_hours - break_hours
    distraction_factor = len([h for h in hours_worked if h < 1.5])
    efficiency = (effective_hours / total_hours) * 100 if total_hours > 0 else 0
    return efficiency, distraction_factor

hours = [2.5, 1.0, 3.0, 0.8, 2.2]
break_time = 1.2

# Secondary metric: error rate analysis
def calculate_error_density(errors, lines_of_code):
    if lines_of_code == 0:
        return 0
    return (errors / lines_of_code) * 100

err_count = 6
loc = 150
er_density = calculate_error_density(err_count, loc)

# Simulate team feedback score from peer reviews (string processing)
raw_feedback = "++--+++----++"
positive_revs = raw_feedback.count('+')
negative_revs = raw_feedback.count('-')
net_sentiment = positive_revs - negative_revs
feedback_score = max(0, net_sentiment)

# Core evaluation logic
productivity, dist_f = analyze_productivity(hours, break_time)
adjusted_productivity = productivity - (dist_f * 2.5)

error_penalty = er_density * 1.8

# Misleading intermediate calculations (distractors)
theoretical_max_efficiency = 100 - (len(hours) * 0.3)
stress_index = (sum(hours) + break_time) / (len(hours) + 1)
phantom_metric = stress_index * 0.7 + dist_f  # unused downstream

# Final performance scoring
def evaluate_performance(efficiency, error_rate, peer_feedback):
    base_score = efficiency * 0.6
    deduction = error_rate * 1.5
    bonus = min(peer_feedback * 2, 20)
    result = base_score - deduction + bonus
    return round(result, 2)

final_score = evaluate_performance(adjusted_productivity, error_penalty, feedback_score)

# Print final result
print(f"Result: {final_score}")