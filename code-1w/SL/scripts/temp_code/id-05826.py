from collections import defaultdict

# Simulate resource allocation in a distributed node system
def calculate_node_capacity():
    base_nodes = 12
    expansion_factor = 1.75
    decay_rate = 0.92
    temp_storage = []

    # Initialize node health and load metrics
    node_health = defaultdict(lambda: 100)
    for i in range(base_nodes):
        if i % 5 == 0:
            node_health[i] -= 15
        elif i % 3 == 0:
            node_health[i] -= 8

    # Simulate dynamic load balancing over time intervals
    time_intervals = 6
    cumulative_load = 0
    peak_fluctuation = 0
    historical_peaks = []

    for t in range(1, time_intervals + 1):
        current_load = (t * expansion_factor * 18) * (decay_rate ** t)
        if t % 2 == 0:
            current_load *= 1.15  # transient surge
        cumulative_load += current_load
        
        fluctuation = abs(current_load - (t * expansion_factor * 18))
        if fluctuation > peak_fluctuation:
            peak_fluctuation = fluctuation
            
        historical_peaks.append(fluctuation * 0.87)

    average_peak = sum(historical_peaks) / len(historical_peaks) if historical_peaks else 0

    # Redundant health summary (not used in final calculation)
    healthy_count = sum(1 for h in node_health.values() if h >= 90)
    degraded_count = base_nodes - healthy_count
    health_ratio = healthy_count / base_nodes if base_nodes else 0

    # Core capacity logic
    nominal_capacity = base_nodes * 90
    system_utilization = int(cumulative_load * 0.42)

    # Buffer logic with misleading intermediate steps
    ideal_buffer = nominal_capacity * 0.1
    risk_factor = 0.7 if degraded_count > 3 else 1.2
    volatility_discount = average_peak * 0.05
    
    # Irrelevant conditional branch (dead code due to logic)
    if health_ratio > 1.0:
        risk_factor *= 0.9
    else:
        temp_storage.append(ideal_buffer * 0.3)

    projected_buffer = ideal_buffer * risk_factor - volatility_discount
    buffer_adjustment = max(int(projected_buffer), 5)

    # Key statement
    final_capacity = system_utilization + buffer_adjustment
    
    # Print result as required
    print(f"Result: {final_capacity}")
    
    return final_capacity

# Execute function
calculate_node_capacity()