def evaluate_performance(log_entries):
    base_points = 0
    penalty_count = 0
    for entry in log_entries:
        if 'ERROR' in entry:
            penalty_count += 1
        elif 'SUCCESS' in entry:
            base_points += 15
    
    raw_total = base_points - (penalty_count * 5)
    temp_status = 'active' if raw_total > 0 else 'inactive'
    processed_points = abs(raw_total) if temp_status == 'active' else 0
    
    level_adjustment = len(log_entries) % 4
    bonus_multiplier = 2 if 'CRITICAL_SUCCESS' in ''.join(log_entries) else 1
    final_score = processed_points // 3 + bonus_multiplier * level_adjustment
    return final_score

log_data = ['SUCCESS', 'INFO', 'SUCCESS', 'ERROR', 'DEBUG', 'CRITICAL_SUCCESS']
result = evaluate_performance(log_data)
print(f"Result: {result}")