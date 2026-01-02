import math

# Simulated sensor data processing with red herrings and distractions
def preprocess_signal(raw_input):
    filtered = [x for x in raw_input if x > -50 and x < 150]
    shifted = [x + 27 for x in filtered]
    return shifted

# Distractor function: looks relevant but unused in final computation
def deprecated_normalization(vec):
    if len(vec) == 0:
        return []
    max_val = max(vec)
    return [v / max_val * 100 for v in vec]

# Another decoy transformation - appears useful but not part of main logic
def frequency_shift(data, factor=3):
    return [d * factor % 97 for d in data]

# Real transformation chain
mapping_grid = [i**2 % 89 for i in range(120)]


def apply_cipher(sequence):
    ciphered = []
    for idx, val in enumerate(sequence):
        if idx % 3 == 0:
            ciphered.append(val ^ mapping_grid[idx % len(mapping_grid)])
        elif idx % 5 == 0:
            ciphered.append(val + mapping_grid[idx % 43])
        else:
            ciphered.append(val)
    return ciphered

# String-based distraction: encodes nothing actually used later
def generate_signature(nonce="sensor_log"):
    rotated = nonce[5:] + nonce[:5]
    upper_version = rotated.upper()
    coded = ''.join([chr((ord(c) - 65 + 13) % 26 + 65) if c.isalpha() else c for c in upper_version])
    return coded[::-1]

# Core analysis logic
threshold_reference = [1.2, 3.5, 7.1, 9.8, 12.0]

def evaluate_stability(readings):
    baseline = sum(readings) / len(readings)
    variance = sum((x - baseline) ** 2 for x in readings) / len(readings)
    return math.sqrt(variance) if variance > 0 else 0.0


def extract_features(dataset):
    # Slice only middle portion
    mid_section = dataset[len(dataset)//4 : len(dataset)//4*3]
    
    # Multiple feature extractions, some irrelevant
    peak = max(mid_section)
    trough = min(mid_section)
    span = peak - trough
    
    # Hidden signal embedded via bit manipulation
    encoded_flag = 0
    for v in mid_section:
        encoded_flag ^= int(v) & 0xF
    
    # Actual path: compute weighted centroid
    total_weight = 0
    weighted_pos = 0
    for i, val in enumerate(mid_section):
        weight = val ** 0.5
        total_weight += weight
        weighted_pos += i * weight
    
    centroid = weighted_pos / total_weight if total_weight != 0 else 0
    
    # Return multiple values; only one used later
    return {
        'centroid': centroid,
        'span': span,
        'flag': encoded_flag,
        'peak': peak
    }


def analyze_pattern(data_chunk, limit):
    # Apply actual transformations
    processed = preprocess_signal(data_chunk)
    secured = apply_cipher(processed)
    features = extract_features(secured)
    
    # Secondary filtering based on threshold
    active_segments = [x for x in secured if abs(x - features['centroid']) > limit]
    
    # Compute diagnostic metric using complex expression
    score_component_a = features['span'] * 0.7
    score_component_b = len(active_segments) * 2.3
    stability_metric = evaluate_stability(secured)
    
    # Final diagnostic uses only specific components
    # Despite many variables above, only these contribute:
    intermediate = (score_component_a + score_component_b) * (1 + math.sin(math.pi / 3))
    adjustment = 1 if stability_metric < 15 else 0.9
    final_score = intermediate * adjustment
    
    # This is the target variable
    final_diagnostic = int(round(final_score))
    
    # Red herring print (not affecting result)
    if final_diagnostic > 100:
        debug_tag = generate_signature("alert_99")
        _ = f"Diagnostic flagged: {debug_tag}"
    
    return final_diagnostic

# Irrelevant global constants (distractors)
MAX_BUFFER_SIZE = 1024
CALIBRATION_OFFSET = -17.3
RETRY_LIMIT = 5

# Main execution flow
if __name__ == "__main__":
    # Initial raw data - deterministic input
    sensor_stream = [22, 18, 94, -12, 88, 33, 77, 105, -8, 44, 66, 55, 99, 12, 8, 101, 37, 29, 73, 61]
    
    # Distraction: unused transformation path
    compressed = [x for x in sensor_stream if x % 2 == 1]  # odd numbers only
    reshaped = [(compressed[i], compressed[i+1]) for i in range(0, len(compressed)-1, 2)]
    
    # Transformations that feed into the answer
    transformed_data = preprocess_signal(sensor_stream)
    key_threshold = threshold_reference[1]  # 3.5
    
    # Critical statement
    final_diagnostic = analyze_pattern(transformed_data, key_threshold)
    
    # Output result as required
    print(f"Target result: {final_diagnostic}")