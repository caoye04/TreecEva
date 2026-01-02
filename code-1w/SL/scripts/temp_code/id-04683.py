from collections import defaultdict, Counter
import math

def analyze_response_time(entries):
    # Irrelevant analysis function (dead code path)
    avg = sum(e['response'] for e in entries) / len(entries)
    return avg if avg > 0.1 else 0.1

def compute_entropy(data):
    # Distractor: computes entropy but not used in final result
    freq = Counter(data)
    total = len(data)
    entropy = 0.0
    for count in freq.values():
        p = count / total
        entropy -= p * math.log2(p)
    return round(entropy, 6)

def extract_signals(logs):
    # Extracts signal_strength values; partially relevant but obfuscated
    signals = []
    for i, log in enumerate(logs):
        if i % 2 == 0 and 'signal_strength' in log:
            signals.append(log['signal_strength'] * 1.5)
        elif 'backup_signal' in log:
            signals.append(log['backup_signal'] * 0.7)
    return signals

def validate_integrity(checksums):
    # Unused validation logic (red herring)
    base = sum(checksums) % 7
    return base != 0

def filter_anomalies(dataset):
    # Misleading preprocessing step
    filtered = [d for d in dataset if d.get('status') != 'ERROR']
    return filtered

def calculate_efficiency(metrics):
    # Complex transformation with irrelevant components
    efficiency_list = []
    temp_cache = defaultdict(float)
    for idx, m in enumerate(metrics):
        raw = m.get('throughput', 0) - m.get('latency', 0)
        adjusted = raw * (1 + m.get('priority', 1) * 0.05)
        temp_cache[idx] = adjusted
        if adjusted > 10:
            efficiency_list.append(adjusted * 0.9)
        else:
            efficiency_list.append(adjusted * 1.1)
    return efficiency_list

def aggregate_performance(log_entries, weights):
    # Core function that determines the answer
    total_weighted = 0.0
    weight_sum = 0.0

    # Real data processing chain
    filtered_logs = filter_anomalies(log_entries)
    signals = extract_signals(filtered_logs)
    efficiencies = calculate_efficiency(filtered_logs)

    for i, log in enumerate(filtered_logs):
        w = weights[i % len(weights)]
        base_metric = log.get('base_metric', 1.0)

        # Actual computation path
        signal = signals[i] if i < len(signals) else 1.0
        efficiency = efficiencies[i] if i < len(efficiencies) else 1.0

        contribution = base_metric * signal * efficiency * w
        total_weighted += contribution
        weight_sum += w

    # Final deterministic result
    final = total_weighted / weight_sum if weight_sum != 0 else 0
    return round(final, 6)

# Simulated system log data (real input)
log_data = [
    {'timestamp': 1678886400, 'base_metric': 3.2, 'signal_strength': 0.9, 'status': 'OK', 'throughput': 12, 'latency': 2, 'priority': 2},
    {'timestamp': 1678886401, 'base_metric': 2.8, 'backup_signal': 1.1, 'status': 'OK', 'throughput': 15, 'latency': 4, 'priority': 1},
    {'timestamp': 1678886402, 'base_metric': 3.5, 'signal_strength': 1.2, 'status': 'ERROR', 'throughput': 8, 'latency': 1, 'priority': 3},
    {'timestamp': 1678886403, 'base_metric': 4.0, 'signal_strength': 0.8, 'status': 'OK', 'throughput': 20, 'latency': 5, 'priority': 2},
    {'timestamp': 1678886404, 'base_metric': 3.1, 'backup_signal': 1.0, 'status': 'OK', 'throughput': 10, 'latency': 3, 'priority': 1}
]

# System weights (cycled during aggregation)
system_weights = [0.5, 1.2, 0.8, 1.5, 0.7]

# Distractor variables (unused but plausible)
checksum_values = [234, 567, 129, 888, 451]
data_stream = ['A', 'B', 'C', 'B', 'D', 'E', 'F', 'D']
redundant_stats = {
    'max_latency': max(d.get('latency', 0) for d in log_data),
    'error_count': sum(1 for d in log_data if d['status'] == 'ERROR'),
    'data_volume': sum(d.get('throughput', 0) for d in log_data)
}

# Entropy distractor
data_entropy = compute_entropy(data_stream)

# Signal extraction (used indirectly)
extracted_signals = extract_signals(log_data)

# Efficiency metrics (used in core logic)
efficiency_scores = calculate_efficiency(log_data)

# Main result computation
final_score = aggregate_performance(log_data, system_weights)

# Output result as required
print(f"Target result: {final_score}")