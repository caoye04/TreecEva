def analyze_performance(data):
    # Irrelevant helper function with dead logic
    peak = max(data)
    avg = sum(data) / len(data)
    deviation = [abs(x - avg) for x in data]
    threshold = avg + 0.5 * (peak - avg)
    outliers = [x for x in data if x > threshold]  # Unused
    return len(deviation)  # Not used in main logic


def calculate_utilization(rate, base):
    # Semi-relevant computation, partially distracts
    factor = 0.85 if rate > base else 1.0
    adjusted = rate * factor
    penalty = 0.9 if adjusted < 50 else 1.0
    return adjusted * penalty

# Main scenario: Calculate system capacity from mixed units and efficiency mappings
unit_specs = [
    {'id': 'U1', 'type': 'A', 'base_power': 120, 'overhead': 15},
    {'id': 'U2', 'type': 'B', 'base_power': 80, 'overhead': 10},
    {'id': 'U3', 'type': 'A', 'base_power': 140, 'overhead': 20},
    {'id': 'U4', 'type': 'C', 'base_power': 60, 'overhead': 5}
]

efficiency_map = {'A': 0.92, 'B': 0.88, 'C': 0.82}

# Extract relevant attributes using enumerate and zip (Python idioms)
indices, powers, overheads = [], [], []
for i, spec in enumerate(unit_specs):
    indices.append(i)
    powers.append(spec['base_power'])
    overheads.append(spec['overhead'])

# Misleading aggregation - looks important but not used
aggregate_metrics = list(zip(indices, powers, overheads))
weighted_overhead = sum([p * o for p, o in zip(powers, overheads)]) / sum(powers) if powers else 0

# Key transformation using lambda (required feature)
scale_factor = lambda x: x * 1.1 if x < 100 else x * 0.95
adjusted_powers = [scale_factor(p) for p in powers]

# Simulate utilization levels (some distraction here)
util_levels = []
for p in adjusted_powers:
    util = calculate_utilization(p, 100)
    util_levels.append(util)

# Real computation begins: effective throughput per unit
throughput = []
type_counters = {'A': 0, 'B': 0, 'C': 0}  # Tracking for potential extension (unused)
for i, spec in enumerate(unit_specs):
    raw_output = adjusted_powers[i] * efficiency_map[spec['type']]
    final_output = raw_output - overheads[i] * 0.7  # Net usable capacity
    throughput.append(final_output)

# Modular arithmetic to simulate cyclic load balancing
load_cycle = sum(throughput) % 7
buffer_contribution = 0
for cycle in range(int(load_cycle)):
    buffer_contribution += (cycle + 1) * 0.25

# Final capacity calculation – this is the key statement
final_capacity = sum(throughput) + buffer_contribution

# Print result as required
print(f"Result: {final_capacity}")