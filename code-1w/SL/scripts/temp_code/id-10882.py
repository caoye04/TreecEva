from collections import defaultdict
import math

# Simulated system benchmark logs with execution times and status
benchmark_logs = [
    {'task': 'parse_init', 'time_ms': 45, 'success': True, 'retries': 0},
    {'task': 'validate_schema', 'time_ms': 120, 'success': True, 'retries': 1},
    {'task': 'encode_payload', 'time_ms': 200, 'success': False, 'retries': 3},
    {'task': 'compress_stream', 'time_ms': 95, 'success': True, 'retries': 0},
    {'task': 'transmit_data', 'time_ms': 300, 'success': False, 'retries': 2},
    {'task': 'verify_checksum', 'time_ms': 60, 'success': True, 'retries': 0},
    {'task': 'finalize_session', 'time_ms': 150, 'success': True, 'retries': 1}
]

# Irrelevant helper: counts total characters in task names (distractor)
total_chars = sum(len(log['task']) for log in benchmark_logs)

# Noise variable: average retry count across all tasks (semi-relevant but not used in final logic)
avg_retries = sum(log['retries'] for log in benchmark_logs) / len(benchmark_logs)

# Threshold for acceptable performance (in ms)
thresh_func = lambda t: t < 100
threshold = 110

# Group tasks by success status (distractor data structure)
status_map = defaultdict(list)
for log in benchmark_logs:
    status_map[log['success']].append(log['time_ms'])

# Compute failure rate (not directly used but adds cognitive load)
total_failures = len([log for log in benchmark_logs if not log['success']])
failure_rate = total_failures / len(benchmark_logs)

# Core logic: score based on fast and successful tasks
fast_success_count = 0
penalty_points = 0

for log in benchmark_logs:
    time_ms = log['time_ms']
    success = log['success']
    retries = log['retries']
    
    # Primary condition: only successful tasks can contribute
    if success:
        if time_ms <= threshold:
            fast_success_count += 1
        else:
            # Minor penalty for slow but successful tasks
            penalty_points += 1
    else:
        # Heavier penalty for failures, scaled by retries
        penalty_points += 2 + retries // 2

# Secondary metric: geometric mean of successful task times (distractor)
success_times = [log['time_ms'] for log in benchmark_logs if log['success']]
geometric_mean = math.exp(sum(math.log(t) for t in success_times) / len(success_times)) if success_times else 0

# Final scoring formula
base_score = fast_success_count * 10
adjusted_score = base_score - (penalty_points * 3)

# Additional noise: normalize to hypothetical scale (unused)
normalized = adjusted_score / 100.0 if adjusted_score > 0 else 0

# Key statement
final_score = aggregate_performance(benchmark_logs, threshold)

# Implementation of aggregate function using lambda and list comprehension
def aggregate_performance(logs, thresh):
    valid_benefit = sum(10 for entry in logs if entry['success'] and entry['time_ms'] <= thresh)
    valid_penalty = sum(3 for entry in logs if not entry['success'])
    retry_penalty = sum(entry['retries'] for entry in logs if not entry['success'])
    return valid_benefit - valid_penalty - retry_penalty

# Print result
print(f"Result: {final_score}")