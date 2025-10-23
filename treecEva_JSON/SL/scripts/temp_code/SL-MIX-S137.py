from functools import reduce

def modified_fibonacci(n, mod_base=7):
    if n <= 0:
        return []
    elif n == 1:
        return [1]
    elif n == 2:
        return [1, 1]
    
    seq = [1, 1]
    for i in range(2, n):
        next_val = seq[i-1] + seq[i-2] + ((seq[i-1] - seq[i-2]) % mod_base)
        seq.append(next_val)
    return seq

def compute_acoustic_signature():
    # Generate the modified Fibonacci sequence
    fib_terms = modified_fibonacci(10, 5)
    
    # Apply transformation using map and lambda
    transformed = list(map(lambda x: x[1] ** (x[0] % 3), enumerate(fib_terms)))
    
    # Filter even numbers and calculate their product
    even_transformed = list(filter(lambda x: x % 2 == 0, transformed))
    
    # Handle case when no even numbers exist
    if not even_transformed:
        return 0
    
    acoustic_signature = reduce(lambda a, b: a * b, even_transformed)
    return acoustic_signature

acoustic_signature = compute_acoustic_signature()
print(f"Result: {acoustic_signature}")