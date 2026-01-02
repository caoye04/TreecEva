from itertools import combinations

# Simulate a water distribution network analysis
inflow_sources = [45, 12, 78, 23, 56]
outflow_sinks = [34, 21, 67, 15]

# Distractor: Calculate all possible 3-source combinations (not used in final result)
temp_combinations = list(combinations(inflow_sources, 3))
combination_count = len(temp_combinations)

# Distractor: Dummy transformation on outflows
adjusted_outflows = [x * 1.0 for x in outflow_sinks]  # No actual change

# Track cumulative metrics (semi-relevant but not final)
cumulative_in = 0
cumulative_out = 0
for i in range(len(inflow_sources)):
    cumulative_in += inflow_sources[i]
    if i < len(outflow_sinks):
        cumulative_out += outflow_sinks[i]

# Actual key computation
inflows = [x for x in inflow_sources if x > 20]  # Filter significant inflows
outflows = [x for x in outflow_sinks if x > 18]  # Filter significant outflows

# Key statement
net_flow = sum(inflows) - sum(outflows)

# Additional red herring: unused dictionary structure
flow_summary = {
    'total_in': sum(inflow_sources),
    'total_out': sum(outflow_sinks),
    'efficiency': sum(outflows) / sum(inflows) if sum(inflows) > 0 else 0
}

# Final output
Result: {net_flow}