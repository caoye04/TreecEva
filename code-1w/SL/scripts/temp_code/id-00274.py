import math

# Simulated sensor readings and task execution results
task_set = ['calibration', 'alignment', 'validation', 'diagnostics']
results = [True, False, True, True]

# Irrelevant utility function (dead code path)
def normalize_readings(data):
    return [x / max(data) for x in data]

# Sensor baseline drift compensation (unused)
baseline_drift = 0.03
compensated_offsets = [round(baseline_drift * i, 3) for i in range(4)]

# Auxiliary state tracking (partially irrelevant)
execution_log = {}
status_flags = set()
status_flags.add('initialized')
status_flags.add('ready')

# Bitmask simulation for hardware status (distractor)
hw_status_code = 0b1010
error_mask = 0b1100
is_error = bool(hw_status_code & error_mask)

# Redundant transformation (irrelevant)
transformed_results = []
for idx, res in enumerate(results):
    if res:
        transformed_results.append((idx + 1) * 1.5)
    else:
        transformed_results.append(0.0)

# Tuple unpacking with dummy values (misleading)
primary_task, _, secondary_task, _ = task_set

# Scoring weights (some are unused)
weights = {
    'calibration': 0.4,
    'alignment': 0.3,
    'validation': 0.2,
    'diagnostics': 0.1,
    'fallback': 0.05  # Unused weight
}

# Linear search for failed tasks (used in evaluation)
failed_indices = []
for i in range(len(results)):
    if not results[i]:
        failed_indices.append(i)

# Set operations to identify incomplete vs expected (core concept)
expected_tasks = set(task_set)
completed_tasks = set([task_set[i] for i, r in enumerate(results) if r])
incomplete_tasks = expected_tasks - completed_tasks

# Complex conditional scoring logic
base_score = 0
penalty = 0

if 'calibration' in completed_tasks:
    base_score += 80
if len(incomplete_tasks) > 0:
    penalty += len(incomplete_tasks) * 15

# Bonus for consecutive successes (bit operation as red herring)
consecutive_bonus = 0
for i in range(len(results) - 1):
    if results[i] and results[i+1]:
        # Using XOR to mislead about control flow
        flag = (i ^ (i+1)) % 2
        if flag == 0:
            consecutive_bonus += 5

# Integer division and rounding used meaningfully
raw_score = base_score - penalty + consecutive_bonus
normalized_score = int(raw_score // 1.0)  # Simulate integer truncation

# Final non-linear adjustment using logarithmic scaling (only applied if score > 0)
if normalized_score > 0:
    adjusted_score = round(math.log(normalized_score) * 10, 2)
else:
    adjusted_score = 0

# Destructuring assignment (tuple unpacking) with distraction
_, alignment_outcome, _, diag_outcome = results

# Core evaluation function
def evaluate_performance(tasks, outcomes):
    # Recompute completion set inside function (redundant but consistent)
    completed = set([tasks[i] for i, out in enumerate(outcomes) if out])
    if 'diagnostics' in completed:
        trust_factor = 1.2
    else:
        trust_factor = 0.8
    
    # Use of set length and arithmetic
    success_count = len(completed)
    total_tasks = len(tasks)
    ratio = success_count / total_tasks
    
    # Final score computed from multiple paths
    final = int((adjusted_score * ratio * trust_factor))
    
    # Dead code: this branch is never reached due to fixed inputs
    if False:
        fallback = sum([1 for t in tasks if t.startswith('x')])
        final += fallback * 10
        
    return final

# Execution point of interest
final_score = evaluate_performance(task_set, results)

# Output result as required
print(f"Result: {final_score}")