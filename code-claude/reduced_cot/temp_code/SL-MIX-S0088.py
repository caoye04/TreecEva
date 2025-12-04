def process_password(password):
    # Extract only alphanumeric characters
    clean_pass = ''.join(c for c in password if c.isalnum())
    
    # Calculate base value from character positions
    base_value = 0
    for i, char in enumerate(clean_pass):
        base_value += (i + 1) * ord(char)
    
    # Convert to binary string with padding
    binary_str = bin(base_value)[2:]
    padding_needed = 16 - (len(binary_str) % 16)
    if padding_needed < 16:
        binary_str = '0' * padding_needed + binary_str
    
    # Split into chunks for processing
    chunks = [binary_str[i:i+8] for i in range(0, len(binary_str), 8)]
    
    # Calculate checksum (this is a distraction)
    checksum = 0
    for chunk in chunks:
        checksum += int(chunk, 2) % 256
    
    # Select specific portion for the key
    selected_chunk = chunks[1]  # Second chunk
    reversed_chunk = selected_chunk[::-1]  # Reverse it
    
    # Add some noise bits (distraction)
    noise_bits = '1010'
    binary_value = reversed_chunk + noise_bits
    binary_value = binary_value[:-4]  # Remove the noise
    
    # Calculate encryption key
    encryption_key = int(binary_value, 2) ^ checksum
    
    # Additional calculations (distractions)
    verification_code = (base_value // 100) + (checksum * 2)
    security_level = min(10, len(clean_pass) * 2)
    
    # Log the results
    print(f"Password strength: {security_level}/10")
    print(f"Verification code: {verification_code}")
    print(f"Result: {encryption_key}")
    
    return encryption_key

# Process a sample password
password = "Secure!123"
final_key = process_password(password)