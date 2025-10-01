import math

def process_nested_data(data):
    result = 0
    for key, value in data.items():
        if isinstance(value, dict):
            result += process_nested_data(value)
        elif isinstance(value, list):
            for i, item in enumerate(value):
                if isinstance(item, (int, float)):
                    result += item * (i + 1)
                elif isinstance(item, str):
                    result += len(item) * ord(item[0])
        elif isinstance(value, (int, float)):
            result += value
    return result

def calculate_advanced_stats(numbers):
    if not numbers:
        return 0
    
    # Calculate geometric mean
    product = 1
    for num in numbers:
        if num > 0:
            product *= num
    geometric_mean = product ** (1/len(numbers)) if len(numbers) > 0 else 0
    
    # Calculate harmonic mean
    reciprocal_sum = sum(1/num for num in numbers if num != 0)
    harmonic_mean = len(numbers) / reciprocal_sum if reciprocal_sum != 0 else 0
    
    # Return weighted combination
    return (geometric_mean * 0.6) + (harmonic_mean * 0.4)

# Main execution starts here
complex_data = {
    'level1_a': {
        'level2_a': [12, 'hello', 7.5, [3, 4]],
        'level2_b': {
            'level3_a': [2.5, 'world', 10],
            'level3_b': 42
        }
    },
    'level1_b': [15, 'test', 3.14, {'inner': [1, 2, 3]}],
    'level1_c': 100
}

# Process the nested data structure
processed_value = process_nested_data(complex_data)

# Perform bit operations on the processed value
bit_shifted = (int(processed_value) & 0xFF) << 2
bit_xor = bit_shifted ^ 0xAA

# Generate a sequence based on the bit operations
sequence = []
for i in range(1, int(math.sqrt(bit_xor)) + 1):
    if bit_xor % i == 0:
        sequence.append(i)
        if i != bit_xor // i:
            sequence.append(bit_xor // i)

# Calculate advanced statistics on the sequence
stats_result = calculate_advanced_stats(sequence)

# Apply trigonometric transformation
trig_transform = math.sin(stats_result) * math.cos(stats_result/2) * 100

# Final calculation combining all previous results
final_result = int((trig_transform + processed_value + bit_xor) / 3) % 1000

print(f"Result: {final_result}")