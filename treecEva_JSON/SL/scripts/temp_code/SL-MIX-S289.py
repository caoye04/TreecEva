import math

def complex_transform(data):
    transformed = []
    for i, val in enumerate(data):
        if i % 2 == 0:
            transformed.append(val ** 2)
        else:
            transformed.append(math.sqrt(abs(val)))
    return transformed

def nested_operation(matrix):
    flattened = [item for sublist in matrix for item in sublist]
    processed = complex_transform(flattened)
    return sum(processed) / len(processed)

def recursive_reduce(lst, depth=0):
    if depth >= 3:
        return sum(lst)
    else:
        new_lst = []
        for i in range(0, len(lst), 2):
            if i + 1 < len(lst):
                new_lst.append(lst[i] ^ lst[i+1])
            else:
                new_lst.append(lst[i])
        return recursive_reduce(new_lst, depth + 1)

# Initialize complex nested data structures
matrix_data = [
    [3, -4, 5],
    [-2, 7, -1],
    [6, 0, -8]
]

# Perform nested operations
avg_value = nested_operation(matrix_data)

# Generate sequence based on average
sequence = []
for i in range(1, 6):
    term = (avg_value * i) % 17
    sequence.append(int(term))

# Apply bitwise reduction
reduced_value = recursive_reduce(sequence)

# Complex mathematical transformation
angle = reduced_value * math.pi / 180
trig_result = (math.sin(angle) + math.cos(angle)) * 100

# Final calculation step
result = int(abs(trig_result) * 2.5) % 1000

print(f"Result: {result}")