import itertools

# Simulated sensor data processing with diagnostic analysis
def collect_sensor_readings():
    raw_samples = [0.8, 1.2, -0.5, 3.1, 2.7, -1.3, 0.0, 1.9]
    scaling_factor = 1.75
    adjusted = [round(x * scaling_factor, 3) for x in raw_samples]
    return adjusted

# Irrelevant auxiliary function (distractor)
def calculate_compression_ratio(size_original, size_compressed):
    if size_compressed == 0:
        return float('inf')
    return round(size_original / size_compressed, 2)

# Signal conditioning with red herring operations
def filter_noise(data, threshold=1.0):
    cleaned = []
    noise_log = []  # Dead variable - never used again
    suppression_count = 0

    for val in data:
        if abs(val) < threshold:
            cleaned.append(0.0)
            noise_log.append(val)
            suppression_count += 1
        else:
            cleaned.append(val)
    
    # Misleading intermediate calculation (distractor)
    avg_suppression = suppression_count / len(data) if data else 0
    return cleaned

# Data transformation with tuple unpacking and conditional expressions
def generate_frequency_bands(signal):
    low_band = []
    mid_band = []
    high_band = []
    
    for x in signal:
        band = 'low' if abs(x) < 1.0 else ('mid' if abs(x) < 2.0 else 'high')
        if band == 'low':
            low_band.append(x * 0.5)
        elif band == 'mid':
            mid_band.append(x * 1.2)
        else:
            high_band.append(x * 1.5)
    
    # Complex unpacking with decoy usage
    lengths = (len(low_band), len(mid_band), len(high_band))
    l, m, h = lengths
    adjustment_vector = [l * 0.1, m * 0.15, h * 0.2]  # Computed but unused
    
    return list(itertools.chain(low_band, mid_band, high_band))

# Recursive peak detection (core relevant logic)
def detect_peaks_recursive(seq, index=0, peaks=None):
    if peaks is None:
        peaks = []
    
    if index >= len(seq):
        return peaks
    
    # Check for local maximum
    if (index == 0 or seq[index] > seq[index-1]) and (index == len(seq)-1 or seq[index] > seq[index+1]):
        if seq[index] != 0.0:  # Avoid zero peaks
            peaks.append(seq[index])
    
    return detect_peaks_recursive(seq, index + 1, peaks)

# Main analysis pipeline
processed_data = collect_sensor_readings()
processed_data = filter_noise(processed_data, threshold=1.2)
processed_data = generate_frequency_bands(processed_data)

# Decoy data structure manipulation
snapshot_buffer = [{'timestamp': i, 'value': v} for i, v in enumerate(processed_data)]
deep_copy_ref = snapshot_buffer[::-1]  # Unused copy

# Irrelevant statistical summary (distractor)
def compute_moment(sequence, order=2):
    mean_val = sum(sequence) / len(sequence) if sequence else 0
    return sum((x - mean_val) ** order for x in sequence) / len(sequence)

moment_2 = compute_moment(processed_data, 2)
moment_3 = compute_moment(processed_data, 3)  # Calculated but not used

# Core diagnostic logic
peak_values = detect_peaks_recursive(processed_data)
peak_energy = sum(p ** 2 for p in peak_values)
signal_power = sum(x ** 2 for x in processed_data) / len(processed_data) if processed_data else 0

# Final diagnostic metric computation
power_ratio = signal_power / peak_energy if peak_energy != 0 else 0
final_diagnostic = int(round(1000 * power_ratio))

print(f"Result: {final_diagnostic}")