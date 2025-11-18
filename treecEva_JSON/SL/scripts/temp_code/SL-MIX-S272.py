import math
from functools import reduce
from collections import Counter

network_logs = [120, 256, 97, 512, 101, 79, 300, 1024, 103, 200, 400, 89, 150, 600, 750]

# Helper function to check if a number is prime
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

# Calculate mean and standard deviation
packet_count = len(network_logs)
total_size = sum(network_logs)
mean_size = total_size / packet_count
variance = sum((x - mean_size) ** 2 for x in network_logs) / packet_count
std_dev = math.sqrt(variance)

# Threshold for anomaly detection
threshold = mean_size + std_dev

# Identify primes using list comprehension and filter
prime_packets = [size for size in network_logs if is_prime(size)]

# Count anomalies using short-circuit evaluation and ternary operator
anomaly_count = sum(1 for p in prime_packets if p > threshold)

print(f"Result: {anomaly_count}")