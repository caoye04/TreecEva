import math

# Simulated sensor data processing with embedded diagnostics
def collect_readings():
    raw_values = [0.88, -1.22, 3.14, 2.71, -0.55]
    scale_factor = 1.75
    adjusted = [round(v * scale_factor, 3) for v in raw_values]
    return adjusted

# Irrelevant auxiliary function - dead code path
def legacy_calibrate(x):
    return (x + 2) ** 0.5 if x > 0 else 0

# Noise filtering using moving average (relevant)
def smooth_signal(data):
    window = 3
    smoothed = []
    for i in range(len(data)):
        if i < window - 1:
            smoothed.append(data[i])
        else:
            avg = sum(data[i - window + 1:i + 1]) / window
            smoothed.append(round(avg, 3))
    return smoothed

# Bit manipulation for error flag simulation (distractor)
def encode_status(code, mode=0):
    flag = 0b1010
    if mode == 1:
        flag = (flag << 4) | 0b1100
    elif mode == 2:
        flag ^= 0b1111
    return flag ^ code  # Unused in final logic

def extract_features(signal):
    # Extract statistical features
    mean_val = sum(signal) / len(signal)
    variance = sum((x - mean_val) ** 2 for x in signal) / len(signal)
    peak = max(abs(x) for x in signal)
    
    # Distractor: string-based status (irrelevant to final result)
    status_msg = f"Signal peak: {peak:.2f}"
    status_upper = status_msg.upper().replace("SIGNAL", "DIAG")
    checksum_str = str(hash(status_upper))[-3:]
    
    # Real feature vector
    return {
        'mean': mean_val,
        'variance': variance,
        'peak': peak,
        'length': len(signal)
    }

# Complex conditional analysis with early returns (key logic)
def analyze_signal(features):
    if isinstance(features, list):
        data = extract_features(features)
    else:
        data = features
    
    # Misleading intermediate computation (red herring)
    temp_score = (data['mean'] * 100) + (data['variance'] * 10)
    if temp_score < 0:
        adjustment = math.log(abs(temp_score) + 1)
    else:
        adjustment = math.sin(temp_score)
    
    # Core decision logic with nesting depth 4
    baseline = 500
    if data['peak'] > 2.5:
        if data['variance'] > 1.0:
            if data['mean'] > 0:
                baseline += 127
            else:
                baseline -= 89
        else:
            baseline += 45
    elif data['peak'] > 1.5:
        if data['length'] >= 5:
            baseline += 67
        else:
            baseline -= 34
    else:
        baseline = 200
    
    # Final transformation using bit operations (relevant)
    processed_baseline = (baseline ^ 0b11010110) & 0b11111111
    return processed_baseline

# Orchestration with decoy calls
if __name__ == "__main__":
    readings = collect_readings()                    # Step 1
    filtered = smooth_signal(readings)               # Step 2
    features = extract_features(filtered)            # Step 3
    
    # Decoy function call with no effect
    _ = encode_status(123, mode=1)
    _ = encode_status(456, mode=2)
    
    # Critical execution point
    final_diagnostic = analyze_signal(features)
    
    # Print required output
    print(f"Result: {final_diagnostic}")