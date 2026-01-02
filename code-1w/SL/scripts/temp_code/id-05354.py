import itertools

def analyze_node_sequence(sequence):
    # Irrelevant helper function (dead code path)
    return sum(a * b for a, b in zip(sequence, sequence[1:]))

def compute_entropy(data):
    # Unused mathematical red herring
    from math import log2
    total = sum(data)
    return -sum((x / total) * log2(x / total) for x in data if x > 0)

def signal_filter(buffer, threshold=0.5):
    # Distractor: complex-looking but unused signal processing
    return [x for x in buffer if abs(x) > threshold]

def main():
    # Simulated network diagnostics with heavy distractions
    node_loads = [12, 15, 8, 20, 13, 7, 9]
    temp_readings = [34.2, 36.1, 33.8, 37.5, 35.0, 32.9, 36.3]
    packet_loss = [0.01, 0.03, 0.02, 0.05, 0.04, 0.01, 0.02]
    
    # Decoy data structures
    audit_trail = {'init': 'pass', 'checksum': 0xDEADBEEF, 'status': 'nominal'}
    backup_config = {
        'version': '2.1.0',
        'timeout': 30,
        'retries': 3,
        'threshold': 0.75,
        'debug_mode': False
    }
    
    # Real computation buried in noise
    rolling_window = lambda arr, w: [arr[i:i+w] for i in range(len(arr)-w+1)]
    windowed_loads = rolling_window(node_loads, 3)
    
    # Compute moving average of node loads
    moving_avg = [sum(window) / 3 for window in windowed_loads]
    
    # Misleading intermediate: peak detection (unused)
    peaks = [i for i in range(1, len(moving_avg)-1) if moving_avg[i-1] < moving_avg[i] > moving_avg[i+1]]
    
    # Real logic starts here — stability based on load variance
    variance_proxy = sum(
        (node_loads[i] - node_loads[i-1])**2 for i in range(1, len(node_loads))
    ) / (len(node_loads) - 1)
    
    # Secondary metric: temperature trend
    temp_trend = sum(
        1 if temp_readings[i] > temp_readings[i-1] else -1
        for i in range(1, len(temp_readings))
    )
    
    # Hidden relevant transformation
    coded_shift = (variance_proxy * 10) ^ 255  # Bitwise red herring?
    
    # Actually used: packet loss sum mod 100
    loss_metric = int(sum(packet_loss) * 100) % 100
    
    # Core calculation disguised as one among many
    base_stability = 100 - loss_metric
    adjusted_stability = base_stability - int(variance_proxy)
    
    # Simulate historical comparison (distractor)
    historical_avg = 12.5
    deviation_score = abs(sum(node_loads) / len(node_loads) - historical_avg) * 10

    # Critical data structure: logs and diagnostics
    network_state_log = [
        {'time': t, 'load': load, 'temp': temp} 
        for t, (load, temp) in enumerate(zip(node_loads, temp_readings))
    ]
    
    diagnostics = {
        'peak_count': len(peaks),
        'deviation_score': deviation_score,
        'temp_trend_direction': 'increasing' if temp_trend > 0 else 'decreasing',
        'coded_shift': coded_shift,
        'base_stability': base_stability
    }
    
    # The actual answer depends only on specific derivation:
    # But this looks like just another operation
    def aggregate_metrics(log, meta):
        load_vals = [entry['load'] for entry in log]
        total_change = sum(abs(load_vals[i] - load_vals[i-1]) for i in range(1, len(load_vals)))
        stability_index = meta['base_stability'] - total_change
        return {
            'stability_index': int(stability_index),
            'total_transitions': total_change,
            'consistency_flag': total_change < 20
        }
    
    # THIS IS THE KEY STATEMENT
    final_diagnostic = aggregate_metrics(network_state_log, diagnostics)['stability_index']
    
    # Print required output
    print(f"Result: {final_diagnostic}")
    
    # Dead code block (never reached)
    if False:
        fallback = compute_entropy(node_loads)
        analyze_node_sequence(temp_readings)

    return final_diagnostic

if __name__ == "__main__":
    main()