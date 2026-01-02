from collections import defaultdict
from itertools import combinations

# Simulate task completion results with metadata
task_data = [
    {'id': 'T1', 'status': 'success', 'duration': 120, 'errors': 0, 'priority': 3},
    {'id': 'T2', 'status': 'failure', 'duration': 95, 'errors': 4, 'priority': 5},
    {'id': 'T3', 'status': 'success', 'duration': 200, 'errors': 1, 'priority': 4},
    {'id': 'T4', 'status': 'success', 'duration': 80, 'errors': 0, 'priority': 2},
    {'id': 'T5', 'status': 'failure', 'duration': 150, 'errors': 6, 'priority': 5}
]

# Irrelevant helper: counts character pairs in task IDs (distractor)
def count_adjacent_pairs(items):
    counter = defaultdict(int)
    for item in items:
        s = item['id']
        for i in range(len(s) - 1):
            counter[s[i:i+2]] += 1
    return counter

# Misleading preprocessing: computes unused duration stats
duration_stats = {
    'mean': sum(t['duration'] for t in task_data) / len(task_data),
    'max': max(t['duration'] for t in task_data),
    'min': min(t['duration'] for t in task_data)
}

# Generate all priority-error combos for analysis (partially relevant)
priority_error_map = defaultdict(list)
for task in task_data:
    priority_error_map[task['priority']].append(task['errors'])

# Weight adjustment based on error distribution (used later)
base_weights = {p: 1.0 for p in priority_error_map}
for p, errors in priority_error_map.items():
    avg_err = sum(errors) / len(errors)
    base_weights[p] *= (1 + avg_err / 2)  # Heavier penalty for high-error priorities

# Distractor: unused combination analysis
useless_combos = []
for combo in combinations(task_data, 2):
    if combo[0]['status'] != combo[1]['status']:
        diff = abs(combo[0]['duration'] - combo[1]['duration'])
        useless_combos.append(diff // 10)  # Binned difference (not used)

# Success tracking with side logging (semi-relevant)
success_log = []
current_batch = []
for task in task_data:
    current_batch.append(task['id'])
    if task['status'] == 'success':
        success_log.append({
            'batch': list(current_batch),
            'count': len([t for t in task_data if t['id'] in current_batch and t['status'] == 'success'])
        })
        current_batch.clear()  # Reset after logging success

# Core evaluation logic
def evaluate_performance(tasks, weights):
    total_score = 0
    bonus_applied = False
    recent_failures = 0

    for idx, task in enumerate(tasks):
        base_score = 10 if task['status'] == 'success' else -5
        priority_factor = weights[task['priority']]
        time_efficiency = (200 - task['duration']) / 100  # Normalize to ~1 scale
        error_penalty = task['errors'] * 1.5

        # Conditional bonus logic
        if idx > 0 and tasks[idx-1]['status'] == 'success' and task['status'] == 'success':
            base_score += 3  # Small consecutive success bonus

        # Accumulate failure streak for penalty
        if task['status'] == 'failure':
            recent_failures += 1
            if recent_failures >= 2:
                base_score -= 4  # Streak penalty
        else:
            recent_failures = 0

        # Final contribution
        contribution = (base_score - error_penalty) * priority_factor * max(time_efficiency, 0.5)
        total_score += contribution

    # Final adjustment: if more than 2 successes, add team efficiency bonus
    success_count = sum(1 for t in tasks if t['status'] == 'success')
    if success_count > 2:
        total_score += 8.5  # Arbitrary team synergy bonus

    return int(round(total_score))

# Execute key computation
task_results = task_data  # Alias for clarity in function call
final_score = evaluate_performance(task_results, base_weights)

# Print result as required
print(f"Target result: {final_score}")