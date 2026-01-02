def analyze_productivity(hours_worked, breaks_taken):
    efficiency_ratio = hours_worked / (breaks_taken + 1) if breaks_taken > 0 else hours_worked * 1.5
    penalty = 0.95 if breaks_taken > 3 else 1.0
    adjusted_hours = hours_worked * penalty
    return adjusted_hours * efficiency_ratio


def count_characters(text_map):
    total_chars = 0
    for key in text_map:
        total_chars += len(text_map[key])
    temp_debug_value = total_chars * 0.1  # Irrelevant to final result
    return total_chars

def track_progress(completed_tasks, total_tasks):
    if total_tasks == 0:
        return 0
    progress_rate = completed_tasks / total_tasks
    if progress_rate > 0.8:
        bonus_factor = 1.2
    elif progress_rate > 0.5:
        bonus_factor = 1.1
    else:
        bonus_factor = 0.9
    projected_completion = (total_tasks - completed_tasks) * bonus_factor
    return projected_completion  # Not used directly

def evaluate_performance(log, multiplier):
    base_score = 0
    char_count = count_characters(log['task_notes'])
    productivity = analyze_productivity(log['hours'], log['breaks'])
    
    for task in log['tasks']:
        if task['priority'] == 'high':
            base_score += 10
        elif task['priority'] == 'medium':
            base_score += 6
        else:
            base_score += 3
        
        if task['completed']:
            base_score += 2
    
    # Simulated complexity with conditional expression and modular arithmetic
    modifier = 1.5 if productivity >= 30 else (1.2 if productivity >= 20 else 0.8)
    extra_weight = (char_count % 7) * 0.3
    
    intermediate_debug = base_score * extra_weight  # Distractor
    
    # Key logic step
    final_raw = base_score * modifier + extra_weight
    
    # Dead code path — misleading but harmless
    if base_score < 0:
        final_raw = 0
    
    # Final computation
    return int(final_raw * multiplier)

# Simulation data
base_multiplier = 2

project_log = {
    'hours': 25,
    'breaks': 4,
    'tasks': [
        {'priority': 'high', 'completed': True},
        {'priority': 'medium', 'completed': True},
        {'priority': 'low', 'completed': False},
        {'priority': 'high', 'completed': False},
        {'priority': 'medium', 'completed': True}
    ],
    'task_notes': {
        'planning': 'Initial architecture and module breakdown',
        'coding': 'Implemented core algorithms and tests',
        'review': 'Code review notes and feedback summary'
    }
}

# Tracking unused metrics
predicted_remaining = track_progress(3, 5)
dummy_aggregate = predicted_remaining * 1.1  # Red herring variable

# Critical execution point
final_score = evaluate_performance(project_log, base_multiplier)

print(f"Result: {final_score}")