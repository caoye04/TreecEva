from collections import namedtuple

# Define pie characteristics
Pie = namedtuple('Pie', ['name', 'profit', 'size'])

# Available pies
available_pies = [
    Pie('Apple', 12, 3),
    Pie('Blueberry', 15, 5),
    Pie('Cherry', 10, 2),
    Pie('Pumpkin', 8, 4)
]

display_capacity = 7

# Calculate profit density and sort
pie_densities = [(pie.profit / pie.size, pie) for pie in available_pies]
pie_densities.sort(reverse=True, key=lambda x: x[0])

# Greedy selection
selected_pies = []
remaining_capacity = display_capacity

for density, pie in pie_densities:
    if pie.size <= remaining_capacity:
        selected_pies.append(pie)
        remaining_capacity -= pie.size

# Calculate total profit
max_profit = sum(pie.profit for pie in selected_pies)

print(f"Result: {max_profit}")