import math

# Simulated sensor array data processing with diagnostic logic
def fetch_raw_readings():
    return [127, 255, 193, 64, 222, 87, 150, 201, 95, 178]

def calibrate(value):
    # Complex calibration curve: not all values are used in final path
    if value < 100:
        return (value * 1.8) + 32
    elif value < 200:
        return value + (value % 7)
    else:
        return int(value * 0.95)

def transform_scale(val):
    # Unused red herring function - looks important but never called
    return round(math.log(val + 1) * 10, 2)

def filter_outliers(data, limit=200):
    # Only values below limit are kept, but some distractor logic included
    cleaned = []
    high_count = 0  # misleading counter
    for x in data:
        if x > limit:
            high_count += 1
        else:
            cleaned.append(x)
    # Distractor: this adjustment seems relevant but isn't used
    adjustment_factor = 1.05 if high_count > 2 else 0.98
    return cleaned  # adjustment_factor not returned or used

def encrypt_key(n):
    # Bit manipulation decoy - looks like it might be needed later
    key = n ^ 255
    key = (key << 2) & 255 | (key >> 6)
    return key

def generate_checksum(seq):
    # Checksum computed but only conditionally used (never actually triggered)
    chk = 0
    for i, v in enumerate(seq):
        chk ^= (v + i) % 256
    return chk

def process_readings(raw):
    calibrated = [calibrate(v) for v in raw]
    
    # Apply conditional offset based on length (real step)
    if len(calibrated) % 2 == 1:
        calibrated = [c + 5 for c in calibrated]
    
    # String-based flag encoding - irrelevant but plausible
    status_flags = ''
    for c in calibrated:
        if c > 150:
            status_flags += 'H'
        elif c < 100:
            status_flags += 'L'
        else:
            status_flags += 'M'
    
    # Decoy transformation using string methods
    reversed_flags = status_flags[::-1].replace('H', 'X').replace('L', 'Y')
    
    # Linear search for first over-threshold value (red herring computation)
    threshold_index = -1
    for idx, val in enumerate(calibrated):
        if val > 190:
            threshold_index = idx
            break
    
    # Real processing path: average of specific subset
    subset = [c for c in calibrated if c > 120 and c < 190]
    avg = sum(subset) / len(subset) if subset else 0
    
    # Another decoy: checksum generated but unused
    _ = generate_checksum(calibrated)
    
    return {
        'data': calibrated,
        'average_midrange': avg,
        'flags': status_flags,
        'index_hint': threshold_index,
        'size_tag': f'SZ{len(calibrated)}'
    }

def analyze_readings(proc_data, thresh):
    readings = proc_data['data']
    mid_avg = proc_data['average_midrange']
    
    # Bitwise analysis decoy
    bit_analysis = 0
    for r in readings[:4]:
        bit_analysis += bin(r).count('1')
    
    # Conditional logic chain with multiple branches (only one matters)
    diagnostic = 0
    if mid_avg < thresh:
        diagnostic = 1001
    elif mid_avg == thresh:
        diagnostic = 2002
    else:
        base = int(mid_avg)
        # Complex-looking but deterministic calculation
        temp = (base ^ 17) + (base >> 3)
        temp = temp * 3 - (temp // 4)
        if temp % 2 == 0:
            diagnostic = temp + 5
        else:
            diagnostic = temp - 3
    
    # Irrelevant string operation that mimics validation
    tag = proc_data['size_tag']
    validation_code = ''.join([ch * 2 for ch in tag[:3]])
    
    # Final answer depends only on this line, others are distractions
    final_diagnostic = diagnostic * 2  # actual output-determining step
    
    # Dead code path: never executed due to fixed conditions
    if len(validation_code) > 100:
        final_diagnostic -= 500
    
    return final_diagnostic

# Main execution flow
raw_sensor_data = fetch_raw_readings()
processed_data = process_readings(raw_sensor_data)
threshold = 145
final_diagnostic = analyze_readings(processed_data, threshold)
print(f"Result: {final_diagnostic}")