def analyze_access_patterns(logs):
    # Irrelevant function analyzing access patterns (dead end)
    stats = {}
    for entry in logs:
        ip = entry.split()[0]
        stats[ip] = stats.get(ip, 0) + 1
    return {k: v for k, v in stats.items() if v > 1}


def validate_checksum(data):
    # Distractor: computes a checksum but not used in final result
    chk = 0
    for d in data:
        chk ^= hash(str(d)) % 256
    return chk % 100 == 42

# Simulated system log entries with mixed content
log_entries = [
    "192.168.1.10 START task_78A",
    "10.0.0.5 UPDATE priority=high",
    "192.168.1.10 END task_78A",
    "172.16.3.9 INIT buffer_reset",
    "10.0.0.5 START task_99X",
    "192.168.1.10 START task_42B"
]

# User engagement metrics across modules
user_metrics = [
    {'module': 'auth', 'attempts': 12, 'success': 9, 'latency': [120, 145, 130, 118]},
    {'module': 'storage', 'attempts': 8, 'success': 6, 'latency': [210, 195, 220]},
    {'module': 'compute', 'attempts': 15, 'success': 14, 'latency': [95, 102, 99, 105, 97]},
    {'module': 'network', 'attempts': 10, 'success': 7, 'latency': [310, 290]}  # Lower success rate
]

# Irrelevant global tracking variables
system_uptime = 43200
active_sessions = 23
config_flags = [0x1A, 0x3F, 0x0C]

# Auxiliary function that appears important but only partially contributes
def compute_module_weight(module_data):
    base = module_data['success'] / module_data['attempts']
    delay_factor = sum(module_data['latency']) / len(module_data['latency'])
    penalty = 0.1 if delay_factor > 200 else 0
    return round(base - penalty, 3)

# Core aggregation logic with meaningful computation buried in noise
valid_modules = set()
for record in user_metrics:
    if record['success'] >= 5:
        valid_modules.add(record['module'])

# Misleading intermediate calculation using enumerate and zip (mostly red herring)
temp_analysis = []
for i, (log, metric) in enumerate(zip(log_entries, user_metrics)):
    access_count = len([l for l in log_entries if l.startswith(f"192.168")])
    score_hint = (i + 1) * metric['attempts'] // (metric['success'] + 1)
    temp_analysis.append((i, access_count, score_hint))

# Real processing begins here — non-obvious due to distractions above
def aggregate_performance(logs, metrics):
    # Extract task start events from logs
    task_starts = [line for line in logs if "START" in line]
    task_ids = [line.split()[2] for line in task_starts]
    
    # Use set operations to filter unique active tasks
    task_prefixes = {tid.split('_')[0] for tid in task_ids}  # {'task'}
    numeric_ids = [int(tid.split('_')[1][:-1]) for tid in task_ids]  # [78, 42]
    
    # Actual signal: sum of odd-positioned numeric IDs
    raw_sum = sum(num for idx, num in enumerate(numeric_ids) if idx % 2 == 0)
    
    # Combine with weighted success rate from valid modules
    total_weight = 0.0
    for m in metrics:
        if m['module'] in valid_modules:
            total_weight += compute_module_weight(m)
    
    # Final score combines both code paths — only one correct interpretation
    scaling_factor = len(task_starts)  # 3 starts
    final_component = raw_sum * scaling_factor
    adjustment = int(total_weight * 100)
    
    # Key assignment point
    final_score = final_component + adjustment
    
    # Dead code branch — looks relevant but never executed
    if validate_checksum(config_flags):
        final_score -= 1000
    
    return final_score

# Execute core logic
final_score = aggregate_performance(log_entries, user_metrics)

# Print result as required
print(f"Target result: {final_score}")