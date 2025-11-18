palette = [
    {'red': 200, 'green': 150, 'blue': 100},
    {'red': 255, 'green': 200, 'blue': 180},
    {'red': 120, 'green': 130, 'blue': 140},
    {'red': 180, 'green': 190, 'blue': 200},
    {'red': 100, 'green': 100, 'blue': 100}
]

intensities = [color['red'] + color['green'] + color['blue'] for color in palette]
matching_colors_count = sum(1 for intensity in intensities if intensity > 600)
print(f'Result: {matching_colors_count}')