import math
from collections import defaultdict

# Packet sizes in bytes
packet_sequence = [128, 512, 256, 1024, 64, 2048, 32]

# Initialize tracking structures
size_frequency = defaultdict(int)
security_scores = []

for idx, size in enumerate(packet_sequence):
    # Update frequency map
    size_frequency[size] += 1
    
    # Calculate base score using logarithmic scaling
    base_score = math.log(size, 2) if size > 0 else 0
    
    # Apply position-based exponential modifier
    position_modifier = math.pow(1.5, idx % 3)
    
    # Compute current packet's contribution
    packet_contribution = int(base_score * position_modifier)
    
    # Apply frequency penalty for repeated sizes using short-circuit evaluation
    if size_frequency[size] > 1 and size_frequency[size] <= 3:
        packet_contribution //= 2
    elif size_frequency[size] > 3:
        packet_contribution = 0
    
    security_scores.append(packet_contribution)

# Calculate final security score with arithmetic operations
final_security_score = sum(security_scores) + (max(security_scores) - min(security_scores))
print(f"Result: {final_security_score}")