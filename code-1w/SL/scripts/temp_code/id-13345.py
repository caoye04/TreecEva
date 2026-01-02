from collections import defaultdict

# Simulated benchmark data for code reasoning tasks
task_ids = [101, 102, 103, 104]
execution_times = [0.23, 0.45, 0.33, 0.67]  # in seconds
accuracy_flags = [True, True, False, True]
complexity_levels = [3, 5, 4, 6]

# Irrelevant distraction: mapping task types (not used in final logic)
task_type_map = {tid: 'arithmetic' if i % 2 == 0 else 'logic' for i, tid in enumerate(task_ids)}

# Initialize tracking structures
runtime_stats = defaultdict(float)
completion_status = {}

# Dummy preprocessing: normalize execution times (semi-relevant but not directly used)
normalized_times = []
mean_time = sum(execution_times) / len(execution_times)
for t in execution_times:
    normalized_times.append((t - mean_time) / mean_time)

# Assign baseline status (some dead code paths)
for idx, tid in enumerate(task_ids):
    completion_status[tid] = 'completed'
    if idx == 2:
        temp_flag = accuracy_flags[idx]  # red herring variable
        continue  # misleading control flow

# Build core benchmark data with relevant metrics
benchmark_data = []
for i, tid in enumerate(task_ids):
    benchmark_data.append({
        'id': tid,
        'time': execution_times[i],
        'accurate': accuracy_flags[i],
        'level': complexity_levels[i]
    })

# Misleading intermediate calculation: average complexity (not directly used)
avg_complexity = sum(complexity_levels) / len(complexity_levels)
discount_factor = 0.9 if avg_complexity > 4 else 1.0

# Core logic: calculate performance score
def calculate_performance(data):
    base_score = 0
    penalty = 0
    bonus = 0
    
    # Use enumerate and zip together (required python idiom)
    for idx, (entry, norm_t) in enumerate(zip(data, normalized_times)):
        base_score += entry['level'] * 10
        if entry['accurate']:
            bonus += 5 + idx  # reward accuracy with position factor
        else:
            penalty += int(entry['time'] * 100)
        
        # Tracking unused stats (distractor)
        runtime_stats[f'window_{idx}'] += entry['time']

    # Additional distraction: min/max analysis (unused)
    all_levels = [e['level'] for e in data]
    level_range = max(all_levels) - min(all_levels)

    # Final computation
    raw_performance = base_score + bonus - penalty
    adjusted = raw_performance * discount_factor  # uses earlier discount
    final_score = round(adjusted, 2)
    
    return final_score

# Execute key statement
temp_result = sum(normalized_times)  # irrelevant computation
final_score = calculate_performance(benchmark_data)
print(f"Result: {final_score}")