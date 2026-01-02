from collections import Counter

# Simulate network packet analysis with directional flow tracking
def analyze_packet_flow(log_entries):
    direction_map = {'A': 'in', 'B': 'out', 'C': 'in', 'D': 'out'}
    valid_sources = ['src_a', 'src_b', 'src_c']
    inflow_counter = Counter()
    outflow_counter = Counter()
    temp_buffer = []

    for entry in log_entries:
        source = entry.split('|')[0]
        direction_flag = entry.split('|')[1]
        payload = entry.split('|')[2]
        
        # Irrelevant string processing (distractor)
        checksum = sum(ord(c) for c in payload) % 100
        if checksum < 0:  # Dead code path (never executed)
            temp_buffer.append(checksum)

        # Extract and map actual flow direction
        mapped_dir = direction_map.get(direction_flag, None)
        if mapped_dir and source in valid_sources:
            if mapped_dir == 'in':
                inflow_counter['in'] += len(payload)
                inflow_counter['packet_count'] += 1
            elif mapped_dir == 'out':
                outflow_counter['out'] += len(payload)
                outflow_counter['packet_count'] += 1

    # Compute derived metrics (semi-relevant)
    total_in_packets = inflow_counter['packet_count']
    total_out_packets = outflow_counter['packet_count']
    avg_in_size = inflow_counter['in'] / total_in_packets if total_in_packets else 0
    avg_out_size = outflow_counter['out'] / total_out_packets if total_out_packets else 0

    # Key computation point
    net_flow = inflow_counter['in'] - outflow_counter['out']

    # Additional irrelevant aggregation
    size_ratio = avg_in_size / avg_out_size if avg_out_size else 0
    flow_balance_score = (total_in_packets + 1) / (total_out_packets + 1)

    # Final output
    print(f"Result: {net_flow}")
    return net_flow

# Input data
logs = [
    "src_a|A|hello",
    "src_b|B|world123",
    "src_c|A|data_flow_2024",
    "src_a|B|temp_payload",
    "src_b|A|final_test_case"
]

# Execute
result = analyze_packet_flow(logs)