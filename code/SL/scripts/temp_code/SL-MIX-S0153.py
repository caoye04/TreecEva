def modifier_func(x):
    return x * 2 - 1

data_points = [5, 8, 12, 3, 7]
transform_data = lambda data, func: sum(func(val) for val in data[1:4])

base_value = 42
unused_var = "distraction"

final_result = transform_data(data_points, modifier_func)
print(f"Result: {final_result}")