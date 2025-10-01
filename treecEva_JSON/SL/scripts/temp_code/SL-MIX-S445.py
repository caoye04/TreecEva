import math

def process_nested_data(data):
    result = 0
    for i, sublist in enumerate(data):
        sub_result = 1
        for j, val in enumerate(sublist):
            if j % 2 == 0:
                sub_result *= (val + i)
            else:
                sub_result -= (val - j)
        result += sub_result
    return result

def transform_string(s):
    transformed = ''
    for i, char in enumerate(s):
        if i % 3 == 0:
            transformed += char.upper()
        elif i % 3 == 1:
            transformed += str(ord(char) % 10)
        else:
            transformed += char.lower()
    return transformed

def calculate_geometric_mean(numbers):
    product = 1
    for num in numbers:
        product *= num
    return product ** (1/len(numbers))

data_structure = [
    [2, 5, 8, 11],
    [3, 7, 12],
    [1, 4, 6, 9, 15]
]

string_input = "ComplexReasoning"

# Step 1: Process nested data
processed_value = process_nested_data(data_structure)

# Step 2: Transform string
transformed_string = transform_string(string_input)

# Step 3: Extract numbers from transformed string
extracted_numbers = [int(ch) for ch in transformed_string if ch.isdigit()]

# Step 4: Calculate geometric mean of extracted numbers
geometric_mean = calculate_geometric_mean(extracted_numbers)

# Step 5: Perform advanced mathematical operations
log_value = math.log(processed_value + 1)
trig_value = math.sin(geometric_mean) * math.cos(log_value)

# Step 6: Bitwise operations
bitwise_result = (int(log_value) & int(geometric_mean)) | (int(trig_value) << 2)

# Step 7: Final calculation
final_result = (bitwise_result ^ int(processed_value)) + len(transformed_string)

print(f"Result: {final_result}")