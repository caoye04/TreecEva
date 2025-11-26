measurements = [15, 22, 8, 31, 42, 17, 24, 9, 36, 11]
threshold = 20
filtered_count = len([x for x in measurements if x >= threshold and x % 2 == 0])
print(f"Result: {filtered_count}")