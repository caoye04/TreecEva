from collections import defaultdict, Counter
import math

# Simulated sensor data feed (irrelevant but plausible)
sensor_readings = [1024, 2048, 512, 3072, 1536, 768, 4096]
filtered_sensors = [x for x in sensor_readings if x > 1000]

# Irrelevant auxiliary function (decoy)
def analyze_health(logs):
    if not logs:
        return False
    avg_load = sum(logs) / len(logs)
    return avg_load < 2000

# Unused data structures (distractors)
system_status = {'active': True, 'mode': 'debug', 'version': '2.1.9'}
temp_cache = defaultdict(int)
for i in range(5):
    temp_cache[f'key_{i}'] += i * 10

# Core performance metrics (relevant data)
metric_data = {
    'latency': [120, 145, 130, 155, 110],
    'throughput': [85, 90, 88, 92, 87],
    'retries': [3, 1, 4, 0, 2]
}

# Misleading intermediate calculation (red herring)
baseline_efficiency = 0.0
for val in metric_data['latency']:
    baseline_efficiency += 1 / val
baseline_efficiency = round(baseline_efficiency, 3)  # Used nowhere

# Decoy transformation (dead path)
transformed = []
for t in metric_data['throughput']:
    transformed.append(math.log(t ** 1.5))

# Real processing begins here
latency_weighted = 0
for i, lat in enumerate(metric_data['latency']):
    latency_weighted += lat * (0.5 ** i)  # Exponential decay weighting

throughput_avg = sum(metric_data['throughput']) / len(metric_data['throughput'])
retry_penalty = sum([r * 10 for r in metric_data['retries']])

# Bit manipulation distraction (irrelevant)
flag = 0b101010
mask = 0b111100
masked_flag = flag & mask
shifted = masked_flag << 2

# Another decoy: unused dictionary aggregation
diagnostic_stats = Counter()
for key, values in metric_data.items():
    diagnostic_stats[key] = len(values)

# Conditional red herring with unreachable logic impact
adjustment_factor = 1.0
if len(metric_data['retries']) > 10:  # Never true
    adjustment_factor = 0.9
elif baseline_efficiency > 0.04:  # Looks relevant but isn't used correctly
    adjustment_factor = 1.1

# Actual core logic (non-obvious due to noise)
effective_latency = 1000 / latency_weighted  # Inverse relationship
effective_throughput = throughput_avg * 10
raw_score = effective_latency + effective_throughput - retry_penalty

# Final evaluation using dictionary lookup and arithmetic
scaling_map = {0: 1.0, 1: 1.2, 2: 1.4, 3: 1.6, 4: 1.8}
scale = scaling_map.get(len(metric_data['retries']) - 1, 1.0)

final_score = raw_score * scale  # Key statement

print(f"Result: {final_score}")