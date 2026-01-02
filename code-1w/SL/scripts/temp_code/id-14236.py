from collections import defaultdict, Counter
import math

# Simulated system metrics from a distributed network node
metrics = {
    'latency_ms': [120, 85, 95, 200, 75, 130, 90],
    'packet_loss': [0.01, 0.03, 0.02, 0.15, 0.01, 0.04, 0.02],
    'throughput_mbps': [88, 92, 85, 45, 90, 87, 89],
    'retries': [1, 2, 1, 6, 1, 3, 1]
}

# Baseline thresholds for normal operation
baseline = {
    'max_latency': 100,
    'max_loss': 0.05,
    'min_throughput': 80,
    'max_retries': 2
}

# Irrelevant statistical red herring: computes skewness but never used
def calculate_skewness(data):
    n = len(data)
    mean = sum(data) / n
    variance = sum((x - mean) ** 2 for x in data) / n
    if variance == 0:
        return 0.0
    std_dev = math.sqrt(variance)
    skew = sum(((x - mean) / std_dev) ** 3 for x in data) / n
    return round(skew, 4)

# Misleading auxiliary function that looks important but is unused
def analyze_packet_jitter(latency_list):
    jitter = [abs(latency_list[i] - latency_list[i-1]) for i in range(1, len(latency_list))]
    return sum(jitter) / len(jitter) if jitter else 0

# Decoy data structure with plausible but unused metrics
historical_data = defaultdict(list)
historical_data['latency_trend'].extend([110, 95, 102, 88, 94])
historical_data['alert_count'] = 3

# Another decoy: tracks state but not part of final logic
node_status = {}
for node_id in ['N1', 'N2', 'N3']:
    node_status[node_id] = {'active': True, 'last_seen': 1623456789}

# Distractor: complex-looking transformation with no downstream effect
aggregated_metrics = [
    (lat, thr, pkt * 100) 
    for lat, thr, pkt in zip(
        metrics['latency_ms'], 
        metrics['throughput_mbps'], 
        metrics['packet_loss']
    ) if thr > 50
]

# Unused list comprehension that appears to preprocess data
filtered_by_loss = [
    (idx, val) for idx, val in enumerate(metrics['packet_loss']) if val < 0.03
]

# Real logic begins: count how many readings exceed baseline thresholds
exceedance_count = defaultdict(int)
for key, values in metrics.items():
    threshold_key = f"max_{key}".replace('max_retries', 'max_retries')  # simulate dynamic key
    if key == 'latency_ms':
        for v in values:
            if v > baseline['max_latency']:
                exceedance_count['latency'] += 1
    elif key == 'packet_loss':
        for v in values:
            if v > baseline['max_loss']:
                exceedance_count['loss'] += 1
    elif key == 'throughput_mbps':
        for v in values:
            if v < baseline['min_throughput']:
                exceedance_count['throughput'] += 1
    elif key == 'retries':
        for v in values:
            if v > baseline['max_retries']:
                exceedance_count['retries'] += 1

# Secondary distraction: builds a frequency map that isn't used later
loss_frequency = Counter(metrics['packet_loss'])
high_retry_indices = [i for i, r in enumerate(metrics['retries']) if r > 2]

# Core evaluation logic — depends only on total_exceedances
total_exceedances = sum(exceedance_count.values())

# Simulate weighted scoring with dummy components
base_penalty = total_exceedances * 15
adaptive_factor = 1.0
if total_exceedances > 10:
    adaptive_factor = 0.8
elif total_exceedances > 5:
    adaptive_factor = 0.9

# Introduce fake normalization path
normalization_shift = math.log(total_exceedances + 1, 2) if total_exceedances > 0 else 0
fake_adjustment = (normalization_shift * 5) // 1  # Looks meaningful, not actually impactful

# Final score calculation — this is the actual answer path
raw_score = 100 - base_penalty
final_score = int(raw_score * adaptive_factor)

# Print result as required
print(f"Result: {final_score}")