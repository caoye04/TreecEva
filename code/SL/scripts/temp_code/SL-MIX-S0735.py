def apply_filter(data_tuple):
    filter_func = lambda x: x * 2 if x > 5 else x + 3
    return tuple(filter_func(item) for item in data_tuple)

def convert_data(points):
    conversion = lambda x: x - 1
    return tuple(conversion(p) for p in points)

data_points = (8, 4, 7, 2)
converted_data = convert_data(data_points)
final_processing = apply_filter(converted_data)
processed_value = sum(final_processing)
print(f"Result: {processed_value}")