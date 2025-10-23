def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

# Calculate special spiral sequence
spiral_sequence = [
    pow(fibonacci(i), fibonacci(i-1), 1000) if i > 0 else 1
    for i in range(13)
]

# Apply geometric transformation using lambda
transform = lambda x, y: (x * y) % 1000
spiral_density = transform(sum(spiral_sequence[:8]), len(spiral_sequence))

print(f'Result: {spiral_density}')