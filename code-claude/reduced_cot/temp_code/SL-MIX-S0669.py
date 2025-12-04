def analyze_traffic(packets, filter_type=None):
    # Traffic analyzer helper function
    if filter_type == 'UDP':
        return sum([p & 0xFF for p in packets if p > 0x1000])
    elif filter_type == 'TCP':
        return sum([p >> 4 for p in packets if p % 2 == 0])
    else:
        return sum([p for p in packets]) // len(packets)

def extract_and_process(data_stream, protocol_idx):
    # Extract relevant bytes from network packets and compute checksum
    if not data_stream or protocol_idx < 0:
        return -1
    
    # Extract slice based on protocol index
    relevant_data = data_stream[protocol_idx::3]
    
    # Initialize tracking variables
    checksum = 0
    error_count = 0
    processing_flags = [False, True, True, False]
    
    # Process the data slice
    for i, packet in enumerate(relevant_data):
        # Skip corrupted packets (simulation)
        if packet < 0:
            error_count += 1
            continue
            
        # Apply different processing based on packet position
        if i % 4 == 0:
            # Header packet - XOR with current checksum
            checksum ^= packet
        elif i % 4 == 1:
            # Data packet - add to checksum if processing flag is set
            if processing_flags[1]:
                checksum += packet & 0x3F  # Use only 6 lower bits
        elif i % 4 == 2:
            # Control packet - subtract from checksum if value exceeds threshold
            if packet > 50 and processing_flags[2]:
                checksum -= packet // 10
        else:
            # Footer packet - always add to checksum
            checksum += (packet >> 2)  # Right shift by 2
    
    # Apply final transformation if errors were detected
    if error_count > 0:
        # This is a distraction - we'll overwrite checksum below
        error_adjustment = error_count * 5
        checksum = (checksum + error_adjustment) & 0xFF
    
    # Final checksum calculation - only this matters for the result
    if len(relevant_data) > 0:
        checksum = sum(relevant_data) & 0xFF
    
    return checksum

# Network packet simulation
network_packets = [72, 101, 108, 108, 111, 87, 111, 114, 108, 100]

# Analysis parameters
protocol_types = ['TCP', 'UDP', 'ICMP']
protocol_index = 2  # Start from the third packet
packet_threshold = 100

# Perform preliminary analysis (distraction)
preliminary_scan = analyze_traffic(network_packets, 'UDP')
filtered_packets = [p for p in network_packets if p > 90]

# Extract header information (distraction)
header_value = network_packets[0] if network_packets else 0
trailer_value = network_packets[-1] if network_packets else 0
header_xor = header_value ^ trailer_value

# Main processing
checksum = extract_and_process(network_packets, protocol_index)

# Verification steps (distraction)
verification_value = sum(network_packets) % 256
security_token = (header_xor + len(network_packets)) ^ 0xA5

print(f"Result: {checksum}")