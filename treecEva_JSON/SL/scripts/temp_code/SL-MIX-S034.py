import math

def process_nested_structure(data):
    total = 0
    for key, value in data.items():
        if isinstance(value, dict):
            total += process_nested_structure(value)
        elif isinstance(value, list):
            for item in value:
                if isinstance(item, int):
                    total += item * 2
                elif isinstance(item, str):
                    total += len(item)
        elif isinstance(value, int):
            total += value ** 2
    return total

data_structure = {
    'a': {
        'b': [1, 2, 'hello'],
        'c': 5
    },
    'd': [
        10,
        'world',
        {
            'e': 3,
            'f': [4, 'test']
        }
    ],
    'g': 7
}

intermediate_sum = process_nested_structure(data_structure)

# Perform bit-wise operations
bitwise_result = (intermediate_sum << 2) & 255

# Apply trigonometric function
trig_value = math.sin(math.pi / 6)  # sin(30 degrees)
rounded_trig = round(trig_value, 2)

# String manipulation
sample_string = "ComplexReasoningChallenge"
char_sum = sum(ord(c) for c in sample_string if c.isupper())

# Final calculation
final_result = (bitwise_result ^ char_sum) + int(rounded_trig * 100)
print(f'Result: {final_result}')