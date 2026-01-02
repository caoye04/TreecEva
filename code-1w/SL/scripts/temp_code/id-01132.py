import math

# Simulated sensor data preprocessing with distractions
def generate_noise(length, seed=42):
    # Irrelevant function - dead code path
    result = []
    for i in range(length):
        val = (seed * i + 17) % 101
        result.append((val / 100) * (-1)**i)
    return result

def deprecated_filter(data):
    # Outdated filter - never called
    return [x for x in data if abs(x) > 0.3]

# Core transformation pipeline
def encode_sequence(seq):
    return [int(x * 10) % 7 for x in seq]

def shift_window(arr, offset):
    return arr[offset:] + arr[:offset]

def evaluate_peaks(values):
    # Distractor: looks important but unused
    peaks = 0
    for i in range(1, len(values)-1):
        if values[i] > values[i-1] and values[i] > values[i+1]:
            peaks += 1
    return peaks

# Main processing components
def transform_signal(raw):
    scaled = [math.sin(x / 3.0) for x in raw]
    filtered = [x for x in scaled if x >= 0]
    return filtered[:10]

def apply_mask(data, mask_type='A'):
    if mask_type == 'A':
        return [d ^ 5 for d in data]
    else:
        return [d ^ 3 for d in data]

# Critical recursive function for frame processing
def recursive_compress(seq, threshold):
    if len(seq) <= 1:
        return seq
    mid = len(seq) // 2
    left = recursive_compress(seq[:mid], threshold)
    right = recursive_compress(seq[mid:], threshold)
    combined = (left[0] + right[0]) if left and right else (left[0] if left else (right[0] if right else 0))
    if abs(combined) > threshold:
        return [combined]
    return left + right

def process_frame(data_chunk):
    # Key transformation steps
    temp_state = [x * 2 + 1 for x in data_chunk]
    
    # Bit manipulation layer
    processed = []
    for val in temp_state:
        bit_shifted = (val << 1) & 0xFF
        processed.append(bit_shifted ^ 0xAA)
    
    # Conditional logic with red herring branch
    mode_flag = len(processed) % 2 == 0
    if mode_flag:
        secondary_route = sum([p | 0x55 for p in processed])  # Unused computation
    else:
        dummy_calc = math.log(abs(sum(processed)) + 1)  # Misleading intermediate
    
    # Real computation path
    base_result = sum(processed) >> 2
    
    # List comprehension with filtering
    refined = [r for r in processed if r % 3 == 0]
    adjustment = len(refined) * 7
    
    # Final decision using conditional expression
    signal_strength = base_result if base_result > 50 else (base_result * 2)
    
    # Apply adjustment only if certain condition met (it will be)
    final_value = signal_strength + adjustment if len(refined) > 0 else signal_strength
    
    return final_value

# Initialization of various irrelevant variables (distractors)
data_source = list(range(15))
noise_profile = generate_noise(20)
legacy_config = {'version': 'old', 'active': False}
temp_buffer = [0] * 8

# Simulated input acquisition
raw_input_stream = [6, 3, 8, 2, 9, 1, 7]

# Signal transformation chain
encoded = encode_sequence(raw_input_stream)  # [0, 1, 4, 6, 3, 5, 1]
shifted = shift_window(encoded, 2)  # [4, 6, 3, 5, 1, 0, 1]
scaled_signal = transform_signal(shifted)  # sin(x/3), positive-only, capped at 10

# Masking operation (distraction)
masked_data = apply_mask([int(s*100) for s in scaled_signal], 'A')

# Decoy recursive call
coarse_peaks = evaluate_peaks(masked_data)

# Critical data transformation
transformed_data = [int(abs(math.cos(x)) * 10) for x in range(len(scaled_signal))]

# Introduce another distraction variable
normalization_factor = math.sqrt(sum([t**2 for t in transformed_data]) + 1e-8)
denoised_reference = [t / normalization_factor for t in transformed_data]

# Key execution point
signal_output = process_frame(transformed_data)

# Print result as required
print(f"Target result: {signal_output}")