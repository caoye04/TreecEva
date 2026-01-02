import math

# Irrelevant helper function (decoy)
def compute_entropy(data):
    total = 0
    for x in data:
        if x > 0:
            total -= x * math.log(x)
    return total

# Unused transformation (dead code path)
def transform_legacy(signal):
    return [int(s ** 1.5) for s in signal if s % 2 == 1]

# Core processing pipeline
def filter_noise(signal, threshold=5.0):
    """Apply adaptive noise filter using median baseline."""
    median_val = sorted(signal)[len(signal)//2]
    filtered = []
    for val in signal:
        if abs(val - median_val) >= threshold / 2:
            filtered.append(val * 0.9)
        else:
            filtered.append(median_val + 0.1)  # Suppress near-median values
    return filtered

# Signal modulation analysis
def extract_envelope(signal):
    peak = max(signal)
    trough = min(signal)
    return (peak - trough) / 2

# Distractor: unused frequency estimator
def estimate_dominant_frequency(signal, sample_rate=1000):
    n = len(signal)
    fft_result = [complex(0, 0)] * n
    for k in range(n):
        for t in range(n):
            angle = -2 * math.pi * t * k / n
            fft_result[k] += complex(signal[t] * math.cos(angle), signal[t] * math.sin(angle))
    magnitudes = [abs(f) for f in fft_result]
    return magnitudes.index(max(magnitudes)) * sample_rate / n

# Real processing chain
def preprocess_signal(raw):
    scaled = [x * 1.75 for x in raw]
    offset_corrected = [x - 0.5 for x in scaled]
    return offset_corrected

# Data fusion via lambda abstraction (key python feature)
combine_metrics = lambda a, b, c: (a * 0.4) + (b * 0.35) + (c * 0.25)

# Main diagnostic analyzer
def analyze_signal(data_chunk):
    # Step 1: Extract basic statistics
    mean_val = sum(data_chunk) / len(data_chunk)
    
    # Step 2: Compute dispersion metrics
    variance = sum((x - mean_val) ** 2 for x in data_chunk) / len(data_chunk)
    std_dev = math.sqrt(variance)
    
    # Step 3: Detect asymmetry
    skew_numerator = sum((x - mean_val) ** 3 for x in data_chunk)
    skew_denominator = len(data_chunk) * (std_dev ** 3)
    skewness = skew_numerator / skew_denominator if skew_denominator != 0 else 0
    
    # Step 4: Calculate envelope and normalized power
    envelope = extract_envelope(data_chunk)
    normalized_power = sum(x**2 for x in data_chunk) / len(data_chunk)
    
    # Step 5: Apply non-linear weighting based on skewness
    if skewness > 0.5:
        adjustment_factor = 1.8
    elif skewness < -0.5:
        adjustment_factor = 1.2
    else:
        adjustment_factor = 1.5  # Balanced case
    
    # Step 6: Weighted combination using lambda function
    primary_metric = combine_metrics(std_dev, envelope, normalized_power)
    
    # Step 7: Final adjustment with conditional logic
    if primary_metric > 10 and adjustment_factor == 1.8:
        final_score = primary_metric * adjustment_factor * 0.9
    elif primary_metric <= 5:
        final_score = primary_metric * adjustment_factor * 1.1
    else:
        final_score = primary_metric * adjustment_factor
    
    # Step 8: Floor at minimum detectable level
    if final_score < 3.2:
        final_score = 3.2
    
    return final_score

# Simulated sensor input (real data)
sensor_readings = [2.1, 3.4, 2.8, 3.9, 4.2, 3.6, 2.5, 3.1, 4.0, 3.8]

# Irrelevant pre-processing chain (distractor)
temp_analysis = compute_entropy([x/10 for x in sensor_readings])
legacy_transform = transform_legacy(sensor_readings)

# Actual execution path
raw_data_stream = sensor_readings[:]
preprocessed_data = preprocess_signal(raw_data_stream)
filtered_data = filter_noise(preprocessed_data, threshold=4.5)

# Key statement
final_diagnostic = analyze_signal(filtered_data)

# Print result as required
print(f"Target result: {final_diagnostic}")