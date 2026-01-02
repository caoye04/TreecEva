from collections import defaultdict

# Simulate sensor node network with location-based data
locations = ['alpha', 'beta', 'gamma', 'delta', 'epsilon']
signal_strengths = [3.2, 4.1, 2.8, 4.5, 3.7]
node_range = [150, 200, 120, 220, 180]
activation_threshold = 3.5

# Initialize storage for aggregated metrics
node_metrics = defaultdict(float)
for loc, strength in zip(locations, signal_strengths):
    node_metrics[loc] += strength

# Associate each location with its transmission capacity
transmission_data = list(zip(locations, node_range))

# Filter nodes with above-threshold signal strength
stable_nodes = [loc for loc, strength in zip(locations, signal_strengths) if strength >= activation_threshold]

# Extract transmission capacities for stable nodes only
filtered_zips = [(loc, cap) for loc, cap in transmission_data if loc in stable_nodes]

# Compute total transmission capacity of stable nodes
total_capacity = sum(capacity for _, capacity in filtered_zips)

# Irrelevant distraction: count how many letters in all location names (minimal interference)
letter_count = sum(len(loc) for loc in locations)

print(f"Result: {total_capacity}")