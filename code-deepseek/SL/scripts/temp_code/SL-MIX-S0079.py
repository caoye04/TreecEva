data_values = [3, 7, 2, 9, 5]
multiplier_list = [2, 1, 4, 3, 2]

enumerate_product = []
for index, value in enumerate(data_values):
    product = value * multiplier_list[index]
    enumerate_product.append(product)

# Some additional processing that doesn't affect the result
intermediate_sum = sum(data_values)
temp_calc = intermediate_sum * 2

final_result = sum(enumerate_product)
print(f"Result: {final_result}")