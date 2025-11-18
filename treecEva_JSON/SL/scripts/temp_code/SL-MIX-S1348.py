import itertools
from functools import reduce

# Simulated network packet headers (each 32-bit value)
packet_headers = [0x1A2B3C4D, 0xF0E1D2C3, 0x55AA55AA, 0xCAFEBABE, 0xDEADBEEF]

# Frequency map for byte analysis
byte_freq_map = {}
for header in packet_headers:
    for i in range(4):
        byte_val = (header >> (i * 8)) & 0xFF
        byte_freq_map[byte_val] = byte_freq_map.get(byte_val, 0) + 1

# Bitwise checksum calculation with XOR folding
checksum_register = 0xFFFFFFFF
for header in packet_headers:
    # Rotate left by 7 bits and XOR with header
    rotated = ((header << 7) | (header >> 25)) & 0xFFFFFFFF
    checksum_register ^= rotated
    # Apply mask to constrain register
    checksum_register &= 0x7FFFFFFF

# Calculate frequency penalty using list comprehension
freq_penalties = [count for count in byte_freq_map.values() if count > 1]
total_penalty = sum(freq_penalties) if freq_penalties else 0

# Combine checksum with penalty using bitwise operations
penalty_shifted = total_penalty << 4
combined_metric = checksum_register ^ penalty_shifted

# Final exfiltration score calculation
exfil_score = (combined_metric & 0xFFFF) + (combined_metric >> 16)
print(f"Result: {exfil_score}")