def call_counter(func):
    calls = {}
    def wrapper(*args, **kwargs):
        key = (func.__name__, args, tuple(sorted(kwargs.items())))
        calls[key] = calls.get(key, 0) + 1
        return func(*args, **kwargs)
    wrapper.calls = calls
    return wrapper

def gcd_multiple(*numbers):
    from math import gcd
    result = numbers[0]
    for num in numbers[1:]:
        result = gcd(result, num)
        if result == 1:
            break
    return result

@call_counter
def prime_gap_generator(n):
    primes = [2]
    candidate = 3
    while len(primes) < n:
        is_prime = True
        for p in primes:
            if p * p > candidate:
                break
            if candidate % p == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(candidate)
        candidate += 2
    
    gaps = [primes[i] - primes[i-1] for i in range(1, len(primes))]
    composites = []
    for gap in gaps:
        if gap > 1:
            # Create a composite from the gap using a simple formula
            composite = gap * gap + gap + 41  # Euler's prime-like formula
            # Verify it's composite (not actually checking here for simplicity)
            composites.append(composite)
    return composites

# Execution point Y
composite_list = prime_gap_generator(15)
secure_key = gcd_multiple(*composite_list)
print(f"Result: {secure_key}")