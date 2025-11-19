import re

color_palette = {'#FF5733', '#33FF57', '#3357FF'}
transformation = lambda x: int(x, 16) // 256

art_input = "#FF5733 and #33FF57 blended"
matches = re.findall(r'#([A-F0-9]{6})', art_input)

processed_colors = {transformation(match) for match in matches}
base_code = sum(processed_colors)

if base_code > 500:
    final_code = base_code + len(color_palette)
else:
    final_code = base_code - len(color_palette)

print(f'Result: {final_code}')