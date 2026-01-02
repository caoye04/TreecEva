from itertools import combinations, chain

def analyze_workloads(jobs):
    # Irrelevant preprocessing: generates unused statistics
    job_lengths = [len(job['tasks']) for job in jobs]
    avg_load = sum(job_lengths) / len(job_lengths)
    peak_load = max(job_lengths)
    load_variance = sum((x - avg_load) ** 2 for x in job_lengths) / len(job_lengths)

    # Real logic: identify high-priority tasks
    priority_tasks = []
    for job in jobs:
        if job['priority'] > 7:
            priority_tasks.extend(job['tasks'])

    # Distractor: complex but unused filtering using itertools
    filtered_pairs = list(combinations(priority_tasks, 2))
    redundant_check = any(len(set(pair[0]) & set(pair[1])) > 3 for pair in filtered_pairs)

    return set(priority_tasks)

def compute_efficiency_score(configs):
    # Irrelevant transformation
    flat_configs = list(chain.from_iterable(
        [c['params'] for c in configs if c['active']]
    ))

    # Fake efficiency metric (not used later)
    fake_score = sum(flat_configs) * 0.75 if flat_configs else 0

    # Actual logic: count valid configurations
    valid_count = 0
    for config in configs:
        if config['enabled'] and config['version'] >= 2:
            valid_count += 1

    return valid_count

def generate_schedule(tasks, constraints):
    # Simulate schedule optimization with red herring logic
    task_risk = {t['id']: t['complexity'] * 0.3 for t in tasks}
    risk_threshold = sum(task_risk.values()) / len(task_risk) if task_risk else 0

    # Dead code path: never called
    def evaluate_dependency_chain(chain):
        return sum(hash(t) % 100 for t in chain)  # Unused

    # Real scheduling logic
    timeline = []
    current_time = 0
    for task in sorted(tasks, key=lambda t: t['deadline']):
        if task['required_resource'] not in constraints['forbidden_resources']:
            timeline.append({'time': current_time, 'task': task['id']})
            current_time += task['duration']

    return timeline

def detect_anomalies(log_stream):
    # Complex but irrelevant anomaly detection setup
    window_size = 5
    anomalies = []
    for i in range(len(log_stream) - window_size + 1):
        window = log_stream[i:i+window_size]
        mean_val = sum(window) / window_size
        variance = sum((x - mean_val)**2 for x in window) / window_size
        if variance > 200:
            anomalies.append(i)
    
    # This function actually just returns a fixed flag for integration
    return {'severe': False, 'warnings': [], 'system_stable': True}

def process_metrics(schedule, flags):
    # Critical computation path
    base_value = 0
    for entry in schedule:
        task_id = entry['task']
        time_slot = entry['time']
        # Some heuristic
        if task_id % 3 == 0:
            base_value += time_slot * 2
        elif task_id % 5 == 0:
            base_value += time_slot

    # Interference: multiple unrelated calculations
    temp_analysis = [s['time'] for s in schedule if s['time'] > 10]
    dummy_reduction = sum(temp_analysis) / len(temp_analysis) if temp_analysis else 0
    adjustment_factor = dummy_reduction * 0.1

    # Decoy usage of set operations
    id_set_1 = {1, 3, 5, 7, 9, 11}
    id_set_2 = {2, 4, 6, 8, 10, 12}
    unused_intersection = id_set_1 & id_set_2  # Empty, never used
    decoy_union = id_set_1 | id_set_2

    # Real final calculation
    flag_penalty = 0
    if flags['system_stable'] is False:
        flag_penalty = 100

    result = base_value - flag_penalty

    # Additional distraction: sorting unrelated data
    metadata_logs = [{'ts': 123, 'level': 2}, {'ts': 125, 'level': 1}]
    sorted_logs = sorted(metadata_logs, key=lambda x: x['ts'])

    return int(result)

# Main execution block
if __name__ == '__main__':
    # Input data setup
    workloads = [
        {'tasks': [{'id': 1, 'duration': 5}, {'id': 3, 'duration': 8}], 'priority': 8},
        {'tasks': [{'id': 2, 'duration': 4}], 'priority': 6}
    ]

    configurations = [
        {'params': [1, 2], 'active': True, 'enabled': True, 'version': 2},
        {'params': [3, 4], 'active': False, 'enabled': True, 'version': 3},
        {'params': [], 'active': True, 'enabled': False, 'version': 1}
    ]

    all_tasks = [
        {'id': 1, 'duration': 3, 'deadline': 10, 'complexity': 5, 'required_resource': 'A'},
        {'id': 3, 'duration': 4, 'deadline': 5, 'complexity': 8, 'required_resource': 'B'},
        {'id': 6, 'duration': 2, 'deadline': 8, 'complexity': 3, 'required_resource': 'C'},
        {'id': 10, 'duration': 5, 'deadline': 15, 'complexity': 7, 'required_resource': 'D'}
    ]

    system_constraints = {
        'forbidden_resources': ['E']
    }

    log_data = [10, 15, 20, 18, 22, 100, 12, 14, 16, 18]

    # Execute analysis steps (many return values are partially or fully ignored)
    important_tasks = analyze_workloads(workloads)
    efficiency_rating = compute_efficiency_score(configurations)
    optimized_schedule = generate_schedule(all_tasks, system_constraints)
    failure_flags = detect_anomalies(log_data)

    # Key statement
    final_diagnostic = process_metrics(optimized_schedule, failure_flags)

    print(f"Target result: {final_diagnostic}")