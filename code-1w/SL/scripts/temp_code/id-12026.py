import math

# Simulated sensor data processing with embedded diagnostics
def collect_readings():
    raw_readings = [127, 255, 192, 64, 224, 32, 168, 96]
    scale_factor = 0.75
    adjusted = [x * scale_factor for x in raw_readings]
    return adjusted

# Irrelevant helper: format timestamp (distractor)
def format_timestamp(seconds):
    hours = int(seconds // 3600)
    mins = int((seconds % 3600) // 60)
    secs = int(seconds % 60)
    return f'{hours:02}:{mins:02}:{secs:02}'

# Noise filter with bit manipulation red herring
def filter_noise(data):
    cleaned = []
    mask = 0xFF  # 8-bit mask (seemingly relevant)
    shift_key = 3
    
    for val in data:
        truncated = int(val) & mask  # Bitwise op (misleading use)
        if truncated > 100:
            cleaned.append(truncated / 2.0)
        else:
            cleaned.append(truncated / 1.5)
    
    # Dead code path: never executed due to logic above
    if len(cleaned) > 100:
        cleaned = [x for x in cleaned if x % 2 == 0]
    
    return cleaned

# Signal envelope detection (partially relevant)
def detect_envelope(signal):
    peak = max(signal)
    avg = sum(signal) / len(signal)
    ratio = peak / avg if avg != 0 else 0
    
    # Decoy calculation with string distraction
    status_flag = 'NORMAL' if ratio < 1.8 else 'WARNING'
    debug_msg = f'Signal {status_flag.lower().capitalize()} at {ratio:.2f}x'
    
    # Return only numeric feature
    return ratio

# Data reshaping with tuple unpacking (distractor)
def reshape_stream(stream):
    if len(stream) % 2 != 0:
        stream.append(0)
    
    pairs = [(stream[i], stream[i+1]) for i in range(0, len(stream), 2)]
    flattened = []
    for a, b in pairs:
        flattened.extend([a*0.9, b*1.1])
    
    # Unused transformation path
    if any(x < 0 for x in flattened):
        inverted = [-x for x in flattened]
        return inverted  # Never taken
    
    return flattened

# Core analysis with conditional expression
def analyze_signal(data):
    size = len(data)
    base_metric = sum(math.sin(x * 0.1) for x in data)
    adjustment = 1.0 if size > 5 else 0.5
    
    # Conditional expression on transformed string (key python idiom)
    mode_flag = 'A' if 'high'.upper() in ['LOW', 'MED', 'HIGH'] else 'B'
    multiplier = 2.0 if mode_flag == 'A' else 1.5
    
    # Final computation chain
    intermediate = base_metric * adjustment * multiplier
    
    # Additional irrelevant transformation
    checksum = 0
    for i, x in enumerate(data):
        checksum += (i + 1) * int(x)
    checksum %= 97
    
    # Final diagnostic is NOT affected by checksum (red herring)
    final_score = intermediate + 10.0  # Offset added here
    return final_score

# Orchestration function with early return
def main_pipeline():
    timestamp_snapshot = 3723  # HH:MM:SS = 01:02:03
    time_label = format_timestamp(timestamp_snapshot)
    
    readings = collect_readings()
    noisy_check = sum(1 for x in readings if x > 100)
    
    # Early exit not triggered (distraction)
    if noisy_check == 0:
        return -999.0
    
    filtered = filter_noise(readings)
    envelope_ratio = detect_envelope(filtered)
    
    # Inject envelope feature into data (subtle relevance)
    extended_data = [x * envelope_ratio for x in filtered]
    
    reshaped = reshape_stream(extended_data)
    
    # Critical statement
    final_diagnostic = analyze_signal(reshaped)
    
    # Print required result
    print(f'Result: {final_diagnostic}')
    return final_diagnostic

# Execute
main_pipeline()