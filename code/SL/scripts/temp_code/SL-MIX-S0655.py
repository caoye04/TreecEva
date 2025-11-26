network_devices = ['router', 'switch', 'firewall', 'load_balancer']
device_throughput = [120, 85, 65, 95]
connection_weights = [1.2, 0.8, 1.1, 0.9]

# Calculate raw throughput for each device
raw_throughputs = []
for i, (device, throughput) in enumerate(zip(network_devices, device_throughput)):
    weighted = throughput * connection_weights[i]
    raw_throughputs.append(weighted)

# Distractor calculations that don't affect final result
device_count = len(network_devices)
average_throughput = sum(device_throughput) / device_count

# Calculate total throughput (relevant)
total_throughput = sum(raw_throughputs)

# Calculate network overhead (relevant)
base_overhead = 25
protocol_penalty = 8
network_overhead = base_overhead + protocol_penalty

# Unused intermediate calculation
max_capacity = max(device_throughput) * 1.5

# Final calculation
net_bandwidth = total_throughput - network_overhead

print(f"Net bandwidth: {net_bandwidth}")