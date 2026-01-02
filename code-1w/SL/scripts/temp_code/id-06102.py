def evaluate_performance(records, weights):
    base_score = 0
    bonus_points = 0
    penalty = 0
    temp_result = {}
    intermediate_values = []

    # Extract and normalize key metrics
    attendance_rate = records.get('attendance', 0) / 30.0
    project_count = records.get('projects', 0)
    error_count = records.get('errors', 0)
    peer_feedback = len(records.get('feedback', ''))

    # Irrelevant string processing (distractor)
    feedback_chars = [c for c in records.get('feedback', '') if c.isalpha()]
    char_frequency = {}
    for char in feedback_chars:
        char_frequency[char] = char_frequency.get(char, 0) + 1
    unique_letters = len(char_frequency)

    # Real scoring logic begins
    if attendance_rate >= 0.9:
        base_score += weights['attendance'] * 10
    elif attendance_rate >= 0.75:
        base_score += weights['attendance'] * 7
    else:
        penalty += 5

    if project_count > 5:
        bonus_points += 10
        extra_projects = project_count - 5
        for i in range(extra_projects):
            bonus_points += min(i, 4)  # Diminishing returns
    else:
        base_score += project_count * weights['project']

    # Deduct based on errors
    penalty += error_count * 3

    # Use of dictionary to map performance bands (relevant)
    performance_band = {
        'A': 90, 'B': 80, 'C': 70, 'D': 60, 'F': 50
    }
    band_key = 'B'
    if base_score + bonus_points - penalty >= 85:
        band_key = 'A'
    elif base_score + bonus_points - penalty >= 75:
        band_key = 'B'
    else:
        band_key = 'C'

    # Secondary adjustment using band multiplier
    band_multiplier = performance_band[band_key] / 100.0
    adjusted_score = (base_score + bonus_points - penalty) * band_multiplier

    # Final nonlinear adjustment based on peer feedback length
    feedback_factor = 1 + (peer_feedback * 0.05)
    final_raw = adjusted_score * feedback_factor

    # Dead code path (distractor)
    if False:
        debug_log = {}
        for k, v in records.items():
            debug_log[k] = str(v) + '_processed'

    # Final score clamped and rounded
    final_score = int(round(final_raw))
    return final_score

# Main execution
kpi_weights = {
    'attendance': 8,
    'project': 6,
    'initiative': 5
}
employee_data = {
    'attendance': 28,
    'projects': 7,
    'errors': 2,
    'feedback': 'excellent teamwork and consistent delivery'
}

result_tracker = []
for i in range(1):  # Single iteration loop (moderate nesting)
    temp_cache = {}
    computed = None
    computed = evaluate_performance(employee_data, kpi_weights)
    result_tracker.append(computed)

final_score = result_tracker[-1]
print(f"Result: {final_score}")