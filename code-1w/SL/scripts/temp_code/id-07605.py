from itertools import compress, cycle

# Simulate sensor readings across distributed nodes
node_signals = [12, 15, 10, 8, 23, 19, 27, 30, 25, 20, 18, 22]
threshold = 20

# Irrelevant baseline calibration (distractor)
calibration_offset = sum([x * 0.1 for x in range(len(node_signals))])
baseline_adjusted = [sig + 0.5 for sig in node_signals]

# Extract high-activity segments using slicing and masking
high_load_mask = [sig > threshold for sig in node_signals]
active_segments = list(compress(node_signals, high_load_mask))

# Secondary filtering with lambda-based dynamic threshold
age_cycles = [4, 6, 3, 7, 5, 8, 2, 9, 1, 4, 6, 5]
dynamic_filter = lambda signal, age: signal > (18 + age * 0.3)
filtered_by_age = [s for s, a in zip(node_signals, age_cycles) if dynamic_filter(s, a)]

# State tracker for operational integrity (some distraction)
operational_nodes = []
for idx, signal in enumerate(node_signals):
    if signal >= 10 and age_cycles[idx] < 8:
        operational_nodes.append(idx)
    else:
        continue
    if signal > 25:  # Early break on critical node
        break

# Auxiliary computation: nominal load profile (semi-relevant)
nominal_load = 0
for seg in active_segments:
    nominal_load += seg * 0.8

# Core diagnostic logic
system_diagnostic = lambda nodes: sum(
    node_signals[i] ** 2 for i in nodes if i % 2 == 0
) // (len(nodes) or 1)

# Critical execution point
final_analysis = system_diagnostic(operational_nodes)

# Tracking peak capacity from filtered physical limits
peak_capacity = max(filtered_by_age) * len(active_segments) // 2

# Additional red herring: cyclic padding (unused)
padded_stream = list(zip(baseline_adjusted, cycle([0.0])))[::2]

print(f"Result: {peak_capacity}")