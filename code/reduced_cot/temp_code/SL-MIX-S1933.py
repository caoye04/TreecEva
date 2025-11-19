import math

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

word = 'MATH'
alphabet_indices = [ord(char) - ord('A') + 1 for char in word]
prime_indices = [idx for idx in alphabet_indices if is_prime(idx)]

# Calculate LCM of prime indices
lcm_result = 1
for num in prime_indices:
    lcm_result = (lcm_result * num) // math.gcd(lcm_result, num)

print(f"Result: {lcm_result}")