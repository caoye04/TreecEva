import math

def fibonacci(n):
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

data = [
    {'values': [2, 3, 5, 8, 13], 'operation': 'sum'},
    {'values': [1, 1, 2, 3, 5, 8], 'operation': 'product'},
    {'values': [4, 9, 16, 25], 'operation': 'sqrt_sum'},
    {'values': [7, 11, 13, 17, 19], 'operation': 'prime_filter_sum'}
]

processed = []
for item in data:
    vals = item['values']
    op = item['operation']
    if op == 'sum':
        processed.append(sum(vals))
    elif op == 'product':
        prod = 1
        for v in vals:
            prod *= v
        processed.append(prod)
    elif op == 'sqrt_sum':
        processed.append(sum(math.sqrt(v) for v in vals))
    elif op == 'prime_filter_sum':
        processed.append(sum(v for v in vals if is_prime(v)))

mapped = {}
for i, val in enumerate(processed):
    mapped[f'key_{i}'] = fibonacci(i) * val

nested = {
    'layer1': {
        'layer2': {
            'target': mapped['key_2']
        }
    },
    'layer1_alt': {
        'layer2_alt': mapped['key_1']
    }
}

# Perform a complex calculation using nested values
a = nested['layer1']['layer2']['target']
b = nested['layer1_alt']['layer2_alt']
c = processed[3]

# Final calculation step
result = (a ^ b) & (c << 2)  # Bitwise operations

print(f'Result: {result}')