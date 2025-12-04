def compute_fibonacci(limit):
    """Generate Fibonacci sequence up to limit"""
    sequence = [1, 1]
    while sequence[-1] + sequence[-2] <= limit:
        sequence.append(sequence[-1] + sequence[-2])
    return sequence

def analyze_network_packet(packet_data, security_level):
    """Analyze network packet and extract security metrics"""
    # Extract header information (distractor)
    header_size = (packet_data & 0xFF00) >> 8
    protocol_type = packet_data & 0xFF
    
    # Calculate checksum (distractor)
    checksum = (header_size * 17) ^ protocol_type
    
    # Security validation
    validation_bits = 0
    if security_level > 3:
        validation_bits = (packet_data & 0xF000) >> 12
    else:
        validation_bits = (packet_data & 0x0F00) >> 8
    
    return validation_bits | (checksum & 0x0F)

# Initialize system parameters
system_state = 0x1234
network_load = 78
security_threshold = 4

# Generate reference sequences
fibonacci_sequence = compute_fibonacci(200)
primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

# Process incoming data packets
packet_buffer = [0x3A21, 0x4F19, 0x7B22, 0x8C01]
valid_packets = 0

for packet in packet_buffer:
    # Update system state based on packet (distractor)
    system_state = (system_state + packet) & 0xFFFF
    
    # Process packet if system is not overloaded (distractor)
    if network_load < 90:
        security_bits = analyze_network_packet(packet, security_threshold)
        if security_bits > 0:
            valid_packets += 1

# Determine data integrity level (relevant for key generation)
integrity_level = valid_packets * primes[valid_packets % len(primes)]

# Calculate potential threat vectors (distractor)
threat_vectors = []
for i in range(5):
    vector = (system_state & (0xF << (i*4))) >> (i*4)
    threat_vectors.append(vector)

# Security parameter extraction
valid_bits = integrity_level + (fibonacci_sequence[valid_packets] if valid_packets < len(fibonacci_sequence) else 0)

# Generate encryption key based on security parameters
encryption_key = (valid_bits >> 2) ^ ((fibonacci_sequence[-3] & 0xFF) << 3)

# Attempted decryption with wrong key (distractor)
decryption_attempt = encryption_key ^ system_state
if decryption_attempt % 2 == 0:
    alternative_key = encryption_key + 1
else:
    alternative_key = encryption_key - 1

# Diagnostic information (distractor)
diagnostic_data = {
    'system_state': hex(system_state),
    'network_load': network_load,
    'valid_packets': valid_packets,
    'integrity_level': integrity_level
}

print(f"Result: {encryption_key}")