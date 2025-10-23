from collections import deque
import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return abs(a * b) // gcd(a, b)

def fibonacci(n):
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

# Key derivation function using lambda and closure
transform_ops = [
    lambda x: x * 2 if x % 2 == 0 else x + 3,
    lambda x: fibonacci(x % 10) if x > 5 else x,
    lambda x: x ^ (x >> 1) if x & 1 else x | (x << 1)
]

# Initialization vector
init_vector = 12345

# Prime factorization step
factors = []
num = init_vector
divisor = 2
while divisor * divisor <= num:
    if num % divisor == 0:
        factors.append(divisor)
        num //= divisor
    else:
        divisor += 1
if num > 1:
    factors.append(num)

# Stack-based transformation
stack = deque()
for factor in factors:
    if is_prime(factor):
        stack.append(factor)
    else:
        if stack:
            stack.pop()

# LCM calculation of remaining stack elements
lcm_result = 1
while stack:
    element = stack.popleft()
    lcm_result = lcm(lcm_result, element)

# Apply transformation operations
derived_key = lcm_result
for op in transform_ops:
    derived_key = op(derived_key)
    
# Final adjustment based on logical conditions
if derived_key > 100 and not (derived_key & 1):
    derived_key = derived_key >> 2
elif derived_key <= 100 or (derived_key & 1):
    derived_key = derived_key << 1

print(f"Result: {derived_key}")