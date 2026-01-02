def preprocess_signal(raw_data, threshold=0.5):
    """
    Normalize signal and filter noise.
    This function is only partially relevant; some computations are red herrings.
    """
    normalized = [x / max(raw_data) for x in raw_data]
    filtered = [x for x in normalized if x > threshold]
    stats = {
        'peak': max(normalized),
        'baseline': sum(normalized) / len(normalized),
        'entropy': 0.0
    }

    # Distractor: entropy calculation (not used later)
    for x in normalized:
        if x > 0:
            stats['entropy'] -= x * x

    # Misleading intermediate result
    dummy_metric = sum([int(x * 100) for x in normalized]) % 7

    return filtered


def transform_coordinates(indices):
    """
    Apply coordinate transformation (dead code path - not actually used).
    """
    transformed = []
    for i, idx in enumerate(indices):
        angle = i * 3.14159 / 180
        x = idx * math.cos(angle)
        y = idx * math.sin(angle)
        transformed.append((x, y))
    return transformed


def extract_features(signal_chunks):
    """
    Extract key features using bit manipulation and logical checks.
    Only certain parts contribute to final result.
    """
    features = []
    for chunk in signal_chunks:
        if len(chunk) == 0:
            continue
        
        # Real computation: XOR-based signature
        sig = 0
        for val in chunk:
            scaled = int(val * 100)
            sig ^= scaled
            
        # Red herring: checksum that looks important but isn't used
        checksum = 0
        for j, v in enumerate(chunk):
            checksum += (j + 1) * v
        
        # Another decoy variable
        anomaly_score = abs(sig - checksum) * 100
        
        features.append(sig)
    
    return features


def decode_frame(features):
    """
    Decode frame using string-based encoding logic.
    Uses string methods as required.
    """
    encoded_parts = []
    for f in features:
        # Convert feature to binary string with padding
        bin_str = format(abs(f) % 256, '08b')  # Use only lower byte
        
        # String manipulation: reverse every other block
        if f % 2 == 0:
            bin_str = bin_str[::-1]
            
        # Insert fake delimiter (distractor)
        formatted = bin_str[:4] + '-' + bin_str[4:]
        
        # Actual use: count number of '1's
        ones = bin_str.count('1')
        encoded_parts.append(ones)
    
    return encoded_parts


def analyze_signal(frames):
    """
    Final analysis: combine results with recursion.
    """
    def recursive_weight(seq, depth=0):
        if len(seq) <= 1:
            return seq[0] if seq else 0
        if depth > 3:
            return seq[0]
        mid = len(seq) // 2
        left = recursive_weight(seq[:mid], depth + 1)
        right = recursive_weight(seq[mid:], depth + 1)
        return (left ^ right) + depth  # Bitwise mix

    # Real path: decode then weight
    decoded = decode_frame(frames)
    
    # Distractor: unused statistical aggregation
    avg_decode = sum(decoded) / len(decoded) if decoded else 0
    mode_like = max(set(decoded), key=decoded.count) if decoded else 0
    
    # Critical: this is the actual computation chain
    return recursive_weight(decoded)

# --- Main Execution ---
import math

# Simulated sensor readings (real input)
raw_sensor_data = [
    0.12, 0.81, 0.45, 0.89, 0.23,
    0.77, 0.65, 0.91, 0.34, 0.72,
    0.55, 0.83, 0.41, 0.97, 0.29
]

# Step 1: Preprocess signal (filtering irrelevant low values)
filtered_signal = preprocess_signal(raw_sensor_data, threshold=0.4)

# Step 2: Frame segmentation (creates chunks)
segmented_frames = []
for i in range(0, len(filtered_signal), 3):
    segment = filtered_signal[i:i+3]
    segmented_frames.append(segment)

# Step 3: Extract features from each frame (bitwise XOR signatures)
extracted_features = extract_features(segmented_frames)

# Step 4: Analyze the full signal sequence
final_diagnostic = analyze_signal(extracted_features)

# Print result as required
print(f"Target result: {final_diagnostic}")