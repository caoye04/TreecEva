from collections import defaultdict, Counter

# Simulated system metrics from a distributed computing environment
task_durations = [2.3, 1.8, 4.1, 3.2, 2.9, 5.0, 3.7, 2.4]
resource_usage = [0.65, 0.82, 0.47, 0.71, 0.93, 0.33, 0.68, 0.77]
node_heartbeats = [True, True, False, True, True, False, True, True]

def analyze_stability(heartbeats):
    # Irrelevant function - distractor
    uptime_ratio = sum(heartbeats) / len(heartbeats)
    return uptime_ratio > 0.7

def calculate_efficiency(durations, usage):
    # Another plausible but unused function
    avg_duration = sum(durations) / len(durations)
    avg_usage = sum(usage) / len(usage)
    return (1 / avg_duration) * (1 - avg_usage)

# Unused transformation - red herring
duration_rankings = {}
for i, dur in enumerate(sorted(task_durations, reverse=True)):
    duration_rankings[dur] = i + 1

# Misleading normalization attempt (not used in final logic)
normalized_durations = []
max_dur = max(task_durations)
for d in task_durations:
    norm_val = d / max_dur if max_dur != 0 else 0
    normalized_durations.append(round(norm_val, 3))

# Decoy data structure with extra processing
event_log = defaultdict(list)
for idx, (d, u) in enumerate(zip(task_durations, resource_usage)):
    category = 'high_load' if u > 0.7 else 'normal'
    event_log[category].append((idx, d, u))

# Fake anomaly detection
anomalies = []
for i, (d, u) in enumerate(zip(task_durations, resource_usage)):
    if d > 4.0 and u < 0.5:
        anomalies.append(i)

# Core relevant variables
metrics = {
    'avg_duration': sum(task_durations) / len(task_durations),
    'completion_rate': sum(node_heartbeats) / len(node_heartbeats),
    'load_balance': 1 - Counter([round(u, 1) for u in resource_usage]).most_common(1)[0][1] / len(resource_usage)
}

weights = {
    'avg_duration': 0.4,
    'completion_rate': 0.35,
    'load_balance': 0.25
}

# Bit manipulation decoy - looks important but unused
config_flag = 0b1011
retry_enabled = config_flag & 0b1000  # Check fourth bit
backoff_strategy = (config_flag & 0b0110) >> 1
checksum = (config_flag ^ 0b1111) + 3

# Red herring: complex conditional expression with no side effects
system_status = 'optimal' if (analyze_stability(node_heartbeats) and 
                             calculate_efficiency(task_durations, resource_usage) > 0.4) else 'degraded'

# Critical computation path obscured by distractions
def evaluate_performance(perf_metrics, metric_weights):
    score = 0.0
    # Key calculation steps
    duration_component = (4.0 - perf_metrics['avg_duration']) * metric_weights['avg_duration']
    completion_component = perf_metrics['completion_rate'] * metric_weights['completion_rate']
    balance_component = perf_metrics['load_balance'] * metric_weights['load_balance']
    
    # Accumulate score through multiple steps
    temp_score = duration_component
    temp_score += completion_component
    temp_score += balance_component
    
    # Final adjustment based on hidden rule
    if perf_metrics['completion_rate'] >= 0.75:
        temp_score *= 1.1  # Performance bonus
    
    return temp_score

# Dead code path - never executed
if __debug__:
    def debug_trace(x):
        print(f'Debug: {x}')

# Unused list comprehension distraction
efficiency_flags = ['high' if d < 3.0 and u > 0.6 else 'low' for d, u in zip(task_durations, resource_usage)]

# Actual execution point that determines answer
final_score = evaluate_performance(metrics, weights)

# Output required result
print(f"Result: {final_score}")