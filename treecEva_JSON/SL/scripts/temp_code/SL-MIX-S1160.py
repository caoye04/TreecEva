import re
from collections import Counter
def process_message_id(hex_id):
    # Convert hex to integer
    numeric_value = int(hex_id, 16)
    # Apply bitwise transformations
    masked_value = numeric_value & 0xFF
    shifted_value = masked_value << 2
    xor_result = shifted_value ^ 0xAA
    return xor_result

def calculate_checksum(message_string):
    # Character frequency analysis
    char_freq = Counter(message_string)
    # Sum frequencies of alphanumeric characters only
    freq_sum = sum(count for char, count in char_freq.items() if char.isalnum())
    # Bitwise adjustment
    adjusted_sum = freq_sum | 0x0F
    return adjusted_sum

# Main processing
message_log = ['A1B2C3D4', 'E5F6A7B8', 'C9D0E1F2']
validation_counter = 0
for msg_id in message_log:
    # Extract alphanumeric components using regex
    clean_msg = ''.join(re.findall(r'[A-F0-9]', msg_id))
    processed_id = process_message_id(msg_id)
    checksum = calculate_checksum(clean_msg)
    # Combine results with arithmetic and bitwise ops
    combined = (processed_id + checksum) & 0xFFFF
    validation_counter += (combined >> 4) ^ 0x55

print(f'Result: {validation_counter}')