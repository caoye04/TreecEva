import math
from statistics import mean, variance

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

# Network node identifiers
node_ids = [15, 28, 33, 46, 59, 72, 85, 98]

# Calculate pairwise XOR interactions
xor_results = {}
for i in range(len(node_ids)):
    for j in range(i+1, len(node_ids)):
        xor_val = node_ids[i] ^ node_ids[j]
        xor_results[(node_ids[i], node_ids[j])] = xor_val

# Filter XOR results where GCD of operands is a prime number
filtered_values = []
for (a, b), xor_val in xor_results.items():
    if is_prime(gcd(a, b)):
        filtered_values.append(xor_val)

# Compute interference stability index
if len(filtered_values) > 1:
    stability_index = mean(filtered_values) + math.sqrt(variance(filtered_values))
elif len(filtered_values) == 1:
    stability_index = filtered_values[0]
else:
    stability_index = 0

print(f"Result: {int(stability_index)}")