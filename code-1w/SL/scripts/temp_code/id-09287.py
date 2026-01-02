from collections import defaultdict

# Simulate a task evaluation system with noise and intermediate metrics
def analyze_complexity(task):
    return sum(ord(c) for c in task[:3]) % 7

def compute_latency_penalty(task_size):
    # Irrelevant latency simulation
    penalty = 0
    for i in range(min(task_size, 10)):
        penalty += (i ** 2) % 3
    return penalty

def filter_valid_tasks(tasks):
    valid = []
    temp_buffer = []
    for t in tasks:
        if len(t) > 4 and 'x' not in t:
            temp_buffer.append(t)
    # Only use some of the filtered data
    for tb in temp_buffer:
        if tb[0].lower() != 'd':
            valid.append(tb)
    return valid

def generate_baseline_map(valid_tasks):
    # Creates mapping but only partially used later
    baseline = defaultdict(int)
    for task in valid_tasks:
        key = task[0].upper()
        baseline[key] += 1
    adjustment = 0
    for k in baseline:
        adjustment += ord(k) % 5
    return dict(baseline), adjustment

def evaluate_task_group(task_list, mode='strict'):
    counts = defaultdict(int)
    sizes = [len(t) for t in task_list]
    avg_size = sum(sizes) / len(sizes) if sizes else 0
    
    # Distractor: complex conditional not fully impacting result
    threshold = 5
    if avg_size > 6:
        threshold -= 1
    elif avg_size < 4:
        for s in sizes:
            if s % 2 == 0:
                threshold += 0.5
                break

    for task in task_list:
        complexity = analyze_complexity(task)
        if len(task) >= threshold and complexity >= 3:
            counts['qualified'] += 1
        else:
            counts['excluded'] += 1
    
    # Dead code path (never reached due to logic)
    if mode == 'debug':
        counts['debug_mode'] = True
        
    return dict(counts), threshold

def evaluate_performance(results, base_threshold):
    score = 0
    bonus_tracker = defaultdict(list)
    
    # Meaningful computation
    for res in results:
        if res['status'] == 'success':
            score += res['value']
            bonus_tracker['success'].append(res['value'])
        elif res['status'] == 'retry_success':
            adjusted = res['value'] - 1
            score += adjusted
            bonus_tracker['retries'].append(adjusted)
    
    # Red herring: elaborate but unused structure
    summary_stats = {
        'max_bonus': max(bonus_tracker['success']) if bonus_tracker['success'] else 0,
        'penalty_count': len(bonus_tracker['retries']),
        'distribution': {i: bonus_tracker['success'].count(i) for i in set(bonus_tracker['success'])}
    }
    
    # Actual final adjustment
    if len(bonus_tracker['retries']) > 2:
        score -= 3
    if base_threshold < 4.5:
        score += 1
    
    return int(score)

# Main execution flow
task_names = ['encrypt_data', 'validate_token', 'hash_lookup', 'decode_payload', 'verify_access', 'fetch_resource']
filtered_tasks = filter_valid_tasks(task_names)
baseline_map, adj = generate_baseline_map(filtered_tasks)

eval_counts, thresh = evaluate_task_group(filtered_tasks, mode='strict')

# Simulated result logs (core input)
result_log = [
    {'task': 'encrypt_data', 'status': 'success', 'value': 7},
    {'task': 'validate_token', 'status': 'success', 'value': 6},
    {'task': 'hash_lookup', 'status': 'retry_success', 'value': 5},
    {'task': 'decode_payload', 'status': 'retry_success', 'value': 8},
    {'task': 'verify_access', 'status': 'retry_success', 'value': 4},
    {'task': 'fetch_resource', 'status': 'success', 'value': 9}
]

# Latency distractor call (no effect on final result)
latency_noise = 0
for entry in result_log:
    size_factor = len(entry['task'])
    latency_noise += compute_latency_penalty(size_factor)

base_threshold = thresh - 1.2
final_score = evaluate_performance(result_log, base_threshold)
print(f"Target result: {final_score}")