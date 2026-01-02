def calculate_network_capacity(speeds, efficiency):
    adjusted_speeds = [s * efficiency for s in speeds]
    total_bandwidth = sum(adjusted_speeds)
    penalty = 0
    if len(speeds) > 3:
        penalty = total_bandwidth * 0.1
    return int(total_bandwidth - penalty)

# Network link speeds in Mbps
devices = ['router', 'switch', 'bridge', 'repeater']
link_speeds = [100, 200, 150, 300]
efficiency_factor = 0.85

# Irrelevant device count tracking (distractor)
device_count = len(devices)
max_speed = max(link_speeds)

final_capacity = calculate_network_capacity(link_speeds, efficiency_factor)
print(f"Result: {final_capacity}")