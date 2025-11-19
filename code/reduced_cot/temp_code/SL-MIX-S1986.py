from typing import List, Tuple

class ColorPalette:
    def __init__(self, colors: List[Tuple[int, int, int]]):
        self.colors = colors

# Define a palette with RGB color tuples
palette = ColorPalette([
    (100, 150, 200),
    (50, 75, 100),
    (200, 100, 50),
    (25, 125, 175)
])

# Extract red components using list comprehension
red_components = [color[0] for color in palette.colors]

# Calculate average red intensity
average_red = sum(red_components) // len(red_components)

# Brightness adjustment function using lambda
adjust_brightness = lambda x: x * 2 + 10

# Apply the adjustment to the average
adjusted_red_intensity = adjust_brightness(average_red)

print(f"Result: {adjusted_red_intensity}")