from collections import defaultdict, Counter

# Simulated network packet analysis with noise filtering and integrity scoring
def analyze_packet_sequence(raw_packets):
    packet_frequencies = Counter()
    cumulative_delay = 0.0
    retransmission_count = 0
    timing_outliers = []
    sequence_integrity = defaultdict(int)
    
    for i, packet in enumerate(raw_packets):
        size, delay, seq = packet['size'], packet['delay'], packet['seq']
        packet_frequencies[size] += 1
        cumulative_delay += delay
        
        if delay > 0.5:
            timing_outliers.append(i)
        
        if seq < i:  # Out-of-order or retransmitted
            retransmission_count += 1
            sequence_integrity['retransmitted'] += 1
        else:
            sequence_integrity['in_order'] += 1

    avg_delay = cumulative_delay / len(raw_packets)
    unique_sizes = len(packet_frequencies)
    peak_size_freq = max(packet_frequencies.values())
    
    # Irrelevant statistical distraction
    variance_proxy = sum((packet['delay'] - avg_delay) ** 2 for packet in raw_packets)
    std_dev_estimate = variance_proxy ** 0.5
    
    # Misleading intermediate score
    temporal_coherence = (len(raw_packets) - len(timing_outliers)) / len(raw_packets)
    redundancy_penalty = retransmission_count * 0.05
    
    processed_data = {
        'base_integrity': sequence_integrity['in_order'],
        'anomalies': sequence_integrity['retransmitted'],
        'size_diversity': unique_sizes,
        'outlier_ratio': len(timing_outliers) / len(raw_packets),
        'avg_delay': avg_delay,
        'temporal_coherence': temporal_coherence,  # Not actually used
        'redundancy_penalty': redundancy_penalty   # Not actually used
    }
    
    return processed_data

# Secondary helper with red herring logic
def evaluate_bandwidth_efficiency(data_chunk):
    efficiency_map = {}
    total_volume = 0
    null_slots = 0
    
    for item in data_chunk:
        total_volume += item
        if item == 0:
            null_slots += 1
    
    efficiency_map['volume'] = total_volume
    efficiency_map['nulls'] = null_slots
    efficiency_map['efficiency'] = total_volume / (len(data_chunk) + 1e-8)
    
    # This function is never called but adds cognitive load
    return efficiency_map

# Core scoring logic
def calculate_final_score(data):
    base = data['base_integrity']
    anomalies = data['anomalies']
    diversity = data['size_diversity']
    delay_factor = data['avg_delay']
    
    # Complex but deterministic formula
    stability_index = base - anomalies
    normalized_diversity = min(diversity, 10) / 10.0
    delay_penalty = int(delay_factor * 100)  # Convert to integer penalty
    
    # Multi-step computation with intermediate distractors
    temp_adjustment = 0
    for x in range(1, 5):
        temp_adjustment += (stability_index + x) % 3
    
    # Final score calculation — only this matters
    final_score = stability_index * 10 + int(normalized_diversity * 100) - delay_penalty
    
    # Unused debug variables
    debug_info = {
        'step1': stability_index,
        'step2': normalized_diversity,
        'step3': delay_penalty,
        'phantom': temp_adjustment
    }
    
    return final_score

# Input data (simulated packet stream)
raw_packets = [
    {'size': 1400, 'delay': 0.12, 'seq': 0},
    {'size': 1200, 'delay': 0.15, 'seq': 1},
    {'size': 1400, 'delay': 0.65, 'seq': 1},
    {'size': 1300, 'delay': 0.18, 'seq': 3},
    {'size': 1200, 'delay': 0.20, 'seq': 4},
    {'size': 1500, 'delay': 0.70, 'seq': 4},
    {'size': 1400, 'delay': 0.22, 'seq': 6},
    {'size': 1600, 'delay': 0.25, 'seq': 7},
    {'size': 1300, 'delay': 0.80, 'seq': 7},
    {'size': 1400, 'delay': 0.28, 'seq': 9}
]

# Processing pipeline
processed_data = analyze_packet_sequence(raw_packets)
final_score = calculate_final_score(processed_data)
print(f"Result: {final_score}")