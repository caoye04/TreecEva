import itertools

def is_prime(n):
    """Check if a number is prime."""
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

# Network packet data (packet ID, priority, size in bytes)
packet_batch_1 = {23, 17, 41, 13, 29, 8, 12, 19, 31, 7}
packet_batch_2 = {17, 19, 29, 37, 41, 43, 8, 16, 4}

# Temporary sets for analysis
temp_set_1 = {x for x in range(5, 50, 3)}
temp_set_2 = {x for x in range(10, 45, 5)}

# Calculate intersection of packet batches
valid_intersection = packet_batch_1.intersection(packet_batch_2)

# Create a list of potential port numbers
port_candidates = list(range(1024, 1034))
port_candidates.extend([8080, 8443, 9000])

# Simulate network traffic analysis
traffic_samples = list(itertools.islice(itertools.cycle([64, 128, 256, 512, 1024]), 10))
filtered_traffic = [x for x in traffic_samples if x > 100]

# Priority calculation (not directly relevant to result)
priority_sum = sum(valid_intersection)
priority_bits = priority_sum & 0x3F  # Apply bitmask

# Extract prime numbers from valid intersection
filtered_intersection = {x for x in valid_intersection if is_prime(x)}

# Some additional calculations that don't affect the result
max_packet_size = max(filtered_traffic + [0])
min_packet_id = min(packet_batch_1.union(packet_batch_2))

# Calculate average priority (not used in final result)
avg_priority = sum(valid_intersection) / len(valid_intersection) if valid_intersection else 0

print(f"Result: {filtered_intersection}")