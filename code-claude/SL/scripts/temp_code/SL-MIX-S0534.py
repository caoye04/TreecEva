def calculate_transmission_integrity(signal_strength, noise_ratio):
    # Simulate signal integrity calculation (not used in main logic)
    integrity = 100 - (signal_strength * noise_ratio / 10)
    if integrity < 0:
        return 0
    return min(100, integrity)

# Dictionary mapping characters to numerical values
message_values = {
    'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9,
    'j': 10, 'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17,
    'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26
}

# Encrypted message from space station
encrypted_message = "satellite_communication_protocol_v2.3"

# Signal metadata (not relevant to core calculation)
metadata = {
    "station_id": "XRS-7b",
    "timestamp": 1647982345,
    "signal_strength": 87.5,
    "noise_ratio": 0.23,
    "encryption_level": 3
}

# Process the message
filtered_chars = [c for c in encrypted_message if c.isalpha()]
reversed_message = filtered_chars[::-1]

# Calculate potential frequencies (distraction)
char_frequency = {}
for char in filtered_chars:
    if char in char_frequency:
        char_frequency[char] += 1
    else:
        char_frequency[char] = 1

# Find characters at prime positions (distraction)
prime_positions = [2, 3, 5, 7, 11, 13, 17, 19, 23]
prime_chars = [filtered_chars[i] for i in prime_positions if i < len(filtered_chars)]

# Calculate integrity score based on signal metadata (distraction)
integrity_score = calculate_transmission_integrity(
    metadata["signal_strength"], 
    metadata["noise_ratio"]
)

# Apply decoding algorithm based on position and character values
position_values = []
for i, char in enumerate(filtered_chars):
    # Complex formula that doesn't affect final result
    position_value = (i * message_values.get(char, 0)) % 30
    position_values.append(position_value)

# Extract priority characters based on specific pattern
priority_indices = [3, 7, 9, 14, 19, 24]
priority_chars = [filtered_chars[i] for i in priority_indices if i < len(filtered_chars)]

# Calculate checksum (distraction)
checksum = sum(message_values.get(c, 0) for c in filtered_chars) % 256

# Calculate redundancy factor (distraction)
redundancy = len(set(filtered_chars)) / len(filtered_chars) if filtered_chars else 0

# Apply decoding algorithm - this is the key operation
decoded_message = sum(map(lambda x: message_values[x], priority_chars))

# Perform verification (distraction)
verification_key = (checksum * int(metadata["encryption_level"])) % 100

# Apply additional transformation that doesn't affect the result
if integrity_score > 90:
    # This condition is false (integrity_score is ~79.9)
    decoded_message = decoded_message * 2

print(f"Decoded message value: {decoded_message}")
