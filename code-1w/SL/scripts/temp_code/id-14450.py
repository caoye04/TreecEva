def transform_data(values, limit):
    filtered = [x for x in values if x % 2 == 1]  # Keep odd numbers
    processed = list(map(lambda x: (x ** 2) % limit, filtered))
    return sum(processed[:3])

# Sensor readings with modular constraints
data = [17, 22, 13, 8, 19, 4, 25]
threshold = 10
offset = 5  # Unused variable (minor distraction)
temp_buffer = [0] * 3  # Irrelevant pre-allocation

result = transform_data(data, threshold)
print(f"Result: {result}")