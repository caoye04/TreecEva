import math

# Simulated network node data with health metrics
def generate_node_data():
    nodes = []
    for i in range(16):
        node = {
            'id': f'N{i:02d}',
            'load': (i * 7.5) % 100,
            'temp': 45 + (i * 3) % 40,
            'uptime': 1000 + i * 100,
            'errors': max(0, int((i - 5) ** 1.5))
        }
        nodes.append(node)
    return nodes

# Irrelevant helper - looks important but unused in critical path
def compute_fusion_score(records):
    total = 0
    for r in records:
        if r['load'] > 70:
            total += r['temp'] * 0.3
    return round(total, 2)

# Distraction function: processes latency but not used in final result
def analyze_latency_pattern(nodes):
    latencies = [((n['load'] * n['temp']) / 100) for n in nodes]
    avg_lat = sum(latencies) / len(latencies)
    threshold_count = len([l for l in latencies if l > avg_lat])
    return threshold_count * 0.7  # red herring

# Real processing begins here
network_nodes = generate_node_data()

# Distractor: filtering nodes by arbitrary criteria (not affecting final result)
high_load_nodes = [n for n in network_nodes if n['load'] > 60]
overheated_nodes = [n for n in network_nodes if n['temp'] > 80]

# More distraction: fake recalibration process
baseline_offset = 0.95
for node in network_nodes:
    node['calibrated_load'] = node['load'] * baseline_offset  # unused later
    node['stability_index'] = math.cos(math.radians(node['temp']))  # dead calculation

# Begin actual relevant computation chain
active_count = len([n for n in network_nodes if n['uptime'] > 1500])

# Compute error-weighted temperature (only some nodes contribute)
weighted_temps = []
for node in network_nodes:
    weight = 1
    if node['errors'] > 3:
        weight *= 0.8
    if node['load'] > 75:
        weight *= 0.9
    weighted_temps.append(node['temp'] * weight)

# Summation point - relevant
weighted_avg_temp = sum(weighted_temps) / len(weighted_temps)

# Another irrelevant transformation
transformed_metrics = {
    f"node_{n['id']}": {
        'score': (n['load'] - n['errors']) * n['stability_index']
    } for n in network_nodes
}

# Critical data restructuring: group by load quartile
quartile_breaks = [0, 25, 50, 75, 100]
node_quartiles = {i: [] for i in range(4)}
for node in network_nodes:
    q_idx = 0
    for j in range(3):
        if node['load'] >= quartile_breaks[j+1]:
            q_idx += 1
    node_quartiles[q_idx].append(node)

# Decoy accumulation - looks like aggregation but unused
shadow_accumulator = 0
for q in sorted(node_quartiles.keys()):
    q_max_temp = max(node['temp'] for node in node_quartiles[q])
    shadow_accumulator += q_max_temp * (q + 1)

# Real signal: count nodes in high-risk category (high load + high temp + errors)
risk_threshold = 0.75
risk_factor_lookup = {}
for node in network_nodes:
    risk_score = 0
    if node['load'] > 70:
        risk_score += 0.4
    if node['temp'] > 75:
        risk_score += 0.35
    if node['errors'] > 2:
        risk_score += 0.25
    risk_factor_lookup[node['id']] = risk_score

high_risk_nodes = [nid for nid, rs in risk_factor_lookup.items() if rs >= risk_threshold]

# Begin multi-step diagnostic logic
base_diagnostic = len(high_risk_nodes) * 100

# Secondary correction factor based on quartile distribution
quartile_3_nodes = node_quartiles[3]
correction_factor = len(quartile_3_nodes) * 1.5 if weighted_avg_temp > 60 else len(quartile_3_nodes) * 0.8

# Tertiary adjustment using mathematical combination
entropy_component = 0
if len(high_risk_nodes) > 0:
    p_vals = [risk_factor_lookup[nid] / sum(risk_factor_lookup.values()) for nid in high_risk_nodes]
    entropy_component = -sum(p * math.log(p) for p in p_vals if p > 0)

intermediate_diagnostic = base_diagnostic + correction_factor

# Final aggregation uses list comprehension and dict op - key step
quartile_3_ids = [n['id'] for n in quartile_3_nodes]
name_hash_sum = sum([sum([ord(c) for c in node_id]) for node_id in quartile_3_ids])
dict_overlay = {i: name_hash_sum % (i + 5) for i in range(5)}
overlay_adjustment = sum(dict_overlay.values())

# KEY STATEMENT
final_diagnostic = aggregate_metrics(network_nodes)

# Actual definition of the aggregation function - defined late to obscure flow
def aggregate_metrics(nodes):
    # Recompute only essential elements to simulate stateless processing
    high_risk = []
    for n in nodes:
        score = 0
        score += 0.4 if n['load'] > 70 else 0
        score += 0.35 if n['temp'] > 75 else 0
        score += 0.25 if n['errors'] > 2 else 0
        if score >= 0.75:
            high_risk.append(n)
    
    base = len(high_risk) * 100
    
    # Recalculate quartile membership inside function
    q3 = [n for n in nodes if n['load'] >= 75]
    corr = len(q3) * 1.5 if sum(n['temp'] for n in q3) / len(q3) > 60 else len(q3) * 0.8
    
    # Hash-based adjustment from node IDs in Q3
    q3_hashes = [sum(ord(c) for c in n['id']) for n in q3]
    hash_sum = sum(q3_hashes)
    adjustment_map = {i: hash_sum % (i + 5) for i in range(5)}
    inner_adj = sum(adjustment_map.values())
    
    return int(base + corr + inner_adj)

print(f"Target result: {final_diagnostic}")