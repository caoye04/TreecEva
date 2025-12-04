def secure_transform(data, security_key):
    mask = 0b10101010
    key = security_key
    original_value = data
    
    # Perform bitwise encryption operation
    encrypted_value = ((original_value & mask) | (~original_value & ~mask)) ^ key
    
    # Verification step (distraction)
    verification = encrypted_value & 0xFF
    
    print(f"Result: {encrypted_value}")
    return encrypted_value

# Main execution
input_data = 170  # 0b10101010 in decimal
security_key = 85  # 0b01010101 in decimal
result = secure_transform(input_data, security_key)