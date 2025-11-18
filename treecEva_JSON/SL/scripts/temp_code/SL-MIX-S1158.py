from functools import reduce
from collections import namedtuple

def tokenize_header(header_str):
    return [token.encode() for token in header_str.split(':')]

def xor_shift_transform(tokens):
    transformed = []
    for i, token in enumerate(tokens):
        # XOR each byte with its position and apply left shift
        shifted_bytes = bytes((byte ^ i) << 1 & 0xFF for byte in token)
        transformed.append(shifted_bytes)
    return transformed

def compute_anomaly_weights(transformed_data):
    weights = []
    for item in transformed_data:
        # Apply bitwise AND with mask 0x7F and sum
        masked_sum = sum(byte & 0x7F for byte in item)
        weights.append(masked_sum)
    return weights

# Packet header analysis
PacketHeader = namedtuple('PacketHeader', ['source', 'destination', 'flags'])
header_info = PacketHeader(
    source="192.168.1.100",
    destination="10.0.0.5",
    flags="SYN:ACK:PSH"
)

# Process the flags field for anomaly detection
raw_tokens = tokenize_header(header_info.flags)
transformed_packets = xor_shift_transform(raw_tokens)
anomaly_weights = compute_anomaly_weights(transformed_packets)

# Calculate final anomaly score using functional approach
anomaly_score = reduce(lambda acc, w: acc ^ (w << 2), anomaly_weights, 0) & 0xFFFF

print(f"Result: {anomaly_score}")