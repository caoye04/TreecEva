import base64
from collections import namedtuple

# Define packet structure
def process_packets():
    Packet = namedtuple('Packet', ['id', 'payload', 'priority'])
    
    # Encoded packets with custom scheme
    encoded_packets = [
        "eFtVXlZcQ1xAW1BdRFpEXURaQg==",
        "cFhZW19dW1hcX1pdXltfWw==",
        "QkJBQkFCQUJCQUJBQkFCQQ=="
    ]
    
    # Decryption keys
    xor_keys = [15, 32, 7, 23]
    
    # Step 1: Decode and decrypt packets
    decrypted_payloads = []
    for i, packet in enumerate(encoded_packets):
        # Base64 decode
        decoded_bytes = base64.b64decode(packet)
        
        # XOR decryption with rotating key
        decrypted = bytes([b ^ xor_keys[j % len(xor_keys)] for j, b in enumerate(decoded_bytes)])
        decrypted_payloads.append(decrypted.decode('utf-8'))
    
    # Step 2: Create packet objects
    packets = [
        Packet(id=1001 + i, payload=payload, priority=len(payload))
        for i, payload in enumerate(decrypted_payloads)
    ]
    
    # Step 3: Compute weighted checksum using floating point
    total_weighted_length = 0.0
    for p in packets:
        weight = p.priority * 0.75
        adjusted_length = float(len(p.payload)) + (weight / 3.0)
        total_weighted_length += adjusted_length
    
    # Step 4: Apply security transformation
    security_modifiers = {p.id: p.priority * 1.25 for p in packets}
    max_modifier = max(security_modifiers.values())
    
    # Final security score calculation
    security_score = (total_weighted_length * 2.5) - max_modifier
    
    return round(security_score, 2)

# Execute the function and print result
final_score = process_packets()
print(f"Target result: {final_score}")