palette_alpha = {'#FF5733', '#33FF57', '#3357FF', 'FFCA33'}
palette_beta = {'#FF33A8', '#A833FF', '#33FFCA', '#FFFF00', 'invalid_color'}

merged_palette = palette_alpha | palette_beta
filtered_palette = {color for color in merged_palette if color.startswith('#') and len(color) == 7}
color_count = len(filtered_palette)
final_count = color_count & 15

print(f'Result: {final_count}')