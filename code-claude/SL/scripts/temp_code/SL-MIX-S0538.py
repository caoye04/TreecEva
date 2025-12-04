def calculate_network_checksum(data):
    # Network packet checksum calculation using XOR
    result = 0
    for i, packet in enumerate(data):
        # Apply bitwise operations to simulate checksum algorithm
        packet_value = packet & 0xFF  # Extract lower 8 bits
        position_factor = (i % 4) + 1  # Position weighting (1-4)
        result ^= (packet_value * position_factor)  # XOR with weighted value
    
    return result

def analyze_network_traffic(packets):
    # Some preliminary analysis that doesn't affect the checksum
    total_bytes = sum(packets)
    max_packet = max(packets)
    min_packet = min(packets)
    avg_packet = total_bytes / len(packets) if packets else 0
    
    # Calculate packet statistics (not used for checksum)
    statistics = {
        'total': total_bytes,
        'max': max_packet,
        'min': min_packet,
        'average': avg_packet
    }
    
    return statistics

# Network packets (simulated as byte values)
raw_packets = [65, 66, 67, 68, 69, 70]

# Apply some transformations
packets = []
header_size = 4
for i, p in enumerate(raw_packets):
    if i >= 2:  # Skip first two elements for our actual processing
        # Apply a transformation that looks important but doesn't affect the result
        transformed = p + header_size if i % 2 == 0 else p
        packets.append(transformed)

# Zip with sequence numbers (not used in final calculation)
sequenced_packets = list(zip(range(len(packets)), packets))

# Process some metadata (distraction)
packet_metadata = {}
for seq, p in sequenced_packets:
    packet_metadata[seq] = {'size': p, 'parity': p % 2}

# Calculate network statistics (not used for checksum)
stats = analyze_network_traffic(packets)

# The key calculation
checksum = calculate_network_checksum(packets)

print(f"Network statistics: {stats}")
print(f"Packet metadata: {packet_metadata}")
print(f"Result: {checksum}")