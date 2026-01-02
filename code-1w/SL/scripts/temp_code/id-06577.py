import math

# Simulated sensor data acquisition
def acquire_signal():
    raw_data = [i * 0.5 + math.sin(i * 0.3) for i in range(30)]
    offset_correction = sum(raw_data[:5]) / 5
    corrected = [x - offset_correction for x in raw_data]
    return corrected

# Irrelevant auxiliary function (decoy)
def compute_entropy(data):
    total = 0.0
    for x in data:
        if x > 0:
            total -= x * math.log(x)
    return total  # Unused in main logic

# Signal preprocessing with slicing and filtering
def preprocess(signal):
    filtered = []
    for i in range(2, len(signal) - 2):
        avg = sum(signal[i-2:i+3]) / 5
        filtered.append(avg)
    
    # Extra processing path that's not used (dead code path)
    if len(filtered) > 100:
        extended = filtered + [0] * 10
    else:
        extended = None  # Never used
    
    downsampled = filtered[::2]  # Slicing operation
    normalized = [x / max(abs(min(downsampled)), abs(max(downsampled))) for x in downsampled]
    return normalized

# Frequency bin analysis (misleading intermediate)
def estimate_dominant_frequency(signal):
    length = len(signal)
    fft_real = [sum(signal[j] * math.cos(2 * math.pi * k * j / length) for j in range(length)) for k in range(5)]
    fft_imag = [sum(signal[j] * math.sin(2 * math.pi * k * j / length) for j in range(length)) for k in range(5)]
    magnitudes = [math.sqrt(r*r + i*i) for r, i in zip(fft_real, fft_imag)]
    return magnitudes.index(max(magnitudes)) if magnitudes else 0

# Core diagnostic logic
def detect_anomaly_peaks(data):
    peaks = []
    for i in range(1, len(data) - 1):
        if data[i] > data[i-1] and data[i] > data[i+1] and data[i] > 0.8:
            peaks.append(i)
    return len(peaks) > 0

# Main analysis function
def analyze_signal(samples):
    # Multiple nested conditions with logical operations
    if not samples:
        return -1
    
    threshold = 0.75
    above_thresh = [x for x in samples if x > threshold]
    below_thresh = [x for x in samples if x <= threshold]
    
    high_activity_ratio = len(above_thresh) / len(samples)
    
    # Complex conditional expression
    base_score = 40 if high_activity_ratio > 0.3 else 20
    
    # Additional logic with bit manipulation red herring
    magic_flag = 0b1010
    if len(above_thresh) & 1:  # Bitwise AND (partially relevant)
        magic_flag ^= 0b1100
    
    # Linear search for first significant drop (relevant)
    drop_index = -1
    for i in range(1, len(samples)):
        if samples[i] < samples[i-1] * 0.5 and samples[i-1] > 0.7:
            drop_index = i
            break
    
    # Sorting decoy (creates distraction but unused)
    sorted_inverted = sorted([1/x for x in above_thresh if x != 0], reverse=True)
    median_surrogate = sorted_inverted[len(sorted_inverted)//2] if sorted_inverted else 0.0
    
    # Final decision logic chain
    has_peaks = detect_anomaly_peaks(samples)
    has_early_drop = drop_index != -1 and drop_index < len(samples) // 2
    
    # Composite boolean logic with short-circuit evaluation
    if has_peaks and high_activity_ratio > 0.25 or (has_early_drop and base_score == 40):
        diagnostic_value = 768 + (magic_flag & 0b1111)
    elif len(below_thresh) > len(above_thresh):
        diagnostic_value = 256
    else:
        diagnostic_value = 512
    
    # Final adjustment based on slice statistics
    mid_segment = samples[len(samples)//4 : 3*len(samples)//4]
    if len(mid_segment) > 0 and sum(1 for x in mid_segment if x > 0.9) >= 3:
        diagnostic_value += 16
    
    return diagnostic_value

# Execution flow
signal_input = acquire_signal()
processed_samples = preprocess(signal_input)

# Dead variable assignments (irrelevant)
current_power = sum(x*x for x in signal_input)
baseline_noise = math.fsum(math.cos(x) for x in signal_input)
entropy_metric = compute_entropy(signal_input)  # Computed but unused
freq_bin = estimate_dominant_frequency(signal_input)  # Another unused metric

# Key statement
final_diagnostic = analyze_signal(processed_samples)
print(f"Result: {final_diagnostic}")