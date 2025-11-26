data = [12, 7, 25, 18, 9, 14, 30, 22, 15, 8]
threshold = 20
filtered_data = [x for x in data if x > threshold]
filtered_count = len([x for x in data if x % 3 == 0 or x % 5 == 0])
print(f"Result: {filtered_count}")