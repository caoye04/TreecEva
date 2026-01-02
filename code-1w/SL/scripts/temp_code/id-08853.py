from itertools import combinations, chain

def analyze_bandwidth(segments):
    total_links = 0
    bandwidth_snapshot = []
    for seg in segments:
        size = len(seg)
        total_links += size * (size - 1) // 2  # complete graph links
        if size > 2:
            bandwidth_snapshot.append(sum(seg) / len(seg))
    return total_links

# Network segment data (simulated node capacities in Mbps)
network_segments = [
    [10, 20, 30],
    [40, 50],
    [60, 70, 80, 90],
    [100]
]

# Irrelevant preprocessing: generate all 2-node subgroups (distractor)
all_pairs = list(combinations(chain.from_iterable(network_segments), 2))
pair_sums = [a + b for a, b in all_pairs if a < 60]  # partial filter, unused later

# Secondary metric: count segments above average (semi-relevant distractor)
avg_cap = sum(len(s) for s in network_segments) / len(network_segments)
large_segments = [s for s in network_segments if len(s) > avg_cap]

# Helper function to compute effective utilization
def calculate_utilization(segments):
    base_load = 0
    penalty_factor = 0.0
    for idx, segment in enumerate(segments):
        n = len(segment)
        if n == 1:
            base_load += segment[0] * 0.5
        elif n == 2:
            base_load += sum(segment) * 0.7
        else:
            # Complex case: n >= 3
            sorted_vals = sorted(segment, reverse=True)
            top_two_contribution = (sorted_vals[0] + sorted_vals[1]) * 0.8
            remainder = sum(sorted_vals[2:]) * 0.3
            base_load += top_two_contribution + remainder
            penalty_factor += 0.1 * (n - 2)
    
    # Apply penalty and normalize by number of segments
    adjusted_load = base_load * (1 - penalty_factor / len(segments))
    return int(adjusted_load)

# Unused diagnostic trace
segment_entropy = []
for s in network_segments:
    if len(s) > 1:
        mean_val = sum(s) / len(s)
        variance = sum((x - mean_val) ** 2 for x in s) / len(s)
        segment_entropy.append(variance ** 0.5)

# Key computation with moderate interference
final_capacity = calculate_utilization(network_segments)
Result: final_capacity