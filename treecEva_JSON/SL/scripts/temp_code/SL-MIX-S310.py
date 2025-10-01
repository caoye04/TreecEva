import math

def process_nested_data(data_structure):
    result = 0
    for i, sublist in enumerate(data_structure):
        temp_sum = sum(sublist)
        if i % 2 == 0:
            result += temp_sum * (i + 1)
        else:
            result -= temp_sum // (i + 1)
    return result

def transform_string(s):
    vowels = 'aeiouAEIOU'
    consonants = ''.join([c for c in s if c.isalpha() and c not in vowels])
    return len(consonants) ** 2

data = [
    [1, 2, 3, 4, 5],
    [6, 7, 8],
    [9, 10, 11, 12],
    [13, 14]
]

# Step 1: Process the nested data structure
processed_value = process_nested_data(data)

# Step 2: Perform mathematical transformations
angle_rad = math.pi / 4
trig_result = math.sin(angle_rad) * math.cos(angle_rad)

# Step 3: Bitwise operations
bitwise_result = (processed_value & 0xFF) ^ 0xAA

# Step 4: String transformation
sample_text = "AdvancedProgrammingLanguageModelEvaluation"
string_result = transform_string(sample_text)

# Step 5: Complex calculation combining all results
intermediate = int(trig_result * 1000) + bitwise_result
exponent = math.log(string_result, 2)
final_result = (intermediate ** 2) % int(exponent * 10)

print(f"Result: {final_result}")