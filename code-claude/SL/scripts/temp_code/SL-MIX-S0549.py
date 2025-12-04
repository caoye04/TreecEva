# Calculate the total area of selected geometric shapes from a dataset

# Shape data: (shape_type, area in sq units)
shape_data = [
    ('circle', 28.3),
    ('square', 16.0),
    ('triangle', 12.5),
    ('rectangle', 24.0),
    ('hexagon', 33.6),
    ('pentagon', 20.7),
    ('circle', 50.3),
    ('square', 25.0)
]

# Shapes we want to include in our calculation
target_shapes = {'square', 'rectangle', 'triangle'}

# Some preliminary analysis
all_shapes = {shape for shape, _ in shape_data}
unique_count = len(all_shapes)
average_area = sum(area for _, area in shape_data) / len(shape_data)

# Filter and calculate the total area of target shapes
filtered_area = sum(area for shape, area in shape_data if shape in target_shapes)

# Final result
print(f"Target result: {filtered_area}")