import heapq
from collections import namedtuple

def hex_to_int(hex_str):
    return int(hex_str, 16)

def compute_xor_checksum(values):
    result = 0
    for val in values:
        result ^= val
    return result

Packet = namedtuple('Packet', ['seq_num', 'header', 'payload_checksum'])

# Encoded packet data (sequence number, header hex, payload checksum hex)
encoded_packets = [
    ('0x03', '0xFF00AB', '0xC4'),
    ('0x01', '0x12AF3B', '0x9F'),
    ('0x02', '0x8C2D4E', '0x3A')
]

# Step 1: Decode sequence numbers and build packet objects
packet_queue = []
for seq_hex, header_hex, chksum_hex in encoded_packets:
    seq_num = hex_to_int(seq_hex)
    chksum = hex_to_int(chksum_hex)
    packet = Packet(seq_num, header_hex, chksum)
    heapq.heappush(packet_queue, (seq_num, packet))

# Step 2: Reorder packets using heap
ordered_packets = []
while packet_queue:
    _, pkt = heapq.heappop(packet_queue)
    ordered_packets.append(pkt)

# Step 3: Perform error checking with XOR on payload checksums
checksum_values = [pkt.payload_checksum for pkt in ordered_packets]
intermediate_checksum = compute_xor_checksum(checksum_values)

# Step 4: Apply ternary correction if intermediate checksum is odd
final_checksum = intermediate_checksum + 10 if intermediate_checksum % 2 == 1 else intermediate_checksum - 5

print(f"Result: {final_checksum}")