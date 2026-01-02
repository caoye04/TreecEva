def analyze_distribution(data):
    frequency = {}
    for item in data:
        frequency[item] = frequency.get(item, 0) + 1
    return frequency

# Simulate resource allocation across distributed nodes
def calculate_node_load(node_id, base_load, modifiers):
    temp_score = 0
    for mod in modifiers:
        if mod == 'boost':
            temp_score += 3
        elif mod == 'drain':
            temp_score -= 2
    adjusted_load = base_load + temp_score
    return max(adjusted_load, 0)

resource_map = {
    'node_a': [8, ['boost', 'boost']],
    'node_b': [5, ['drain', 'boost']],
    'node_c': [7, ['boost']],
    'node_d': [4, ['drain', 'drain']]
}

allocation_log = set()
buffer_cache = []

for node, (load, mods) in resource_map.items():
    allocation_log.add(f'{node}_allocated')
    load_value = calculate_node_load(node, load, mods)
    buffer_cache.append(load_value * 1.1)

# Track character patterns in node identifiers
node_chars = ''.join(resource_map.keys())
char_freq = analyze_distribution(node_chars)
dominant_char_count = max(char_freq.values())

# Misleading intermediate calculation (distractor)
total_buffered = sum(buffer_cache)
avg_buffered = total_buffered / len(buffer_cache) if buffer_cache else 0

# Core logic: capacity depends on char diversity and adjusted loads
effective_nodes = 0
max_load = 0

for node, (base, _) in resource_map.items():
    adjusted = calculate_node_load(node, base, resource_map[node][1])
    if adjusted > 3:
        effective_nodes += 1
    if adjusted > max_load:
        max_load = adjusted

# Use set operations to simulate redundancy elimination
redundant_keys = {k for k in resource_map if 'a' in k}
active_keys = set(resource_map.keys()) - redundant_keys
utilization_factor = len(active_keys) / len(resource_map) if resource_map else 0

# Final capacity calculation (key statement)
final_capacity = (effective_nodes * max_load) + (dominant_char_count ** 2)

# Print result for evaluation
print(f"Result: {final_capacity}")