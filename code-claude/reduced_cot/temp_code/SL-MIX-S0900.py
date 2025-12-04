# Simple message encryption using bitwise operations

message = 42  # Original message to encrypt
key = 15      # Encryption key

# Lambda function to encrypt a message using XOR cipher
cipher = lambda msg, k: msg ^ k

# Some processing variables
validation = message & key  # Bitwise AND for validation
check_sum = message | key  # Bitwise OR for checksum

# Encrypt the message
encrypted_code = cipher(message, key)

print(f"Validation: {validation}")
print(f"Checksum: {check_sum}")
print(f"Result: {encrypted_code}")