from collections import defaultdict

# Simulate processing of employee performance reports across departments
def process_reports(raw_entries):
    department_counts = defaultdict(int)
    employee_scores = {}
    temp_aggregates = []

    for entry in raw_entries:
        dept = entry['department']
        emp_id = entry['id']
        base_perf = entry['performance']
        bonus_factor = entry.get('bonus', 1.0)

        # Irrelevant aggregation (distractor)
        department_counts[dept] += 1

        # Core score calculation
        adjusted_score = base_perf * bonus_factor
        if adjusted_score > 90:
            adjusted_score -= 5  # minor penalty for outliers

        employee_scores[emp_id] = adjusted_score

        # Dead-end computation (distractor)
        temp_aggregates.append(sum(department_counts.values()) + len(temp_aggregates))

    return employee_scores

# Analyze textual feedback to derive sentiment adjustment
def analyze_feedback(feedback_list):
    sentiment_shift = 0
    word_count = 0
    positive_terms = {'excellent', 'outstanding', 'strong', 'reliable', 'dedicated'}
    negative_terms = {'poor', 'lacking', 'weak', 'inconsistent'}

    char_histogram = {}  # Distractor: tracking character frequency

    for feedback in feedback_list:
        words = feedback.lower().split()
        word_count += len(words)

        for char in feedback:
            char_histogram[char] = char_histogram.get(char, 0) + 1

        for word in words:
            if word in positive_terms:
                sentiment_shift += 1
            elif word in negative_terms:
                sentiment_shift -= 2  # stronger penalty for negative

    # Normalize shift by total words (only used if word_count > 0)
    normalized_shift = sentiment_shift / word_count if word_count > 0 else 0
    
    # This value is unused later (red herring)
    avg_chars_per_word = sum(char_histogram.values()) / word_count if word_count > 0 else 0

    return normalized_shift

# Main evaluation logic
def evaluate_performance(report_data, threshold):
    scores = process_reports(report_data['employee_data'])
    feedback_shift = analyze_feedback(report_data['feedback'])

    total_eligible = 0
    cumulative_value = 0.0
    id_lengths = []  # Tracking ID string lengths - irrelevant

    for emp_id, score in scores.items():
        # Apply threshold filter
        if score >= threshold:
            total_eligible += 1
            cumulative_value += score

        # Useless side computation (distractor)
        id_lengths.append(len(str(emp_id)))

    # Compute average of eligible employees
    avg_score = cumulative_value / total_eligible if total_eligible > 0 else 0

    # Apply feedback-based adjustment
    adjusted_avg = avg_score + (feedback_shift * 3)

    # Secondary adjustment based on arbitrary rule (still relevant)
    if total_eligible > 5:
        adjusted_avg += 2  # team performance bonus

    # Final nonlinear transformation (critical step)
    final_score = int((adjusted_avg ** 1.1) // 1)  # integer truncation after growth

    # Spurious post-processing (dead code)
    outlier_flag = False
    for val in id_lengths:
        if val > 10:
            outlier_flag = True
            break

    return final_score

# Input data
raw_employee_data = [
    {'id': 101, 'department': 'engineering', 'performance': 85, 'bonus': 1.1},
    {'id': 102, 'department': 'engineering', 'performance': 92, 'bonus': 1.0},
    {'id': 103, 'department': 'marketing', 'performance': 78, 'bonus': 1.05},
    {'id': 104, 'department': 'marketing', 'performance': 88, 'bonus': 1.0},
    {'id': 105, 'department': 'sales', 'performance': 95, 'bonus': 0.95},
    {'id': 106, 'department': 'sales', 'performance': 83, 'bonus': 1.1},
    {'id': 107, 'department': 'engineering', 'performance': 90, 'bonus': 1.0},
    {'id': 108, 'department': 'engineering', 'performance': 87, 'bonus': 1.05}
]

feedback_texts = [
    "Excellent work this quarter, very reliable and dedicated",
    "Some inconsistencies noted, needs improvement",
    "Outstanding results in project delivery",
    "Poor engagement lately, lacking initiative",
    "Strong contributor, always dependable"
]

data_bundle = {
    'employee_data': raw_employee_data,
    'feedback': feedback_texts
}

threshold = 85

# Execute main logic
final_score = evaluate_performance(data_bundle, threshold)
print(f"Result: {final_score}")