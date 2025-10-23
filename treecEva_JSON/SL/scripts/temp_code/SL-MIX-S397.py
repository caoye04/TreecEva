from collections import defaultdict
import hashlib

def compute_segment_hash(segment):
    return int(hashlib.md5(segment.encode()).hexdigest()[:8], 16)

def process_message_segments(segments):
    # Initialize transformation matrix
    transform_matrix = [
        [0b1010, 0b0101, 0b1111],
        [0b1100, 0b0011, 0b0110],
        [0b1001, 0b0110, 0b1010]
    ]
    
    # Initialize segment registry
    segment_registry = defaultdict(int)
    
    # Process each segment
    for i, segment in enumerate(segments):
        # Compute hash of segment
        segment_hash = compute_segment_hash(segment)
        
        # Apply bitwise transformations
        transformed_value = (segment_hash ^ 0xCAFEBABE) & 0xFFFFFFFF
        shifted_value = (transformed_value << 3) | (transformed_value >> 29)
        
        # Update registry with transformed value
        segment_registry[i] = shifted_value
    
    # Apply matrix transformation
    matrix_result = [0, 0, 0]
    for i in range(3):
        for j in range(3):
            matrix_result[i] ^= (segment_registry[j] & transform_matrix[i][j])
    
    # Calculate final secure checksum
    secure_checksum = 0
    for i, val in enumerate(matrix_result):
        secure_checksum ^= (val << (i * 8))
    
    return secure_checksum

# Message segments for processing
message_segments = ["START", "DATA_PAYLOAD", "END"]

# Process the message and get the secure checksum
secure_checksum = process_message_segments(message_segments)
print(f"Result: {secure_checksum}")