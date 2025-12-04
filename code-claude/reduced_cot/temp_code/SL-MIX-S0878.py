# Network packet validation system
# Each packet has a value calculated from its header bits

header_bits = [0b1101, 0b0110, 0b1011, 0b0101, 0b1010]
packet_values = []

# Process each header bit with its position
for i, bits in enumerate(header_bits):
    # Apply position-based XOR transformation
    transformed = bits ^ (i + 1)
    packet_values.append(transformed)

# Calculate integrity values using zip
integrity_factors = [2, 1, 3, 1, 2]
integrity_values = []
for val, factor in zip(packet_values, integrity_factors):
    integrity_values.append(val * factor)

# Track statistics
total_integrity = sum(integrity_values)
avg_integrity = total_integrity / len(integrity_values)

# Calculate final checksum from packet values
checksum = sum(packet_values)

print(f"Result: {checksum}")