def analyze_response(time_spent, threshold=2.5):
    return lambda x: x > threshold if time_spent else lambda x: x >= threshold

# Simulate user interaction with system responses
time_logs = [1.2, 3.4, 2.1, 4.8, 2.7]
accuracy_data = [0.88, 0.94, 0.76, 0.91, 0.85]
feedback_list = []

for i in range(len(time_logs)):
    is_critical = analyze_response(time_logs[i] > 3.0)(accuracy_data[i])
    normalized_time = (time_logs[i] * 1.5) % 5
    temp_weight = normalized_time * 0.1
    
    # Irrelevant intermediate calculation (distractor)
    debug_value = (i + 1) * temp_weight if i % 2 == 0 else 0
    
    score_component = accuracy_data[i] * 100 + (5 - normalized_time) * 10
    
    # Dead code path (misleading but syntactically present)
    if False:
        score_component -= debug_value * 2
        redundant_check = True

    feedback_entry = {
        'id': i,
        'score': score_component,
        'flagged': is_critical,
        'weight': temp_weight
    }
    feedback_list.append(feedback_entry)

# Aggregation function using lambda and conditional logic
aggregate_performance = lambda data: sum(
    item['score'] for item in data if item['flagged']
) + len([item for item in data if not item['flagged']])

# Key statement
final_score = aggregate_performance(feedback_list)

# Print result for evaluation
print(f"Result: {final_score}")