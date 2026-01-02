def calculate_network_utilization(packets, bandwidth):
    transmission_times = list(map(lambda p: round(p / bandwidth, 3), packets))
    usage_levels = [min(t * 100, 100) for t in transmission_times]
    
    # Irrelevant metadata (low interference)
    device_id = "NET-001"
    log_timestamp = "2024-05-21T10:00:00Z"
    
    peak_utilization = max(usage_levels)
    return peak_utilization

# Input data
packets = [1250, 800, 1500, 600, 1100]
bandwidth = 10

result = calculate_network_utilization(packets, bandwidth)
print(f"Target result: {result}")