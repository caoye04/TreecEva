def evaluate_performance(days_present, stats):
    base_score = len(days_present)
    bonus = 0
    
    # Calculate performance multipliers
    if 'excellent' in stats['feedback']:
        bonus += 10
    
    if stats['tasks_completed'] > 8:
        bonus += 5
    
    # Irrelevant metric (minimal distraction)
    unused_warning_count = stats.get('warnings', 0)
    
    multiplier = 1.5 if stats['efficiency'] > 0.85 else 1.2
    
    raw_score = (base_score * 2) + bonus
    final_score = raw_score * multiplier
    
    return int(final_score)

# Simulate employee data
days_attended = {'mon', 'tue', 'wed', 'thu', 'fri'}
performance_metrics = {
    'tasks_completed': 9,
    'efficiency': 0.88,
    'feedback': ['good', 'excellent'],
    'warnings': 1
}

final_score = evaluate_performance(days_attended, performance_metrics)
print(f"Target result: {final_score}")