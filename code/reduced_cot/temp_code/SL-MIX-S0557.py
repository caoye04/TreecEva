from collections import namedtuple

# Define a Point for spatial calculations
Point = namedtuple('Point', ['x', 'y'])

# Initial RGB values
red_channel, green_channel, blue_channel = 142, 68, 233

# Step 1: Apply bitwise transformations
transformed_red = (red_channel << 2) & 255
transformed_green = (green_channel >> 1) | 64
transformed_blue = blue_channel ^ 170

# Step 2: Calculate spatial distance from origin
pixel_point = Point(transformed_red % 256, transformed_green % 256)
distance_from_origin = int((pixel_point.x ** 2 + pixel_point.y ** 2) ** 0.5)

# Step 3: Logical adjustments based on distance and blue channel
if distance_from_origin > 128 and not (transformed_blue < 100):
    adjusted_blue = transformed_blue & 240
else:
    adjusted_blue = transformed_blue | 15

# Step 4: Compute weighted luminance with bitwise masking
luminance_base = (transformed_red * 0.299) + (transformed_green * 0.587) + (adjusted_blue * 0.114)
mask = 0b11111100  # Mask to preserve higher bits
final_luminance = int(luminance_base) & mask

print(f"Result: {final_luminance}")