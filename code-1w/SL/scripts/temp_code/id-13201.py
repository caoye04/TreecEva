import math

# Simulated sensor array data processing with diagnostic logic
def process_sensor_readings(raw_samples, sensitivity):
    # Irrelevant preprocessing (distractor)
    normalized = [x / max(raw_samples) for x in raw_samples]
    offset_correction = sum(normalized[:3]) * 0.1

    # Core signal filtering (relevant)
    filtered_data = []
    for i, val in enumerate(raw_samples):
        if abs(val - sensitivity) > 5:
            if i % 2 == 0:
                adjusted = val * 0.8 + offset_correction
            else:
                adjusted = val * 1.1 - offset_correction
            if adjusted > sensitivity * 1.3:
                filtered_data.append(int(adjusted))
    
    # Dead code path (misleading)
    if len(filtered_data) > 100:
        return [x for x in filtered_data if x % 2 == 0]
    else:
        temp_result = [x for x in filtered_data if x > 0]
        temp_result.sort(reverse=True)
        # Unused result
        _ = temp_result[:5]

    return filtered_data

# Advanced signal analysis with bit manipulation and thresholds
def analyze_signal(data, limit):
    if not data:
        return -1
    
    # Distractor: unused statistical calculations
    mean_val = sum(data) / len(data)
    variance = sum((x - mean_val) ** 2 for x in data) / len(data)
    std_dev = math.sqrt(variance)
    
    # Relevant bitwise transformation chain
    transformed = 0
    for idx, sample in enumerate(data):
        if idx >= 6:
            break
        # Complex conditional expression (required feature)
        shift_amount = (sample & 7) if (idx % 3 == 0) else (3 if sample > limit else 1)
        # Bit manipulation with conditional update
        if sample % 4 == 0:
            transformed ^= (sample << shift_amount)
        elif sample % 3 == 0:
            transformed |= (sample >> shift_amount)
        else:
            transformed += (sample & (sample + 1))  # Bitwise trick
    
    # Set operation to filter intermediate states (required feature)
    history = set()
    accumulator = transformed
    for _ in range(4):
        next_acc = (accumulator * 7) % 10007
        if next_acc in history:
            break
        history.add(next_acc)
        accumulator = next_acc
    
    # Final computation using slicing of virtual segments (required feature)
    hex_rep = format(accumulator, 'b').zfill(16)
    segments = [hex_rep[i:i+4] for i in range(0, len(hex_rep), 4)]
    # Use only alternating segments
    selected_bits = ''.join(segments[::2])
    final_value = int(selected_bits, 2)
    
    # Early termination based on control flow
    if final_value > 5000:
        final_value //= 3
    
    return final_value

# Misleading auxiliary functions (decoy)
def calculate_entropy(sequence):
    from collections import Counter
    counts = Counter(sequence)
    total = len(sequence)
    entropy = 0
    for count in counts.values():
        p = count / total
        entropy -= p * math.log2(p)
    return round(entropy, 4)

def validate_checksum(arr):
    checksum = 0
    for i, v in enumerate(arr):
        checksum ^= (v + i) * 3
    return format(checksum, 'x')

# Main execution with realistic parameters
sensor_input = [12, 15, 24, 36, 45, 48, 60, 72, 81, 96, 108, 120, 135, 144]
sensitivity_level = 20
threshold = 25

# Signal processing pipeline
filtered_data = process_sensor_readings(sensor_input, sensitivity_level)

# Diagnostic analysis
final_diagnostic = analyze_signal(filtered_data, threshold)

# Red herring: unused derived values
reversed_data = filtered_data[::-1]
summary_stats = {"peak": max(filtered_data), "base": min(filtered_data), "count": len(filtered_data)}
diag_copy = final_diagnostic * 2  # Unused

# Target result output
print(f"Result: {final_diagnostic}")