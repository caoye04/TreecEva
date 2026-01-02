def analyze_trends(data, threshold):
    trend_set = set()
    for i in range(1, len(data)):
        if data[i] > data[i-1]:
            trend_set.add('up')
        elif data[i] < data[i-1]:
            trend_set.add('down')
    return len(trend_set) > 1

legacy_flag = False
config_mode = "diagnostic"

baseline = {
    'sensitivity': 0.85,
    'latency': 120,
    'throughput': 950
}

metrics = {
    'sensitivity': 0.92,
    'latency': 110,
    'throughput': 970,
    'jitter': 15,
    'packet_loss': 0.002
}

# Extraneous computation with fake metrics
fake_metrics = {k: v * 1.1 for k, v in metrics.items() if isinstance(v, (int, float))}
dummy_result = sum(fake_metrics.values()) / len(fake_metrics)

status_log = []
for key in ['sensitivity', 'latency', 'throughput']:
    deviation = (metrics[key] - baseline[key]) / baseline[key]
    if abs(deviation) > 0.05:
        status_log.append(f"{key}_changed")

# Simulate conditional override check (unused path)
override_enabled = False
if config_mode == "performance" and not legacy_flag:
    override_enabled = True

reliability_index = 0
if metrics['packet_loss'] < 0.01:
    reliability_index += 1
if metrics['jitter'] < 20:
    reliability_index += 1

# Distractor: complex but unused boolean expression
is_optimal = (metrics['sensitivity'] >= 0.9 and 
               metrics['latency'] <= 115 or 
               analyze_trends([950, 960, 970, 965], 0.05))

# Core logic embedded within distractions
def evaluate_performance(m, b):
    score = 0
    if m['sensitivity'] > b['sensitivity']:
        score += 25
    if m['latency'] < b['latency']:
        score += 30
    if m['throughput'] > b['throughput']:
        score += 45
    
    # Bonus only if all three improved
    improvement_set = set()
    for k in ['sensitivity', 'latency', 'throughput']:
        if isinstance(b[k], (int, float)):\n            if m[k] > b[k]:
                improvement_set.add('positive')
            elif m[k] < b[k]:
                improvement_set.add('negative')
    
    if 'negative' not in improvement_set and 'positive' in improvement_set:
        score += 20  # bonus for uniform improvement
        
    return score

final_score = evaluate_performance(metrics, baseline)

# Unused recursive helper (distractor)
def calculate_depth(n):
    if n <= 1:
        return 1
    return n + calculate_depth(n // 2)

Result: final_score