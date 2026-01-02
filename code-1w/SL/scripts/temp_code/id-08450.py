import math

# Simulated sensor data processing with diagnostic logic
def preprocess_signal(raw_samples):
    filtered = [x for x in raw_samples if abs(x) > 0.1]
    normalized = [round(x / max(filtered), 3) for x in filtered]
    return normalized

# Irrelevant helper: Spectral centroid (not used in final result)
def spectral_centroid(signal):
    powers = [abs(x) ** 2 for x in signal]
    weighted_freqs = [i * powers[i] for i in range(len(powers))]
    return sum(weighted_freqs) / sum(powers) if sum(powers) != 0 else 0

# Data transformation chain
def encode_signal(signal):
    encoded = []
    for val in signal:
        shifted = int((val + 1) * 1000)
        # Bit manipulation red herring
        obfuscated = (shifted ^ 0xFF) & 0xFFFF
        encoded.append(obfuscated)
    return encoded

# Decoy function: Looks important but unused in critical path
def validate_checksum(data_chunk):
    checksum = 0
    for item in data_chunk:
        checksum = (checksum + item) % 257
    return checksum == 127

# Core logic obscured by multiple layers
def compress_signal(encoded_vals):
    # Convert to set to eliminate duplicates (actual use of set operation)
    unique_vals = set(encoded_vals)
    sorted_vals = sorted(unique_vals, reverse=True)
    # Apply non-linear transform
    compressed = []
    for v in sorted_vals:
        if v % 2 == 0:
            compressed.append(int(math.sqrt(v)) * 2)
        else:
            compressed.append((v % 7) * 3)
    return compressed

# Threshold analysis using set operations
def build_threshold_set(base_level):
    linear_part = {base_level + i for i in range(5)}
    exponential_part = {int(math.exp(i)) for i in range(1, 5)}
    # Combine sets - actual use of set union
    return linear_part.union(exponential_part)

# Main analysis with recursive filtering
def analyze_signal(data_list, thresholds):
    def recursive_filter(values, level):
        if level == 0 or not values:
            return [v for v in values if v < 50]  # Base case
        new_vals = []
        for v in values:
            if v in thresholds:
                # Introduce side-branch distraction
                temp_flag = (v ^ 255) > 100
                if temp_flag:
                    new_vals.append(v // 2)
            else:
                new_vals.append(v - level)
        return recursive_filter(new_vals, level - 1)
    
    filtered_result = recursive_filter(data_list, 3)
    
    # Critical computation buried in logic
    magnitude = sum(filtered_result)
    adjustment_factor = len(thresholds) / 8
    
    # Decoy statistics (never used)
    mean_val = sum(filtered_result) / len(filtered_result) if filtered_result else 0
    peak = max(filtered_result) if filtered_result else 0
    
    # Final diagnostic calculation (this is the real answer)
    final_diagnostic = int(magnitude * adjustment_factor) + 1337
    
    # Dead code path - misleading control flow
    if final_diagnostic < 0:
        final_diagnostic = abs(final_diagnostic)
    elif final_diagnostic == 42:
        final_diagnostic = 1337  # Red herring override
    
    return final_diagnostic

# --- Execution Flow ---
raw_sensor_data = [-0.5, 0.0, 1.2, -1.8, 0.4, 2.1, -0.3, 1.9, 0.0, -2.5]
denoised = preprocess_signal(raw_sensor_data)
encoded_data = encode_signal(denoised)
compressed_data = compress_signal(encoded_data)

# Unused intermediate calculations (distractors)
peak_value = max(encoded_data)
avg_encoded = sum(encoded_data) / len(encoded_data)

# Real execution begins here
threshold_set = build_threshold_set(10)

# Key statement: This produces the answer
final_diagnostic = analyze_signal(compressed_data, threshold_set)

# Print required output
print(f"Result: {final_diagnostic}")