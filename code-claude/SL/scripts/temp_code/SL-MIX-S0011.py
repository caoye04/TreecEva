# Data transmission verification system
# Calculate checksum of message bytes using XOR with position

message = "hello"
logger_active = True
retry_count = 3

# Convert message to byte values
message_bytes = [ord(char) for char in message]

# Generate position weights
position_weights = list(range(len(message_bytes)))

# Calculate checksum using XOR with position
checksum = sum([message_value ^ position for position, message_value in enumerate(message_bytes)])

# Validate message integrity
valid = checksum > 0

# For debugging
if logger_active:
    print(f"Message: {message}")
    print(f"Byte values: {message_bytes}")
    print(f"Result: {checksum}")