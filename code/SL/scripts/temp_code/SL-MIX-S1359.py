from functools import reduce
import base64

def process_packets(headers):
    # Apply XOR folding reduction on header values
    folded = reduce(lambda x, y: x ^ y, headers, 0)
    
    # Conditional transformation based on parity
    transformed = (folded << 2) if folded % 2 == 0 else (folded >> 1)
    
    # Encode and decode cycle with base64
    encoded = base64.b64encode(str(transformed).encode())
    decoded = int(base64.b64decode(encoded).decode())
    
    # Final checksum calculation with ternary adjustment
    checksum = decoded + 100 if decoded > 50 else decoded - 50
    return checksum

# Packet header sequence
packet_headers = [0x1A, 0x2B, 0x3C, 0x4D, 0x5E]

# Process the packets
checksum = process_packets(packet_headers)
print(f"Result: {checksum}")