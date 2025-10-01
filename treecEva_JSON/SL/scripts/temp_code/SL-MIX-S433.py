import math

def transform_data(data):
    transformed = []
    for i, val in enumerate(data):
        if i % 3 == 0:
            transformed.append(val ** 2)
        elif i % 3 == 1:
            transformed.append(math.sqrt(abs(val)))
        else:
            transformed.append(val * -1)
    return transformed

def process_bits(x, y):
    a = x & y
    b = x | y
    c = x ^ y
    d = a << 2
    e = b >> 1
    return (c + d) * e

data_structure = {
    "level1": {
        "level2a": [7, -2, 9, 16, -5],
        "level2b": {
            "level3": [
                {"x": 3, "y": 4},
                {"x": 5, "y": 12}
            ]
        }
    },
    "level1b": [10, 20, 30]
}

# Step 1: Extract and transform list from level2a
list_a = data_structure["level1"]["level2a"]
transformed_list = transform_data(list_a)
sum_transformed = sum(transformed_list)

# Step 2: Process coordinates using Pythagorean theorem and bitwise operations
coords = data_structure["level1"]["level2b"]["level3"]
bitwise_results = []
for coord in coords:
    hypotenuse = int(math.hypot(coord["x"], coord["y"]))
    product = coord["x"] * coord["y"]
    bitwise_results.append(process_bits(hypotenuse, product))

# Step 3: Manipulate level1b array
modified_b = [x+1 for x in data_structure["level1b"]]
multiplication_chain = 1
for num in modified_b:
    multiplication_chain *= num

# Final computation
final_sum_components = sum(bitwise_results) + sum_transformed
final_result = (final_sum_components * 2) - (multiplication_chain // 100)
print(f"Result: {final_result}")