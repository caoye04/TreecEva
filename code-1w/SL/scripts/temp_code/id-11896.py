from collections import defaultdict, Counter
import math

# Simulated system telemetry data
timestamps = [1623456780, 1623456785, 1623456790, 1623456795, 1623456800]
cpu_loads = [0.78, 0.82, 0.91, 0.88, 0.76]
memory_usage = [0.65, 0.71, 0.79, 0.85, 0.82]
disk_iops = [120, 135, 110, 140, 130]

# Auxiliary irrelevant metrics (distractors)
network_latency_ms = [23.5, 25.1, 24.8, 26.3, 27.0]  # Not used in final calculation
gpu_temp_c = [68, 70, 72, 71, 69]  # Dead code path
packet_loss_rate = [0.001, 0.002, 0.001, 0.003, 0.001]  # Unused

# System thresholds and weights
system_thresholds = {
    'cpu': 0.85,
    'memory': 0.80,
    'disk': 125
}

weight_map = defaultdict(float)
weight_map.update({'cpu': 0.5, 'memory': 0.3, 'disk': 0.2})

# Irrelevant security policy rules (red herring)
security_policy = {
    'min_password_length': 12,
    'session_timeout_minutes': 30,
    'max_login_attempts': 3
}

# Log entry structure
class LogEntry:
    def __init__(self, ts, cpu, mem, disk, lat=None):
        self.timestamp = ts
        self.cpu_util = cpu
        self.memory_util = mem
        self.disk_iops = disk
        self.latency = lat
        self.anomaly_score = 0.0

    def calculate_health_index(self):
        # Misleading intermediate score
        return (self.cpu_util * 100) + (self.memory_util * 80)

# Generate log entries
log_entries = []
for i, t in enumerate(timestamps):
    entry = LogEntry(t, cpu_loads[i], memory_usage[i], disk_iops[i], network_latency_ms[i])
    log_entries.append(entry)

# Decoy function: appears useful but unused in critical path
def compute_entropy(data):
    counts = Counter(data)
    total = len(data)
    return -sum((count / total) * math.log2(count / total) for count in counts.values())

# Auxiliary transformation with partial relevance
transformed_metrics = []
for idx, (entry, disk_op) in enumerate(zip(log_entries, disk_iops)):
    metric_bundle = {
        'index': idx,
        'timestamp': entry.timestamp,
        'load_product': entry.cpu_util * entry.memory_util,
        'iops_deviation': abs(disk_op - 125),
        'temporal_weight': math.cos(idx * math.pi / 4)  # Oscillating weight (distractor)
    }
    transformed_metrics.append(metric_bundle)

# Secondary processing: some results are filtered out
recent_logs = [e for e in log_entries if e.timestamp >= 1623456790]

# Core diagnostic engine
alert_flags = []
cumulative_risk = 0.0
baseline_ref = {'cpu': [], 'mem': [], 'disk': []}

for entry in recent_logs:
    # Track baseline (only for later unused analysis)
    baseline_ref['cpu'].append(entry.cpu_util)
    baseline_ref['memory'].append(entry.memory_util)
    baseline_ref['disk'].append(entry.disk_iops)
    
    # Actual alert logic
    risk_score = 0.0
    if entry.cpu_util > system_thresholds['cpu']:
        risk_score += weight_map['cpu'] * (entry.cpu_util - system_thresholds['cpu'])
    if entry.memory_util > system_thresholds['memory']:
        risk_score += weight_map['memory'] * (entry.memory_util - system_thresholds['memory'])
    if entry.disk_iops < system_thresholds['disk']:
        risk_score += weight_map['disk'] * (system_thresholds['disk'] - entry.disk_iops) * 0.01
    
    entry.anomaly_score = round(risk_score, 4)
    alert_flags.append(risk_score > 0)
    cumulative_risk += risk_score

# Spurious correlation check (dead code path)
correlation_proxy = 0.0
for i in range(1, len(cpu_loads)):
    if cpu_loads[i] > cpu_loads[i-1] and memory_usage[i] < memory_usage[i-1]:
        correlation_proxy += 0.1

# Final aggregation and decision engine
def process_metrics(logs, thresholds):
    # Unused statistical summary (distractor)
    stats_summary = {
        'total_entries': len(logs),
        'peak_cpu': max(e.cpu_util for e in logs),
        'avg_iops': sum(e.disk_iops for e in logs) / len(logs)
    }
    
    # Relevant computation: weighted anomaly integration
    valid_logs = [e for e in logs if e.timestamp >= 1623456790]  # Filter applied again
    
    # Compute composite diagnostic using only anomaly scores
    raw_scores = [e.anomaly_score for e in valid_logs]
    
    # Apply exponential backoff weighting based on recency
    weights = [math.exp(i * 0.1) for i in range(len(raw_scores))]
    weighted_sum = sum(score * w for score, w in zip(raw_scores, weights))
    total_weight = sum(weights)
    
    # Final diagnostic index
    diagnostic_index = weighted_sum / total_weight if total_weight > 0 else 0.0
    
    # Additional correction based on trend
    if len(raw_scores) >= 3:
        trend = (raw_scores[-1] - raw_scores[0]) * 100
        if trend > 0:
            diagnostic_index *= 1.1
    
    return round(diagnostic_index, 6)

# Execute main processing
final_diagnostic = process_metrics(log_entries, system_thresholds)

# Diagnostic output (do not modify)
print(f"Result: {final_diagnostic}")