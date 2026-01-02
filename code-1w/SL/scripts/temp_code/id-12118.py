def analyze_system_load(loads, threshold=75):
    # Irrelevant helper function (dead code path)
    return sum(1 for load in loads if load > threshold)

# Simulated system log entry with timestamp and metrics
class LogEntry:
    def __init__(self, ts, cpu, mem, disk, net):
        self.timestamp = ts
        self.cpu_usage = cpu
        self.memory_usage = mem
        self.disk_io = disk
        self.network_activity = net

# Misleading auxiliary computation
redundant_scaling_factor = 0.87
normalization_offset = 42

# Real system thresholds (used later)
system_thresholds = {
    'cpu': 80,
    'memory': 85,
    'disk_write': 200,
    'latency_spike': 150
}

# Distractor dictionary with unused keys
diagnostic_weights = {
    'cpu': 0.35,
    'mem': 0.25,
    'disk': 0.20,
    'network': 0.10,
    'bandwidth': 0.05,  # Unused red herring
    'power_draw': 0.05   # Another decoy
}

# Simulated log entries over time
log_entries = [
    LogEntry(1001, 78, 82, 180, 110),
    LogEntry(1002, 83, 86, 195, 115),
    LogEntry(1003, 81, 83, 210, 120),
    LogEntry(1004, 79, 80, 190, 125),
    LogEntry(1005, 85, 88, 220, 130)
]

# Fake aggregation (never used)
total_bandwidth_score = 0
for entry in log_entries:
    total_bandwidth_score += entry.network_activity * 0.01

# Decoy list comprehension with side effects (no side effect actually)
_ = [entry.disk_io ** 2 for entry in log_entries if entry.cpu_usage > 90]  # No such entry

# Core processing function that actually matters
def compute_health_vector(entries, config):
    anomalies = 0
    cumulative_score = 0.0
    recent_spikes = []

    for idx, entry in enumerate(entries):
        # Check multiple conditions using complex logic
        cpu_high = entry.cpu_usage > config['cpu']
        mem_high = entry.memory_usage > config['memory']
        disk_peak = entry.disk_io > config['disk_write']

        # Logical combination with short-circuit evaluation
        if cpu_high and mem_high or disk_peak:
            anomalies += 1
            # Weighted anomaly score
            spike_score = (
                (entry.cpu_usage - config['cpu']) * 1.2 +
                (entry.memory_usage - config['memory']) * 1.1 +
                (entry.disk_io - config['disk_write']) * 0.8
            )
            recent_spikes.append(spike_score)

        # Use of zip to align with dummy indices
        dummy_indices = list(range(len(entries)))
        for i, (e, di) in enumerate(zip(entries, dummy_indices)):
            if i == idx and e.timestamp % 2 == 0:
                cumulative_score += 0.1  # Rare case, minor red herring

    # Real contribution: average spike severity only if anomalies exist
    avg_severity = sum(recent_spikes) / len(recent_spikes) if recent_spikes else 0.0
    
    # Final vector includes count and severity
    return anomalies, avg_severity

# Higher-order function with lambda (actual usage)
build_diagnostic = lambda vec: (vec[0] * 100) + round(vec[1] * 10)  # Mapping to integer metric

# Unused recursive attempt (distractor)
def predict_failure_risk(level, depth=3):
    if depth == 0:
        return level
    return predict_failure_risk(level * 1.1 + 5, depth - 1)

# Actual key processing pipeline
def process_metrics(logs, thresholds):
    # Intermediate transformation
    raw_data = [(e.cpu_usage, e.memory_usage, e.disk_io) for e in logs]
    
    # Spurious bit manipulation (looks important but isn't used in final result)
    bit_fiddled = 0
    for d in raw_data:
        bit_fiddled ^= (d[0] << 2) | (d[1] & 0x7F)  # Complex but irrelevant
    
    # Real work happens here
    health_vec = compute_health_vector(logs, thresholds)
    diagnostic_code = build_diagnostic(health_vec)
    
    # Additional check: if more than 2 anomalies, apply bonus degradation
    if health_vec[0] > 2:
        diagnostic_code += 50
    
    # Final adjustment based on hidden pattern (every third entry has high disk IO)
    third_entry_disk = logs[2].disk_io  # 210
    if third_entry_disk > 200:
        diagnostic_code += 17

    return diagnostic_code

# Critical execution point
final_diagnostic = process_metrics(log_entries, system_thresholds)

# Print result as required
print(f"Result: {final_diagnostic}")