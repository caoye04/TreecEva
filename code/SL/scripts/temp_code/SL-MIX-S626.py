import math

def hex_to_rgb(value):
    value = value.lstrip('#')
    lv = len(value)
    return tuple(int(value[i:i + lv // 3], 16) for i in range(0, lv, lv // 3))

def rgb_to_hex(rgb):
    return '#{:02x}{:02x}{:02x}'.format(*rgb)

color_palette = ['#ff5733', '#33ff57', '#3357ff']
transformed_colors = []

for hex_code in color_palette:
    r, g, b = hex_to_rgb(hex_code)
    r = r ^ (g & 0b11110000) if r > 100 else r | 0b00001111
    g = g >> 2 if g % 4 == 0 else g << 1
    b = int(math.sqrt(b) * 10) if b > 100 else b * 2
    transformed_colors.append((r, g, b))

luminance_values = [
    0.299 * rgb[0] + 0.587 * rgb[1] + 0.114 * rgb[2]
    for rgb in transformed_colors
]

is_bright = [lum > 50 for lum in luminance_values]
adjusted_colors = [
    (rgb[0] + 10 if bright else rgb[0] - 5,
     rgb[1] + 20 if bright else rgb[1] - 10,
     rgb[2] + 30 if bright else rgb[2] - 15)
    for rgb, bright in zip(transformed_colors, is_bright)
]

final_hue = sum(
    map(lambda x: x[0] ^ x[1] ^ x[2], adjusted_colors)
) % 256
print(f"Result: {final_hue}")