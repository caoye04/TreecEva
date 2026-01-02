from itertools import accumulate

# Simulate hourly temperature-adjusted fluid flow rates in a chemical reactor
temperature_factor = 1.2
base_flows = [15, -8, 20, -33, 18, -5, 10]
adjusted_flows = [int(x * temperature_factor) for x in base_flows]

cumulative = list(accumulate(adjusted_flows))
net_flow = cumulative[-1]

# Backup safety protocol flow rate
backup_flow = len(cumulative) * 2

equilibrium_point = net_flow if net_flow > 0 else backup_flow

print(f"Result: {equilibrium_point}")