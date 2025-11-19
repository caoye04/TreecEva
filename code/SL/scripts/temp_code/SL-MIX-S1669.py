import math
from collections import defaultdict, Counter

# Packet header analysis for threat detection
class PacketHeader:
    def __init__(self, flags, payload_entropy, priority):
        self.flags = flags  # 16-bit flag field
        self.entropy = payload_entropy
        self.priority = priority

# Simulated packet stream
packets = [
    PacketHeader(0b1100101010110011, 0.85, 2),
    PacketHeader(0b1011001111001010, 0.92, 1),
    PacketHeader(0b1111000011110000, 0.78, 3),
    PacketHeader(0b1010101010101010, 0.95, 1)
]

# Initialize threat detection system
flag_patterns = defaultdict(int)
threat_counter = Counter()
security_score = 0

# Process packets with security analysis
for packet in packets:
    # Calculate entropy-based risk (logarithmic component)
    if packet.entropy > 0:
        entropy_risk = int(math.log(packet.entropy) * 100)
    else:
        entropy_risk = 0
    
    # Analyze flag combinations using bitwise operations
    suspicious_flags = (packet.flags & 0xF000) >> 12  # Extract high nibble
    critical_flags = packet.flags & 0x00FF  # Extract low byte
    xor_pattern = suspicious_flags ^ critical_flags
    
    # Update pattern tracking
    flag_patterns[xor_pattern] += 1
    
    # Check for known threat signatures with short-circuit evaluation
    if packet.priority == 1 and (packet.entropy > 0.9 or (xor_pattern & 0xA0) == 0xA0):
        threat_level = 3
    elif packet.priority <= 2 and packet.entropy > 0.8:
        threat_level = 2
    else:
        threat_level = 1
    
    # Apply greedy prioritization to threat counter
    threat_counter[threat_level] += 1
    
    # Calculate exponential weighting factor
    weight = math.exp(threat_level - 1)
    
    # Update cumulative security score
    security_score += int((entropy_risk * weight) + (xor_pattern << threat_level))

# Apply final adjustments based on pattern distribution
pattern_sorted = sorted(flag_patterns.items(), key=lambda x: x[1], reverse=True)
if pattern_sorted and pattern_sorted[0][1] > 1:
    security_score = security_score >> 2  # Reduce score if repeated patterns

print(f"Result: {security_score}")