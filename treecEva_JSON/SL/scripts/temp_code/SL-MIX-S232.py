import math

def process_data(data):
    transformed = []
    for i, val in enumerate(data):
        if i % 2 == 0:
            transformed.append(val ** 2)
        else:
            transformed.append(math.sqrt(abs(val)))
    return transformed

def aggregate(transformed_data):
    total = 0
    for i, val in enumerate(transformed_data):
        if i % 3 == 0:
            total += val
        elif i % 3 == 1:
            total -= val
        else:
            total *= val if val != 0 else 1
    return total

def normalize(value, factor=1.5):
    return round(value / factor, 2)

data = [4, -9, 2, -16, 5, 36, -49, 8, 64]
processed = process_data(data)
aggregated = aggregate(processed)
normalized = normalize(aggregated)

# Apply final transformation
result = int(normalized) ^ 0xFF
print(f'Result: {result}')