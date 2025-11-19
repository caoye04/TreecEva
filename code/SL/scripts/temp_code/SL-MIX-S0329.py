from collections import defaultdict

tokens = ['0x1A3F', '0x4B2C', '0x1A3F', '0xF0F0', '0x4B2C', '0x1A3F', '0xC3A5']
valid_token_freq = defaultdict(int)

for hex_token in tokens:
    # Remove '0x' prefix and convert to uppercase for uniformity
    clean_token = hex_token[2:].upper()
    
    # Calculate checksum by XOR-ing all nibbles
    checksum = 0
    for char in clean_token:
        # Convert hex character to its decimal value
        nibble_val = int(char, 16)
        checksum ^= nibble_val
    
    # If checksum is zero, consider it a valid token
    if checksum == 0:
        valid_token_freq[clean_token] += 1

# Compute security score
security_score = 0
for token_hex, freq in valid_token_freq.items():
    # Convert token back to integer base 10
    token_numeric = int(token_hex, 16)
    security_score += token_numeric * freq

print(f"Result: {security_score}")