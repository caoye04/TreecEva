from collections import Counter

elevation_data = "E:15 E:22 E:15 E:33 E:22 E:44 E:55 E:66 E:22 E:77"
tokens = elevation_data.split()
elevation_values = []

for token in tokens:
    if token.startswith('E:'):
        try:
            elevation_values.append(int(token[2:]))
        except ValueError:
            pass

elevation_counter = Counter(elevation_values)
unique_elevations = frozenset(elevation_counter.keys())
even_elevation_sum = sum(e for e in unique_elevations if e % 2 == 0)
terrain_stability_score = len(unique_elevations) * even_elevation_sum

print(f"Result: {terrain_stability_score}")