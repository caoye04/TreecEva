def decrypt_message(message, key):
    # Simple XOR decryption with dictionary mapping
    result = 0
    char_values = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6}
    position_multipliers = {0: 1, 1: 2, 2: 3}
    
    for i, char in enumerate(message):
        if i < len(position_multipliers):
            # Apply position-based multiplier and XOR with key
            char_value = char_values.get(char, 0)
            multiplier = position_multipliers[i]
            result += (char_value * multiplier) ^ key
    
    return result

# Message processing
encrypted_message = "CAB"
temporary_key = 7
cipher_key = temporary_key & 0xF  # Ensure key is 4-bits only

# Decrypt the message
decrypted_value = decrypt_message(encrypted_message, cipher_key)
print(f"Result: {decrypted_value}")