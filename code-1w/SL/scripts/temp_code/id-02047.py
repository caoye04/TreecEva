from itertools import cycle

def process_sequences(values, shift):
    shifted = [(v + shift) % 17 for v in values]
    filtered = list(filter(lambda x: x > 5, shifted))
    rolling_sum = 0
    for i, val in enumerate(cycle(filtered)):
        if i >= len(filtered) * 2:
            break
        rolling_sum += val
    return rolling_sum // 2

data = [3, 8, 12, 4, 9]
offset = 7
temp_var_ignore = [x ** 0.5 for x in data]  # Irrelevant computation
result = process_sequences(data, offset)
print(f"Result: {result}")