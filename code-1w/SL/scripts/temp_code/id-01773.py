import math

# Simulated sensor data processing with embedded diagnostics
def collect_readings():
    raw = [127, 85, 170, 240, 30, 65, 200]
    processed = []
    for val in raw:
        if val > 127:
            processed.append(val ^ 64)
        elif val < 64:
            processed.append(val * 2)
        else:
            processed.append(val | 15)
    return processed

# Irrelevant helper: audio normalization (red herring)
def normalize_audio(signal):
    peak = max(abs(x) for x in signal)
    return [int(x * 0.8 / peak) for x in signal] if peak > 0 else signal

# Data transformation with bit manipulation and filtering
def transform_signal(data, mode='fast'):
    shifted = [(x >> 2) for x in data]
    filtered = [x for x in shifted if x % 3 != 0]
    # Decoy computation
    checksum = sum(x ^ 255 for x in data) % 100
    enhanced = [x + (x & 7) for x in filtered]
    return enhanced

# Core pattern analyzer: combines arithmetic, logic, and bit ops
def analyze_pattern(seq):
    base = 0
    for i, val in enumerate(seq):
        if i % 2 == 0:
            base += int(math.sin(math.pi * val / 180) * 100)  # sin in degrees scaled
        else:
            temp = (val ^ (val << 1)) & 255
            base -= (temp % 7) ** 2
    # Secondary adjustment based on sequence traits
    length_factor = len(seq) if len(seq) > 3 else 1
    magic_offset = 42 if any(x & 8 for x in seq[:3]) else 0
    return base * length_factor + magic_offset

# Unused diagnostic function (dead code path)
def legacy_diagnostic(arr):
    return sum(x & 0xF for x in arr) << 1

# String-based metadata processor (distractor with string methods)
def parse_header(header_str):
    lines = header_str.strip().split('\n')
    tags = []
    for line in lines:
        clean = line.strip()
        if clean.startswith('#') or not clean:
            continue
        key, *value = clean.split(':', 1)
        if value:
            tags.append(key.strip().upper())
    return ';'.join(tags).replace(' ', '_')

# Lambda for dynamic threshold (meets language feature requirement)
dynamic_thresh = lambda readings, multiplier: [r for r in readings if r > multiplier * 50]

# Main execution flow
if __name__ == "__main__":
    # Step 1: Collect sensor readings
    sensor_data = collect_readings()  # [127->142, 85->95, 170->146, 240->176, 30->60, 65->70, 200->136]
    
    # Step 2: Transform signal (irrelevant normalization applied to wrong data)
    dummy_audio = [-50, 200, -300, 100]
    normalized_audio = normalize_audio(dummy_audio)  # unused later
    
    # Step 3: Transform sensor data
    transformed_data = transform_signal(sensor_data, mode='fast')  # Apply shift and filter
    
    # Step 4: Apply dynamic threshold filter (result not used)
    candidate_nodes = dynamic_thresh(transformed_data, 1.2)
    
    # Step 5: Parse fake header (string method distraction)
    header = '''
    # Metadata Block
    Device: SensorNet-X
    Version: 2.1
    Timestamp: 2023-11-05
    '''
    parsed_tags = parse_header(header)
    
    # Step 6: Analyze pattern in transformed data
    final_diagnostic = analyze_pattern(transformed_data)
    
    # Output result
    print(f"Result: {final_diagnostic}")