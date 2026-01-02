from collections import defaultdict, Counter

# Simulated system performance metrics over time
timestamps = [100, 105, 110, 115, 120, 125, 130]
raw_data = [
    {'cpu': 70, 'mem': 45, 'disk': 20, 'net_in': 10, 'net_out': 15},
    {'cpu': 85, 'mem': 50, 'disk': 25, 'net_in': 12, 'net_out': 14},
    {'cpu': 90, 'mem': 60, 'disk': 30, 'net_in': 13, 'net_out': 16},
    {'cpu': 87, 'mem': 62, 'disk': 35, 'net_in': 14, 'net_out': 18},
    {'cpu': 75, 'mem': 58, 'disk': 28, 'net_in': 13, 'net_out': 17},
    {'cpu': 65, 'mem': 50, 'disk': 22, 'net_in': 11, 'net_out': 15},
    {'cpu': 72, 'mem': 48, 'disk': 20, 'net_in': 10, 'net_out': 14}
]

# Irrelevant historical thresholds (distractor)
historical_thresholds = defaultdict(lambda: 0)
historical_thresholds.update({'cpu_max': 95, 'mem_max': 80, 'disk_max': 70})

# Weight configuration for scoring (relevant)
weights = {'cpu_efficiency': 0.4, 'memory_stability': 0.3, 'io_balance': 0.2, 'network_consistency': 0.1}

# Derived metrics computation
smoothed_metrics = defaultdict(list)
for entry in raw_data:
    smoothed_metrics['cpu_smooth'].append(entry['cpu'] * 0.9 + 10)
    smoothed_metrics['mem_smooth'].append(entry['mem'] * 0.95)
    smoothed_metrics['disk_io'].append(entry['disk'] * 2)
    smoothed_metrics['net_total'].append(entry['net_in'] + entry['net_out'])

# Dead calculation path - computes variance but not used in final score (red herring)
variance_tracker = defaultdict(float)\nfor key, values in smoothed_metrics.items():
    mean_val = sum(values) / len(values)
    variance_tracker[key] = sum((x - mean_val) ** 2 for x in values) / len(values)

# Decoy function that looks important but is never called (distractor)
def calculate_anomaly_score(data):
    count = 0
    for d in data:
        if d['cpu'] > 80 and d['mem'] > 55:
            count += 1
    return count * 10

# Another decoy - complex bit manipulation with no impact (misleading)
flags = 0b101010
flags = flags ^ 0b111111 & 0b010101 | 0b100000
flag_check = (flags >> 5) & 1

# Real processing: compute efficiency metrics
metrics = {}
cpu_base = [d['cpu'] for d in raw_data]
mem_base = [d['mem'] for d in raw_data]

# CPU efficiency: inverse volatility (lower variation = higher score)
cpu_mean = sum(cpu_base) / len(cpu_base)
cpu_deviation = [abs(x - cpu_mean) for x in cpu_base]
metrics['cpu_efficiency'] = 100 - (sum(cpu_deviation) / len(cpu_deviation))

# Memory stability: penalize increasing trend
increasing_pairs = sum(1 for i in range(1, len(mem_base)) if mem_base[i] > mem_base[i-1])
metrics['memory_stability'] = 100 - (increasing_pairs * 10)

# I/O balance: ratio of disk to network activity
total_disk = sum(d['disk'] for d in raw_data)
total_net = sum(d['net_in'] + d['net_out'] for d in raw_data)
metrics['io_balance'] = 50 + (min(total_disk, total_net) / max(total_disk, total_net) * 50) if total_net > 0 else 50

# Network consistency: low variation in net usage
net_values = [d['net_in'] + d['net_out'] for d in raw_data]
net_mean = sum(net_values) / len(net_values)
net_cv = (sum(abs(x - net_mean) for x in net_values) / len(net_values)) / net_mean
metrics['network_consistency'] = 100 - (net_cv * 100)

# Final weighted evaluation (key statement)
def evaluate_performance(met, w):
    total = 0.0
    for k in met:
        weight_key = k.replace('_', '')
        if 'efficiency' in k:
            total += met[k] * w['cpu_efficiency']
        elif 'stability' in k:
            total += met[k] * w['memory_stability']
        elif 'balance' in k:
            total += met[k] * w['io_balance']
        elif 'consistency' in k:
            total += met[k] * w['network_consistency']
    return total

final_score = evaluate_performance(metrics, weights)

# Misleading secondary result printed to distract (not the answer)
peak_cpu_moment = max(enumerate(cpu_base), key=lambda x: x[1])[0]
temporal_weighted_score = sum(i * val for i, val in enumerate(cpu_base)) / sum(cpu_base)

# Only this line matters for the answer
print(f"Result: {final_score}")