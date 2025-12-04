def calculate_checksum(data, multiplier=1):
    # Calculate weighted checksum of data
    checksum = 0
    for i, char in enumerate(data):
        if i % 3 == 0:
            checksum += ord(char) * 2
        else:
            checksum += ord(char)
    return checksum * multiplier

def encrypt_data(input_string, shift):
    # Simple encryption that isn't actually used
    result = ""
    for char in input_string:
        result += chr((ord(char) + shift) % 256)
    return result

def calculate_final_security(fragments, key):
    # Process message fragments to determine security level
    priority_values = []
    integrity_score = 0
    validation_bits = 0
    
    # These values are misleading and not used in final calculation
    decoy_values = []
    threat_level = 5
    anomaly_count = 0
    
    for idx, fragment in enumerate(fragments):
        # Calculate fragment integrity
        if len(fragment) > 0:
            integrity = sum(ord(c) for c in fragment) & 0xFF
            if idx % 2 == 0:
                # Only even-indexed fragments affect security
                priority_values.append(integrity)
            else:
                # Odd-indexed fragments are tracked but don't affect result
                decoy_values.append(integrity * 2)
                
        # Track validation bits using XOR
        if idx < len(key):
            validation_bits ^= (ord(key[idx]) & 0x0F)
            
        # This appears important but doesn't affect final result
        if fragment.lower().startswith('x'):
            threat_level += 1
            anomaly_count += 1
    
    # Calculate misleading integrity score
    for val in decoy_values:
        integrity_score += (val // 2)
    
    # Only process certain priority values based on validation bits
    filtered_values = []
    for i, val in enumerate(priority_values):
        if i < 8:  # Only consider first 8 values
            if (validation_bits & (1 << (i % 4))) != 0:
                filtered_values.append(val)
    
    # Final security level calculation
    if len(filtered_values) > 0:
        base_security = sum(filtered_values) // len(filtered_values)
    else:
        base_security = 0
    
    # Apply security modifiers based on key
    key_modifier = 0
    for i, char in enumerate(key):
        if i % 2 == 0:  # Only use even positions in key
            key_modifier += (ord(char) & 0x1F)  # Use lower 5 bits only
    
    # These operations look important but don't affect result
    if threat_level > 7:
        integrity_score = (integrity_score * threat_level) // 10
    
    if anomaly_count > 0:
        decoy_adjustment = anomaly_count * 5
    else:
        decoy_adjustment = 0
    
    # Calculate final security level
    security_level = (base_security + key_modifier) ^ validation_bits
    
    return security_level

# Main code execution
message_fragments = ["Hello", "X-ray", "Delta", "xylophone", "Omega"]
encryption_key = "S3CR3T"

# Perform some misleading operations
checksum_value = calculate_checksum("SecurityProtocol", 2)
encrypted_data = encrypt_data("ConfidentialData", 7)

# This appears to be preparation for something important
backup_fragments = message_fragments.copy()
for i, fragment in enumerate(backup_fragments):
    if i % 2 == 1:
        backup_fragments[i] = fragment.upper()

# These variables look important but aren't used
priority_index = sum(1 for f in message_fragments if len(f) > 4)
security_zones = {"alpha": 10, "beta": 20, "gamma": 30}
zone_weights = [security_zones.get(f.lower(), 0) for f in message_fragments]

# Calculate the security level - this is the key operation
security_level = calculate_final_security(message_fragments, encryption_key)

# Some post-calculation operations that don't affect the result
if checksum_value > 1000:
    security_level_backup = security_level + 50
else:
    security_level_backup = security_level

# This appears to modify security_level but actually creates a new variable
adjusted_security = security_level + sum(zone_weights) // len(zone_weights)

print(f"Result: {security_level}")