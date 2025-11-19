import math

def count_divisors(n):
    count = 0
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            if i * i == n:
                count += 1
            else:
                count += 2
    return count

# Find number with most divisors in range [50, 100]
divisor_counts = [(n, count_divisors(n)) for n in range(50, 101)]
optimal_package_size = max(divisor_counts, key=lambda x: x[1])[0]

print(f"Result: {optimal_package_size}")