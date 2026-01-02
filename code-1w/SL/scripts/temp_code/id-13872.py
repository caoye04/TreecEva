def analyze_workload(hours, tasks):
    efficiency_ratio = (tasks * 1.5) / max(hours, 1)
    stress_index = 0
    if hours > 8:
        stress_index += 2
    if tasks < 3:
        stress_index += 1
    return efficiency_ratio >= 2.0 and stress_index < 3

def validate_data(entries):
    valid_count = 0
    for entry in entries:
        parts = entry.split(',')
        if len(parts) != 2:
            continue
        try:
            hour_val = int(parts[0])
            task_val = int(parts[1])
            if 0 <= hour_val <= 24 and 0 <= task_val <= 50:
                valid_count += 1
        except ValueError:
            pass
    return valid_count >= 3

def calculate_performance_rating():
    raw_entries = ['7,5', '9,2', '6,4', '10,1', '8,3']
    
    # Irrelevant preprocessing: counts characters in entries (not used later)
    total_chars = sum(len(e) for e in raw_entries)
    avg_char_length = total_chars / len(raw_entries) if raw_entries else 0
    
    # Semi-relevant validation
    is_data_valid = validate_data(raw_entries)
    
    # Core logic masked by distraction
    completed_tasks = 0
    total_hours = 0
    high_pressure_days = 0
    
    for entry in raw_entries:
        h, t = map(int, entry.split(','))
        total_hours += h
        completed_tasks += t
        if h > 9 and t < 3:
            high_pressure_days += 1
    
    # Distractor: unused computation path
    hypothetical_efficiency = (completed_tasks * 2.0) / (total_hours + 1)
    penalty_factor = 1.0
    if high_pressure_days > 1:
        penalty_factor = 0.8
    
    # Actual scoring logic
    base_score = completed_tasks * 10 - total_hours
    adjustment = 5 if analyze_workload(total_hours, completed_tasks) else -10
    final_score = base_score + adjustment
    
    # Early termination check (never triggers due to data)
    if not is_data_valid:
        return -1
    
    # Additional red herring: string-based analysis with no impact
    flagged_entries = [e for e in raw_entries if '10' in e or '1' in e.split(',')[1]]
    flag_count = len(flagged_entries)
    temp_debug = f'Detected {flag_count} flagged entries'  # unused
    
    return final_score

# Execute and print result
target_result = calculate_performance_rating()
print(f"Result: {target_result}")