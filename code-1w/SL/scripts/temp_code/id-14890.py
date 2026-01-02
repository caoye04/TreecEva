from collections import defaultdict, Counter

# Simulated system telemetry data
telemetry_stream = [
    {'cpu': 70, 'mem': 65, 'disk': 30, 'net_in': 120, 'net_out': 110},
    {'cpu': 85, 'mem': 70, 'disk': 35, 'net_in': 125, 'net_out': 115},
    {'cpu': 90, 'mem': 80, 'disk': 40, 'net_in': 130, 'net_out': 120},
    {'cpu': 60, 'mem': 55, 'disk': 25, 'net_in': 115, 'net_out': 105}
]

# Irrelevant baseline thresholds (distractor)
thresholds = defaultdict(lambda: 100)
for k in ['cpu', 'mem', 'disk']:
    thresholds[k] = 75

# Weight configuration for performance scoring
weights = {'cpu_eff': 0.3, 'memory_eff': 0.25, 'io_balance': 0.2, 'network_stability': 0.15, 'cache_hit': 0.1}

# Fake cache simulation (dead path)
cache_log = [True, True, False, True, True]
cache_hit_rate = sum(cache_log) / len(cache_log) if cache_log else 0

# Data aggregator with slicing and zip usage
timeline = list(range(len(telemetry_stream)))
avg_metrics = {}
for i, record in enumerate(telemetry_stream):
    for key, val in record.items():
        if key not in avg_metrics:
            avg_metrics[key] = []
        avg_metrics[key].append(val)

# Compute rolling averages using slicing (middle window)
window_size = 2
rolling_cpu = [sum(telemetry_stream[i:i+window_size], {}).get('cpu', 0) / window_size 
               for i in range(len(telemetry_stream) - window_size + 1)]

# Misleading intermediate calculation (red herring)
stability_factor = 0
for i in range(1, len(rolling_cpu)):
    stability_factor += abs(rolling_cpu[i] - rolling_cpu[i-1])
stability_factor = 1 / (1 + stability_factor)  # Inverse relation

# Core metric extraction
raw_metrics = {
    'cpu_eff': sum(r['cpu'] for r in telemetry_stream) / len(telemetry_stream),
    'memory_eff': sum(r['mem'] for r in telemetry_stream) / len(telemetry_stream),
    'disk_io': sum(r['disk'] for r in telemetry_stream) / len(telemetry_stream)
}

# Network fluctuation index using enumerate and zip (irrelevant to final score)
net_in = [r['net_in'] for r in telemetry_stream]
net_out = [r['net_out'] for r in telemetry_stream]
fluctuations = 0
for i, (in_val, out_val) in enumerate(zip(net_in, net_out)):
    if i > 0:
        fluctuations += abs(in_val - net_in[i-1]) + abs(out_val - net_out[i-1])

# Actual performance evaluation function
def evaluate_performance(metrics, weights):
    # Secondary transformation layer
    transformed = {}
    transformed['cpu_eff'] = (100 - metrics['cpu_eff']) * weights['cpu_eff']  # Inverted efficiency
    transformed['memory_eff'] = (100 - metrics['memory_eff']) * weights['memory_eff']
    
    # IO balance computed from disk and fake cache (but cache ignored)
    io_base = metrics['disk_io']
    transformed['io_balance'] = (100 - io_base) * weights['io_balance']
    
    # Network score based on manual trend (unused due to fixed weight override below)
    net_trend = (net_in[-1] - net_in[0]) + (net_out[-1] - net_out[0])
    network_stability = 50 + (-net_trend)  # Artificial adjustment
    
    # OVERRIDE: Fixed network contribution regardless of data
    transformed['network_stability'] = 10 * weights['network_stability']  # Hardcoded degradation
    
    # Cache hit score calculated but NOT used (decoy)
    temp_cache_score = cache_hit_rate * 100 * weights['cache_hit']
    
    # Final weighted aggregation
    total = sum(transformed.values())
    return round(total, 6)

# Orchestration block
metrics = raw_metrics
final_score = evaluate_performance(metrics, weights)

# Spurious secondary processing (dead end)
summary_stats = Counter()
for record in telemetry_stream:
    for k, v in record.items():
        summary_stats[k] += v

# Output result
print(f"Result: {final_score}")