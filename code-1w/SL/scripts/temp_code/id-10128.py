from collections import defaultdict, Counter
import math

# Simulated system telemetry data
timing_log = [
    (100, 'sensor_A', 'read'),
    (150, 'sensor_B', 'write'),
    (200, 'sensor_A', 'read'),
    (250, 'sensor_C', 'error'),
    (300, 'sensor_B', 'read'),
    (350, 'sensor_A', 'write'),
    (400, 'sensor_C', 'read')
]

system_flags = [True, False, True, True, False]

# Irrelevant helper function (decoy)
def analyze_bandwidth(log):
    total = sum(entry[0] for entry in log if 'B' in entry[1])
    avg = total / len(log) if log else 0
    return avg * 0.75

# Unused transformation
decoded_signals = [f'{entry[1][-1]}:{entry[2]}' for entry in timing_log]

# Misleading intermediate calculation
baseline_shift = sum([i * 2 for i, flag in enumerate(system_flags) if not flag])

# Fake error counter (dead code path)
error_counter = 0
for entry in timing_log:
    if entry[2] == 'critical':
        error_counter += 1

# Auxiliary structure with red herring data
flag_stats = defaultdict(int)
for i, flag in enumerate(system_flags):
    flag_stats[f'group_{i % 3}'] += int(flag)

# Distractor: complex string processing (no effect on result)
status_summary = ''.join([
    char for entry in timing_log 
    for char in entry[1] + '_' + entry[2]
])[:len(timing_log)*2]

# Noise injection simulation (unused)
noise_pattern = [math.sin(i * 0.1) for i in range(len(timing_log))]
smoothed_noise = [abs(x) ** 0.5 for x in noise_pattern if x < 0.5]

# Real computation begins here — heavily masked by prior noise
active_sensors = set(entry[1] for entry in timing_log)
sensor_ops = Counter(entry[1] for entry in timing_log)

class DiagnosticEngine:
    def __init__(self, ops_counter, flags):
        self.ops = ops_counter
        self.flags = flags
        self.threshold = 2
    
    def evaluate_stability(self):
        unstable_count = 0
        for sensor_id, count in self.ops.items():
            if count > self.threshold:
                unstable_count += 1
        return unstable_count
    
    def compute_health_score(self):
        # This method is never called — deliberate distraction
        base_score = len(self.ops) * 10
        penalty = sum(1 for f in self.flags if not f) * 5
        return base_score - penalty

# Instantiate but don't immediately use
diag_engine = DiagnosticEngine(sensor_ops, system_flags)

# Another decoy variable
effective_bandwidth = analyze_bandwidth(timing_log)

# Key processing chain obscured by context
op_distribution = {
    op_type: len([e for e in timing_log if e[2] == op_type])
    for op_type in ['read', 'write', 'error']
}

# Critical dependency built silently
consistency_ratio = op_distribution['read'] / (op_distribution['write'] + 1)

# Data transformation via list comprehension (required feature)
filtered_durations = [rec[0] for rec in timing_log if rec[2] != 'error']
avg_duration = sum(filtered_durations) / len(filtered_durations) if filtered_durations else 0

# Final aggregation logic hidden among distractions
def aggregate_metrics(log, flags):
    read_count = sum(1 for e in log if e[2] == 'read')
    write_count = sum(1 for e in log if e[2] == 'write')
    recent_flag_activity = sum(int(f) for f in flags[-3:])
    
    # Core calculation buried in multiple terms
    metric_a = read_count * 17
    metric_b = write_count * 11
    metric_c = recent_flag_activity * 5
    
    # Actual answer derivation
    result = metric_a - metric_b + metric_c
    
    # Red herring return branch (never reached)
    if False and len(log) > 100:
        return sum(e[0] for e in log) // 100
    
    return result

# Execution point of interest
final_diagnostic = aggregate_metrics(timing_log, system_flags)

# Output required format
print(f"Result: {final_diagnostic}")