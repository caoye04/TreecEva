def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

# Generate first 10 Fibonacci numbers
fib_sequence = list(fibonacci(10))

# Dictionary comprehension to map Fibonacci numbers to their indices
fib_dict = {value: index for index, value in enumerate(fib_sequence)}

# Calculate the sum of Fibonacci numbers that are keys in the dictionary
fibonacci_sum = sum(fib_dict.keys())

print(f'Result: {fibonacci_sum}')