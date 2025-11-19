from collections import defaultdict

def rgb_to_hsv(r, g, b):
    r, g, b = r/255.0, g/255.0, b/255.0
    mx = max(r, g, b)
    mn = min(r, g, b)
    df = mx-mn
    if mx == mn:
        h = 0
    elif mx == r:
        h = (60 * ((g-b)/df) + 360) % 360
    elif mx == g:
        h = (60 * ((b-r)/df) + 120) % 360
    elif mx == b:
        h = (60 * ((r-g)/df) + 240) % 360
    return round(h)

# Digital art palette colors
artistic_palette = [
    (255, 0, 0), (0, 255, 0), (0, 0, 255),
    (255, 255, 0), (255, 0, 255), (0, 255, 255),
    (128, 0, 128), (255, 165, 0), (75, 0, 130)
]

# Convert RGB to HSV and collect unique hues
hue_values = {rgb_to_hsv(r, g, b) for r, g, b in artistic_palette}

# Count primary hues (red-orange to violet range)
hue_classification = {
    'primary': [h for h in hue_values if (0 <= h <= 60) or (300 <= h < 360)],
    'secondary': [h for h in hue_values if 60 < h < 300]
}

primary_hue_count = len(hue_classification['primary'])

print(f"Result: {primary_hue_count}")