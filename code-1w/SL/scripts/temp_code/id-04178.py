def analyze_feedback(feedback_list):
    sentiment_score = 0
    for entry in feedback_list:
        if 'excellent' in entry:
            sentiment_score += 3
        elif 'good' in entry:
            sentiment_score += 1
        elif 'poor' in entry:
            sentiment_score -= 2
    return sentiment_score

# Irrelevant helper function (decoy)
def calculate_tenure(start_year, current_year=2023):
    return current_year - start_year

def transform_metrics(raw_data):
    processed = []
    for val in raw_data:
        if val < 0:
            processed.append(abs(val) * 2)
        else:
            processed.append(val ** 0.5 if val > 0 else 0)
    return processed

# Misleading normalization function
def normalize_scores(scores):
    total = sum(scores)
    if total == 0:
        return [0 for _ in scores]
    return [round(s / total, 3) for s in scores]

def evaluate_performance(log):
    base_points = 0
    bonus_tracker = []
    penalty_count = 0

    # Real logic starts here — nested and interwoven with distractions
    for record in log:
        task_type = record['type']
        completion_status = record['status']
        quality_flag = record.get('quality', 'medium')

        if task_type == 'development':
            if completion_status == 'complete':
                base_points += 10
                if quality_flag == 'high':
                    bonus_tracker.append(3)
            else:
                penalty_count += 1

        elif task_type == 'review':
            if completion_status == 'pending':
                base_points -= 2
            elif completion_status == 'complete':
                base_points += 5
                if quality_flag == 'low':
                    penalty_count += 1

        # Distraction: irrelevant string processing
        note = record.get('notes', '')
        if isinstance(note, str) and note.strip().lower().startswith('urgent'):
            base_points += len(note.split())  # misleading bump

    # Actual scoring logic buried here
    adjustment_factor = 1 + (len(bonus_tracker) * 0.1) - (penalty_count * 0.05)
    adjusted_points = base_points * adjustment_factor

    # More distraction: unused transformation
    dummy_data = [16, -4, 9, 0, 25]
    transformed = transform_metrics(dummy_data)  # never used

    # Final calculation — depends only on adjusted_points and feedback analysis
    feedback_entries = [
        'Code quality was excellent overall',
        'Good effort on testing',
        'Documentation was poor this sprint'
    ]
    sentiment_impact = analyze_feedback(feedback_entries)

    final_raw = adjusted_points + sentiment_impact

    # Key assignment: this is what the question targets
    final_score = int(round(final_raw))

    # Dead code path (never executed)
    if False:
        fallback = normalize_scores([base_points, len(bonus_tracker)])
        final_score = sum(fallback)

    return final_score

# Simulated input data
assessment_log = [
    {'type': 'development', 'status': 'complete', 'quality': 'high', 'notes': 'Urgent fix deployed'},
    {'type': 'development', 'status': 'incomplete', 'quality': 'medium'},
    {'type': 'review', 'status': 'complete', 'quality': 'low'},
    {'type': 'review', 'status': 'complete', 'quality': 'high', 'notes': 'No urgency'},
    {'type': 'development', 'status': 'complete', 'quality': 'medium'}
]

# Execution point of interest
final_score = evaluate_performance(assessment_log)
print(f"Result: {final_score}")