import math

def complex_transform(data):
    result = []
    for i, val in enumerate(data):
        if i % 2 == 0:
            result.append(val ** 2)
        else:
            result.append(math.sqrt(abs(val)))
    return result

def nested_operation(container):
    total = 0
    for key, value in container.items():
        if isinstance(value, list):
            for item in value:
                if isinstance(item, dict):
                    for k, v in item.items():
                        total += v if isinstance(v, (int, float)) else 0
                else:
                    total += item if isinstance(item, (int, float)) else 0
        elif isinstance(value, dict):
            for k, v in value.items():
                total += v if isinstance(v, (int, float)) else 0
    return total

# Initial data structures
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

nested_dict = {
    'a': [10, {'inner': 5}],
    'b': {'x': 3, 'y': [2, 4]},
    'c': [1, {'deep': {'deeper': 7}}, 3]
}

# Complex calculations
A = sum([row[0] for row in matrix])
B = math.factorial(int(math.log(math.e ** 4)))
C = complex_transform([x for row in matrix for x in row if x > 5])
D = nested_operation(nested_dict)

# Bitwise and logical operations
E = (A << 2) & (B >> 1) | (D ^ 15)
F = not (A > B) and (C[-1] > 10) or (D in [50, 51, 52])

# String manipulations and conversions
text = "Compute: A={}, B={}, C={}, D={}, E={}, F={}"
formatted_text = text.format(A, B, C, D, E, int(F))
char_sum = sum(ord(c) for c in formatted_text if c.isdigit())

# Final calculation
G = (E * char_sum) % 997
H = math.floor(math.sqrt(G))

# Execution point Y
X = (G + H) * (1 if F else -1)

print(f"Result: {X}")