import math

def process_nested_data(data_structure):
    result = 0
    for level1 in data_structure:
        if isinstance(level1, list):
            for level2 in level1:
                if isinstance(level2, dict):
                    for key, value in level2.items():
                        if isinstance(value, str) and value.isdigit():
                            result += int(value) * 2
                        elif isinstance(value, list):
                            temp = 1
                            for item in value:
                                if isinstance(item, int):
                                    temp *= item
                            result += temp
    return result

def complex_calculation(x, y, z):
    a = math.pow(x, 2) + math.sqrt(y)
    b = math.log(z) if z > 0 else 0
    c = (a * b) % (x + y + z) if (x + y + z) != 0 else 0
    return int(c)

# Main execution starts here
nested_data = [
    [1, 2, 3],
    [
        {
            "key1": "42",
            "key2": [2, 3, 5],
            "key3": {
                "inner_key": 100
            }
        },
        {
            "key4": "18",
            "key5": [1, 4, 2],
            "key6": "hello"
        }
    ],
    [4, 5]
]

# Process the nested data structure
processed_value = process_nested_data(nested_data)

# Perform bit operations
bit_result = (processed_value & 0xFF) | ((processed_value >> 4) ^ 0xF)

# Perform mathematical operations
x, y, z = 5, 64, 10
math_result = complex_calculation(x, y, z)

# String manipulations
str1 = "hello"
str2 = "world"
str_combined = str1[::-1] + str2[1:3] + str(math_result)
char_sum = sum(ord(c) for c in str_combined)

# Final calculation
final_result = ((bit_result << 2) + char_sum) % 1000
print(f"Result: {final_result}")