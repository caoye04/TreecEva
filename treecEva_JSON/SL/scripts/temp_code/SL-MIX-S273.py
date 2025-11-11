import math

def prime_factors_sum(n):
    i = 2
    factors_sum = 0
    temp_n = n
    while i * i <= temp_n:
        while temp_n % i == 0:
            factors_sum += i
            temp_n //= i
        i += 1
    if temp_n > 1:
        factors_sum += temp_n
    return factors_sum

def hex_weighted_gcd_checksum(hex_sequence):
    weights = [prime_factors_sum(int(h, 16)) for h in hex_sequence]
    current_gcd = weights[0]
    for w in weights[1:]:
        current_gcd = math.gcd(current_gcd, w)
    return current_gcd * sum(weights)

# Cryptographic checksum calculation
hex_values = ['1A', '2F', '3B', '4C']
checksum_components = [hex_weighted_gcd_checksum(hex_values[i:i+3]) for i in range(len(hex_values)-2)]
final_checksum = math.gcd(checksum_components[0], checksum_components[1])
print(f"Result: {final_checksum}")