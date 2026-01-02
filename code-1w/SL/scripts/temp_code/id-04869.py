import math

# Simulated sensor data processing with embedded diagnostics
def collect_readings():
    raw_samples = [127, 255, 192, 64, 224, 32, 160, 96]
    scale_factor = 0.75
    adjusted = [x * scale_factor for x in raw_samples]
    return adjusted

# Irrelevant helper: string-based status generator (red herring)
def generate_status(code):
    status_map = {200: 'OK', 404: 'Not Found', 500: 'Server Error'}
    return status_map.get(code, 'Unknown')

# Decoy function: never actually called in execution path
def deprecated_filter(data):
    return [x for x in data if x > 100]

# Signal preprocessing with bit manipulation distraction
def preprocess_signal(samples):
    shifted = []
    mask = 0b111111  # Use only lower 6 bits
    for val in samples:
        quantized = int(val)
        masked_val = quantized & mask  # Bitwise AND distraction
        inverted = 63 - masked_val  # Inversion red herring
        if masked_val > 32:
            shifted.append(masked_val << 1)  # Left shift decoy
        else:
            shifted.append(masked_val)
    # Actual relevant transformation
    clipped = [min(x, 100) for x in shifted]  # This matters
    return clipped

# Data chunking with string method distraction (irrelevant but plausible)
def segment_data(signal):
    segments = []
    for i in range(0, len(signal), 2):
        segment = signal[i:i+2]
        # Use of string method – looks meaningful but isn't critical
        tag = f'SEG_{i//2}'.replace('_', '').lower()
        segments.append((segment, tag))
    return segments

# Core analysis: depends on preprocessed values only
def compute_entropy(values):
    total = sum(values)
    if total == 0:
        return 0.0
    entropy = 0.0
    for v in values:
        if v > 0:
            prob = v / total
            entropy -= prob * math.log(prob) if prob > 0 else 0
    return round(entropy, 6)

# Diagnostic engine - key function
valid_codes = {1: 'Normal', 2: 'Elevated', 3: 'Critical'}  # Unused global (distractor)

def analyze_signal(cleaned):
    base_metric = sum(cleaned)
    
    # Dummy checksum with XOR (looks important, partially irrelevant)
    checksum = 0
    for x in cleaned:
        checksum ^= int(x)
    
    # Real computation path starts here
    threshold = 350
    if base_metric > threshold:
        category = 3
    elif base_metric > 200:
        category = 2
    else:
        category = 1
    
    # Final diagnostic is a transformed metric
    adjustment = 1.75 if category == 3 else (1.25 if category == 2 else 1.0)
    final_score = base_metric * adjustment
    
    # Introduce tuple unpacking distraction
    temp_a, temp_b = (final_score, checksum)
    refined = temp_a  # Only this matters
    
    # String formatting decoy
    log_entry = f"Diagnostic: {refined:.2f}".split(':')
    
    return refined

# Orchestration with dead code paths
if __name__ == "__main__":
    readings = collect_readings()  # Step 1
    processed = preprocess_signal(readings)  # Step 2
    chunks = segment_data(processed)  # Step 3, tag ignored
    
    # Dead branch: based on impossible condition (misleading)
    if len(readings) < 5:
        fallback = [x * 2 for x in processed]
        processed_chunk = fallback
    else:
        # Extract first data segment values only
        processed_chunk = chunks[0][0]  # Uses first segment
    
    # Key statement: where answer is determined
    final_diagnostic = analyze_signal(processed_chunk)
    
    # Print required output
    print(f"Result: {final_diagnostic}")