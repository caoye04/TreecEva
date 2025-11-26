data_points = [2, 5, 8, 11, 14]
weights = [1.5, 2.0, 0.5, 1.0, 2.5]
reference_data = [3, 6, 9, 12, 15]

# Calculate weighted average
final_metric = sum(x*y for x, y in zip(data_points, weights)) / len(data_points)

print(f"Result: {final_metric}")