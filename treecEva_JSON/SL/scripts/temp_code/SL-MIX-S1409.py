import re
from collections import Counter

def calculate_base_score(header):
    # Count occurrences of each hexadecimal digit
    hex_chars = re.findall(r'[0-9A-F]', header.upper())
    freq = Counter(hex_chars)
    score = sum(count * (ord(char) - ord('0') if char.isdigit() else ord(char) - ord('A') + 10) for char, count in freq.items())
    return score

def recursive_modifier(value, depth=3):
    if depth == 0:
        return value
    # Divide and conquer approach
    left_part = value >> 2
    right_part = value & 0x3
    modified_value = (left_part ^ right_part) + (value & 0xF)
    return recursive_modifier(modified_value, depth - 1)

def compute_threat_level(header):
    base_score = calculate_base_score(header)
    # Apply bitwise transformations
    stage_one = base_score ^ 0xAA
    stage_two = (stage_one << 1) | (stage_one >> 3)
    # Recursive adjustment
    adjusted_score = recursive_modifier(stage_two)
    # Normalize with modulo arithmetic
    normalized = adjusted_score % 256
    return normalized

# Packet header analysis
packet_header = "4FAB2C9E7D"

# Dictionary comprehension for segment scores
segment_scores = {i: compute_threat_level(packet_header[i:i+4]) for i in range(0, len(packet_header), 4)}

# Merge with base modifier scores using frozenset operations
base_modifiers = {0: 15, 1: 30, 2: 45}
combined_keys = frozenset(segment_scores.keys()).union(frozenset(base_modifiers.keys()))
merged_scores = {k: segment_scores.get(k, 0) + base_modifiers.get(k, 0) for k in combined_keys}

# Final aggregation using XOR
final_threat_score = 0
for val in merged_scores.values():
    final_threat_score ^= val

print(f"Result: {final_threat_score}")