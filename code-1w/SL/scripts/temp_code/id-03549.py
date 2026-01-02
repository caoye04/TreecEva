def transform_data(values, func):
    return sum([func(x) for x in values if x % 2 == 0])

# Irrelevant helper (mild distraction)
def auxiliary_op(n):
    return (n * 2) + 1

# Data setup
raw_data = [3, 6, 8, 11, 14, 17]
offset = 4
processed = [x - offset for x in raw_data]

# Key function using lambda
key_func = lambda z: z ** 2 - z

# Core computation step
result = transform_data(processed, key_func)

# Output result as required
print(f"Result: {result}")