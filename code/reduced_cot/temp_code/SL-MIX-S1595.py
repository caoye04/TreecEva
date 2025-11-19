import hashlib

def hex_to_binary(hex_string):
    return bin(int(hex_string, 16))[2:].zfill(len(hex_string) * 4)

def process_packet(packet_id):
    # Convert hex packet ID to binary representation
    binary_repr = hex_to_binary(packet_id)
    
    # Apply bitwise rotation
    rotated = binary_repr[4:] + binary_repr[:4]
    
    # Hash the rotated binary string
    hash_object = hashlib.sha256(rotated.encode())
    hex_dig = hash_object.hexdigest()
    
    # Sum ASCII values of first 8 characters of hash
    ascii_sum = sum(ord(char) for char in hex_dig[:8])
    return ascii_sum

# Network packet identifiers in hexadecimal
network_packets = ['A1B2C3D4', 'E5F6A7B8', 'C9D0E1F2', 'F3A4B5C6']

# Frequency map for packet type classification
packet_frequency = {
    'A1B2C3D4': 'TCP',
    'E5F6A7B8': 'UDP',
    'C9D0E1F2': 'ICMP',
    'F3A4B5C6': 'TCP'
}

# Security weight mapping for packet types
security_weights = {
    'TCP': 3,
    'UDP': 2,
    'ICMP': 1
}

# Process packets using list comprehension and accumulate weighted security index
processed_values = [process_packet(packet) for packet in network_packets]

# Calculate security index using weighted sum based on packet types
security_index = sum(
    value * security_weights[packet_frequency[network_packets[i]]]
    for i, value in enumerate(processed_values)
)

# Apply final transformation: XOR with magic number
magic_number = 0x5A
security_index ^= magic_number

print(f"Result: {security_index}")