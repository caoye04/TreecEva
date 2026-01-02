def analyze_workload(hours, tasks):
    if not hours or not tasks:
        return 0
    efficiency = tasks / hours if hours > 0 else 0
    return efficiency * 100

# Simulate employee performance metrics
total_hours_worked = 45
tasks_completed = 18

# Distractor variables - not used in final calculation
distraction_multiplier = 3.14159
temp_result_cache = [0] * 100
unused_flag = True

baseline_target = 20
efficiency_ratio = analyze_workload(total_hours_worked, tasks_completed)

# Simulate conditional bonus logic
if efficiency_ratio >= 40:
    bonus_awarded = True
    adjustment_factor = 1.2
else:
    bonus_awarded = False
    adjustment_factor = 0.9

# Additional distraction: irrelevant string processing
data_stream = "LogEntry:2024:PERF"
processed_tag = data_stream.lower().replace(":", "_") if "PERF" in data_stream else "default"

# Simulate tiered performance level
performance_tier = 'High' if efficiency_ratio > 45 else 'Standard' if efficiency_ratio > 30 else 'Low'

# Secondary distraction: unused loop with side computation
rolling_sum = 0
for i in range(5):
    rolling_sum += i * 2  # Irrelevant to final result

# Main scoring logic with conditional expression
base_score = efficiency_ratio * 1.5
penalty = 10 if total_hours_worked > 40 else 5
adjusted_score = base_score - penalty

# Final performance rating using helper function and conditional logic
def calculate_performance_rating():
    extra_load = tasks_completed % 4
    load_compensation = 8 if extra_load >= 2 else 4
    
    # Nested conditionals with distractor math
    complexity_factor = 0
    for t in [2, 3]:
        for h in [1, 2]:
            complexity_factor += (t ** h)  # evaluates to 2^1 + 2^2 + 3^1 + 3^2 = 2+4+3+9=18
    
    # Unused state tracking
    state_log = {"phase": "final", "valid": True}
    
    intermediate = adjusted_score + load_compensation
    return int(intermediate * adjustment_factor) if bonus_awarded else int(intermediate)

final_score = calculate_performance_rating()
print(f"Result: {final_score}")