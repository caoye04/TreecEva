def analyze_student_response(response_time, accuracy, complexity_level):
    base_score = 0
    time_bonus = 0
    penalty = 0

    if response_time < 2.0:
        time_bonus = 1.5
    elif response_time < 5.0:
        time_bonus = 0.5
    else:
        penalty += 0.8

    if accuracy >= 90:
        base_score = 10
    elif accuracy >= 70:
        base_score = 7
    else:
        base_score = 4

    adjusted_score = (base_score + time_bonus - penalty) * complexity_level
    
    # Distractor: irrelevant computation for alternate metric
    hypothetical_efficiency = (accuracy / (response_time + 0.1)) * complexity_level
    efficiency_flag = hypothetical_efficiency > 15

    return adjusted_score


def compute_baseline_average(scores_list):
    total = sum(scores_list)
    count = len(scores_list)
    average = total / count if count > 0 else 0
    
    # Dead code path - never used later
    if average > 8:
        status = "stable"
    else:
        status = "variable"
    
    return average  # Not actually used in main logic


def aggregate_performance(feedback_data, difficulty_bias):
    raw_values = []
    temp_log = []
    cumulative_offset = 0
    
    for student_id, data in feedback_data.items():
        rt = data['response_time']
        acc = data['accuracy']
        level = data['complexity']
        
        # Valid computation step
        individual_score = analyze_student_response(rt, acc, level)
        raw_values.append(individual_score)
        
        # Distractor: tracking unused diagnostics
        temp_log.append(f'Student {student_id}: {individual_score:.2f}')
        cumulative_offset += len(student_id) % 3  # Irrelevant accumulation
    
    # Core logic: apply bias correction and cap extremes
    biased_scores = [score * difficulty_bias for score in raw_values]
    filtered_scores = [s for s in biased_scores if s >= 5.0]  # Filter out low performers
    
    # Final aggregation
    total_performance = sum(filtered_scores)
    final_score = round(total_performance / len(filtered_scores), 3) if filtered_scores else 0
    
    # Additional red herring variables
    outlier_count = len([x for x in biased_scores if x > 12])
    compression_factor = total_performance / (sum(raw_values) + 0.01)
    
    return final_score

# Main execution block
feedback_data = {
    'S001': {'response_time': 1.8, 'accuracy': 94, 'complexity': 1.2},
    'S002': {'response_time': 3.5, 'accuracy': 87, 'complexity': 1.1},
    'S003': {'response_time': 6.2, 'accuracy': 72, 'complexity': 0.9},
    'S004': {'response_time': 2.1, 'accuracy': 91, 'complexity': 1.3},
    'S005': {'response_time': 4.8, 'accuracy': 68, 'complexity': 1.0}
}

difficulty_bias = 1.05
baseline_scores = [7.2, 6.8, 8.1, 7.5, 6.9]

# Unused helper call - distractor
avg_base = compute_baseline_average(baseline_scores)

# Key statement
final_score = aggregate_performance(feedback_data, difficulty_bias)

print(f"Result: {final_score}")