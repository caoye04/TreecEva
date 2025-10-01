import math

def process_nested_data(data):
    total = 0
    for i, sublist in enumerate(data):
        if i % 2 == 0:
            transformed = [math.log(x) if x > 0 else 0 for x in sublist]
        else:
            transformed = [math.sqrt(abs(x)) for x in sublist]
        total += sum(transformed)
    return total

def apply_bitwise_operations(numbers):
    result = numbers[0]
    for i in range(1, len(numbers)):
        if i % 3 == 0:
            result ^= numbers[i]
        elif i % 3 == 1:
            result |= numbers[i]
        else:
            result &= numbers[i]
    return result

data_structure = [
    [math.e, math.pi, -math.e],
    [4, 9, 16],
    [math.e**2, math.pi**2, -(math.e*math.pi)],
    [25, 36, 49]
]

# Step 1: Process nested data
processed_value = process_nested_data(data_structure)

# Step 2: Generate sequence based on processed value
sequence_length = int(abs(processed_value)) % 10 + 5
fib_sequence = []
for i in range(sequence_length):
    if i == 0 or i == 1:
        fib_sequence.append(i + 1)
    else:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])

# Step 3: Apply bitwise operations on Fibonacci sequence
bitwise_result = apply_bitwise_operations(fib_sequence)

# Step 4: Perform final calculation
final_result = int((bitwise_result ** 1.5) // math.log(processed_value + math.e))

print(f'Result: {final_result}')