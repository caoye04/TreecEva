import re

color_palette = ['#FFA07A', '#7B68EE', '#00FA9A', '#FF1493', '#20B2AA', '#FFD700', '#8A2BE2', '#A52A2A', '#5F9EA0', '#D2691E']
featured_colors_count = sum(1 for color in color_palette if re.search(r'A', color))
print(f'Result: {featured_colors_count}')