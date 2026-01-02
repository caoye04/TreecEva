from collections import defaultdict, Counter
import math

# Simulated system telemetry data
timestamps = [1623456780, 1623456789, 1623456795, 1623456802, 1623456810]
raw_logs = [
    'INFO: cpu_load=0.75, temp=68, fan_speed=2000',
    'WARN: cpu_load=0.88, temp=75, fan_speed=2800',
    'INFO: cpu_load=0.65, temp=70, fan_speed=2200',
    'CRIT: cpu_load=0.95, temp=85, fan_speed=3500',
    'INFO: cpu_load=0.70, temp=72, fan_speed=2400'
]

# Irrelevant preprocessing - red herring
hash_mapping = {i: hash(str(t) + str(i)) % 10000 for i, t in enumerate(timestamps)}
decoy_values = [abs(hash_mapping[i] - hash(raw_logs[i]) % 1000) for i in range(len(raw_logs))]
shadow_buffer = list(map(lambda x: (x * 17) % 997, decoy_values))

# Real data extraction
log_entries = []
for log in raw_logs:
    parts = log.split(': ', 1)[1].split(', ')
    entry = {}
    for part in parts:
        k, v = part.split('=')
        entry[k] = float(v)
    log_entries.append(entry)

# System state with multiple decoy fields
system_state = {
    'uptime': 43200,
    'version': 'v2.7.1',
    'mode': 'performance',
    'cache_size_mb': 512,
    'security_level': 3,
    'last_backup': 1623440000,
    'network_latency_ms': 45,
    'power_cycles': 127,
    'thermal_threshold': 80,
    'overclock_enabled': False
}

# Distractor function - never called but looks important
def analyze_failure_risk(entries, state):
    critical_count = sum(1 for e in entries if e['cpu_load'] > 0.9)
    max_temp = max(e['temp'] for e in entries)
    return (critical_count * 100) + (max_temp - 70)

# Another decoy - unused transformation
temp_history = [e['temp'] for e in log_entries]
trend_score = sum(temp_history[i] < temp_history[i+1] for i in range(len(temp_history)-1))

# Real processing begins here
health_counters = defaultdict(int)
load_samples = []
fan_efficiency = []

for entry in log_entries:
    cpu = entry['cpu_load']
    temp = entry['temp']
    fan = entry['fan_speed']
    
    if cpu > 0.8:
        health_counters['high_cpu'] += 1
    if temp > 75:
        health_counters['high_temp'] += 1
    
    load_samples.append(cpu)
    fan_efficiency.append(fan / (temp + 1) if temp > 0 else 0)

# Secondary distractor: complex unused calculation
entropy_metric = 0.0
if len(load_samples) > 1:
    mean_load = sum(load_samples) / len(load_samples)
    variance = sum((x - mean_load) ** 2 for x in load_samples) / len(load_samples)
    entropy_metric = math.log(variance + 1) if variance > 0 else 0

# Decoy data structure
anomaly_matrix = [[0 for _ in range(3)] for _ in range(3)]
for i, e in enumerate(log_entries):
    idx = int(e['cpu_load'] * 2)
    jdx = int(e['temp'] // 20)
    if idx < 3 and jdx < 3:
        anomaly_matrix[idx][jdx] += 1

# Core logic embedded within distractions
def evaluate_stability(metrics_list):
    weights = {'cpu_load': 0.6, 'temp': 0.3, 'fan_speed': 0.1}
    scores = []
    for m in metrics_list:
        raw_score = (m['cpu_load'] * weights['cpu_load'] + 
                   (m['temp'] / 100) * weights['temp'] + 
                   (1 - m['fan_speed'] / 4000) * weights['fan_speed'])
        scores.append(100 * (1 - raw_score))
    return sum(scores) / len(scores)

baseline_performance = evaluate_stability(log_entries)

# Misleading intermediate - looks like threshold check but not final
stability_flag = 'STABLE' if baseline_performance > 65 else 'UNSTABLE'

# Actual target computation path
def process_metrics(entries, state):
    # Extract meaningful features
    cpu_vals = [e['cpu_load'] for e in entries]
    temp_vals = [e['temp'] for e in entries]
    
    # Compute derived indicators
    avg_cpu = sum(cpu_vals) / len(cpu_vals)
    max_temp = max(temp_vals)
    temp_exceeds = sum(1 for t in temp_vals if t > state['thermal_threshold'])
    
    # Efficiency ratio with bit manipulation red herring
    speed_sum = sum(e['fan_speed'] for e in entries)
    bit_mask = 0b1111  # Unused bitwise distraction
    masked_speed = speed_sum & bit_mask  # Computed but irrelevant
    
    # Real formula
    diagnostic_weight = 1.0
    if state['mode'] == 'performance':
        diagnostic_weight += 0.25
    if temp_exceeds > 0:
        diagnostic_weight += 0.4 * temp_exceeds
    
    base_diagnostic = (avg_cpu * 1000) + (max_temp * 10) - (masked_speed * 0.5)
    final_value = int(base_diagnostic * diagnostic_weight)
    
    # Additional distraction: unused conditional branch
    if final_value > 1000 and state['overclock_enabled']:
        adjustment = state['power_cycles'] % 7
        final_value -= adjustment  # Never executed due to overclock_enabled=False
    
    return final_value

# Key execution point
final_diagnostic = process_metrics(log_entries, system_state)

# Print result as required
print(f"Target result: {final_diagnostic}")