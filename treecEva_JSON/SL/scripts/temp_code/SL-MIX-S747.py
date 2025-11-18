import re
from collections import defaultdict

packet_headers = ['AUTH_2023', 'ENCRYPT_v2', 'SYN_ACK_101', 'DATA_XYZ789']
char_frequency = defaultdict(int)
intermediate_values = []

for idx, header in enumerate(packet_headers):
    masked_sum = 0
    for pos, char in enumerate(header):
        ascii_val = ord(char)
        shifted_pos = pos << (idx & 3)  # Shift position by index mod 4
        xor_result = ascii_val ^ shifted_pos
        masked_value = xor_result & 0xF0  # Keep only upper 4 bits
        masked_sum += masked_value
        if re.match(r'[A-Z]', char):  # Count uppercase letters
            char_frequency[char] += 1
    intermediate_values.append(masked_sum)

# Calculate final security score
security_score = 0
for i, val in enumerate(intermediate_values):
    if i % 2 == 0:
        security_score |= val  # Bitwise OR for even indices
    else:
        security_score ^= val  # Bitwise XOR for odd indices

# Apply final adjustment based on character frequency
if len(char_frequency) > 10:
    security_score >>= 2
else:
    security_score <<= 1

print(f"Result: {security_score}")