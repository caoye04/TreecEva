import itertools

# System health monitoring with mixed computational paradigms
def analyze_node_stability(readings):
    avg = sum(readings) / len(readings)
    variance = sum((x - avg) ** 2 for x in readings) / len(readings)
    return avg, variance

# Irrelevant helper - distractor function (dead path)
def compute_fft_proxy(signal):
    """Simulate frequency domain analysis - unused in final computation"""
    proxy = 0
    for i in range(len(signal)):
        proxy += signal[i] * (i % 3)
    return proxy  # never used

# Bit manipulation red herring
def obscure_priority(level):
    shifted = (level << 3) & 0xFF
    masked = shifted ^ 0b10101010
    return masked | (level >> 2)  # computed but not contributing to answer

# Core data transformation
network_nodes = {
    'node_a': { 'metrics': [12, 15, 14, 13, 16], 'weight': 0.8, 'active': True },
    'node_b': { 'metrics': [9, 11, 10, 12], 'weight': 1.2, 'active': True },
    'node_c': { 'metrics': [18, 20, 19, 17, 21, 16], 'weight': 0.9, 'active': False },  # inactive node
    'node_d': { 'metrics': [7, 8, 6, 9, 8], 'weight': 1.1, 'active': True }
}

system_load = [0.65, 0.72, 0.78, 0.69, 0.75]
sample_waveform = [1, 2, 1, 3, 2, 1, 2]  # decoy input

# Distractor: complex but unused calculation chain
temporal_pattern = list(itertools.accumulate(system_load, lambda a, b: a * 0.7 + b * 0.3))
smoothed = [round(x, 3) for x in temporal_pattern]
fft_surrogate = compute_fft_proxy(sample_waveform)
priority_mask = obscure_priority(42)

# Intermediate irrelevant aggregation
dummy_aggregate = 0
for key, node in network_nodes.items():
    if len(node['metrics']) > 4:
        dummy_aggregate += len(node['metrics']) * node['weight']

dummy_aggregate = round(dummy_aggregate, 2)

# Real processing begins here — conditional filtering and weighted analysis
active_nodes = [node for node in network_nodes.values() if node['active']]
processed_data = []

for node in active_nodes:
    raw = node['metrics']
    weight = node['weight']
    base_avg, var = analyze_node_stability(raw)
    # Apply weight only if variance below threshold
    if var < 2.5:
        adjusted = base_avg * weight
    else:
        adjusted = base_avg * (weight * 0.8)  # penalty
    processed_data.append(adjusted)

# Secondary filter based on system load phase
load_avg = sum(system_load) / len(system_load)
if load_avg > 0.7:
    # Use top 3 values only
    sorted_vals = sorted(processed_data, reverse=True)
    selected = sorted_vals[:3]
else:
    selected = processed_data

# Final metric composition
weighted_sum = sum(selected)
correction_factor = 1.0

# Determine correction via bit logic distraction (partially relevant condition)
flag = priority_mask & 0b11111111
if flag > 100:
    correction_factor = 0.95
else:
    correction_factor = 1.05  # this will be used

# Actual final computation
aggregate = weighted_sum * correction_factor

# Red herring: dictionary mutation that doesn't affect result
diagnostics_log = {k: len(v['metrics']) for k, v in network_nodes.items()}
diagnostics_log['snapshot'] = 'stable'
diagnostics_log['final_value'] = 'placeholder'  # misleading label

# Key statement — target of query
final_diagnostic = aggregate_metrics(network_nodes, system_load)

# Supporting function defined after use (adds cognitive load)
def aggregate_metrics(nodes, load_profile):
    active_only = [n for n in nodes.values() if n['active']]
    totals = []
    for n in active_only:
        m = n['metrics']
        w = n['weight']
        mean = sum(m) / len(m)
        var = sum((x - mean) ** 2 for x in m) / len(m)
        if var < 2.5:
            val = mean * w
        else:
            val = mean * w * 0.8
        totals.append(val)
    avg_load = sum(load_profile) / len(load_profile)
    if avg_load > 0.7:
        totals = sorted(totals, reverse=True)[:3]
    net_total = sum(totals)
    # Correction tied to bit-op result from earlier
    if (priority_mask & 0xFF) > 100:
        net_total *= 0.95
    else:
        net_total *= 1.05
    return net_total

print(f"Result: {final_diagnostic}")