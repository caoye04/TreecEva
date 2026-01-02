from collections import defaultdict

# Simulate a network load analyzer with fluctuating node traffic
def analyze_network_load(nodes_log):
    daily_stats = defaultdict(lambda: {'load': 0, 'peaks': 0})
    peak_capacity = 0
    historical_max = 0
    total_handled = 0
    volatility_index = 0.0
    adjustment_factor = 1.5

    for timestamp, updates in nodes_log.items():
        current_load = 0
        spike_count = 0

        # Process each node's data update
        for node_id, data_mb in updates:
            daily_stats[node_id]['load'] += data_mb
            current_load += data_mb

            # Track local peaks for this node
            if data_mb > 50:
                daily_stats[node_id]['peaks'] += 1
                spike_count += 1

            # Irrelevant computation: simulate signal degradation (not used later)
            signal_strength = 100 - (data_mb * 0.3) % 17
            _ = signal_strength * adjustment_factor  # Dead computation

        # Update global peak capacity if current load exceeds it
        if current_load > peak_capacity:
            peak_capacity = current_load

        # Secondary tracking variable (never used in final result)
        if current_load > historical_max:
            historical_max = current_load

        # Simulate load balancing adjustment (distractor logic)
        balanced_load = current_load / (len(updates) + 1e-8)
        if balanced_load > 40:
            volatility_index += 1.25
        else:
            volatility_index += 0.1

        # Early termination for high sustained spikes (not triggered in this case)
        if spike_count >= 5 and timestamp > 1500:
            break

        # Accumulate total handled data for throughput stats (semi-relevant)
        total_handled += current_load

        # Red herring: adjust factor based on arbitrary condition
        if timestamp % 100 == 0:
            adjustment_factor *= 0.95

    # Final adjustment (irrelevant to peak_capacity)
    final_throughput = total_handled / len(nodes_log) if nodes_log else 0
    _ = round(volatility_index, 2)

    return peak_capacity

# Input data: simulated network logs over time
network_logs = {
    1000: [('N1', 20), ('N2', 35), ('N3', 45), ('N4', 28)],
    1050: [('N1', 60), ('N2', 40), ('N3', 10), ('N4', 55)],
    1100: [('N1', 15), ('N2', 70), ('N3', 65), ('N4', 30)],
    1150: [('N1', 50), ('N2', 50), ('N3', 50), ('N4', 50)],
    1200: [('N1', 80), ('N2', 10), ('N3', 20), ('N4', 40)]
}

result = analyze_network_load(network_logs)
print(f"Target result: {result}")