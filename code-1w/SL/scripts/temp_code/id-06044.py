def analyze_transmission_integrity(log_entries):
    error_count = 0
    for entry in log_entries:
        if isinstance(entry, str) and 'ERR' in entry:
            error_count += 1
    return error_count > len(log_entries) * 0.1

def calculate_latency_adjustment(size, hops):
    base_latency = size / (hops + 1)
    adjustment = 0.0
    if hops > 3:
        adjustment = base_latency * 0.15
    return adjustment

def preprocess_signal_strength(raw_strengths):
    processed = []
    for s in raw_strengths:
        if s < -90:
            processed.append(-90)
        elif s > -30:
            processed.append(-30)
        else:
            processed.append(s)
    return processed

def optimize_bandwidth(log, base_cap):
    # Real computation path
    valid_entries = [len(e) for e in log if isinstance(e, str) and e.startswith('TX')]
    total_volume = sum(valid_entries)
    avg_packet_size = total_volume / len(valid_entries) if valid_entries else 0
    
    # Distractor: signal processing not actually used in bandwidth
    signal_data = [-72, -88, -65, -95, -40]
    normalized_signals = preprocess_signal_strength(signal_data)
    avg_signal = sum(normalized_signals) / len(normalized_signals)
    signal_penalty = 0.1 if avg_signal < -70 else 0.05
    
    # Distractor: latency calculation that looks relevant but isn't applied
    dummy_sizes = [64, 128, 256]
    dummy_hops = 4
    simulated_latencies = [calculate_latency_adjustment(sz, dummy_hops) for sz in dummy_sizes]
    average_simulated_latency = sum(simulated_latencies) / len(simulated_latencies)
    
    # Real logic continues
    peak_load = max(valid_entries) if valid_entries else 0
    load_factor = (peak_load / avg_packet_size) if avg_packet_size else 0
    
    # Conditional expression (required feature)
    efficiency_bonus = 1.25 if avg_packet_size > 50 else 0.9
    
    # String method usage (required feature)
    metadata_tags = "mode=high-throughput, retries=2, version=3.1"
    config_version = float(metadata_tags.split(',')[2].split('=')[1]) if 'version' in metadata_tags else 2.0
    version_scaling = 1.1 if config_version >= 3.0 else 1.0
    
    # Final bandwidth calculation (this is what matters)
    raw_bandwidth = base_cap * efficiency_bonus * version_scaling
    congestion_modifier = 0.8 if load_factor > 1.8 else 1.0
    final_bandwidth = int(raw_bandwidth * (1 - signal_penalty) * congestion_modifier)
    
    # Irrelevant tracking variables
    transmission_summary = {
        'packets': len(valid_entries),
        'total_bytes': total_volume,
        'peak': peak_load,
        'avg_size': avg_packet_size,
        'anomaly_detected': analyze_transmission_integrity(log)
    }
    
    # This print is NOT the target; we're testing reasoning, not output
    return final_bandwidth

# Setup inputs
tx_log = [
    'TX_DATA_01', 'TX_DATA_02', 'ERR_CRITICAL', 'TX_DATA_03', 'TX_DATA_04',
    'TX_DATA_05', 'TX_DATA_06', 'WARN_TIMEOUT', 'TX_DATA_07', 'TX_DATA_08'
]
base_capacity = 1000

# Execute
final_bandwidth = optimize_bandwidth(tx_log, base_capacity)
print(f"Target result: {final_bandwidth}")