from itertools import islice

data_stream = [42, 15, 87, 23, 56, 91, 34, 78, 12, 65]

# Process data with lambda functions and itertools
is_even = lambda x: x % 2 == 0
transform_data = lambda x: x * 2 - 10

# Create some intermediate computations
processed_chunk = list(islice(data_stream, 5))
temp_sum = sum(processed_chunk)
scaling_factor = temp_sum // 10  # This value isn't used in final calculation

# Main logic chain
filtered_items = [transform_data(x) for x in data_stream if is_even(x)]
redundant_calc = len(data_stream) * scaling_factor  # Distractor computation

final_result = sorted(filtered_items)[-1]
print(f"Result: {final_result}")