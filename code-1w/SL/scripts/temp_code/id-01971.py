import math

# Simulated system telemetry data
technical_metrics = {
    'latency_ms': [120, 85, 93, 110, 97],
    'packet_loss': [0.002, 0.003, 0.001, 0.004, 0.002],
    'jitter': [5, 8, 6, 7, 5],
    'throughput_mbps': [890, 920, 870, 940, 910]
}

# Irrelevant historical reference data (distractor)
historical_baselines = [
    {'year': 2018, 'score': 76.2},
    {'year': 2019, 'score': 78.1},
    {'year': 2020, 'score': 77.5}
]

# Misleading auxiliary function (dead path)
def compute_legacy_metric(data):
    return sum(data) / len(data) * 0.85

# Decoy transformation (not used in final logic)
transformed = list(map(lambda x: x * 1.05, technical_metrics['latency_ms']))

# Spurious intermediate calculation (red herring)
avg_packet_loss = sum(technical_metrics['packet_loss']) / len(technical_metrics['packet_loss'])
adjusted_loss = avg_packet_loss * 100000

# Unused complex structure (distractor)
class PerformanceModel:
    def __init__(self, weight):
        self.weight = weight
    
    def predict(self, x):
        return x * self.weight

model = PerformanceModel(0.9)

# Fake normalization attempt (irrelevant)
normalized_throughput = [x / 1000 for x in technical_metrics['throughput_mbps']]

# Real processing begins here — nested logic with distractors
baseline = {
    'target_latency': 100,
    'max_jitter': 6,
    'min_throughput': 900
}

# Secondary metric computed but only conditionally relevant
reliability_index = 100
for loss in technical_metrics['packet_loss']:
    if loss > 0.0025:
        reliability_index -= 5

# Auxiliary scoring function with red herrings
compute_weight = lambda x, y: (x / y) if y != 0 else 0

# Core evaluation logic buried among noise
def evaluate_latency(latency_list, target):
    count_below = 0
    total = 0
    for val in latency_list:
        total += val
        if val <= target:
            count_below += 1
    average = total / len(latency_list)
    hit_rate = count_below / len(latency_list)
    # Weighted score combining average and consistency
    return (average * 0.6) + (hit_rate * 40)

# Another decoy function (never called)
def analyze_trend(data):
    diff = [data[i+1] - data[i] for i in range(len(data)-1)]
    return sum(diff) / len(diff)

# Bit manipulation distraction (unrelated to main logic)
status_flag = 0b101010
mask = 0b111100
masked_status = status_flag & mask
shifted = masked_status >> 2

# Main evaluation function — contains key logic
metric_data = {}
def evaluate_performance(metrics, base):
    # Step 1: Latency score
    raw_latency_score = evaluate_latency(metrics['latency_ms'], base['target_latency'])
    
    # Step 2: Jitter penalty
    excessive_jitter_periods = 0
    for j in metrics['jitter']:
        if j > base['max_jitter']:
            excessive_jitter_periods += 1
    jitter_penalty = excessive_jitter_periods * 3.5
    
    # Step 3: Throughput bonus
    above_threshold = 0
    for t in metrics['throughput_mbps']:
        if t >= base['min_throughput']:
            above_threshold += 1
    throughput_bonus = above_threshold * 2.1
    
    # Step 4: Combine scores with hidden weights
    base_score = 100 - raw_latency_score  # Invert since lower latency is better
    adjusted_score = base_score - jitter_penalty + throughput_bonus
    
    # Hidden rounding rule (integer division)
    final_int_score = int(adjusted_score)  # truncates toward zero
    
    # Apply subtle correction based on reliability index (only if high)
    if reliability_index >= 90:
        final_int_score += 1
    
    # Critical line — this is where final_score is assigned
    return final_int_score

# Unused list comprehension (distractor)
doubled_jitter = [j*2 for j in technical_metrics['jitter'] if j > 5]

# Initialization of metric_data (simulates ETL process)
metric_data['latency_ms'] = technical_metrics['latency_ms']
metric_data['jitter'] = technical_metrics['jitter']
metric_data['throughput_mbps'] = technical_metrics['throughput_mbps']

# Key assignment statement — answer depends on this execution
final_score = evaluate_performance(metric_data, baseline)

# Print result as required
print(f"Result: {final_score}")