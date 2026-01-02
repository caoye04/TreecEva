import math

# Simulated sensor data processing with diagnostic analysis
def collect_samples(duration):
    samples = []
    for t in range(0, duration * 10):
        # Real signal component: damped oscillation
        signal = 150 * math.exp(-t / 200) * math.sin(t / 5)
        # Noise floor and interference
        noise = (t % 7) * 3.14 + math.cos(t / 9) * 12
        total = signal + noise + 50
        samples.append(total)
    return samples

# Irrelevant helper - decoy function
def smooth_data(data):
    smoothed = [data[0]]
    for i in range(1, len(data) - 1):
        avg = (data[i-1] + data[i] + data[i+1]) / 3
        smoothed.append(avg)
    smoothed.append(data[-1])
    return smoothed

# Signal thresholding with hysteresis (used)
def apply_hysteresis(data, low=85, high=95, on_val=1, off_val=0):
    state = off_val
    result = []
    for x in data:
        if state == off_val and x >= high:
            state = on_val
        elif state == on_val and x <= low:
            state = off_val
        result.append(state)
    return result

# Frame segmentation based on zero-crossings (used)
def segment_into_frames(signal):
    frames = []
    current_frame = []
    for i in range(1, len(signal)):
        # Detect negative zero crossing
        if signal[i-1] > 0 > signal[i]:
            if current_frame:
                frames.append(current_frame)
                current_frame = []
        current_frame.append(signal[i])
    if current_frame:
        frames.append(current_frame)
    return frames

# Misleading feature extraction - mostly irrelevant
def extract_features(frame):
    length = len(frame)
    peak = max(frame, default=0)
    trough = min(frame, default=0)
    mean_val = sum(frame) / length if length else 0
    variance = sum((x - mean_val) ** 2 for x in frame) / length if length else 0
    # Decoy metrics
    entropy_like = -sum((x / 100) * math.log(abs(x / 100) + 1e-8) for x in frame)
    fft_approx = sum(math.sin(frame[i] * i) for i in range(0, len(frame), 3))
    return {
        'length': length,
        'peak': peak,
        'trough': trough,
        'mean': mean_val,
        'variance': variance,
        'entropy_proxy': entropy_like,  # unused distraction
        'fft_mock': fft_approx           # unused distraction
    }

# Core processing pipeline
samples = collect_samples(12)

# Apply filtering chain
filtered = [x for x in samples if 20 < x < 180]  # remove outliers
thresholded = apply_hysteresis(filtered)

# Reconstruct signal using thresholded gate (used)
gated_signal = [samples[i] for i in range(len(samples)) if i < len(thresholded) and thresholded[i] == 1]

decoy_transformation = ''.join([chr(int(65 + (abs(hash(str(x))) % 26))) for x in filtered[:10]])  # string distractor

# Segment signal into meaningful chunks
raw_frames = segment_into_frames(gated_signal)

# Process each frame with feature extraction
frame_features = []
for raw_frame in raw_frames:
    # Slice only central portion of each frame
    center_start = len(raw_frame) // 4
    center_end = 3 * len(raw_frame) // 4
    core_segment = raw_frame[center_start:center_end]
    
    # Extract features including red herrings
    feats = extract_features(core_segment)
    
    # Add derived properties - some relevant, some not
    if feats['length'] > 0:
        feats['amplitude'] = feats['peak'] - feats['trough']
        feats['skew_proxy'] = (feats['peak'] + feats['trough']) / 2 - feats['mean']
        feats['damping_ratio'] = abs(feats['mean'] / (feats['amplitude'] + 1)) if feats['amplitude'] > 0 else 0
        # Fake complexity
        feats['checksum'] = sum(ord(c) for c in f"F{int(feats['variance'])}") % 100
    
    frame_features.append(feats)

# Secondary filter: only frames with sufficient amplitude
processed_frames = [f for f in frame_features if f.get('amplitude', 0) > 40]

# Another decoy: zip and enumerate misuse
temporal_weights = []
for idx, (feat, sample) in enumerate(zip(processed_frames, samples[::max(len(samples)//len(processed_frames),1)])):
    weight = idx * 0.1 + math.sin(sample / 50)
    temporal_weights.append(weight * (sample % 5))  # irrelevant accumulation

# Critical analysis function (uses only specific fields)
def analyze_signal(frames):
    if not frames:
        return -1
    total_score = 0
    for f in frames:
        # Only these factors matter
        a = f['amplitude']
        d = f['damping_ratio']
        m = f['mean']
        # Complex but deterministic formula
        contribution = (a * 0.7) - (d * 50) + (m * 0.3)
        if contribution > 60:
            total_score += int(contribution // 3)
        else:
            total_score -= int(d * 10)
    # Final transformation
    final_value = int((total_score * 1.45) % 873)
    return final_value

# Key execution point
final_diagnostic = analyze_signal(processed_frames)

print(f"Target result: {final_diagnostic}")