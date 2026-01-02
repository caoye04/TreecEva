import itertools

# System health monitoring simulation with layered diagnostics

def analyze_subsystem readings(readings):
    base_score = 0
    for r in readings:
        if r < 0:
            base_score += abs(r) * 0.5
        elif r > 100:
            base_score += 1
        else:
            base_score += r * 0.1
    return int(base_score)

# Irrelevant signal preprocessing (distractor)
def filter_noise(signal, threshold=0.75):
    return [s for s in signal if s > threshold]

# Unused diagnostic mode (dead code path)
def legacy_diagnostic(data):
    return sum(d ** 0.5 for d in data if d > 10)

# Main diagnostic pipeline
sensor_inputs = [120, -5, 45, 200, 78, -15, 99]
reference_frame = {'baseline': 37.5, 'tolerance': 2.1, 'gain': 1.8}

# Complex data transformation chain (mixed relevance)
adjusted_inputs = []
for val in sensor_inputs:
    if val < 0:
        adjusted_inputs.append(abs(val) * reference_frame['gain'])
    elif val > 150:
        adjusted_inputs.append(val * 0.8)
    else:
        adjusted_inputs.append(val)

# Distractor: unused transformation sequence
temporal_sequence = list(itertools.accumulate([3, 1, 4, 1, 5], lambda x, y: x + y % 3))
expanded_view = list(itertools.product([2, 3], [4, 5]))
flattened = [item for pair in expanded_view for item in pair]

# Real computation begins here — heavily buried
raw_diagnostics = analyze_subsystem_readings(adjusted_inputs)
system_offset = int(reference_frame['baseline'] // reference_frame['tolerance'])

# Multiple red herring variables
counterfeit_index = len(flattened) * system_offset - 9
placeholder_audit = sum(temporal_sequence) / 2
mock_validation = placeholder_audit > counterfeit_index

# Core logic interlaced with decoys
diagnostic_map = {}
for i, v in enumerate(adjusted_inputs):
    diagnostic_map[f'node_{i}'] = v % 13

grouped_diagnostics = {}
for k, g in itertools.groupby(diagnostic_map.items(), key=lambda x: x[1] > 5):
    grouped_diagnostics[k] = list(g)

# Actual aggregation path (non-obvious)
valid_nodes = grouped_diagnostics.get(True, [])
aggregate_score = len(valid_nodes) * raw_diagnostics // 3

# Critical statement — answer derivation point
final_diagnostic = aggregate_score + system_offset

# Final irrelevant sort operation (misleading)
sorted_diagnostic_keys = sorted(diagnostic_map.keys(), key=lambda x: int(x.split('_')[1]), reverse=True)

print(f"Result: {final_diagnostic}")