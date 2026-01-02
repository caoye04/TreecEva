from collections import defaultdict
import math

# Simulate employee performance tracking with interference

# Core data
employee_tasks = [85, 90, 78, 92, 88]
task_weights = [0.2, 0.3, 0.1, 0.25, 0.15]
attendance_records = [1, 1, 0, 1, 1]  # 1 = present, 0 = absent

# Distractor variables (not directly used in final score)
pseudo_entropy = 0.0
for x in range(5):
    pseudo_entropy += math.sin(x) * math.cos(x)
dummy_cache = set()
for i in range(len(employee_tasks)):
    dummy_cache.add((i, employee_tasks[i] % 7))

# Intermediate calculations
weighted_sum = sum(t * w for t, w in zip(employee_tasks, task_weights))
attendance_bonus = 10 if sum(attendance_records) >= 4 else 0
base_productivity = weighted_sum + attendance_bonus

# Risk factor computation with conditional logic and red herring
risk_logs = []
high_risk_count = 0
for val in employee_tasks:
    adjusted = val - 80
    if adjusted > 10:
        risk_logs.append('overperforming')
    elif adjusted < -5:
        risk_logs.append('underperforming')
        high_risk_count += 1
    else:
        risk_logs.append('stable')

# Unused but plausible metric
average_risk_level = len(risk_logs) / (high_risk_count + 1)

# Real risk factor (only this matters)
risk_factor = 1.0
if high_risk_count >= 2:
    risk_factor = 0.8
elif high_risk_count == 1:
    risk_factor = 0.9

# Secondary distractor: set operations with no impact
task_set_a = {85, 90, 78}
task_set_b = {90, 92, 88}
symmetric_diff = task_set_a.symmetric_difference(task_set_b)
union_size = len(task_set_a.union(task_set_b))

# Conditional expression used idiomatically
productivity = base_productivity if base_productivity > 85 else 85 * 1.1

# Helper function that appears complex but is straightforward
def evaluate_performance(prod, risk):
    # Apply risk adjustment
    adjusted = prod * risk
    
    # Artificial complexity: normalize using unused cache
    normalization_shift = 0
    for item in dummy_cache:
        normalization_shift += item[0]  # This does nothing meaningful
    normalization_shift = normalization_shift % 1  # Always affects decimal only
    
    # Final score with negligible shift (but deterministic)
    final = adjusted + normalization_shift
    
    # More red herring: log transformation not applied
    if final > 100:
        temp_log = math.log(final)
        # Not used
    
    return round(final, 2)

# Critical execution point
final_score = evaluate_performance(productivity, risk_factor)

# Output result as required
print(f"Result: {final_score}")