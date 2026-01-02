def calculate_network_capacity(bandwidths, weights):
    total = 0
    for i, bw in enumerate(bandwidths):
        weight = weights[i % len(weights)]
        adjusted_bw = bw * weight
        if adjusted_bw > 50:
            total += adjusted_bw // 10
        else:
            total += adjusted_bw // 5
    return total

# Network link bandwidths in Mbps
link_bandwidths = [80, 30, 60, 25]

# Node importance weights
node_weights = [1.5, 2.0, 1.0]

# Irrelevant auxiliary variable (minor distraction)
baseline_threshold = 40

final_capacity = calculate_network_capacity(link_bandwidths, node_weights)
print(f"Result: {final_capacity}")