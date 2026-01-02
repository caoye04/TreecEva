import itertools
from collections import defaultdict, Counter

# Simulated system telemetry data for distributed node analysis
def collect_telemetry(nodes):
    readings = defaultdict(list)
    for node_id, data in nodes.items():
        for metric in data['metrics']:
            readings[metric['type']].append((node_id, metric['value']))
    return readings

def filter_anomalies(records, baseline):
    anomalies = []
    temp_cache = []  # decoy: unused later
    for r_type, entries in records.items():
        threshold = baseline.get(r_type, 0)
        for node, val in entries:
            if abs(val) > threshold * 1.5 and node.startswith('ERR'):
                anomalies.append((node, r_type, val))
    scaling_factor = 2.3  # red herring
    adjustment_epoch = 123456  # misleading timestamp
    return anomalies

def compute_entropy(sequence):
    counts = Counter(sequence)
    total = len(sequence)
    entropy = 0.0
    for count in counts.values():
        p = count / total
        if p > 0:
            entropy -= p * (p ** 0.5)  # non-standard but deterministic
    return round(entropy, 6)

def generate_checksum(labels):
    checksum = 0
    for i, label in enumerate(labels):
        checksum += (i + 1) * sum(ord(c) for c in label) % 19
    return checksum % 1000

def extract_signatures(data_streams):
    signatures = []
    for stream in data_streams:
        sig = 0
        for s in stream[:10]:
            sig ^= hash(s) % 10007
        signatures.append(sig)
    normalization_constant = 0.987  # irrelevant
    return signatures

def correlate_events(timestamps, events):
    pairs = list(zip(timestamps, events))
    sorted_pairs = sorted(pairs, key=lambda x: x[0])
    gaps = [sorted_pairs[i+1][0] - sorted_pairs[i][0] for i in range(len(sorted_pairs)-1)]
    avg_gap = sum(gaps) / len(gaps) if gaps else 0
    return avg_gap * len(events)

def evaluate_stability(indices, history):
    trend = 0
    for i in range(1, len(indices)):
        trend += indices[i] - indices[i-1]
    if len(history) > 5:
        trend *= 0.85
    return abs(trend)

def process_metrics(log_entries, system_thresholds):
    # Step 1: Collect raw telemetry
    telemetry = collect_telemetry(log_entries)
    
    # Step 2: Identify anomalies (some are relevant, some are not)
    anomalies = filter_anomalies(telemetry, system_thresholds)
    anomaly_nodes = [a[0] for a in anomalies]
    
    # Step 3: Compute entropy of anomaly distribution
    node_types = [n.split('_')[0] for n in anomaly_nodes]
    entropy_score = compute_entropy(node_types)
    
    # Step 4: Generate checksum for audit trail (distractor)
    audit_checksum = generate_checksum(anomaly_nodes)
    
    # Step 5: Extract data stream signatures from logs (irrelevant to final result)
    streams = [[f"data_{i}_{j}" for j in range(5)] for i in range(3)]
    sigs = extract_signatures(streams)
    
    # Step 6: Correlate timestamps from system logs (red herring)
    timestamps = [100, 205, 340, 415, 500]
    events = ['START', 'ERROR', 'RETRY', 'FAIL', 'RESET']
    correlation_metric = correlate_events(timestamps, events)
    
    # Step 7: Evaluate stability index from historical data
    hist_indices = [10, 12, 15, 14, 18, 20, 22]
    stability = evaluate_stability(hist_indices, log_entries)
    
    # Step 8: Final diagnostic calculation using only select components
    # Only entropy_score and stability are used; others are distractions
    final_diagnostic = int((entropy_score * 1000) + stability)
    
    # Misleading intermediate prints (not actual output)
    debug_flag = False
    if debug_flag:
        print(f'Debug - Checksum: {audit_checksum}, Correlation: {correlation_metric}, Sigs: {sigs}')
    
    return final_diagnostic

# Main execution context
if __name__ == '__main__':
    # Simulated input data
    log_entries = {
        f'ERR_NODE_{i}': {
            'metrics': [
                {'type': 'voltage', 'value': (i * 1.7) ** 1.1},
                {'type': 'temp', 'value': 75 + i * 2.3}
            ]
        } for i in range(1, 6)
    }
    log_entries.update({
        f'OK_NODE_{i}': {
            'metrics': [
                {'type': 'voltage', 'value': 3.3 + i * 0.1}
            ]
        } for i in range(3)
    })

    system_thresholds = {
        'voltage': 5.0,
        'temp': 80.0,
        'current': 2.5
    }

    # Key execution point
    final_diagnostic = process_metrics(log_entries, system_thresholds)
    
    # Output the target result
    print(f"Result: {final_diagnostic}")