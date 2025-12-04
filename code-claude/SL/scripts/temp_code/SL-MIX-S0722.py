# Analyzing sensor data: counting values that meet specific criteria

temperatures = [8, 12, 15, 22, 18, 5]
humidity_levels = [45, 60, 72, 30, 51]

# Combine readings for analysis
numbers = temperatures + humidity_levels

# Some statistical calculations
average = sum(numbers) / len(numbers)
maximum = max(numbers)
minimum = min(numbers)

# Filter readings based on specific conditions
filtered_count = len(list(filter(lambda x: x % 2 == 0 and x > 10, numbers)))

# Additional processing for reporting
total_readings = len(numbers)
valid_percentage = (filtered_count / total_readings) * 100

print(f"Result: {filtered_count}")