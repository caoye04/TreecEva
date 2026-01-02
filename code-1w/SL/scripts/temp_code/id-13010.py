def calculate_network_capacity(speeds, efficiency):
    adjusted_speeds = [speed * efficiency for speed in speeds]
    total_bandwidth = sum(adjusted_speeds)
    peak_load = max(adjusted_speeds)
    utilization_ratio = total_bandwidth / peak_load
    return int(total_bandwidth * (1 + utilization_ratio) // 2)

# Network link speeds in Mbps
test_links = (100, 200, 150, 300)
efficiency_factor = 0.85
link_speeds = list(test_links)
baseline_metric = 42  # Irrelevant metric for minimal distraction

final_capacity = calculate_network_capacity(link_speeds, efficiency_factor)
print(f"Result: {final_capacity}")