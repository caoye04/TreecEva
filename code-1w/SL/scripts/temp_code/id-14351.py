import math

# Simulated sensor data processing with embedded diagnostics
def collect_sensor_readings():
    raw_readings = [127, 255, 192, 64, 224, 32, 168, 96]
    scale_factor = 0.75
    adjusted = [x * scale_factor for x in raw_readings]
    return adjusted

# Irrelevant helper: color conversion (distractor)
def rgb_to_grayscale(r, g, b):
    return 0.299 * r + 0.587 * g + 0.114 * b

# Misleading diagnostic flag (red herring)
current_status = 'STABLE'

# Signal conditioning with noise filtering
def preprocess(signal_list):
    filtered = []
    for val in signal_list:
        if val > 100:
            filtered.append(val * 0.9)
        elif val > 50:
            filtered.append(val * 0.95)
        else:
            filtered.append(val)
    # Additional transformation
    normalized = [round(x / max(filtered) * 255) for x in filtered]
    return normalized

# Bit manipulation analysis (relevant only in part)
def compute_checksum(data_seq):
    checksum = 0
    for item in data_seq:
        checksum ^= item  # XOR into checksum
        checksum = (checksum << 1) & 0xFF | (checksum >> 7)
    return checksum

# Unused decoy function: spectral analysis (dead path)
def perform_fft(samples):
    # This function is defined but never used
    N = len(samples)
    fft_result = [0 + 0j] * N
    for k in range(N):
        for n in range(N):
            angle = -2 * math.pi * k * n / N
            fft_result[k] += complex(samples[n]) * complex(math.cos(angle), math.sin(angle))
    return fft_result

# Data classification based on thresholds (partially relevant)
def classify_amplitude(value):
    if value > 200:
        return 'HIGH'
    elif value > 100:
        return 'MEDIUM'
    else:
        return 'LOW'

# Main processing pipeline
def analyze_signal(data):
    # Step 1: Categorize each point (distractor usage)
    categories = [classify_amplitude(x) for x in data]
    
    # Step 2: Compute statistical moments (some distraction)
    mean_val = sum(data) / len(data)
    variance = sum((x - mean_val) ** 2 for x in data) / len(data)
    std_dev = math.sqrt(variance)
    
    # Step 3: Detect peaks above dynamic threshold
    dynamic_threshold = mean_val + 0.5 * std_dev
    peak_count = sum(1 for x in data if x > dynamic_threshold)
    
    # Step 4: Analyze bit patterns in byte values (key step)
    byte_entropy = 0
    for val in data:
        byte_val = val & 0xFF
        ones = bin(byte_val).count('1')
        byte_entropy += abs(ones - 4)  # deviation from balanced bits
    
    # Step 5: Checksum of every third element (critical)
    subsample = [data[i] for i in range(0, len(data), 3)]
    key_checksum = compute_checksum(subsample)
    
    # Step 6: Conditional adjustment based on entropy and peaks
    if peak_count >= 3:
        adjustment = 2
    else:
        adjustment = -1
    
    # Final diagnostic score: combination of checksum and entropy trend
    base_score = key_checksum * adjustment
    entropy_trend = int(byte_entropy // 2)
    
    # Red herring: status override check (never triggers)
    if current_status == 'CRITICAL' and entropy_trend > 50:
        final_score = 999
    else:
        final_score = base_score - entropy_trend + 17
    
    # Critical assignment point
    final_diagnostic = final_score
    return final_diagnostic

# Global configuration (distractor)
SYSTEM_MODE = 'DIAGNOSTIC'
CALIBRATION_OFFSET = 0.05
LOG_INTERVAL = 10

# Execution flow
if __name__ == '__main__':
    # Collect and process sensor data
    raw_data = collect_sensor_readings()
    processed_data = preprocess(raw_data)
    
    # Perform secondary irrelevant analysis
    histogram = {}
    for val in processed_data:
        bucket = val // 10 * 10
        histogram[bucket] = histogram.get(bucket, 0) + 1
    
    # Core analysis
    final_diagnostic = analyze_signal(processed_data)
    
    # Output result
    print(f"Result: {final_diagnostic}")