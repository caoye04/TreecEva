import math

def analyze_trend(data, threshold):
    trend_score = 0
    noise_counter = 0  # distractor
    for i in range(1, len(data)):
        if data[i] > data[i-1]:
            trend_score += 1
        elif data[i] < data[i-1]:
            trend_score -= 0.5
    return trend_score if trend_score >= threshold else 0

def calculate_efficiency(ratio):
    if ratio <= 0:
        return 0
    efficiency = math.log(ratio) * 100
    temp_adjustment = efficiency * 0.1  # red herring
    return round(efficiency, 2)

def validate_stability(readings):
    mean = sum(readings) / len(readings)
    variance = sum((x - mean) ** 2 for x in readings) / len(readings)
    stability = 1 / (1 + variance)  # higher variance → lower stability
    return stability

def dummy_normalization(x):  # dead function, never used
    return (x - min(x)) / (max(x) - min(x))

def process_entries(entry_list):
    processed = []
    for entry in entry_list:
        processed.append({
            'id': entry['id'],
            'value': entry['value'] * 1.05,
            'flagged': False
        })
    return processed  # irrelevant to final result

def evaluate_performance(log, config):
    # Extract relevant sequences
    cpu_loads = [entry['cpu'] for entry in log if entry['type'] == 'system']
    mem_uses = [entry['mem'] for entry in log if entry['type'] == 'system']
    
    # Distractor variables
    avg_cpu = sum(cpu_loads) / len(cpu_loads)
    peak_memory = max(mem_uses)
    unused_snapshot = {'avg_cpu': avg_cpu, 'peak': peak_memory}  # decoy
    
    # Real logic begins
    base_metric = len(log) * config.get('scale_factor', 1)
    
    # Bit manipulation as obfuscation layer
    encoded_offset = (base_metric << 2) ^ 0b1010  # shift and XOR
    decoded_offset = (encoded_offset ^ 0b1010) >> 2  # reverse to get original scale
    
    # Use slicing to extract critical window
    recent_logs = log[-5:]  # last 5 entries
    recent_cpu = [e['cpu'] for e in recent_logs]
    
    # Trend analysis on recent behavior
    trend_value = analyze_trend(recent_cpu, threshold=2)
    
    # Efficiency from average/memory ratio
    avg_mem = sum(mem_uses) / len(mem_uses)
    if avg_mem > 0:
        efficiency_rating = calculate_efficiency(sum(cpu_loads) / avg_mem)
    else:
        efficiency_rating = 0
    
    # Stability score
    stability_score = validate_stability(cpu_loads)
    
    # Weighted combination
    weights = config['weights']
    raw_score = (
        decoded_offset * weights['length'] +
        trend_value * weights['trend'] +
        efficiency_rating * weights['efficiency'] +
        stability_score * 100 * weights['stability']
    )
    
    # Final adjustment with dictionary lookup
    adjustment_map = {0: -5, 1: -2, 2: 0, 3: 3, 4: 5, 5: 8}
    adjustment_key = min(int(stability_score * 10), 5)
    adjustment = adjustment_map.get(adjustment_key, 0)
    
    final_score = int(raw_score + adjustment)
    
    # Critical execution point
    return final_score

# Simulated data
baseline_config = {
    'scale_factor': 3,
    'weights': {
        'length': 0.4,
        'trend': 6.0,
        'efficiency': 0.15,
        'stability': 0.25
    }
}

metrics_log = [
    {'type': 'system', 'cpu': 70, 'mem': 45, 'id': 1},
    {'type': 'system', 'cpu': 72, 'mem': 46, 'id': 2},
    {'type': 'system', 'cpu': 75, 'mem': 48, 'id': 3},
    {'type': 'system', 'cpu': 73, 'mem': 50, 'id': 4},
    {'type': 'system', 'cpu': 78, 'mem': 52, 'id': 5},
    {'type': 'system', 'cpu': 80, 'mem': 55, 'id': 6},
    {'type': 'network', 'bytes': 1024},  # irrelevant type
    {'type': 'system', 'cpu': 82, 'mem': 53, 'id': 7},
    {'type': 'system', 'cpu': 85, 'mem': 58, 'id': 8},
    {'type': 'system', 'cpu': 83, 'mem': 59, 'id': 9},
    {'type': 'system', 'cpu': 88, 'mem': 60, 'id': 10}
]

# Process but don't use (distractor call)
ignored_output = process_entries([{'id': 1, 'value': 100}, {'id': 2, 'value': 200}])

# Key execution point
final_score = evaluate_performance(metrics_log, baseline_config)

print(f"Result: {final_score}")