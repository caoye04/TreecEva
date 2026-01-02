from collections import defaultdict
from itertools import zip_longest

# Simulate system telemetry data
telemetry_stream = [
    {'cpu': 75, 'mem': 60, 'disk': 200, 'net_in': 45, 'net_out': 60},
    {'cpu': 80, 'mem': 62, 'disk': 180, 'net_in': 50, 'net_out': 65},
    {'cpu': 90, 'mem': 75, 'disk': 150, 'net_in': 55, 'net_out': 70},
    {'cpu': 95, 'mem': 85, 'disk': 130, 'net_in': 60, 'net_out': 80}
]

# Irrelevant baseline thresholds (distractor)
thresholds = defaultdict(lambda: 100)
thresholds.update({'cpu': 92, 'mem': 88, 'disk': 140})

# Weight configuration for scoring (critical)
weights = {'efficiency': 0.4, 'throughput': 0.35, 'stability': 0.25}

# Auxiliary function to compute rolling average (partially relevant)
def smooth_signal(values, window=2):
    smoothed = []
    for i in range(len(values)):
        start = max(0, i - window + 1)
        smoothed.append(sum(values[start:i+1]) / (i - start + 1))
    return smoothed

# Helper to detect spikes (distractor - not used in final score)
def count_spikes(data_list, threshold=10):
    return sum(1 for i in range(1, len(data_list)) if abs(data_list[i] - data_list[i-1]) > threshold)

# Extract time-series metrics (relevant)
cpu_load = [entry['cpu'] for entry in telemetry_stream]
memory_usage = [entry['mem'] for entry in telemetry_stream]
disk_io = [entry['disk'] for entry in telemetry_stream]

# Compute derived features (some irrelevant)
avg_cpu = sum(cpu_load) / len(cpu_load)
peak_memory = max(memory_usage)
total_io = sum(disk_io)

# Smoothed signals (only one will be used)
smoothed_cpu = smooth_signal(cpu_load)
smoothed_mem = smooth_signal(memory_usage)
smoothed_disk = smooth_signal(disk_io)  # Unused distractor

# Spike analysis (completely irrelevant to final result)
cpu_spike_count = count_spikes(cpu_load)
mem_spike_count = count_spikes(memory_usage, threshold=5)

# Performance metric computation
metric_data = {}

# Efficiency: based on inverse of average CPU load (normalized)
efficiency = (100 - avg_cpu) / 100

# Throughput: decreasing trend in disk IO is bad
io_trend = sum(disk_io[i] - disk_io[i+1] for i in range(len(disk_io)-1))
throughput = min(1.0, max(0.0, io_trend / 200))

# Stability: measured by low variation in smoothed CPU
variance = sum((x - avg_cpu)**2 for x in smoothed_cpu) / len(smoothed_cpu)
stability = 1 - (variance / 100)

metric_data['efficiency'] = efficiency
metric_data['throughput'] = throughput
metric_data['stability'] = stability

# Misleading alternative calculation (dead path)
if len(telemetry_stream) > 5:
    fallback_score = sum(efficiency * 2 for _ in range(3))
else:
    temp_weights = [0.5, 0.3, 0.2]
    # This block runs but doesn't contribute
    debug_values = list(zip_longest([efficiency], [throughput], [stability], fillvalue=0))

# Final evaluation function
def evaluate_performance(metrics, weight_dict):
    raw_score = 0.0
    for key, weight in weight_dict.items():
        if key in metrics:
            raw_score += metrics[key] * weight
    
    # Apply artificial ceiling and floor
    bounded_score = max(0.0, min(1.0, raw_score))
    
    # Convert to scaled integer score
    return int(bounded_score * 1000)

# Execute critical statement
final_score = evaluate_performance(metric_data, weights)

# Print result as required
print(f"Result: {final_score}")