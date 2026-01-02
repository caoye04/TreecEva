import math

def legacy_transform(x):
    # Obsolete function - never called in execution path
    return (x ** 2 + 3 * x + 1) % 100

def auxiliary_filter(values):
    # Unused helper with misleading logic
    return [v for v in values if v % 3 == 0]

def decode_signal(sequence):
    temp_result = 0
    shift_accum = 0
    for i, val in enumerate(sequence):
        if i % 2 == 0:
            temp_result += val * (i + 1)
        else:
            shift_accum ^= (val << 2)
    return temp_result  # Only this part is used

def compute_entropy(vector):
    # Distractor: complex unused computation
    norm = sum(v ** 2 for v in vector) ** 0.5
    probs = [v / norm for v in vector]
    entropy = -sum(p * math.log2(p) for p in probs if p > 0)
    return round(entropy, 4)

def evaluate_thresholds(arr):
    # Dead code path - included as red herring
    count = 0
    for x in arr:
        if x > 50 and x % 7 == 0:
            count += 1
    return count

def process_pipeline(input_data):
    # Core relevant logic with embedded distractions
    base_values = [x for x in input_data if x > 0]  # Filter positives
    shifted = [((x << 1) | 1) for x in base_values]  # Bit manipulation
    
    # Irrelevant transformation chain
    decoy_mapped = []
    for y in shifted:
        if y < 100:
            decoy_mapped.append(y ** 0.5)
        else:
            decoy_mapped.append(y / 2)
    
    # Sorting decoy - result not used
    sorted_decoy = sorted(decoy_mapped, reverse=True)
    median_guess = sorted_decoy[len(sorted_decoy)//2] if sorted_decoy else 0
    
    # Conditional expression with meaningful side
    adjustment = 7 if sum(shifted) > 300 else 3
    
    # Actual critical computation
    signal = [x % 25 for x in base_values]
    processed = decode_signal(signal)
    final_adjusted = processed * adjustment
    
    # Final red herring: unused conditional assignment
    status_flag = 'valid' if final_adjusted % 2 == 0 else 'offset_required'
    if status_flag == 'offset_required':
        final_adjusted += 100  # Never executed
    
    return final_adjusted

# Simulated sensor data stream
raw_stream = [12, -5, 8, 0, 15, -3, 21, 4, 7]
data_stream = [x * 2 for x in raw_stream]  # Amplify signal

# Misleading pre-processing steps
checksum = sum(x ^ 2 for x in data_stream) % 89
buffer_state = ''.join(str(abs(x))[-1] for x in data_stream)
diagnostic_code = f"CHK-{checksum}:{buffer_state}"

# Key execution point
final_output = process_pipeline(data_stream)
print(f"Result: {final_output}")