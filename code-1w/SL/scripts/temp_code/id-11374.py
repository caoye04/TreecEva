from collections import defaultdict, Counter
import itertools

# Simulated system metrics from a distributed logging framework
timestamps = [1623456000 + i*300 for i in range(20)]
raw_logs = [
    'INFO: Task completed successfully',
    'WARN: Memory usage high',
    'ERROR: Failed to connect',
    'INFO: Retrying connection',
    'DEBUG: Retry attempt 1',
    'INFO: Connection restored',
    'INFO: Processing batch',
    'WARN: Latency spike detected',
    'INFO: Batch processed',
    'INFO: System stable'
] * 2

# Irrelevant auxiliary mapping (distractor)
status_weights = {'INFO': 1, 'WARN': 3, 'ERROR': 5, 'DEBUG': 0}

# Misleading aggregation path (dead code)
def legacy_aggregate(logs):
    count = 0
    for log in logs:
        if 'ERROR' in log and 'CRITICAL' not in log:
            count += 2
    return count * 1.5

# Unused transformation function (red herring)
def transform_timestamps(ts_list):
    return [t % 86400 // 60 for t in ts_list]  # minutes since midnight

# Decoy statistical analyzer (never called)
class MetricsAnalyzer:
    def __init__(self, window=5):
        self.window = window
        self.history = []
    
    def analyze_trend(self, values):
        if len(values) < self.window:
            return 0
        recent = values[-self.window:]
        return sum(recent) / len(recent)

# Fake normalization logic with no impact (distractor)
bogus_factors = [0.98, 1.02, 0.99, 1.01, 0.97]
normalized_weights = {k: v * 1.1 for k, v in status_weights.items()}
adjusted_scores = [wf * 1.05 for wf in bogus_factors]

# Real data processing begins here
log_levels = [log.split(':')[0] for log in raw_logs]
level_counts = Counter(log_levels)

# Secondary distraction: unused combinatorics
pairwise_combinations = list(itertools.combinations_with_replacement(['INFO','WARN'], 3))
combination_filter = [c for c in pairwise_combinations if 'WARN' in c]
filter_sum = sum(len(c) for c in combination_filter)  # unused

# Construct metric data with some relevant transformations
metric_data = defaultdict(float)
for level, count in level_counts.items():
    if level == 'INFO':
        metric_data['success_rate'] += count * 0.8
    elif level == 'WARN':
        metric_data['warning_density'] += count * 1.2
    elif level == 'ERROR':
        metric_data['error_frequency'] += count * 2.5

# Additional irrelevant calculation (misdirection)
rolling_averages = []
for i in range(1, len(timestamps)):
    diff = timestamps[i] - timestamps[i-1]
    rolling_averages.append(diff / 60.0)
mean_interval = sum(rolling_averages) / len(rolling_averages) if rolling_averages else 0

# Base threshold computed from partial real logic mixed with noise
base_components = [level_counts.get('INFO', 0), level_counts.get('WARN', 0)]
noise_offset = len([t for t in raw_logs if 'DEBUG' in t]) * 0.1
base_threshold = (base_components[0] * 0.7 + base_components[1] * 0.3) + noise_offset

# Core evaluation logic buried among distractions
def evaluate_performance(metrics, threshold):
    score = 0
    # Real scoring logic
    if metrics['success_rate'] > threshold:
        score += int(metrics['success_rate'] - threshold)
    if metrics['warning_density'] > 10:
        score -= int(metrics['warning_density'] // 2)
    if metrics['error_frequency'] > 0:
        score -= int(metrics['error_frequency'] * 3)
    
    # Artificial complexity: bitwise adjustment
    temp = score ^ 256  # flip high byte
    temp = temp & 511     # clamp to 9 bits
    if temp > 256:
        temp -= 512      # signed interpretation
    final = abs(temp) ^ 128  # another transformation
    
    # Final adjustment based on logical condition chain
    flags = [
        metrics['success_rate'] > 10,
        metrics['warning_density'] < 15,
        metrics['error_frequency'] == 0
    ]
    if all(flags):
        final *= 1.25
    elif any(flags) and not all(flags):
        final *= 0.9
    else:
        final *= 0.75
    
    return round(final, 4)

# Critical execution point
final_score = evaluate_performance(metric_data, base_threshold)

# Irrelevant post-processing block (dead code path)
if final_score < 0:
    recovery_attempts = 3
    while recovery_attempts > 0:
        final_score += 10
        recovery_attempts -= 1

# Unused diagnostic output (distraction)
diagnostic_report = {
    'entries': len(raw_logs),
    'unique_levels': len(level_counts),
    'peak_warnings': max([level_counts.get('WARN', 0)]),
    'system_uptime': timestamps[-1] - timestamps[0]
}

# Actual output
print(f"Target result: {final_score}")