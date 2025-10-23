from collections import defaultdict

# Initial drone setup
waypoints = [(2, 3), (-1, 4), (3, -2), (-2, -1), (0, 5), (1, -3)]
energy_map = defaultdict(int)
initial_position = (0, 0)
current_position = list(initial_position)

# Movement and energy collection
for dx, dy in waypoints:
    current_position[0] += dx
    current_position[1] += dy
    coord_tuple = tuple(current_position)
    energy_map[coord_tuple] += sum(abs(x) for x in coord_tuple) + 1

# Calculate energy from even-coordinate locations
total_even_energy = sum(
    energy
    for (x, y), energy in energy_map.items()
    if x % 2 == 0 and y % 2 == 0
)

print(f"Result: {total_even_energy}")