from collections import namedtuple
import base64

def process_cryptographic_layer(data, key):
    return ''.join(chr(ord(c) ^ key) for c in data)

def calculate_weighted_sum(text):
    return sum(ord(char) * (i + 1) for i, char in enumerate(text))

# Initialize cryptographic components
MessagePacket = namedtuple('MessagePacket', ['content', 'encoding_key'])
cipher_key = 42
initial_payload = "SECRET"
encoded_template = {i: chr(ord(c) + i) for i, c in enumerate(initial_payload)}

# Process message through first transformation layer
packet = MessagePacket(content=initial_payload, encoding_key=cipher_key)
transformed_content = process_cryptographic_layer(packet.content, packet.encoding_key)

# Apply secondary encoding with dictionary merging
secondary_encoding = {k: v.upper() if k % 2 == 0 else v.lower() for k, v in encoded_template.items()}
merged_map = {**encoded_template, **secondary_encoding, len(encoded_template): '!'}

# Generate checksum components using lambda and set operations
char_set = frozenset(transformed_content)
validation_chars = {'S', 'E', 'C', 'R', 'T'}
common_elements = char_set & validation_chars
checksum_lambda = lambda s: sum(ord(c) for c in s) if s else 0

# Calculate intermediate values
intermediate_sum = calculate_weighted_sum(transformed_content)
base64_segment = base64.b64encode(transformed_content.encode()).decode()
segment_length = len(base64_segment)

# Final cryptographic computation using ternary operator
adjusted_sum = intermediate_sum if intermediate_sum > 1000 else intermediate_sum * 2
final_checksum = adjusted_sum + checksum_lambda(common_elements) + (segment_length if '!' in merged_map.values() else 0)

print(f"Result: {final_checksum}")