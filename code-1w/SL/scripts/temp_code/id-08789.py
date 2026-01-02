from collections import Counter, defaultdict

# Simulate data flow monitoring in a network node
packets = [
    ('source_A', 'sink_X'), ('source_B', 'sink_Y'),
    ('source_A', 'sink_Z'), ('source_C', 'sink_X'),
    ('source_A', 'sink_X'), ('source_B', 'sink_Y'),
    ('source_D', 'sink_Z'), ('source_A', 'sink_Y')
]

# Track incoming packets by source
inflow_counter = Counter(src for src, _ in packets)

# Track outgoing packets by sink
outflow_tracker = defaultdict(int)
for _, dst in packets:
    outflow_tracker[dst] += 1

# Auxiliary computation: packet distribution analysis (semi-relevant)
distribution_score = sum(min(inflow_counter[src], outflow_tracker[dst]) for src, dst in packets)

# Secondary metrics (distractor computations)
total_unique_sources = len(inflow_counter)
max_outflow = max(outflow_tracker.values())
avg_inflow_per_source = sum(inflow_counter.values()) / len(inflow_counter)

# Dead code path - never executed but looks relevant
if False:
    correction_factor = 0.9
    for k in inflow_counter:
        inflow_counter[k] = int(inflow_counter[k] * correction_factor)

# Key state variables with distractions
temporary_buffer = [inflow_counter[s] for s in inflow_counter if s.startswith('source_')]
spurious_sum = sum([x*x for x in temporary_buffer if x > 1])  # unused downstream

# Critical calculation point
net_flow = inflow_counter['source_A'] - outflow_tracker.get('sink_X', 0)

# Additional red herring: reverse mapping that isn't used
reverse_lookup = {v: k for k, v in outflow_tracker.items()}

# Final output
print(f"Result: {net_flow}")