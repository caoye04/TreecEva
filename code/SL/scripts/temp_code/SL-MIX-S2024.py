import math
from functools import reduce

def gcd_extended(a, b):
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = gcd_extended(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd, x, y

def lcm(a, b):
    return abs(a * b) // math.gcd(a, b)

# Initialize working variables
message_block = [0x61, 0x62, 0x63, 0x64, 0x65]
working_vars = [0x12345678, 0x9abcdef0, 0xfedcba98, 0x76543210]
transformed_values = []

# Process each byte in the message block
for i, byte in enumerate(message_block):
    # Apply transformation with previous working var
    temp = (working_vars[i % len(working_vars)] + byte) & 0xFFFFFFFF
    
    # Rotate left by 7 bits
    rotated = ((temp << 7) | (temp >> 25)) & 0xFFFFFFFF
    
    # Apply non-linear function
    nonlinear = rotated ^ (rotated >> 11) ^ (rotated << 13)
    
    # Update working variable
    working_vars[(i+1) % len(working_vars)] = (working_vars[(i+1) % len(working_vars)] + nonlinear) & 0xFFFFFFFF
    transformed_values.append(nonlinear)

# Compute statistical metrics
mean_val = sum(transformed_values) / len(transformed_values)
squared_diffs = [(x - mean_val) ** 2 for x in transformed_values]
variance = sum(squared_diffs) / len(squared_diffs)

# Compute primes related to message length
msg_len = len(message_block)
next_prime = msg_len + 1
while not all(next_prime % i for i in range(2, int(math.sqrt(next_prime)) + 1)):
    next_prime += 1

# Calculate checksum using number theory
lcm_val = lcm(int(mean_val), int(variance))
gcd_val, _, _ = gcd_extended(lcm_val, next_prime)
checksum = (lcm_val ^ gcd_val) & 0xFFFFFFFF

print(f"Result: {checksum}")