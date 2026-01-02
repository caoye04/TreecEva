from collections import defaultdict, Counter
import math

# Simulated system metrics from a distributed network node
metrics = {
    'latency_ms': [120, 85, 93, 110, 97, 104],
    'packet_loss': [0.02, 0.01, 0.03, 0.00, 0.02, 0.05],
    'throughput_mbps': [89, 94, 87, 95, 91, 83],
    'retries': [1, 0, 2, 0, 1, 3],
    'jitter_ms': [5, 7, 6, 8, 4, 9]
}

# Baseline thresholds for normal operation
baseline = {
    'latency_threshold': 100,
    'loss_tolerance': 0.025,
    'min_throughput': 85,
    'max_retries': 2
}

# Irrelevant helper (decoy)
def calculate_fft(signal):
    # Unused in logic - red herring
    n = len(signal)
    if n <= 1: return signal
    even = calculate_fft(signal[0::2])
    odd = calculate_fft(signal[1::2])
    return [even[i] + odd[i] * complex(0, -2*math.pi*i/n) for i in range(n//2)]

# Misleading transformation (not used in final path)
temp_transform = lambda x: sum([math.log(y + 1) for y in x if y > 0])
transformed_latency = temp_transform(metrics['latency_ms'])  # Distractor

# Decoy data structure
decoy_stats = defaultdict(int)
for val in metrics['packet_loss']:
    if val > 0.01:
        decoy_stats['high_loss_count'] += 1
    else:
        decoy_stats['low_loss_count'] += 1

# Unused recursive function (dead code path)
def count_above_threshold(data, threshold, idx=0):
    if idx == len(data):
        return 0
    count = 1 if data[idx] > threshold else 0
    return count + count_above_threshold(data, threshold, idx + 1)

# Real processing begins here
def analyze_stability(jitter_series):
    variance = sum((x - sum(jitter_series)/len(jitter_series))**2 for x in jitter_series) / len(jitter_series)
    return variance < 4.0

# Heuristic weighting system
def compute_weighted_deviation(latency_vals, loss_vals, throughput_vals):
    avg_lat = sum(latency_vals) / len(latency_vals)
    avg_loss = sum(loss_vals) / len(loss_vals)
    avg_tp = sum(throughput_vals) / len(throughput_vals)
    
    lat_dev = abs(avg_lat - baseline['latency_threshold'])
    loss_dev = abs(avg_loss - baseline['loss_tolerance'])
    tp_dev = abs(baseline['min_throughput'] - avg_tp)
    
    # Weights are tuned heuristically
    return (0.4 * lat_dev) + (0.5 * loss_dev * 100) + (0.1 * tp_dev)

# Secondary validation (distractor - looks important but not used)
validation_log = []
for i in range(len(metrics['latency_ms'])):
    if metrics['retries'][i] > baseline['max_retries']:
        validation_log.append(f'Node failure at {i}')

# Core evaluation logic
def evaluate_performance(m, b):
    # Step 1: Count how many readings exceed latency threshold
    high_latency_count = 0
    for lt in m['latency_ms']:
        if lt > b['latency_threshold']:
            high_latency_count += 1
    
    # Step 2: Check packet loss bursts (consecutive violations)
    burst_count = 0
    consecutive = 0
    for pl in m['packet_loss']:
        if pl > b['loss_tolerance']:
            consecutive += 1
        else:
            if consecutive >= 2:
                burst_count += 1
            consecutive = 0
    if consecutive >= 2:
        burst_count += 1
    
    # Step 3: Track throughput consistency using Counter
    tp_counter = Counter()
    for tp in m['throughput_mbps']:
        if tp < b['min_throughput']:
            tp_counter['below_min'] += 1
        else:
            tp_counter['above_min'] += 1
    
    # Step 4: Aggregate weighted deviation (key component)
    deviation_score = compute_weighted_deviation(m['latency_ms'], m['packet_loss'], m['throughput_mbps'])
    
    # Step 5: Stability check via jitter
    stable_jitter = analyze_stability(m['jitter_ms'])
    
    # Step 6: Calculate retry penalty
    total_retry_penalty = 0
    for r in m['retries']:
        if r > b['max_retries']:
            total_retry_penalty += (r - b['max_retries']) * 10
    
    # Step 7: Combine factors into composite score
    base_score = 100
    base_score -= high_latency_count * 3
    base_score -= burst_count * 8
    base_score -= tp_counter['below_min'] * 5
    base_score -= int(deviation_score * 2)
    base_score -= total_retry_penalty
    
    if not stable_jitter:
        base_score -= 15
    
    # Final adjustment based on unused validation log size (misleading)
    # Note: This looks like it matters, but validation_log length is 1 → subtracts 2
    base_score -= len(validation_log) * 2  # Subtle distractor!
    
    # Step 8: Apply logarithmic compression (only if positive)
    if base_score > 0:
        final_val = math.log(base_score) * 10
    else:
        final_val = -50
    
    # Key assignment
    final_score = int(round(final_val))
    
    return final_score

# Execution point of interest
final_score = evaluate_performance(metrics, baseline)
print(f"Result: {final_score}")