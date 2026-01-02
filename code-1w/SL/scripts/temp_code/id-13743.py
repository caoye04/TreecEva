import math

# Simulated sensor data processing with diagnostic analysis
def collect_samples(duration, rate=100):
    return [math.sin(t * 0.1) + 0.5 * math.cos(t * 0.3) for t in range(0, int(duration * rate))]

def apply_window(signal, window_type='hann'):
    size = len(signal)
    if window_type == 'hann':
        return [signal[i] * (0.5 - 0.5 * math.cos(2 * math.pi * i / (size - 1))) for i in range(size)]
    return signal

def remove_dc_offset(signal):
    mean_val = sum(signal) / len(signal)
    return [x - mean_val for x in signal]

def compute_magnitude_spectrum(signal):
    # Real FFT approximation using squared magnitudes
    spectrum = []
    n = len(signal)
    for k in range(n // 2):
        re = sum(signal[i] * math.cos(2 * math.pi * k * i / n) for i in range(n))
        im = -sum(signal[i] * math.sin(2 * math.pi * k * i / n) for i in range(n))
        spectrum.append(re * re + im * im)
    return spectrum

def extract_peaks(spectrum, min_distance=5, threshold=1e-5):
    peaks = []
    for i in range(min_distance, len(spectrum) - min_distance):
        if spectrum[i] > threshold and all(spectrum[i] >= spectrum[i + d] for d in range(-min_distance, min_distance + 1) if d != 0):
            peaks.append((i, spectrum[i]))
    return sorted(peaks, key=lambda x: x[1], reverse=True)

def frequency_to_note(freq_index, sample_rate=100):
    # Map frequency bin to musical note name (decorative)
    notes = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
    note_index = int(round(12 * math.log2(freq_index + 1))) % 12 if freq_index > 0 else 0
    octave = int((freq_index + 1) / 12) + 4
    return f'{notes[note_index]}{octave}'

def validate_calibration(data_string, expected_prefix="CAL"):
    # Irrelevant validation function (distractor)
    if not data_string.startswith(expected_prefix):
        return False
    checksum = sum(ord(c) for c in data_string) % 256
    return checksum == 42

def generate_noise(length, seed=42):
    # Dead code path - never used
    rand_seq = [(seed * i * 17) % 1001 / 1000 for i in range(length)]
    return rand_seq

def compress_sequence(seq):
    # Unused compression function (distractor)
    if not seq:
        return ''
    result = []
    count = 1
    for a, b in zip(seq, seq[1:] + ['\0']):
        if a == b:
            count += 1
        else:
            result.append(str(count) + a if count > 1 else a)
            count = 1
    return ''.join(result)

def analyze_signal(signal, sensitivity):
    # Core analysis logic
    cleaned = remove_dc_offset(signal)
    windowed = apply_window(cleaned)
    spectrum = compute_magnitude_spectrum(windowed)
    peaks = extract_peaks(spectrum, threshold=0.01)
    
    # Extract dominant frequency information
    if not peaks:
        return 0.0
    
    dominant_bin = peaks[0][0]
    spectral_entropy = -sum((val / sum(v for _, v in peaks)) * math.log2(val + 1e-8) for _, val in peaks)
    
    # Secondary peak analysis (distraction)
    secondary_notes = []
    for p in peaks[1:4]:
        note = frequency_to_note(p[0])
        secondary_notes.append(note)
    
    # Actual computation path
    temp_slice = str(dominant_bin)[::-1]  # String slicing operation
    reversed_digits = int(temp_slice) if temp_slice.isdigit() else 0
    entropy_factor = int(abs(spectral_entropy * 100))
    
    # Final diagnostic formula
    diagnostic_score = (reversed_digits * 7) - (entropy_factor * 3) + (len(peaks) ** 2)
    
    # Red herring: fake normalization
    if diagnostic_score > 100:
        normalized = math.log(diagnostic_score, 10)
        scaled = normalized * 10
    else:
        scaled = diagnostic_score
    
    # This variable is critical
    final_diagnostic = scaled + 5
    
    # More distractors below
    metadata_tag = f"ANALYSIS_V2:{dominant_bin}:{entropy_factor}"
    is_valid = validate_calibration(metadata_tag)
    compressed_log = compress_sequence(metadata_tag.replace(':', ''))
    
    return final_diagnostic

# Main execution flow
raw_data = collect_samples(duration=2.5, rate=80)

# Filter out low-amplitude samples (preprocessing)
threshold = 0.15
filtered_data = [x for x in raw_data if abs(x) > threshold]

# Truncate to power-of-two length for FFT efficiency (even if unused later)
power_of_two_size = 2 ** int(math.log2(len(filtered_data)))
cropped_data = filtered_data[:power_of_two_size]

# Apply additional filtering based on string pattern matching (distractor)
data_as_str = ''.join(['1' if x > 0 else '0' for x in cropped_data[:16]])
if '1010' in data_as_str:
    cropped_data = cropped_data[1:]

# Signal reshaping via slicing (relevant)
reshaped = cropped_data[::2] + cropped_data[1::2]  # Interleaved slice merge

# Decoy statistical calculations
mean_val = sum(reshaped) / len(reshaped) if reshaped else 0
variance = sum((x - mean_val) ** 2 for x in reshaped) / len(reshaped) if reshaped else 0
peak_to_peak = max(reshaped) - min(reshaped) if reshaped else 0

# Trigger point: this is where the answer is computed
final_diagnostic = analyze_signal(filtered_data, threshold)

# Output result (required format)
print(f"Result: {final_diagnostic}")