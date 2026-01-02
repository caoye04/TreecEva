def analyze_node_health(node):
    # Irrelevant health check with decoy logic
    if len(node['metrics']) == 0:
        return 0.0
    return sum(node['metrics']) / len(node['metrics'])


def compute_bandwidth_efficiency(route):
    # Distractor function: computes something irrelevant
    total = 0
    for r in route:
        total += r.get('bw', 1) * r.get('latency', 0)
    return total if total > 0 else 1e-6


def extract_critical_indices(sequence):
    # Real but obfuscated component: finds peaks in signal
    indices = []
    for i in range(1, len(sequence)-1):
        if sequence[i] > sequence[i-1] and sequence[i] > sequence[i+1]:
            indices.append(i)
    return indices


def transform_data_stream(stream):
    # Heavily distracting transformation with red herring operations
    transformed = [x ** 0.5 for x in stream if x > 0]
    smoothed = []
    for i, val in enumerate(transformed):
        neighbor_sum = 0
        count = 0
        for j in range(max(0, i-2), min(len(transformed), i+3)):
            neighbor_sum += transformed[j]
            count += 1
        smoothed.append(neighbor_sum / count)
    
    # Decoy normalization
    max_val = max(smoothed) if smoothed else 1
    normalized = [x / max_val for x in smoothed]
    
    # Actual relevant operation buried here: sum of even-indexed elements
    relevant_part = sum(normalized[i] for i in range(0, len(normalized), 2))
    return relevant_part


def aggregate_performance(nodes):
    # Core logic hidden among distractions
    signals = []
    weights = []    
    decoy_accumulator = 0  # Misleading variable
    
    for node in nodes:
        health = analyze_node_health(node)
        if health < 0.3:
            continue  # Filter out unhealthy nodes
            
        raw_signal = node.get('signal_trace', [])
        
        # Real processing step 1: extract peak indices
        peaks = extract_critical_indices(raw_signal)
        
        # Real processing step 2: transform signal via complex path
        if len(peaks) > 0:
            sliced = raw_signal[peaks[0]:peaks[-1]+1]  # Use slice between first and last peak
            contribution = transform_data_stream(sliced)
            signals.append(contribution)
            weights.append(node['weight_factor'])
        
        # Distractor block: builds unused structure
        temp_route = [{'bw': i*2, 'latency': (i+1)%5} for i in range(len(raw_signal))]
        efficiency = compute_bandwidth_efficiency(temp_route)
        decoy_accumulator += efficiency * health
    
    # Real final calculation: weighted average of transformed signals
    if not signals:
        return 0.0
    weighted_sum = sum(s * w for s, w in zip(signals, weights))
    total_weight = sum(weights)
    result = weighted_sum / total_weight if total_weight != 0 else 0.0
    
    # Final red herring: unrelated bit manipulation
    magic_offset = 0
    for i in range(len(signals)):
        magic_offset ^= int(weights[i] * 100) & 0xFF
    
    final_score = int(result * 1000) + magic_offset  # Answer is deterministic
    return final_score

# Simulated input data
network_nodes = [
    {
        'metrics': [0.5, 0.6, 0.4],
        'signal_trace': [1, 3, 2, 5, 4, 6, 2, 1],
        'weight_factor': 2.5,
        'id': 'node_01'
    },
    {
        'metrics': [0.8, 0.7, 0.9],
        'signal_trace': [2, 1, 4, 3, 7, 5, 8, 6, 2],
        'weight_factor': 3.0,
        'id': 'node_02'
    },
    {
        'metrics': [0.2, 0.1, 0.3],  # Will be filtered out (health < 0.3)
        'signal_trace': [5, 6, 7, 8, 9],
        'weight_factor': 1.5,
        'id': 'node_03'
    }
]

# Execution point of interest
final_score = aggregate_performance(network_nodes)
print(f"Result: {final_score}")