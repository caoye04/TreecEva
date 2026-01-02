from itertools import combinations, cycle

# Simulate a network packet analysis with performance scoring
def analyze_packet_sequence(packets):
    sequence_scores = []
    checksum_accumulator = 0
    temporal_gaps = []

    # Extract timestamps and sizes for analysis
    for pkt in packets:
        size = pkt['size']
        timestamp = pkt['timestamp']
        checksum_accumulator += size * (timestamp % 7)
        if len(temporal_gaps) > 0:
            temporal_gaps.append(timestamp - previous_time)
        else:
            temporal_gaps.append(0)
        previous_time = timestamp

    # Compute base efficiency score
    base_efficiency = sum(temporal_gaps) / len(temporal_gaps) if temporal_gaps else 0

    # Generate synthetic interference patterns (distractor)
    interference_mask = [i % 5 == 0 for i in range(len(packets))]
    masked_count = sum(interference_mask)
    dummy_metric = masked_count * base_efficiency

    # Real logic: find optimal 3-packet window with highest throughput
    max_window_score = 0
    for start_idx in range(len(packets) - 2):
        window = packets[start_idx:start_idx + 3]
        total_size = sum(pkt['size'] for pkt in window)
        time_span = window[-1]['timestamp'] - window[0]['timestamp']
        if time_span > 0:
            throughput = total_size / time_span
            if throughput > max_window_score:
                max_window_score = throughput

    # Use combinatorics to assess transmission reliability
    reliability_combinations = list(combinations(packets, 2))
    success_pairs = 0
    for pair in reliability_combinations:
        diff = abs(pair[0]['timestamp'] - pair[1]['timestamp'])
        if diff >= 2 and (pair[0]['size'] + pair[1]['size']) % 3 == 0:
            success_pairs += 1

    reliability_score = success_pairs / len(reliability_combinations) if reliability_combinations else 0

    # Distractor: unused complex generator
    def geometric_progression(start, ratio, count):
        val = start
        for _ in range(count):
            yield val
            val *= ratio

    gen = geometric_progression(1.5, 1.1, 10)
    advanced_stat = sum([x for x in gen if x < 5])  # Not used later

    # Final score computation (this is what matters)
    raw_score = max_window_score * 100 + reliability_score * 50 - base_efficiency
    normalized = max(0, min(100, raw_score))  # Clamp to 0-100

    adjustment_factor = 1.0
    if len(packets) > 5:
        adjustment_factor = 1.2
    elif checksum_accumulator > 1000:
        adjustment_factor = 0.9

    final_score = int(normalized * adjustment_factor)

    return final_score


def evaluate_performance(log_entries):
    filtered_packets = []
    priority_counter = 0

    for entry in log_entries:
        if entry['type'] != 'data':
            continue
        if entry['priority'] > 1:
            priority_counter += 1
        # Reconstruct packet from log
        packet = {
            'size': entry['payload_size'] + 20,
            'timestamp': entry['ts']
        }
        filtered_packets.append(packet)

    # Extra distraction: cycle through metadata (not affecting result)
    meta_cycle = cycle(['A', 'B', 'C'])
    for _ in range(len(log_entries)):
        next(meta_cycle)

    result = analyze_packet_sequence(filtered_packets)
    return result

# Input data
log_data = [
    {'type': 'data', 'payload_size': 45, 'ts': 10, 'priority': 2},
    {'type': 'ctrl', 'payload_size': 20, 'ts': 12, 'priority': 0},
    {'type': 'data', 'payload_size': 60, 'ts': 13, 'priority': 1},
    {'type': 'data', 'payload_size': 80, 'ts': 14, 'priority': 3},
    {'type': 'data', 'payload_size': 30, 'ts': 18, 'priority': 1},
    {'type': 'data', 'payload_size': 70, 'ts': 20, 'priority': 2},
    {'type': 'data', 'payload_size': 50, 'ts': 25, 'priority': 1}
]

final_score = evaluate_performance(log_data)
print(f"Result: {final_score}")