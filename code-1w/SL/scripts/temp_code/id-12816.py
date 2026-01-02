def transform_data(values):
    squared = [(x - 10) ** 2 for x in values]
    filtered = list(filter(lambda y: y > 50, squared))
    adjusted = [z - 25 for z in filtered]
    return sum(adjusted)

raw_values = [12, 15, 7, 3, 18]
temp_var_ignore = [x * 2 for x in raw_values]  # Irrelevant operation (distractor)
result = transform_data(raw_values)
print(f"Result: {result}")