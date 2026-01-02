def analyze_workload(tasks, efficiency_factor):
    total_effort = 0
    peak_load = 0
    temp_buffer = []
    for i, (hours, complexity) in enumerate(zip(tasks, [1.2, 0.8, 1.5, 1.0, 0.9])):
        raw_effort = hours * complexity
        adjusted_effort = raw_effort * (1 + 0.1 * i) if i % 2 == 0 else raw_effort * 0.95
        total_effort += adjusted_effort
        temp_buffer.append(adjusted_effort)
        
        if adjusted_effort > peak_load:
            peak_load = adjusted_effort
    
    average_effort = total_effort / len(tasks)
    effort_variance = sum((x - average_effort) ** 2 for x in temp_buffer) / len(temp_buffer)
    return total_effort, peak_load, effort_variance


def track_employee_performance(employee_data):
    base_score = 0
    bonus_adjustment = 0
    penalty_factor = 0
    distraction_counter = 0  # irrelevant tracking
    
    for day, tasks in enumerate(employee_data):
        daily_hours = [t[0] for t in tasks]
        total_hours = sum(daily_hours)
        
        if total_hours < 6:
            penalty_factor += 0.5
        elif total_hours > 10:
            bonus_adjustment += 0.3
        
        # Distractor computation: unrelated to final score
        for h in daily_hours:
            if h == 8:
                distraction_counter += 1
    
    # Real logic begins here
    all_tasks = [task for day_tasks in employee_data for task in day_tasks]
    total_effort, peak, variance = analyze_workload(all_tasks, efficiency_factor=1.1)
    
    base_score = total_effort * 10 - variance * 50
    
    if peak > 15:
        base_score += 20
    
    # Final adjustment based on logical conditions
    if total_effort > 40 and variance < 2.0:
        bonus_adjustment += 1.5
    
    final_raw_score = base_score + (bonus_adjustment * 100) - (penalty_factor * 50)
    return int(round(final_raw_score))


def calculate_performance_rating():
    # Simulated weekly data: each tuple is (hours_worked, task_weight)
    week_data = [
        [(7, 1), (8, 1), (6, 1)],
        [(9, 1), (8, 1), (7, 1)],
        [(6, 1), (10, 1), (8, 1)],
        [(8, 1), (8, 1), (9, 1)],
        [(7, 1), (6, 1), (8, 1)]
    ]
    
    # Irrelevant preprocessing
    flattened = []
    for d in week_data:
        for t in d:
            flattened.append(t)
    
    # Dummy checksum
    checksum = 0
    for i, (h, w) in enumerate(flattened):
        checksum ^= (i + h) & w  # bitwise red herring
    
    # Actual performance calculation
    score = track_employee_performance(week_data)
    
    # Additional distraction: unused transformation
    transformed = [s * 1.05 for s in [score // 2, score, score * 2]]
    
    final_score = score + (checksum % 10)
    return final_score

# Execution point
result = calculate_performance_rating()
print(f"Result: {result}")