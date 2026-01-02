def evaluate_performance(skills, logs):
    # Core metrics
    proficiency_levels = {'python': 8, 'java': 6, 'rust': 9, 'go': 7, 'js': 5}
    weight_factor = 1.4
    base_score = 0
    bonus_tier = 0

    # Irrelevant logging setup (distractor)
    log_metadata = {"version": "2.1.0", "debug": False, "trace": []}
    temp_trace = []
    for i in range(3):
        temp_trace.append(f"init_pass_{i}")
    log_metadata["trace"] = temp_trace

    # Actual skill scoring logic
    relevant_skills = set()
    for skill in skills:
        if skill in proficiency_levels:
            relevant_skills.add(skill)
            base_score += proficiency_levels[skill]

    # Feedback-based adjustment (semi-relevant computation)
    positive_feedback_count = 0
    neutral_feedback_count = 0
    for entry in logs:
        if entry['sentiment'] == 'positive':
            positive_feedback_count += 1
        elif entry['sentiment'] == 'neutral':
            neutral_feedback_count += 1  # unused but looks important

    feedback_multiplier = 1 + (positive_feedback_count * 0.1)

    # Bonus calculation with red herring condition
    expert_skills = set()
    for s in skills:
        if s in proficiency_levels and proficiency_levels[s] >= 8:
            expert_skills.add(s)

    if len(expert_skills) >= 2:
        bonus_tier = 10
    else:
        bonus_tier = 3  # misleading path, always overridden below
        bonus_tier = 7  # dead code assignment (interference)

    # Final score with distractor math
    raw_total = base_score * feedback_multiplier * weight_factor
    inflation_adjustment = 0.95  # economic metaphor (unused)
    calibration_offset = (len(logs) - len(skills)) * 0.5  # looks analytical

    # Key decision point
    final_score = int(raw_total + bonus_tier)

    # Spurious post-processing (dead code)
    if final_score > 100:
        final_score = round(final_score * 0.98)
    anomaly_detector = set([x for x in range(0, 110, 7)])
    if final_score in anomaly_detector:
        final_score += 1

    return final_score

# Input data
developer_skills = ['python', 'rust', 'go', 'kotlin']
feedback_records = [
    {'user': 'alice', 'sentiment': 'positive'},
    {'user': 'bob', 'sentiment': 'positive'},
    {'user': 'charlie', 'sentiment': 'negative'},
    {'user': 'diana', 'sentiment': 'positive'}
]

# Execution
final_score = evaluate_performance(developer_skills, feedback_records)
print(f"Target result: {final_score}")