data = [12, 7, 18, 25, 9, 14, 21, 8, 15]
# This calculates the count of numbers divisible by 3
filtered_count = len([x for x in data if x % 3 == 0])
print(f"Result: {filtered_count}")