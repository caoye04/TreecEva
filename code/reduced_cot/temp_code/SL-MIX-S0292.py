pastry_data = {
    'croissant': (20, 30),
    'muffin': (15, 20),
    'danish': (25, 35),
    'scone': (10, 15),
    'bagel': (30, 40)
}

# Transform pastry data to list of (popularity, cost, name)
pastry_list = [(pop, cost, name) for name, (pop, cost) in pastry_data.items()]

# Calculate popularity per cost ratio and sort in descending order
pastry_efficiency = sorted(
    [(pop / cost, pop, cost, name) for pop, cost, name in pastry_list],
    key=lambda x: x[0],
    reverse=True
)

budget = 100
max_popularity = 0

for _, pop, cost, name in pastry_efficiency:
    if cost <= budget:
        max_popularity += pop
        budget -= cost

print(f'Result: {max_popularity}')