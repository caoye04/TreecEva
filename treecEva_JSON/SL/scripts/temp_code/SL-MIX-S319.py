import math

def process_nested_data(data):
    result = 0
    for i, item in enumerate(data):
        if isinstance(item, list):
            sub_result = process_nested_data(item)
            result += sub_result * (i + 1)
        elif isinstance(item, dict):
            for key, value in item.items():
                if isinstance(value, str):
                    result += len(value) * hash(key) % 100
                else:
                    result += value
        elif isinstance(item, str):
            result += sum(ord(c) for c in item) % 50
        else:
            result += item
    return result

def calculate_advanced_value(x, y, z):
    a = math.pow(x, 2) + math.sqrt(abs(y))
    b = math.log(z + 1) if z > 0 else 0
    c = math.sin(a) * math.cos(b)
    d = int(c * 1000) & 0xFF
    return d

data_structure = [
    5,
    [3, [7, 2], 1],
    {
        "alpha": 10,
        "beta": "hello world",
        "gamma": {
            "delta": 15,
            "epsilon": [4, [9, 3]]
        }
    },
    "test string",
    [
        {
            "nested": "deeply",
            "value": 25
        },
        [
            6,
            {
                "final": "element"
            }
        ]
    ]
]

# Processing step 1: Process the complex nested data structure
processed_value = process_nested_data(data_structure)

# Processing step 2: Perform advanced mathematical calculation
x = processed_value % 100
y = processed_value // 100 - 50
z = len(str(processed_value))
advanced_result = calculate_advanced_value(x, y, z)

# Processing step 3: Bitwise and string operations
binary_str = bin(advanced_result)[2:]  # Remove '0b' prefix
bit_count = binary_str.count('1')
shifted_value = (advanced_result << 2) ^ bit_count

# Processing step 4: Final complex calculation
final_result = ((shifted_value * 3) + math.factorial(bit_count % 5)) % 997

print(f"Result: {final_result}")