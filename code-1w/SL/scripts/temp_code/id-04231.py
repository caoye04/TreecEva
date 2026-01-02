from itertools import combinations

def calculate_link_utilization(bandwidth, users):
    base_util = bandwidth * 0.8
    adjustment = len(users) * 0.05
    return min(base_util * (1 + adjustment), bandwidth)

def calculate_network_capacity(bandwidths, redundancy):
    active_links = bandwidths[1:-1]
    total = sum(active_links)
    if redundancy > 1:
        backup_ratio = 1 / redundancy
        total -= total * backup_ratio
    return int(total)

def analyze_coverage(zones):
    covered = 0
    for zone in zones:
        if zone['status'] == 'active':
            covered += 1
    return covered

# System link bandwidths in Mbps
link_bandwidths = [100, 200, 150, 180, 90, 120]
redundancy_factor = 3

# Irrelevant auxiliary data (minimal distraction)
devices = ['router_a', 'switch_b', 'firewall_x']
topology_pairs = list(combinations(devices, 2))

# Key computation
final_capacity = calculate_network_capacity(link_bandwidths, redundancy_factor)

# Print result
print(f"Result: {final_capacity}")