import itertools

data_points = [12, 8, 15, 6, 9, 11, 7]
processed_data = 0
divisor = 3

for combo in itertools.combinations(data_points, 2):
    if sum(combo) > 20:
        processed_data += sum(combo)

result = processed_data
divisor = 4
processed_data = result // divisor

print(f"Target result: {processed_data}")