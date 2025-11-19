from collections import deque

def decode_header(header):
    return ''.join(chr(ord(c) ^ 0b10101010) for c in header)

def calculate_checksum(segment):
    return sum(ord(c) for c in segment) & 0xFF

# Encoded packet headers
encoded_packets = ['\x85\x94\x81\x97', '\x86\x91\x84\x92', '\x87\x96\x83\x95']

# Processing pipeline
header_stack = []
processing_queue = deque()

# Step 1: Decode and push to stack
for packet in encoded_packets:
    decoded = decode_header(packet)
    header_stack.append(decoded)

# Step 2: Pop from stack and enqueue
while header_stack:
    processing_queue.append(header_stack.pop())

# Step 3: Process checksums
checksums = []
while processing_queue:
    segment = processing_queue.popleft()
    checksum = calculate_checksum(segment)
    checksums.append(checksum)

# Step 4: Combine checksums with bit operations
decoded_checksum = 0
for i, cs in enumerate(checksums):
    if i % 2 == 0:
        decoded_checksum ^= cs << (i // 2)
    else:
        decoded_checksum |= cs >> (i // 1)

decoded_checksum &= 0xFF
print(f"Result: {decoded_checksum}")