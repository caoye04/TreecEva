def compute_checksum(text):
    checksum = 0
    for char in text:
        checksum = (checksum ^ ord(char)) & 0xFF
        # Apply rotation for more complex checksum
        checksum = ((checksum << 1) | (checksum >> 7)) & 0xFF
    return checksum

def encrypt_value(value):
    # Encryption algorithm - XOR with key and apply bit rotation
    key = 42
    result = value ^ key
    result = ((result << 2) | (result >> 6)) & 0xFF
    return result

def decrypt_value(value):
    # Reverse of encryption (not used in main calculation)
    key = 42
    result = ((value >> 2) | (value << 6)) & 0xFF
    result = result ^ key
    return result

# Network status monitoring system
network_devices = {
    'router1': {'status': 'online', 'packets': 2500, 'errors': 5},
    'switch1': {'status': 'offline', 'packets': 0, 'errors': 0},
    'server1': {'status': 'online', 'packets': 7800, 'errors': 12},
    'server2': {'status': 'degraded', 'packets': 3400, 'errors': 45}
}

# Calculate network statistics
total_packets = sum(device['packets'] for device in network_devices.values())
error_rate = sum(device['errors'] for device in network_devices.values()) / total_packets if total_packets else 0

# Process message data
message = "SECURE_TRANSMISSION"
validation_set = set(message.lower())
control_set = {'s', 'e', 'c', 'u', 'r', '_', 't', 'a', 'n', 'i', 'm', 'o'}

# Security validation
is_valid = validation_set.issubset(control_set)
alternative_validation = len(validation_set - control_set) == 0

# Calculate security metrics
security_level = 3 if is_valid else 1
checksum = compute_checksum(message)

# Determine processing mode based on network conditions
processing_mode = 'normal' if error_rate < 0.01 else 'enhanced'
debug_mode = False

# Target value calculation
base_value = len(message) * security_level
adjusted_value = base_value + (checksum if processing_mode == 'enhanced' else 0)
target_value = adjusted_value % 256

# Security operations
encrypted_message = encrypt_value(target_value)
decrypted_check = decrypt_value(encrypted_message) == target_value

# Diagnostic information (not used in main calculation)
if debug_mode:
    diagnostic = {
        'message_length': len(message),
        'unique_chars': len(set(message)),
        'checksum': checksum,
        'security_level': security_level,
        'processing_mode': processing_mode,
        'target_value': target_value,
        'encrypted': encrypted_message,
        'verification': decrypted_check
    }

# Output the result
print(f"Result: {encrypted_message}")