import base64
import numpy as np

def signal_transformer(signal_matrix):
    # Transpose the matrix
    transposed = signal_matrix.T
    
    # Apply bit masking to odd rows (0-indexed)
    for i in range(0, transposed.shape[0], 2):
        transposed[i] = transposed[i] & 0xF0  # Mask lower 4 bits
    
    # Calculate row sums
    row_sums = np.sum(transposed, axis=1)
    
    # Convert to list and apply special encoding
    encoded_sums = [x << 2 for x in row_sums.tolist()]
    
    return encoded_sums

def checksum_validator(data_segment):
    # Create dictionary of positional checksums
    checksum_map = {i: (value ^ (i * 3)) for i, value in enumerate(data_segment)}
    
    # Merge with base validation values
    base_validation = {0: 100, 2: 200, 4: 300}
    merged_checksums = {**checksum_map, **base_validation}
    
    # Calculate final score
    score = sum(merged_checksums.values())
    return score

# Encoded signal data
encoded_data = "NjY2IDUxMiA3NjggNDEwIDU3OCA0ODI="

# Decode and reshape into matrix
raw_bytes = base64.b64decode(encoded_data)
values = [int(x) for x in raw_bytes.decode().split()]
observation_matrix = np.array(values).reshape((3, 2))

# Process the signal
transformed_data = signal_transformer(observation_matrix)

# Validate and calculate final score
verification_score = checksum_validator(transformed_data)

print(f"Result: {verification_score}")