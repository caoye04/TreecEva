import math

# Simulated sensor data processing with embedded diagnostics
def collect_readings():
    raw_signal = [i * 0.7 + (i % 3) for i in range(15)]
    offset = 4.2
    processed = []
    for x in raw_signal:
        adjusted = x + offset
        if adjusted > 10:
            adjusted -= 5.1
        processed.append(round(adjusted, 2))
    return processed

# Irrelevant helper: signal smoothing (not used in final path)
def smooth_signal(data):
    smoothed = [data[0]]
    for i in range(1, len(data)-1):
        avg = (data[i-1] + data[i] + data[i+1]) / 3
        smoothed.append(avg)
    smoothed.append(data[-1])
    return smoothed

# Distraction function: spectral decomposition (never called)
def decompose_spectrum(signal):
    magnitude = 0
    for i, val in enumerate(signal):
        magnitude += val * math.sin(i * 0.5)
    return round(magnitude, 3)

# Key transformation: apply cyclic shift and filter
def transform_readings(data):
    shifted = data[3:] + data[:3]  # Left rotation by 3
    filtered = [x for x in shifted if x >= 5.0]
    return filtered

# Recursive pattern analysis (core logic)
def count_peaks_recursive(seq, idx=0):
    if idx >= len(seq) - 1:
        return 0
    current = seq[idx]
    next_val = seq[idx + 1]
    trend = 1 if next_val > current else (-1 if next_val < current else 0)
    recursive_count = count_peaks_recursive(seq, idx + 1)
    if trend == 1 and idx > 0 and seq[idx - 1] > current:
        return recursive_count + 1
    return recursive_count

# String-based status encoding (uses string method)
def encode_status(code, version="v2"):
    base = f"SYS:{code}:VER-{version}"
    checksum = sum(ord(c) for c in base) % 17
    return base + f"-{checksum}"

# Secondary distraction: data slicing statistics
def compute_slices(data):
    slice_a = data[::2]
    slice_b = data[1::2]
    mean_a = sum(slice_a) / len(slice_a)
    mean_b = sum(slice_b) / len(slice_b)
    variance = ((mean_a - mean_b) ** 2) / 2
    return round(variance, 4)

# Core analysis function
def analyze_pattern(data):
    # Use slicing to extract every second element starting at index 1
    sampled = data[1::2]
    
    # Initialize diagnostic accumulator
    accumulator = 0
    
    # Process each segment
    for i, val in enumerate(sampled):
        if i % 2 == 0:
            accumulator += math.floor(val)
        else:
            accumulator -= int(val // 1.5)
    
    # Conditional expression based on length parity
    adjustment = 7 if len(sampled) % 2 == 0 else -3
    accumulator *= (len(data) % 4)
    accumulator += adjustment
    
    # Apply bit manipulation mask (bitwise operation)
    masked = accumulator & 0xFFFF  # Ensure within 16-bit range
    
    # Final transformation using logarithmic scaling
    if masked > 0:
        scaled = math.log(masked) * 10
    else:
        scaled = 0
    
    # Round to nearest integer
    result = round(scaled)
    
    # Dead code path: unreachable due to structure
    if False and result > 100:
        backup = 0
        for ch in str(result):
            if ch.isdigit():
                backup += int(ch) ** 2
        result = backup
    
    return result

# Unused but plausible intermediate function
def validate_integrity(data):
    return all(x > 0 for x in data)

# Main execution flow
if __name__ == "__main__":
    readings = collect_readings()
    
    # Distractor: compute unused metrics
    slice_variance = compute_slices(readings)
    status_msg = encode_status("OK", "v2")
    decoy_sum = sum(1 for x in readings if x > 6.0)
    
    # Critical transformation step
    transformed_data = transform_readings(readings)
    
    # Red herring: recursive peak counting (not used in final result)
    peak_count = count_peaks_recursive(transformed_data)
    
    # Key statement
    final_diagnostic = analyze_pattern(transformed_data)
    
    # Print result as required
    print(f"Result: {final_diagnostic}")