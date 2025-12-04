data_points = [3, 7, 2, 9, 4]
weights = [1, 2, 3, 4, 5]
temp_sum = 0
total_count = 0

for i, val in enumerate(zip(data_points, weights)):
    point, weight = val
    temp_sum += point * weight
    if i % 2 == 0:
        total_count += weight

print(f"Result: {total_count}")