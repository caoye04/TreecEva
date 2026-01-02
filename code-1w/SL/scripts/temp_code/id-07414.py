def analyze_productivity(log_entries, base_multiplier):
    total_tasks = 0
    failed_tasks = 0
    retry_count = 0
    temporal_weights = []

    for entry in log_entries:
        if 'status' not in entry or 'duration' not in entry:
            continue

        total_tasks += 1
        if entry['status'] == 'failed':
            failed_tasks += 1
            if 'retries' in entry:
                retry_count += len(entry['retries'])

        weight = 1.0
        duration = entry['duration']
        if duration > 500:
            weight *= 0.8
        elif duration < 100:
            weight *= 1.1
        temporal_weights.append(weight)

    failure_rate = failed_tasks / total_tasks if total_tasks else 0
    avg_retry = retry_count / failed_tasks if failed_tasks else 0

    # Distractor: unused metrics
    hypothetical_savings = base_multiplier * (1 - failure_rate) * 100
    projected_growth = avg_retry * 0.5 if hypothetical_savings > 50 else 0

    return total_tasks, failure_rate, temporal_weights


def calculate_adaptive_bonus(tasks_completed, weights):
    if not weights:
        return 0

    base_bonus = tasks_completed * 0.5
    fluctuation_penalty = 0
    prev = weights[0]
    for curr in weights[1:]:
        if abs(curr - prev) > 0.2:
            fluctuation_penalty += 0.05
        prev = curr

    # Irrelevant string processing as distraction
    label = f"TaskFluctuationPenalty_{fluctuation_penalty:.2f}"
    tokens = label.split('_')
    code_hash = sum(ord(c) for c in tokens[-1] if c.isdigit()) % 100

    adjusted_bonus = base_bonus - fluctuation_penalty + (code_hash * 0.01)
    return round(adjusted_bonus, 3)


def evaluate_performance(task_log, efficiency_weight):
    # Extract metadata (unused but looks important)
    system_tag = task_log.get('system_id', '')
    version = task_log.get('version', '')[1:] if task_log.get('version') else ''
    
    entries = task_log['entries']
    multiplier = task_log.get('multiplier', 1.0)
    
    # Core analysis
    tasks, fail_rate, time_weights = analyze_productivity(entries, multiplier)
    
    # Bonus computation with string-based distractor
    raw_bonus = calculate_adaptive_bonus(tasks, time_weights)
    
    # Real logic path
    stability_factor = 1 - fail_rate
    if stability_factor > 0.9:
        efficiency_weight *= 1.2
    elif stability_factor < 0.7:
        efficiency_weight *= 0.8

    performance_index = tasks * stability_factor * efficiency_weight
    final_score = performance_index + raw_bonus

    # Dead code branch - misleading
    if system_tag.startswith("X") and "debug" in version.lower():
        adjustment = len(version) * -0.1
        final_score += adjustment  # Never reached in this input

    return int(round(final_score))

# Input construction
task_log = {
    'system_id': 'PROD-THETA',
    'version': 'v2.1',
    'multiplier': 1.5,
    'entries': [
        {'status': 'success', 'duration': 80},
        {'status': 'failed', 'duration': 600, 'retries': [1, 2]},
        {'status': 'success', 'duration': 120},
        {'status': 'success', 'duration': 90},
        {'status': 'failed', 'duration': 700},
        {'status': 'success', 'duration': 400},
        {'status': 'success', 'duration': 110}
    ]
}
efficiency_weight = 2.0

# Execution point
final_score = evaluate_performance(task_log, efficiency_weight)
print(f"Result: {final_score}")