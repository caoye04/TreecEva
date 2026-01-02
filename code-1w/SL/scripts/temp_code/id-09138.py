from collections import defaultdict

# System configuration for sensor node deployment
node_specs = [
    ('temperature', 'A', 16),
    ('humidity', 'B', 8),
    ('pressure', 'A', 12),
    ('light', 'C', 20),
    ('motion', 'B', 8)
]

# Irrelevant metadata (minimal distraction)
model_version = 'v2.1'
activation_threshold = 0.75

# Map to accumulate capacity per group using defaultdict
capacity_map = defaultdict(int)
for sensor_type, group, base_cap in node_specs:
    multiplier = 2 if 'A' in group else 1
    adjusted_cap = base_cap * multiplier
    capacity_map[group] += adjusted_cap

# Key computation point
total_capacity = sum(capacity_map.values())

# Print result for evaluation
print(f"Target result: {total_capacity}")