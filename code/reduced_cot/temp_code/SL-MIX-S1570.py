import itertools

def process_packets(packets):
    if len(packets) < 3:
        return 0
    
    # Initialize checksum with first three packets XORed together
    checksum = packets[0] ^ packets[1] ^ packets[2]
    
    # Lambda for transforming a packet value with shifts and masking
    transform = lambda x: ((x << 1) & 0xFF) | ((x >> 2) & 0x3F)
    
    # Process remaining packets
    for i in range(3, len(packets)):
        prev1_transformed = transform(packets[i-1])
        prev2_transformed = transform(packets[i-2])
        checksum ^= packets[i] ^ prev1_transformed ^ prev2_transformed
    
    return checksum

# Packet sequence representing data transmission
packet_sequence = [0x12, 0x34, 0x56, 0x78, 0x9A, 0xBC]
final_checksum = process_packets(packet_sequence)
print(f"Result: {final_checksum}")