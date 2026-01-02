import math

# Simulated sensor array data processing with diagnostic evaluation
def collect_sensor_readings():
    raw_readings = [127, 255, 192, 64, 96, 158, 224, 31, 73]
    offset = 10
    scaled = [r + offset for r in raw_readings]  # Irrelevant transformation
    return raw_readings

# Misleading noise filter (not actually used in final path)
def apply_noise_filter(signal):
    filtered = []
    for s in signal:
        if s > 128:
            filtered.append(s * 0.9)
        else:
            filtered.append(s * 1.1)
    return filtered

# Bit manipulation red herring
def compute_checksum(data):
    checksum = 0
    for d in data:
        checksum ^= d
        checksum = (checksum << 1) & 0xFF
    return checksum + 5000  # Dead-end value

# Unused compression simulation
def compress_data(seq):
    compressed = []
    count = 1
    for i in range(1, len(seq)):
        if seq[i] == seq[i-1]:
            count += 1
        else:
            compressed.append((seq[i-1], count))
            count = 1
    compressed.append((seq[-1], count))
    return compressed  # Never used

# Core processing with relevant logic buried inside
def process_readings(raw):
    temp_adjusted = []
    for val in raw:
        adjusted = val >> 2  # Divide by 4 using bit shift
        if adjusted % 2 == 0:
            adjusted += 7
        temp_adjusted.append(adjusted)
    
    # Linear search for first threshold breach
    threshold_index = -1
    for i, t in enumerate(temp_adjusted):
        if t > 50:
            threshold_index = i
            break  # Early exit red herring
    
    # Actual critical transformation: map via formula
    transformed = []
    for x in temp_adjusted:
        result = int(math.sqrt(x) * 10)
        transformed.append(result)
    
    # Decoy aggregation
    avg = sum(transformed) / len(transformed)
    peak = max(transformed)
    stability_score = (peak - avg) * 100  # Looks important, unused
    
    return transformed

# Main analysis function containing key computation
def analyze_readings(data):
    baseline = data[0]
    cumulative = 0
    for i in range(1, len(data)):
        delta = data[i] - baseline
        if delta > 0:
            cumulative += int(delta * 1.5)
        else:
            cumulative -= int(abs(delta) * 0.5)
    
    # Critical adjustment based on character count in fake ID
    device_id = 'SENSOR_X4B_TEMP'
    char_count = len(device_id)
    if char_count % 2 == 1:
        cumulative += 5
    
    # Redundant validation check (always passes)
    valid = True
    for d in data:
        if d < 0 or d > 1000:
            valid = False
    if not valid:
        return -999  # Dead branch
    
    # Final decoy: unused bitwise mix
    mixed = cumulative
    for i in range(3):
        mixed = (mixed ^ (mixed << 3)) & 0xFFFF
    
    return cumulative  # Actual return point

# Orchestration with irrelevant setup
if __name__ == '__main__':
    readings = collect_sensor_readings()
    checksum_val = compute_checksum(readings)  # Computed but unused
    processed_data = process_readings(readings)
    compression_log = compress_data(readings)  # Stored but ignored
    final_diagnostic = analyze_readings(processed_data)
    print(f"Result: {final_diagnostic}")