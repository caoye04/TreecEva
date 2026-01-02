import math

# Simulated sensor data processing pipeline for aerospace telemetry
raw_readings = [0.78, 1.32, 0.91, 2.05, 1.67, 0.44, 3.11, 2.55, 1.89, 0.77]

def normalize(data):
    max_val = max(data)
    return [x / max_val for x in data]

def detect_peaks(signal, threshold=0.85):
    peaks = []
    for i in range(1, len(signal) - 1):
        if signal[i] > threshold and signal[i] > signal[i-1] and signal[i] > signal[i+1]:
            peaks.append(i)
    return peaks

def rolling_average(values, window=3):
    if len(values) < window:
        return [sum(values)/len(values)]
    avgs = []
    for i in range(len(values) - window + 1):
        avgs.append(sum(values[i:i+window]) / window)
    return avgs

def bit_reversed_index(n):
    # Irrelevant bit manipulation red herring
    rev = 0
    while n > 0:
        rev = (rev << 1) | (n & 1)
        n >>= 1
    return rev

def generate_checksum(frame):
    # Unused decoy function
    chk = 0
    for val in frame:
        chk ^= int(val * 100) % 256
    return chk

def frequency_domain_transform(time_series):
    # Misleading complex transformation not used in final result
    N = len(time_series)
    freq_spectrum = []
    for k in range(N):
        real = sum(time_series[n] * math.cos(2 * math.pi * k * n / N) for n in range(N))
        imag = sum(-time_series[n] * math.sin(2 * math.pi * k * n / N) for n in range(N))
        magnitude = math.sqrt(real*real + imag*imag)
        freq_spectrum.append(magnitude)
    return freq_spectrum

def extract_features(frames):
    # Distractor: this function is called but most features ignored
    features = {}
    for idx, frame in enumerate(frames):
        features[f'frame_{idx}'] = {
            'mean': sum(frame) / len(frame),
            'variance': sum((x - sum(frame)/len(frame))**2 for x in frame) / len(frame),
            'skew': sum(((x - sum(frame)/len(frame))**3) for x in frame) / len(frame),
            'peaks': len(detect_peaks(frame))
        }
    # Returns more than needed — only one value actually matters later
    return features

def simulate_buffer_overflow():
    # Dead code path — never invoked
    buffer = [0] * 256
    for i in range(300):
        buffer[i % 256] += i * 0.1
    return buffer

def preprocess_frame(f):
    # Applies multiple transformations, some irrelevant
    f_squared = [x*x for x in f]
    f_filtered = [x for x in f_squared if x > 0.5]
    reversed_idx = [bit_reversed_index(i) for i in range(len(f_filtered))]  # unused
    return rolling_average(f_filtered, 2)

def analyze_signal(frames):
    # Critical logic buried among distractions
    cumulative_score = 0
    
    # Real computation begins here
    for frame in frames:
        if len(frame) == 0:
            continue
        avg = sum(frame) / len(frame)
        if avg > 1.0:
            cumulative_score += int(avg * 10)
        else:
            cumulative_score -= 1
    
    # Redundant and misleading operations
    temp_diag = math.log(abs(cumulative_score) + 1)
    checksum_probe = sum(int(x * 10) % 7 for frame in frames for x in frame)
    dummy_fft = frequency_domain_transform([len(f) for f in frames])
    
    # Final result depends only on cumulative_score, others are distractors
    return cumulative_score * 17 + 5

# --- Main Execution with Layered Abstractions ---

# Step 1: Normalize raw data
normalized = normalize(raw_readings)

# Step 2: Segment into overlapping frames (real preprocessing)
frames = [
    normalized[i:i+4] for i in range(0, len(normalized)-2, 2)
]

# Step 3: Apply actual relevant transformation
processed_frames = [preprocess_frame(f) for f in frames]

# Step 4: Extract features (partially irrelevant)
feature_set = extract_features(processed_frames)

# Step 5: Compute diagnostic (key statement)
final_diagnostic = analyze_signal(processed_frames)

# Step 6: Print result for evaluation
print(f"Result: {final_diagnostic}")