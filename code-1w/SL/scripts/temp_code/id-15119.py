from collections import defaultdict, Counter

# Simulated benchmark results across multiple test phases
test_phases = ['phase_a', 'phase_b', 'phase_c', 'phase_d']
raw_data = [
    (120, 'phase_a', 'success'),
    (145, 'phase_b', 'failure'),
    (130, 'phase_a', 'success'),
    (160, 'phase_c', 'success'),
    (110, 'phase_b', 'success'),
    (150, 'phase_d', 'failure'),
    (135, 'phase_a', 'success'),
    (140, 'phase_c', 'success')
]

# Aggregating results by phase
aggregated = defaultdict(list)
for time_val, phase, status in raw_data:
    aggregated[phase].append(time_val)

# Compute average duration per phase
avg_duration = {phase: sum(times) / len(times) for phase, times in aggregated.items()}

# Track success/failure counts
status_counter = Counter(status for _, _, status in raw_data)
success_count = status_counter['success']
failure_count = status_counter['failure']

# Auxiliary metric: total execution load
execution_load = sum(t[0] for t in raw_data)
overhead_penalty = execution_load * 0.01 if execution_load > 1000 else 0

# Phase completeness check
completed_phases = set(phase for _, phase, _ in raw_data)
expected_completion = len(completed_phases) == len(test_phases)
completeness_bonus = 10 if expected_completion else 0

# Normalize durations to compute efficiency scores
efficiency_scores = {}
baseline = min(avg_duration.values())
for phase, avg_time in avg_duration.items():
    efficiency_scores[phase] = round(baseline / avg_time, 3)

# Calculate aggregate efficiency
aggregate_efficiency = sum(efficiency_scores.values())

# Misleading intermediate calculation (distractor)
temp_fluctuation = max(avg_duration.values()) - min(avg_duration.values())
stability_index = 100 - temp_fluctuation  # Not actually used later

# Secondary distractor: simulate resource usage
resource_usage = defaultdict(int)
for t, phase, _ in raw_data:
    resource_usage[phase] += t // 50
weighted_resource = sum(resource_usage.values()) * 0.5  # Dead-end computation

# Core performance logic
base_performance = success_count * 25
penalty = failure_count * 15

# Final score computation depends only on base_performance, penalty, and aggregate_efficiency
def calculate_performance(results):
    base = base_performance - penalty
    adjusted = base * (1 + aggregate_efficiency / 10)
    return int(adjusted)

final_score = calculate_performance(benchmark_results=None)
Result: final_score