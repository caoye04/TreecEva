import itertools

def analyze_workflow(tasks, thresholds):
    completed = len([t for t in tasks if t['status'] == 'done'])
    total = len(tasks)
    ratio = completed / total if total else 0

    # Distractor: irrelevant computation with string methods
    task_names = [t['name'].strip().upper() for t in tasks]
    concatenated = ''.join(task_names)
    checksum = sum(ord(c) for c in concatenated[:10]) if concatenated else 0

    # Semi-relevant filtering
    critical_tasks = [t for t in tasks if t.get('priority') == 'high']
    missed_critical = len([ct for ct in critical_tasks if ct['status'] != 'done'])

    return ratio, missed_critical, checksum

def compute_efficiency(indices, data_stream):
    # Use of itertools
    paired = list(itertools.zip_longest(indices, data_stream, fillvalue=0))
    weighted = [i * d for i, d in paired]
    
    # Dead code path (not used later)
    if len(weighted) > 10:
        smoothed = [sum(weighted[i:i+3]) / 3 for i in range(len(weighted) - 2)]
    else:
        smoothed = []  # unused

    average = sum(weighted) / len(weighted) if weighted else 0
    return round(average, 3)

def evaluate_performance(output, faults, metric):
    base = output * 100
    penalty = faults * 5
    adjustment = metric * 0.1
    
    # Multiple intermediate steps with distractions
    intermediate = base - penalty + adjustment
    volatility = abs((base - penalty) / base) if base else 0
    stability_bonus = 10 if volatility < 0.2 else 0  # depends on internal logic
    
    # Complex but partially irrelevant condition
    if base > 500 and penalty < 30:
        multiplier = 1.2
    elif adjustment > 5:
        multiplier = 1.1
    else:
        multiplier = 1.0  # default path taken

    final = (intermediate + stability_bonus) * multiplier
    
    # Additional red herring
    debug_info = f"Final pre-round: {final:.3f}"
    final_score = int(round(final))

    return final_score

# Main execution block
if __name__ == "__main__":
    worklog = [
        {'name': 'task1 ', 'status': 'done', 'priority': 'low'},
        {'name': 'task2', 'status': 'incomplete', 'priority': 'high'},
        {'name': 'task3 ', 'status': 'done', 'priority': 'medium'},
        {'name': 'task4', 'status': 'done', 'priority': 'high'},
        {'name': 'task5', 'status': 'incomplete', 'priority': 'low'}
    ]

    # Irrelevant auxiliary data
    sensor_data = [0.5, 1.2, 0.8, 2.3, 1.9]
    indices = [1, 2, 3]

    # Key computations
    completion_ratio, dropped_tasks, _ = analyze_workflow(worklog, thresholds=[0.5, 0.7])
    efficiency_metric = compute_efficiency(indices, sensor_data)
    
    productivity = int(completion_ratio * 100)
    errors = dropped_tasks * 2
    
    # Critical statement
    final_score = evaluate_performance(productivity, errors, efficiency_metric)
    
    print(f"Result: {final_score}")