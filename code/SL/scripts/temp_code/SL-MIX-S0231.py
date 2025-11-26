data_points = [12.5, 8.2, 15.7, 6.9, 20.1, 11.3]
thresholds = [10.0, 9.5, 12.0, 8.0, 18.0, 12.5]

# Calculate points above their respective thresholds
final_count = sum(1 for x, y in zip(data_points, thresholds) if x > y)

# Additional variables for context (minimal interference)
max_point = max(data_points)
min_threshold = min(thresholds)

print(f"Result: {final_count}")