from collections import Counter

# Simulate sensor readings for fluid flow in a chemical plant
readings = [
    ('in', 12), ('in', 15), ('out', 8), ('in', 10),
    ('out', 12), ('out', 5), ('in', 18), ('out', 9)
]

# Extract flow types and values
types, values = zip(*readings)

# Count occurrence of each flow type
type_count = Counter(types)

# Calculate total inflow and outflow using list comprehensions
inflow_values = [v for t, v in readings if t == 'in']
outflow_values = [v for t, v in readings if t == 'out']

inflow_sum = sum(inflow_values)
outflow_sum = sum(outflow_values)

# Critical assignment: compute net fluid flow
net_flow = inflow_sum - outflow_sum

# Print result as required
print(f"Result: {net_flow}")