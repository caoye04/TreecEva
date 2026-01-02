import math

# Simulated sensor data processing with embedded logic chain
def preprocess_signal(raw_stream, threshold=100):
    filtered = [x for x in raw_stream if abs(x) > threshold]
    return filtered[::-1]  # Reverse after filtering

def generate_reference(size, phase=0.1):
    # Distractor: complex-looking but unused later
    return [math.sin(i * phase) for i in range(size + 5)]

def shift_window(sequence, shift_by):
    return sequence[shift_by:] + sequence[:shift_by]

def compute_magnitude(values):
    # Red herring function — looks important but not used in critical path
    return sum([abs(v) for v in values]) / len(values) if values else 0

def extract_features(data_slice):
    # Extract every third element — relevant for transformation
    return data_slice[::3]

def transform_sequence(seq, factor):
    # Apply non-linear scaling
    return [int(x * factor) + 2 for x in seq]

def analyze_pattern(pattern, offset):
    total = 0
    for i, val in enumerate(pattern):
        if i % 2 == 0:
            total += (val ^ offset) & 7  # Bitwise manipulation
        else:
            total -= (val + offset) % 5
    return abs(total)

def validate_checksum(arr):
    # Dead code path — never called
    return sum(arr) % 11 == 0

# Main execution flow
raw_sensor_data = list(range(-150, 180, 7))  # Generate initial sequence
base_offset = 13

# Step 1: Filter and reverse signal
filtered_data = preprocess_signal(raw_sensor_data, threshold=90)

# Step 2: Irrelevant reference generation (distractor)
ref_waveform = generate_reference(len(filtered_data), phase=0.15)

# Step 3: Shift window to align data
aligned_data = shift_window(filtered_data, shift_by=3)

# Step 4: Extract structural features
feature_vector = extract_features(aligned_data)

# Step 5: Transform with scaling factor
transformed_data = transform_sequence(feature_vector, factor=1.25)

# Step 6: Analyze final pattern using offset
final_diagnostic = analyze_pattern(transformed_data, base_offset)

# Output result as required
print(f"Result: {final_diagnostic}")