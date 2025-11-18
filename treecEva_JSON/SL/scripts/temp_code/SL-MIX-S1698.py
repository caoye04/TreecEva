import math

def get_prime_below(n):
    for num in range(n-1, 1, -1):
        is_prime = True
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            return num
    return 2

# Initial configuration
initial_seed = 42
prime_key = get_prime_below(50)
gcd_operand_a = 56
gcd_operand_b = 98

# Cipher transformation
transformed_seed = initial_seed ^ prime_key
transformed_seed <<= 2
transformed_seed ^= math.gcd(gcd_operand_a, gcd_operand_b)

print(f"Result: {transformed_seed}")