from collections import defaultdict
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

# Packet signature registry
packet_registry = [
    (0b110101, 0b101100),
    (0b111000, 0b001111),
    (0b101010, 0b010101),
    (0b111100, 0b000011),
    (0b100110, 0b011001)
]

# Initialize counters
verified_packets_count = 0
signature_stats = defaultdict(int)

# Process each packet
for sender_id, payload_hash in packet_registry:
    # Calculate XOR signature
    xor_signature = sender_id ^ payload_hash
    
    # Check if XOR result is prime
    if is_prime(xor_signature):
        # Apply greedy verification: check if GCD with special key is 1
        special_key = 0b101010
        if gcd(xor_signature, special_key) == 1:
            verified_packets_count += 1
            signature_stats[xor_signature] += 1
    else:
        # For non-prime signatures, apply secondary check using bit shifts
        left_shifted = (sender_id << 1) & 0xFF
        right_shifted = payload_hash >> 1
        combined_check = left_shifted ^ right_shifted
        
        if is_prime(combined_check) and combined_check & 0b11 == 0b01:
            verified_packets_count += 1
            signature_stats[combined_check] += 1

# Final adjustment based on signature distribution
if len(signature_stats) > 3:
    adjustment_factor = sum(k for k in signature_stats.keys() if k & 0b1 == 1) % 7
    verified_packets_count = (verified_packets_count * 2) ^ adjustment_factor

print(f"Result: {verified_packets_count}")