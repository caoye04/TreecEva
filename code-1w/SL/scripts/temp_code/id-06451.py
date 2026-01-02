from collections import Counter, defaultdict

# Simulate network packet flow analysis across different node statuses
def analyze_packet_flow():
    # Initial raw packet logs (simulated)
    packets = [
        ('node_1', 'active', 'in'), ('node_2', 'standby', 'out'),
        ('node_3', 'active', 'in'), ('node_4', 'failed', 'in'),
        ('node_5', 'active', 'out'), ('node_6', 'standby', 'in'),
        ('node_7', 'active', 'in'), ('node_8', 'failed', 'out'),
        ('node_9', 'active', 'out'), ('node_10', 'standby', 'out')
    ]

    # Track inflow counts by status
    inflow_counter = Counter()
    # Track outflow counts by status
    outflow_tracker = defaultdict(int)

    # Auxiliary tracking for diagnostics (distractor)
    diagnostic_log = []
    total_processed = 0
    redundant_sum = 0  # Dead variable - never used in logic

    # Process each packet
    for node_id, status, direction in packets:
        total_processed += 1
        if direction == 'in':
            inflow_counter[status] += 1
            diagnostic_log.append(f"{node_id}: IN -> {status}")
        elif direction == 'out':
            outflow_tracker[status] += 1
            diagnostic_log.append(f"{node_id}: OUT <- {status}")

        # Redundant calculation - adds noise
        for i in range(2):
            redundant_sum += len(node_id) % 3

    # Secondary distractor: analyze diagnostic patterns (not affecting result)
    event_stats = Counter([entry.split(':')[1].strip() for entry in diagnostic_log])
    avg_event_length = sum(len(e) for e in event_stats.keys()) / len(event_stats) if event_stats else 0

    # Core logic: compute net flow for 'active' status
    status = 'active'
    base_inflow = inflow_counter[status]
    base_outflow = outflow_tracker.get(status, 0)
    net_flow = inflow_counter[status] - outflow_tracker.get(status, 0)

    # Additional irrelevant transformation
    normalized_ratio = (net_flow + 1) / (base_inflow + 1) if base_inflow else 0

    # Final output
    print(f"Result: {net_flow}")

analyze_packet_flow()