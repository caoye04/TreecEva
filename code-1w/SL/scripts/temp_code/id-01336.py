import math

def analyze_pattern(seq):
    if len(seq) < 3:
        return 0
    peaks = 0
    for i in range(1, len(seq) - 1):
        if seq[i] > seq[i-1] and seq[i] > seq[i+1]:
            peaks += 1
    return peaks

def transform_data(values):
    shifted = [v << 1 for v in values]
    filtered = [v for v in shifted if v % 3 == 0]
    reversed_filtered = filtered[::-1]
    return [v >> 1 for v in reversed_filtered]

def compute_checksum(items):
    checksum = 0
    for item in items:
        checksum ^= item
        checksum = (checksum + len(items)) % 256
    return checksum

def extract_features(raw):
    segments = []
    for i in range(0, len(raw), 4):
        segment = raw[i:i+4]
        if len(segment) == 4:
            segments.append(sum(segment))
    return segments

def evaluate_stability(metrics):
    if not metrics:
        return 0.0
    mean_val = sum(metrics) / len(metrics)
    variance = sum((x - mean_val) ** 2 for x in metrics) / len(metrics)
    return round(math.sqrt(variance), 6)

def normalize_stream(stream):
    max_val = max(stream)
    return [round(v / max_val, 6) for v in stream] if max_val != 0 else stream

def merge_and_sort(a, b):
    # Irrelevant sorting operation with decoy purpose
    temp = sorted(set(a + b))
    return [x * 2 for x in temp if x % 2 == 1]

def process_sequence(input_data):
    # Core relevant operations
    data_slice = input_data[2:9]  # slicing operation
    transformed = transform_data(data_slice)
    features = extract_features(transformed)
    
    # Decoy dictionary usage
    stats = {
        'length': len(input_data),
        'max': max(input_data),
        'min': min(input_data),
        'sum': sum(input_data)
    }
    
    # Meaningless string manipulation as distraction
    label = "data_block_" + "_".join([str(len(input_data)), str(stats['max'])])
    label_parts = label.split('_')
    suffix = ''.join([part[-1] for part in label_parts if part.isdigit()])
    
    # Another irrelevant computation
    dummy_checksum = compute_checksum([len(label), int(suffix)])
    
    # Key path begins here
    analyzed = analyze_pattern(features)
    normalized = normalize_stream(features)
    stability = evaluate_stability(normalized)
    
    # Final critical computation
    adjustment_factor = math.floor(stability * 100)
    base_result = analyzed * adjustment_factor
    
    # Dead code path - never executed due to condition
    if len(suffix) > 100:
        extra = merge_and_sort(transformed, features)
        base_result += sum(extra)
    
    final_value = base_result - dummy_checksum  # dummy_checksum is deterministic but irrelevant
    return int(final_value)

# Main execution block
if __name__ == '__main__':
    raw_input = [12, 7, 3, 9, 4, 8, 6, 11, 2, 14, 5, 10]
    temp_buffer = [x ** 2 for x in raw_input if x % 2 == 0]  # dead-end list
    lookup_table = {i: chr(65 + i) for i in range(10)}  # unused dictionary
    data_chunk = raw_input[:10]  # slicing to create working chunk
    
    # Red herring function call
    _ = transform_data(temp_buffer)
    
    # Critical execution point
    final_output = process_sequence(data_chunk)
    
    print(f"Result: {final_output}")