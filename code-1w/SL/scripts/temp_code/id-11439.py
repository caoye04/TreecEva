def calculate_net_flow(inflow_set, outflow_set):
    common_nodes = inflow_set.intersection(outflow_set)
    adjustment = sum(map(lambda x: x * 0.1, common_nodes))
    base_inflow = sum(inflow_set)
    base_outflow = sum(outflow_set)
    net_flow = base_inflow - base_outflow - adjustment
    return int(net_flow)

# Simulate fluid network node flows
inflows = {10, 25, 30, 45, 50}
outflows = {20, 30, 40, 50, 60}

# Irrelevant auxiliary variable (minor distraction)
temp_log = "Flow reading complete"

net_flow = calculate_net_flow(inflows, outflows)
print(f"Target result: {net_flow}")