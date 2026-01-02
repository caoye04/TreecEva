import itertools

# Network packet simulation with interference metrics
packet_sizes = [64, 128, 256, 512, 1024]
delay_jitter = [0.05, 0.12, 0.08, 0.15, 0.10]
error_rates = [0.001, 0.002, 0.005, 0.003, 0.004]
transmission_modes = ['TCP', 'UDP', 'QUIC']

# Irrelevant statistical tracking (distractor)
mode_distribution = {mode: 0 for mode in transmission_modes}
for i, mode in enumerate(itertools.cycle(transmission_modes)):
    if i >= len(packet_sizes):
        break
    mode_distribution[mode] += 1

# Simulate latency impact on throughput (semi-relevant)
latency_impact = []
for jitter, base_size in zip(delay_jitter, packet_sizes):
    adjusted = base_size / (1 + jitter)
    latency_impact.append(round(adjusted, 2))

# Core calculation: effective throughput per packet
throughput_per_packet = []
for size, err in zip(packet_sizes, error_rates):
    raw_tput = size * (1 - err)  # Effective data rate after errors
    throughput_per_packet.append(raw_tput)

# Aggregate total system throughput (key path)
aggregate_throughput = sum(throughput_per_packet) / len(throughput_per_packet)

# Redundant transformation (distractor)
packet_slices = packet_sizes[1:4]
slice_mean = sum(packet_slices) / len(packet_slices)
adjusted_slice = slice_mean * (1 - error_rates[2])

# Efficiency model based on jitter variance (key path)
jitter_variance = sum((x - sum(delay_jitter)/len(delay_jitter))**2 for x in delay_jitter) / len(delay_jitter)
efficiency_factor = 0.95 - (jitter_variance * 0.5)

# Final bandwidth computation (critical statement)
final_bandwidth = aggregate_throughput * efficiency_factor

# Dead code path (irrelevant)
if len(error_rates) > 10:
    final_bandwidth *= 0.9
else:
    temp_debug = [x for x in error_rates if x > 0.003]
    debug_sum = sum(temp_debug)

# Output result
print(f"Result: {final_bandwidth}")