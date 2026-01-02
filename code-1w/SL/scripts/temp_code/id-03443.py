def transform(x):
    return x ** 2 + 2

# Initial data sequence
data_sequence = [1, -4, 6, 8, -10, 12, 15]

# Irrelevant distraction: unused variable
unused_offset = 7

# Slice to extract middle portion
sliced_data = data_sequence[2:5]  # [6, 8, -10]

# Filter positive values using lambda
positive_filter = filter(lambda val: val > 0, sliced_data)
filtered_sum = sum(positive_filter)  # 6 + 8 = 14

# Transform and scale result
def transform(x):
    return x ** 2 + 2

result = filtered_sum * transform(3)
print(f"Result: {result}")