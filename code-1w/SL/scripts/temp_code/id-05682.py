import math

# Simulated network telemetry and health monitoring system
def analyze_packet_flow(raw_samples):
    sample_peaks = [max(x, x + 3) for x in raw_samples if x % 2 == 1]
    filtered_signals = list(map(lambda x: x * 1.5 if x > 10 else x * 0.8, sample_peaks))
    return sum(filtered_signals) // len(filtered_signals)


def compute_entropy(data_stream):
    entropy = 0.0
    freq_map = {}
    for item in data_stream:
        freq_map[item] = freq_map.get(item, 0) + 1
    total = len(data_stream)
    for count in freq_map.values():
        prob = count / total
        entropy -= prob * math.log2(prob)
    return round(entropy, 4)

# Irrelevant helper (distractor)
def deprecated_checksum(seq):
    return sum(seq) % 7

# Unused function (dead code path)
def legacy_normalization(vec):
    norm = sum([x**2 for x in vec]) ** 0.5
    return [x/norm for x in vec] if norm else vec

# Misleading intermediate transformation
temp_offset = 42
redundant_buffer = [i * 2 for i in range(15) if i % 3 != 0]
shadow_mask = {x for x in redundant_buffer if x > 20}

# Core signal processing chain
raw_telemetry = [12, 7, 19, 4, 23, 8, 11]
signal_baseline = analyze_packet_flow(raw_telemetry)

# Simulated subsystem diagnostics
health_indicators = [True, False, True, True]
active_nodes = sum(1 for x in health_indicators if x)
node_ratio = active_nodes / len(health_indicators)

# Decoy calculation with plausible but unused result
phantom_metric = (signal_baseline * node_ratio * 100) // 1

# Real data path begins here
working_set = {x for x in raw_telemetry if x > 9}
low_power_nodes = {7, 8, 12}
coverage_gap = working_set - low_power_nodes

# Bit manipulation red herring
bit_flag = 0b1010 ^ 0b1100 & 0b1111
masked_integrity = bit_flag << 2

# Conditional decoy branch (never taken)
if len(coverage_gap) < 2:
    masked_integrity += 1000
else:
    diagnostic_trace = [math.ceil(signal_baseline), int(node_ratio * 10)]

# Key data structures
network_signature = sorted(list(coverage_gap))
system_health = {
    'status': 'nominal',
    'readings': diagnostic_trace,
    'checksum': deprecated_checksum(network_signature)
}

# Complex aggregation logic
irrelevant_aggregate = sum(redundant_buffer) // 3
auxiliary_weight = len(shadow_mask) * 1.5

# Critical computation with set-based logic
def aggregate_metrics(signature, health_report):
    base_score = sum(signature) * health_report['readings'][0]
    adjustment = 0
    if len(signature) >= 3:
        adjustment += health_report['readings'][1] * 2
    # Logical short-circuit distraction
    safety_lock = (len(signature) > 5) and (signature[0] > 100)
    override_flag = not safety_lock or (base_score < 0)
    if override_flag and not safety_lock:
        adjustment -= 5
    else:
        adjustment += 3

    # Final transformation using integer division and rounding
    raw_final = (base_score + adjustment) // 1.5
    return int(round(raw_final))

# Execution point of interest
final_diagnostic = aggregate_metrics(network_signature, system_health)
print(f"Result: {final_diagnostic}")