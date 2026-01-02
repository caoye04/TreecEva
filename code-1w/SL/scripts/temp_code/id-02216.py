import math

# Simulated sensor data processing with diagnostic analysis
def acquire_raw_readings():
    return [0.1, 0.3, 0.4, 0.8, 1.2, 1.5, 1.6, 1.9, 2.1, 2.3, 2.5, 2.7, 3.0]

def filter_noise(signal, threshold=0.5):
    # Real filtering logic
    return [x for x in signal if x >= threshold]

def segment_signal(clean_signal, window_size=3):
    segments = []
    for i in range(0, len(clean_signal) - window_size + 1, window_size):
        segments.append(clean_signal[i:i + window_size])
    return segments

def compute_amplitude(envelope):
    return sum(x ** 2 for x in envelope)

def detect_spike(pattern):
    if len(pattern) < 2:
        return False
    return (pattern[-1] - pattern[0]) > 1.0

def calculate_entropy(data):
    # Irrelevant function - dead end
    total = sum(data)
    probs = [x / total for x in data]
    return -sum(p * math.log(p) for p in probs if p > 0)

def derive_phase_shift(sequence):
    # Distractor computation - unused later
    shift = 0
    for i in range(len(sequence) - 1):
        shift += abs(sequence[i+1] - sequence[i])
    return shift * 0.5

def extract_peaks(readings):
    # Another red herring path
    peaks = []
    for i in range(1, len(readings) - 1):
        if readings[i] > readings[i-1] and readings[i] > readings[i+1]:
            peaks.append(readings[i])
    return peaks

def temporal_align(signal_chunk):
    # Unused transformation
    offset = signal_chunk[0]
    return [x - offset for x in signal_chunk]

def normalize_segment(segment):
    max_val = max(segment)
    return [x / max_val for x in segment] if max_val != 0 else segment

def encode_signature(normalized_block):
    # Bit manipulation distractor
    encoded = 0
    for x in normalized_block:
        encoded ^= int(x * 100) << 2
    return encoded

def analyze_signal(segments):
    diagnostics = []
    
    # Real logic begins here
    for seg in segments:
        if len(seg) != 3:  # Only process full segments
            continue
            
        # Normalize before analysis
        norm_seg = normalize_segment(seg)
        
        # Compute energy amplitude
        amplitude = compute_amplitude(norm_seg)
        
        # Check for spike pattern
        has_spike = detect_spike(seg)
        
        # Decoy entropy calculation on normalized data (not used)
        _ = calculate_entropy([int(x*100) for x in norm_seg])
        
        # Real diagnostic logic: weight amplitude if spike present
        if has_spike:
            diagnostics.append(amplitude * 1.75)
        else:
            diagnostics.append(amplitude * 0.85)
    
    # Final aggregation
    base_score = sum(diagnostics)
    adjustment = len(diagnostics) * 0.12
    final_value = base_score - adjustment
    
    # Misleading rounding attempt (not applied)
    _ = round(final_value * 100) / 100
    
    return final_value

# Begin execution
raw_data = acquire_raw_readings()
filtered_data = filter_noise(raw_data)

# Extract peaks (irrelevant path)
peak_values = extract_peaks(raw_data)  # Dead end

# Derive phase shift from raw (distractor)
_ = derive_phase_shift(raw_data)

# Segment the filtered signal
signal_segments = segment_signal(filtered_data, window_size=3)

# Normalize each segment (real preprocessing)
processed_segments = []
for s in signal_segments:
    aligned = temporal_align(s)  # This does nothing significant due to how data is structured
    processed_segments.append(normalize_segment(aligned))

# Encode signatures (red herring)
encoded_list = []
for ps in processed_segments:
    code = encode_signature(ps)
    encoded_list.append(code)

# Core diagnostic analysis (this is where answer comes from)
final_diagnostic = analyze_signal(processed_segments)

# Print result
print(f"Result: {final_diagnostic}")