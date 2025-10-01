import math

def process_nested_data(data):
    result = 0
    for i, sublist in enumerate(data):
        if i % 2 == 0:
            temp = sum(sublist)
            result += temp ** 2
        else:
            temp = 1
            for x in sublist:
                if x != 0:
                    temp *= x
            result -= temp
    return result

def transform_string(s):
    vowels = 'aeiouAEIOU'
    transformed = ''
    for char in s:
        if char in vowels:
            transformed += str(ord(char))
        else:
            transformed += char.upper()
    return transformed

data_structure = [
    [1, 2, 3],
    [4, 0, 6],
    [7, 8],
    [9, 10, 0, 12],
    [13, 14, 15]
]

string_input = "Hello World"

# Step 1: Process the nested data structure
processed_value = process_nested_data(data_structure)

# Step 2: Transform the string
transformed_string = transform_string(string_input)

# Step 3: Calculate length of transformed string
string_length = len(transformed_string)

# Step 4: Perform complex mathematical operation
intermediate_result = math.log(processed_value + string_length) * math.sin(math.pi / 4)

# Step 5: Bitwise operations
bitwise_result = (int(intermediate_result) & 0xFF) | (string_length << 2)

# Step 6: Final calculation
final_result = (bitwise_result ^ 0xAA) + (processed_value % 17)

print(f"Result: {final_result}")