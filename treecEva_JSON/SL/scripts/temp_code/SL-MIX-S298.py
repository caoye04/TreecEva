def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

def hash_chain(depth, accumulator=0):
    if depth <= 0 or (depth > 10 and accumulator > 1000):
        return accumulator
    fib_index = fibonacci(depth)
    transform = lambda x: (x * 17 + 23) % 1000
    transformed_value = transform(fib_index)
    return hash_chain(depth - 1, accumulator + transformed_value)

# Initialize security parameters
initial_values = {i: fibonacci(i) for i in range(5, 8)}
combined_seed = sum(initial_values.values())
security_token = hash_chain(6, combined_seed)
print(f"Result: {security_token}")