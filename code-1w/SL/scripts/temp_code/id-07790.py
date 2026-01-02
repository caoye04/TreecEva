from collections import defaultdict

# Simulate a productivity tracker across multiple work sessions
def compute_productivity_log():
    session_data = [
        {'start': 0, 'end': 30, 'tasks_completed': 5, 'errors': 1},
        {'start': 35, 'end': 60, 'tasks_completed': 7, 'errors': 0},
        {'start': 90, 'end': 120, 'tasks_completed': 10, 'errors': 2},
        {'start': 150, 'end': 180, 'tasks_completed': 6, 'errors': 1}
    ]

    # Irrelevant accumulator for distraction
    cumulative_time_gap = 0
    gaps = []
    for i in range(1, len(session_data)):
        gap = session_data[i]['start'] - session_data[i-1]['end']
        gaps.append(gap)
        cumulative_time_gap += gap

    # Track task efficiency per session (distraction)
    session_efficiency = {}
    for idx, s in enumerate(session_data):
        raw_effort = s['tasks_completed'] + s['errors']
        if raw_effort > 0:
            session_efficiency[idx] = s['tasks_completed'] / raw_effort
        else:
            session_effort = 1.0

    # Core metrics
    total_tasks = sum(s['tasks_completed'] for s in session_data)
    total_errors = sum(s['errors'] for s in session_data)
    total_duration = max(s['end'] for s in session_data) - min(s['start'] for s in session_data)
    
    # Active minutes: sum of actual working intervals
    active_minutes = sum(s['end'] - s['start'] for s in session_data)
    
    # Distractor: complex error-weighted adjustment (not used in final result)
    penalty_map = defaultdict(int)
    for s in session_data:
        duration = s['end'] - s['start']
        if s['errors'] > 0:
            penalty_map[duration] += s['errors'] * 0.5

    # Ghost variable: looks important but unused
    adjusted_task_rate = total_tasks / total_duration if total_duration else 0

    # Primary output calculation
    base_output = total_tasks * 10 - total_errors * 5  # Quality-adjusted output
    stress_factor = len([s for s in session_data if (s['end'] - s['start']) > 25])
    bonus = stress_factor * 3 if base_output > 200 else stress_factor * 1
    total_output = base_output + bonus

    # Key statement
    efficiency_score = total_output / active_minutes if active_minutes else 0
    
    # Print result as required
    print(f"Result: {efficiency_score}")

    return efficiency_score

# Execute
compute_productivity_log()