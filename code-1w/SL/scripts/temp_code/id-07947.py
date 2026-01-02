def calculate_network_efficiency():
    # Simulate network node performance with interference
    base_signals = [12, 15, 22, 8, 33, 41, 29]
    noise_floor = 3
    adjusted_signals = []
    
    for signal in base_signals:
        if signal > 10:
            adjusted_signal = (signal - noise_floor) * 2
        else:
            adjusted_signal = signal
        adjusted_signals.append(adjusted_signal)
    
    # Irrelevant computation: simulate latency spikes (not used in final result)
    latency_spikes = [0.1 * x for x in range(len(base_signals))]
    total_latency = sum(latency_spikes)
    avg_latency = total_latency / len(latency_spikes) if latency_spikes else 0
    
    # Core data processing
    filtered_power = [p for p in adjusted_signals if p > 20]
    power_sum = sum(filtered_power)
    
    # Use of enumerate and slicing
    indexed_power = list(enumerate(filtered_power[1:], start=1))
    correction_factor = 1
    for idx, val in indexed_power:
        if idx % 2 == 0:
            correction_factor += val % 4
    
    # Set operations to deduplicate (though all are unique here)
    unique_powers = set(filtered_power)
    corrected_sum = power_sum - len(unique_powers)
    
    # Secondary distraction: simulate redundant channel checks
    channel_states = ['active', 'idle', 'active', 'faulty']
    active_channels = [c for c in channel_states if c == 'active']
    idle_channels = len([c for c in channel_states if c == 'idle'])
    
    # Aggregate throughput calculation
    aggregate_throughput = corrected_sum * 2 + correction_factor
    device_count = 5
    final_bandwidth = aggregate_throughput // device_count  # Key statement
    
    # Additional red herring: calculate efficiency ratio (unused)
    efficiency_ratio = aggregate_throughput / (device_count * 1.0) if device_count else 0
    temp_result = efficiency_ratio * 0.95
    
    print(f"Result: {final_bandwidth}")

calculate_network_efficiency()