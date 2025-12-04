import itertools

# Analyzing product dimensions for packaging
width_options = [3, 5, 7]
height_options = [2, 4, 6]
depth_options = [4, 8, 12]

# Store manager wants to know how many dimension combinations will fit through the door
door_width = 10

# Generate all possible dimension combinations
product_combinations = list(itertools.product(width_options, height_options, depth_options))

# Count items where width + height > depth (these require special handling)
valid_combinations = len(list(filter(lambda x: x[0] + x[1] > x[2], product_combinations)))

# Count items where any dimension exceeds door width
oversize_items = sum(1 for combo in product_combinations if max(combo) > door_width)

# Calculate average depth of all products
average_depth = sum(combo[2] for combo in product_combinations) / len(product_combinations)

print(f"Result: {valid_combinations}")