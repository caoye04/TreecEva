croissants_produced = 65
sourdough_loaves = 25
bonus_points = 0

if croissants_produced >= 50 and sourdough_loaves >= 30:
    bonus_points = 2 * croissants_produced + 3 * sourdough_loaves
else:
    bonus_points = 0

print(f'Result: {bonus_points}')