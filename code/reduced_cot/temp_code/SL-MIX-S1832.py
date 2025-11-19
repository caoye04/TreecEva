import math
from functools import reduce

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def prime_factors(n):
    factors = set()
    d = 2
    while d * d <= n:
        while (n % d) == 0:
            factors.add(d)
            n //= d
        d += 1
    if n > 1:
        factors.add(n)
    return factors

def gcd_list(lst):
    return reduce(math.gcd, lst)

network_packets = [1200, 800, 450, 1800, 600, 300, 950, 2100, 750, 1600]
large_packet_scores = []
medium_packets = []

for size in network_packets:
    if size > 1000:
        factors = prime_factors(size)
        score = sum(factors)
        large_packet_scores.append(score)
    elif 500 <= size <= 1000:
        medium_packets.append(size)

# Short-circuit evaluation - only calculate GCD if medium_packets is not empty
medium_gcd = gcd_list(medium_packets) if medium_packets else 0

# Calculate mean of large packet scores if any exist
mean_large_score = sum(large_packet_scores) / len(large_packet_scores) if large_packet_scores else 0

# Final security score combines both metrics
final_security_score = int(mean_large_score + medium_gcd) if large_packet_scores and medium_packets else 0

print(f"Result: {final_security_score}")