import re
from functools import reduce
from itertools import combinations

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def fibonacci_mod(n, mod):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, (a + b) % mod
    return a

def derive_session_key(seed):
    # Step 1: Encode seed as hexadecimal string
    hex_seed = hex(seed)[2:]
    
    # Step 2: Apply regex pattern matching to extract digits
    digits = ''.join(re.findall(r'\d', hex_seed))
    digit_sum = sum(int(d) for d in digits)
    
    # Step 3: Bitwise operations
    xor_result = seed ^ (seed << 3) & 0xFFFF
    and_result = xor_result & ((1 << 8) - 1)
    
    # Step 4: Prime validation and adjustment
    candidate = and_result + digit_sum
    while not is_prime(candidate):
        candidate += 1
    
    # Step 5: Fibonacci scrambling
    fib_index = candidate % 20
    fib_value = fibonacci_mod(fib_index, 256)
    
    # Step 6: Final key combination
    session_key = (candidate << 8) | fib_value
    
    return session_key

# Protocol execution
initial_seed = 0x1A3F
session_key = derive_session_key(initial_seed)
print(f"Result: {session_key}")