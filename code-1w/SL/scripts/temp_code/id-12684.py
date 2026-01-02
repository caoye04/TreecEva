from collections import defaultdict
import itertools

# Simulated system metrics from a distributed task scheduler
task_durations = [12, 15, 10, 8, 20, 14, 16, 9]
node_load = {'A': 78, 'B': 65, 'C': 88, 'D': 54, 'E': 91}
completion_flags = [True, True, False, True, True, False, True, True]

# Irrelevant auxiliary data (distractor)
user_preferences = {'theme': 'dark', 'refresh_rate': 60, 'auto_save': True}
temp_log = [f"entry_{i}" for i in range(len(task_durations))]

# Misleading intermediate calculation (dead path)
def calculate_efficiency(durations):
    return sum(d ** 0.5 for d in durations if d > 10) * 0.7

efficiency_score = calculate_efficiency(task_durations)  # Dead end

# Another red herring: unused transformation
distinct_pairs = list(itertools.combinations(task_durations, 2))
filtered_pairs = [(a, b) for a, b in distinct_pairs if (a + b) % 7 == 0]
pair_count_map = defaultdict(int)
for a, b in filtered_pairs:
    pair_count_map[a] += 1

# Unused statistical decoy
mean_duration = sum(task_durations) / len(task_durations)
adjusted_durations = [d - mean_duration + 5 for d in task_durations]

# Core logic disguised among noise
active_tasks = [d for d, flag in zip(task_durations, completion_flags) if flag]
failed_task_count = completion_flags.count(False)

# Baseline thresholds (simulated)
baseline = {
    'target_duration': 13,
    'max_failures': 3,
    'load_threshold': 70
}

# Simulated metric aggregator (partially relevant)
metrics = defaultdict(float)
metrics['avg_completion'] = sum(active_tasks) / len(active_tasks) if active_tasks else 0
metrics['failure_penalty'] = failed_task_count * 1.5
metrics['node_balance'] = sum(1 for load in node_load.values() if load < baseline['load_threshold'])

# Decoy function that's defined but not used
def analyze_distribution(values):
    hist = defaultdict(int)
    for v in values:
        hist[v // 5] += 1
    return sorted(hist.items())

# Noise: fake normalization
normalized_load = {k: (v - 50) / 40 for k, v in node_load.items()}

# Key distracting computation with misleading name
system_stability = 100 - sum(load ** 0.8 for load in node_load.values() if load > 80) / 2

# Actual critical logic buried in distractions
def evaluate_performance(perf_metrics, base):
    score = 0
    score += max(0, (base['target_duration'] - perf_metrics['avg_completion']) * 2)
    score -= perf_metrics['failure_penalty'] * 3
    score += perf_metrics['node_balance'] * 4
    
    # Hidden adjustment based on subtle condition
    if perf_metrics['avg_completion'] < base['target_duration'] and perf_metrics['node_balance'] >= 2:
        score += 10  # Efficiency bonus
    
    # Red herring branch (never taken due to logic)
    if 'phantom_key' in base:
        score *= base['phantom_key']
        
    return int(score)

# Execution point of interest
final_score = evaluate_performance(metrics, baseline)

# Output required format
print(f"Target result: {final_score}")