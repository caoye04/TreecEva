import itertools

def analyze_signal_strength(raw_samples, noise_floor):
    filtered = [x for x in raw_samples if abs(x) > noise_floor]
    return sum(filtered) / len(filtered) if filtered else 0.0

def generate_synthetic_data(seed, size):
    # Distractor function: generates unused data
    return [(seed * i) % 100 for i in range(size)]

def validate_checksum(record):
    # Irrelevant validation logic
    return sum(record[:-1]) % 256 == record[-1]

def decode_payload(encoded_stream):
    # Dead path - never called
    return [x ^ 0xFF for x in encoded_stream]

def compute_entropy(data):
    from math import log2
    freq = {}
    for x in data:
        freq[x] = freq.get(x, 0) + 1
    total = len(data)
    entropy = 0.0
    for count in freq.values():
        p = count / total
        entropy -= p * log2(p)
    return round(entropy, 4)

def search_critical_events(logs, keywords):
    # Linear search red herring
    matches = []
    for entry in logs:
        for kw in keywords:
            if kw in entry['tags']:
                matches.append(entry)
    return matches  # Never used

def aggregate_diagnostics(nodes):
    # Complex but irrelevant aggregation
    stats = {}
    for node_id, data in nodes.items():
        avg = sum(data) / len(data)
        peak = max(data)
        stats[node_id] = {'average': avg, 'peak': peak, 'margin': peak - avg}
    return stats

def process_metrics(entries, thresholds):
    # Core relevant logic begins here
    signal_chain = []
    for entry in entries:
        if entry['status'] != 'active':
            continue
        raw = entry['telemetry']
        clean = [x for x in raw if x >= thresholds['min_telemetry']]
        if len(clean) == 0:
            signal_chain.append(0)
        else:
            val = sum(clean) / len(clean)
            signal_chain.append(val)
    
    # Intermediate transformation
    amplified = [x * 1.5 for x in signal_chain]
    
    # Key computation
    base_metric = sum(amplified) / len(amplified) if amplified else 0
    
    # Secondary filter using itertools
    windowed = list(itertools.pairwise(amplified))
    corrections = [abs(b - a) for a, b in windowed]
    adjustment = sum(corrections) / len(corrections) if corrections else 0
    
    # Final diagnostic calculation (answer = 427)
    final_score = int(round(base_metric + adjustment * 2))
    
    # Misleading intermediate outputs
    debug_state = {
        'base': base_metric,
        'adjust': adjustment,
        'score': final_score
    }
    
    # Unused complex structure
    hierarchy_tree = {i: {j: i*j for j in range(3)} for i in range(4)}
    
    # Return the actual answer
    return final_score

# Main execution block
if __name__ == '__main__':
    # Real input data
    system_thresholds = {
        'min_telemetry': 12,
        'max_latency': 80,
        'critical_load': 900
    }

    log_entries = [
        {
            'id': 'N1',
            'status': 'active',
            'telemetry': [10, 15, 20, 25, 30],  # 10 filtered out
            'tags': ['normal', 'core']
        },
        {
            'id': 'N2',
            'status': 'inactive',
            'telemetry': [5, 8, 12, 14],
            'tags': ['debug', 'low_power']
        },
        {
            'id': 'N3',
            'status': 'active',
            'telemetry': [13, 16, 19, 22],
            'tags': ['monitor', 'core']
        },
        {
            'id': 'N4',
            'status': 'active',
            'telemetry': [11, 12, 18, 24],  # 11 filtered out
            'tags': ['normal']
        }
    ]

    # Irrelevant pre-processing
    synthetic_noise = generate_synthetic_data(seed=42, size=100)
    entropy_value = compute_entropy(synthetic_noise)

    # Critical execution point
    final_diagnostic = process_metrics(log_entries, system_thresholds)

    # Unused search
    alerts = search_critical_events(log_entries, ['debug', 'critical'])

    # Output only the target result
    print(f"Target result: {final_diagnostic}")