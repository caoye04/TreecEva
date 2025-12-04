data_points = [15, 8, 22, 13, 9]
threshold = 10

# Calculate points above threshold
filtered_points = list(filter(lambda x: x > threshold, data_points))

# Enumerate and sum indices
enumerate_result = [idx * value for idx, value in enumerate(filtered_points)]
final_count = sum(enumerate_result)

print(f"Result: {final_count}")