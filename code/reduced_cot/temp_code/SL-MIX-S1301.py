from functools import reduce

def fibonacci(n):
    if n <= 1:
        return n
    return reduce(lambda x, _: [x[1], x[0] + x[1]], range(2, n+1), [0, 1])[1]

# Calculate the 8th Fibonacci number (generation count)
generation_count = fibonacci(8)

# Each bee requires 3 cells
honeycomb_cells = generation_count * 3

print(f'Result: {honeycomb_cells}')