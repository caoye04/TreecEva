def decode_hex(hex_string):
    # Convert hex string to decimal
    try:
        return int(hex_string, 16)
    except ValueError:
        return 0

def calculate_checksum(data):
    # Calculate a simple checksum
    checksum = 0
    for byte in data.encode():
        checksum = (checksum + byte) % 256
    return checksum

def reverse_bits(num):
    # Reverse the bits in an 8-bit number
    result = 0
    for i in range(8):
        result = (result << 1) | (num & 1)
        num >>= 1
    return result

def calculate_priority(message, key_seq):
    # Main function to calculate message priority
    if not message or not key_seq:
        return -1
    
    # Security check - ignore messages with invalid checksums
    message_checksum = calculate_checksum(message)
    if message_checksum > 200:
        return 0
    
    # Parse message components
    components = message.split('|')
    if len(components) < 3:
        return -2
    
    # Extract metadata from components
    metadata = {}
    for comp in components:
        if ':' in comp:
            key, value = comp.split(':', 1)
            metadata[key.strip()] = value.strip()
    
    # Process security level - higher means more important
    security_level = 0
    if 'sec' in metadata:
        try:
            security_level = int(metadata['sec'])
        except ValueError:
            security_level = 1
    
    # Process timestamp - older messages get lower priority
    timestamp_factor = 1.0
    if 'ts' in metadata:
        try:
            timestamp = int(metadata['ts'])
            # Normalize timestamp factor between 0.5 and 1.5
            timestamp_factor = 1.0 + (timestamp % 100) / 100
            if timestamp < 1000:
                timestamp_factor = 0.5
        except ValueError:
            pass
    
    # Process urgency flag
    urgency = 0
    if 'urg' in metadata:
        urgency_value = metadata['urg'].lower()
        if urgency_value == 'high':
            urgency = 5
        elif urgency_value == 'medium':
            urgency = 3
        elif urgency_value == 'low':
            urgency = 1
    
    # Process payload if present
    payload_value = 0
    if 'payload' in metadata:
        payload = metadata['payload']
        # Extract hex values from payload
        hex_values = []
        for i in range(0, len(payload), 2):
            if i + 2 <= len(payload):
                hex_values.append(payload[i:i+2])
        
        # Calculate payload value
        for hex_val in hex_values[:3]:  # Only use first 3 hex values
            decoded = decode_hex(hex_val)
            # Apply bit manipulation to create distraction
            reversed_bits = reverse_bits(decoded)
            # This operation is actually irrelevant
            masked_value = decoded & 0x3F
            # Only the original decoded value matters
            payload_value += decoded
    
    # Process key sequence
    key_value = 0
    for i, k in enumerate(key_seq):
        if i >= 5:  # Only first 5 keys matter
            break
        key_value += ord(k) - ord('A') + 1 if 'A' <= k <= 'Z' else 0
    
    # Calculate base score
    base_score = security_level * 10 + urgency * 5
    
    # Apply various factors - most are distractions
    adjusted_score = base_score * timestamp_factor
    
    # These calculations are distractions
    distraction_1 = (security_level << 2) | (urgency & 0x3)
    distraction_2 = sum([ord(c) for c in message if c.isalpha()]) % 17
    
    # Calculate hash value - another distraction
    hash_val = 0
    for c in message:
        hash_val = (hash_val * 31 + ord(c)) % 997
    
    # Only this part matters for final calculation
    if 'cmd' in metadata and metadata['cmd'] == 'PRIORITY_OVERRIDE':
        return 999
    
    # Final priority calculation
    priority = int(adjusted_score) + payload_value + key_value
    
    # Apply special case rules - only this one actually matters
    if 'type' in metadata and metadata['type'] == 'CRITICAL':
        priority *= 2
    
    return priority

# Main execution
encrypted_message = "type:CRITICAL|sec:3|ts:1542|urg:medium|payload:2A4F|cmd:PROCESS"
key_sequence = "XYZAB"

# Calculate the message priority
priority_score = calculate_priority(encrypted_message, key_sequence)

# Display the result
print(f"Result: {priority_score}")