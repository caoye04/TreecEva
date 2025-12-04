# Network packet analysis with bitwise operations

def analyze_packets(packet_data):
    # Process raw packet data
    checksums = {}
    priority_queue = []
    
    # Calculate initial metrics
    total_size = sum(len(p) for p in packet_data)
    avg_size = total_size / len(packet_data) if packet_data else 0
    
    for i, packet in enumerate(packet_data):
        # Extract packet information
        packet_id = i + 1
        size = len(packet)
        
        # Calculate checksum (simple XOR of all bytes)
        checksum = 0
        for byte in packet:
            checksum ^= byte
        
        # Store checksum in dictionary
        checksums[packet_id] = checksum
        
        # Calculate priority score (doesn't affect final result)
        priority = (size * 2) // 3
        priority_queue.append((priority, packet_id))
    
    # Find packets with checksums divisible by 4
    divisible_by_4 = [pid for pid, csum in checksums.items() if csum % 4 == 0]
    divisible_count = len(divisible_by_4)
    
    # Calculate base hash from checksum of specific packet
    target_id = 3
    base_hash = checksums.get(target_id, 0)
    if target_id not in checksums:
        base_hash = sum(checksums.values()) & 0xFF
    
    # Apply security mask based on divisible count
    mask = (divisible_count * 7) | 0x12
    
    # Final optimized hash calculation
    optimal_hash = (base_hash ^ mask) & 0xFF
    
    # Validate hash (doesn't affect result)
    is_valid = optimal_hash > 0
    
    return {
        "total_packets": len(packet_data),
        "avg_size": avg_size,
        "divisible_count": divisible_count,
        "hash": optimal_hash
    }

# Test with sample packet data (represented as lists of integers)
packet_data = [
    [65, 66, 67, 68],  # Packet 1
    [70, 71, 72],      # Packet 2
    [80, 90, 100, 110] # Packet 3
]

result = analyze_packets(packet_data)
print(f"Result: {result['hash']}")