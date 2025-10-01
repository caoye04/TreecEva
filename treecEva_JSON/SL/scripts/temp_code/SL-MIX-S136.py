import math

def process_data(lst):
    transformed = []
    for i, val in enumerate(lst):
        if i % 2 == 0:
            transformed.append(val ** 2)
        else:
            transformed.append(math.sqrt(abs(val)))
    return transformed

data = [4, -9, 5, -16, 7]
processed = process_data(data)

# Create a dictionary with processed values as keys and their indices as values
mapped = {val: idx for idx, val in enumerate(processed)}

# Perform a series of operations based on conditions
accumulator = 0
for key in sorted(mapped.keys(), reverse=True):
    index = mapped[key]
    if key > 10:
        accumulator += key * index
    elif key > 5:
        accumulator += key + index
    else:
        accumulator -= key // (index + 1)

# Bitwise manipulation phase
bitwise_result = 0
for i in range(5):
    if i < len(processed):
        bitwise_result ^= int(processed[i]) << (i % 3)

# Final calculation combining accumulator and bitwise results
final_result = (accumulator & bitwise_result) + (accumulator | bitwise_result)

print(f'Result: {final_result}')