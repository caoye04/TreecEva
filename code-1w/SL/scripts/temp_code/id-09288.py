def analyze_traffic(patterns):
    traffic_score = 0
    for p in patterns:
        if len(p) > 4:
            traffic_score += sum([ord(c) % 5 for c in p[:3]])
    return traffic_score

resource_map = {'node_a': 180, 'node_b': 210, 'node_c': 150}
efficiency_log = [0.88, 0.92, 0.76, 0.81]

# Simulate network load distribution
total_load = sum(resource_map.values())
avg_load = total_load / len(resource_map)
adjusted_efficiency = [e * 100 for e in efficiency_log if e >= 0.8]

# Irrelevant string processing (distractor)
payload_templates = ['HDRv2', 'ACKx3', 'META4', 'INITq']
encoded_headers = []
for template in payload_templates:
    parts = template.split('v')
    if len(parts) == 1:
        parts = template.split('x')
    encoded_headers.append(parts[0].lower())

# Misleading statistical computation
median_efficiency = sorted(efficiency_log)[len(efficiency_log)//2]
variance_proxy = sum((e - median_efficiency)**2 for e in efficiency_log) / len(efficiency_log)

# Real logic begins: map resources with efficiency
weighted_capacity = 0
for i, (node, base_cap) in enumerate(resource_map.items()):
    scaling_factor = efficiency_log[i % len(efficiency_log)]
    boosted = base_cap * scaling_factor
    if boosted > 180:
        boosted += 10  # bonus for high performers
    weighted_capacity += boosted

# Secondary adjustment using string-derived weights
token_weights = {}
for idx, token in enumerate(encoded_headers):
    weight = sum(ord(c) - 96 for c in token if c.isalpha())
    token_weights[f't{idx}'] = weight

# Dummy aggregation (not used but looks relevant)
aggregated_tokens = list(zip(payload_templates, adjusted_efficiency))
traffic_summary = {t: analyze_traffic([t]) for t in payload_templates}

# Core allocation optimization
scaling_offset = sum(token_weights.values()) / len(token_weights)
def optimize_allocation(resources, efficiencies):
    base_total = sum(resources.values())
    eff_multiplier = sum(efficiencies) / len(efficiencies)
    adjusted_total = base_total * eff_multiplier
    final_scale = adjusted_total / (avg_load + scaling_offset)
    return int((weighted_capacity + final_scale) // 2.5)

final_bandwidth = optimize_allocation(resource_map, efficiency_log)
print(f"Target result: {final_bandwidth}")