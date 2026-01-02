from collections import Counter, defaultdict

# Simulate data ingestion from multiple sources over time
sources = ['source_A', 'source_B', 'source_A', 'source_C', 'source_A', 'source_B']
sinks = ['sink_X', 'sink_Y', 'sink_X', 'sink_Z']

# Track inflow counts by source
temp_data = [len(sources), len(sinks), len(sources) * 2]
dummy_calc = sum(temp_data) // 3
inflow_counter = Counter(sources)

# Misleading intermediate transformation (not used in final result)
transformed_sinks = [s.replace('X', 'K').upper() for s in sinks if 'Y' not in s]
dropped_entries = len(sinks) - len(transformed_sinks)

# Outflow tracking with default fallback
outflow_tracker = defaultdict(int)
for sink in sinks:
    outflow_tracker[sink] += 1

# Simulate irrelevant state variables
state_log = []
for i in range(2):
    state_log.append(f'cycle_{i}')

# Auxiliary computation that looks important but isn't directly used
baseline = inflow_counter['source_B'] + outflow_tracker['sink_Y']
correction_factor = max(outflow_tracker.values()) if outflow_tracker else 0
adjusted_baseline = baseline - correction_factor

# Key logic: compute net flow from source_A to sink_X
net_flow = inflow_counter['source_A'] - outflow_tracker.get('sink_X', 0)

# Additional red herring: unused derived metric
total_unique_endpoints = len(inflow_counter) + len(outflow_tracker)
redundant_check = total_unique_endpoints > 5

print(f'Result: {net_flow}')