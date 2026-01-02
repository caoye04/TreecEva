from collections import Counter, defaultdict

# Simulate data ingestion from multiple sources with filtering
raw_events = [
    ('source_A', 'ingest', 12), ('source_B', 'ingest', 8), ('source_A', 'drop', 3),
    ('source_C', 'ingest', 15), ('source_A', 'ingest', 5), ('source_B', 'drop', 2),
    ('source_A', 'ingest', 7), ('source_C', 'drop', 4)
]

# Irrelevant aggregation - distractor
latency_log = defaultdict(float)
for src, op, size in raw_events:
    if op == 'ingest':
        latency_log[src] += 0.15 * size  # Simulated processing delay

# Partial extraction - only care about source_A ingests
inflow_data = [size for src, op, size in raw_events if src == 'source_A' and op == 'ingest']
outflow_events = [('sink_X', 9), ('sink_Y', 6), ('sink_Z', 4)]

# Track inflows using Counter
inflow_counter = Counter(inflow_data)  # Counts frequency of each ingest size

# Misleading transformation: normalize inflow to percentages (unused)
total_inflow = sum(inflow_counter.values())
normalized_ratios = {
    k: round(v / total_inflow, 3) for k, v in inflow_counter.items()
} if total_inflow else {}

# Outflow tracking via dictionary
outflow_tracker = {}
for sink, volume in outflow_events:
    outflow_tracker[sink] = outflow_tracker.get(sink, 0) + volume

# Dead code path - never accessed
if 'debug_mode' in locals():
    print(f"Normalized: {normalized_ratios}")

# Key computation point
net_flow = inflow_counter['source_A'] - outflow_tracker.get('sink_X', 0)

# Additional red herring calculation
weighted_score = sum(k * v for k, v in inflow_counter.items()) / total_inflow if total_inflow else 0

# Final output
Result: net_flow