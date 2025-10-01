import math

def process_nested_data(data):
    result = 0
    for i, sublist in enumerate(data):
        if i % 2 == 0:
            for j, val in enumerate(sublist):
                if j % 3 == 0:
                    result += math.pow(val, 2) if val > 0 else 0
                elif j % 3 == 1:
                    result -= math.sqrt(abs(val)) if val < 0 else 0
                else:
                    result *= 2 if val != 0 else 1
        else:
            temp = [x for x in sublist if isinstance(x, (int, float))]
            if temp:
                result += max(temp) - min(temp)
    return result

def transform_string(s):
    vowels = 'aeiouAEIOU'
    consonants = ''.join([c for c in s if c.isalpha() and c not in vowels])
    vowel_count = sum(1 for c in s if c in vowels)
    return len(consonants) * vowel_count

data_structure = [
    [3, -4, 0, 7, -2, 5],
    ['hello', 10, 'world', 3.5],
    [0, -9, 2, -3, 4, -5, 6],
    ['test', 'string', 15, -7, 2.2],
    [1, 1, 1, -8, 0, 3, -1, 4]
]

# Process the nested data
intermediate_result = process_nested_data(data_structure)

# Perform bit operations on the intermediate result
bitwise_result = (intermediate_result << 2) ^ 0xFF

# Transform a string
string_result = transform_string("AdvancedProgramming2023")

# Combine results with trigonometric operations
angle = bitwise_result % 360
trig_result = math.sin(math.radians(angle)) + math.cos(math.radians(angle))

# Final calculation
final_result = int((bitwise_result + string_result) * trig_result)

print(f"Result: {final_result}")