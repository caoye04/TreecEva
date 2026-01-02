data_sequence = [10, 15, 20, 25, 30, 35, 40, 45, 50]
start_index = 2
end_index = 7
sliced_data = data_sequence[start_index:end_index]

# Define a set of valid values using set operations
temp_list = [x * 2 for x in range(5)]
valid_set = set(temp_list) | {25, 35}

# Perform filtering and summation using list comprehension
filtered_sum = sum([x for x in sliced_data if x in valid_set])

# Irrelevant distraction: unused variable
unused_var = [i ** 2 for i in range(3)]

print(f"Result: {filtered_sum}")