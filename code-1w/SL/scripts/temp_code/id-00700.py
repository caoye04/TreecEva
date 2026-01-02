inflows = [15, 23, 18, 9, 14]
outflows = [5, 12, 20, 7, 11]

total_in = sum(inflows)  # Irrelevant aggregation
total_out = sum(outflows)  # Irrelevant aggregation

# Key computation with slicing and summation
net_flow = sum(inflows[:3]) - sum(outflows[1:4])

Result: net_flow