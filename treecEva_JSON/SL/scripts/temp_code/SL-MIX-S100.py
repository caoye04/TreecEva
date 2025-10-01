import math

def process_nested_data(data):
    result = 0
    for i, sublist in enumerate(data):
        if i % 2 == 0:
            temp = sum(sublist)
            result += temp ** 2
        else:
            temp = 1
            for val in sublist:
                if val != 0:
                    temp *= val
            result -= temp
    return result

def transform_string(s):
    vowels = 'aeiouAEIOU'
    transformed = ''
    for char in s:
        if char in vowels:
            transformed += chr(ord(char) + 1)
        elif char.isalpha():
            transformed += chr(ord(char) - 1)
        else:
            transformed += char
    return transformed

data_structure = [
    [1, 2, 3],
    [4, 0, 6],
    [7, 8],
    [0, 9, 2],
    [5]
]

string_input = "Hello World!"

# Step 1: Process the nested data structure
processed_value = process_nested_data(data_structure)

# Step 2: Transform the string
transformed_string = transform_string(string_input)

# Step 3: Calculate ASCII sum of transformed string
ascii_sum = sum(ord(c) for c in transformed_string)

# Step 4: Perform complex mathematical operation
intermediate_result = math.log(processed_value + ascii_sum) * math.sin(ascii_sum % 3.14)

# Step 5: Bitwise operations
bitwise_result = (int(intermediate_result) & 0xFF) | (int(intermediate_result) >> 4)

# Step 6: Final calculation
final_result = (bitwise_result ^ 0xAA) + (len(transformed_string) << 2)

print(f"Result: {final_result}")