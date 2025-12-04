# Network packet analysis
source_data = [0b1101, 0b1010, 0b1100, 0b0101]
target_mask = 0b1010

# Extract bits that match the target pattern
match_condition = lambda x: (x & target_mask) == target_mask
matched_packets = [p for p in source_data if match_condition(p)]

# Calculate filtered bits by extracting the second bit from each packet
get_second_bit = lambda x: (x >> 2) & 1
bits = [get_second_bit(packet) for packet in matched_packets]
filtered_bits = sum(bits)

# Verify packet integrity
valid_count = len(matched_packets)
protocol_overhead = 2

print(f"Result: {filtered_bits}")