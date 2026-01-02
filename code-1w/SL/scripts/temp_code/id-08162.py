import math

# Simulated sensor data processing with diagnostic flags
def collect_sensor_data():
    raw_samples = [i * 0.5 + (i % 7) for i in range(24)]
    timestamps = [t * 100 + 5 for t in range(24)]
    validation_checksum = sum([int(x) for x in raw_samples[::3]])
    return list(zip(timestamps, raw_samples))

# Irrelevant auxiliary function - dead code path
def deprecated_filter(data):
    return [x for x in data if x > 3.5]

# Signal conditioning with multiple distractions
def clean_signal(raw_data):
    cleaned = []
    noise_floor = 0.0
    for ts, val in raw_data:
        adjusted = val * 1.07 - 0.3
        if abs(adjusted) < 0.1:
            adjusted = 0.0
        # Decoy counter
        noise_floor += 0.01
        cleaned.append(round(adjusted, 6))
    return cleaned

# Frame segmentation with red herring logic
def segment_frames(signal):
    frames = []
    window_size = 6
    for i in range(0, len(signal) - window_size + 1, 3):
        frame = signal[i:i + window_size]
        parity_check = sum(1 for x in frame if x > 2.0)
        # Unused derived metric
        entropy_proxy = 0.0
        if parity_check > 0:
            entropy_proxy = math.log(parity_check) * 1.5
        frames.append({
            'data': frame,
            'quality': parity_check,
            'meta': {'index': i, 'valid': len(frame) == window_size}
        })
    return frames

# Misleading transformation chain
def apply_fft_stub(frames):
    transformed = []n    for f in frames:
        fake_magnitude = 0
        for i, x in enumerate(f['data']):
            fake_magnitude += x * math.sin(i * 0.5)
        # This result is never used
        transformed.append({'mag': round(fake_magnitude, 4), 'phase': 0})
    return transformed  # Dead return

# Critical processing hidden among distractions
def extract_features(frames):
    feature_vector = []
    for i, frame in enumerate(frames):
        peak = max(frame['data'])
        avg = sum(frame['data']) / len(frame['data'])
        zero_crossings = 0
        prev = frame['data'][0]
        for x in frame['data'][1:]:
            if prev < 0 <= x or prev > 0 > x:
                zero_crossings += 1
            prev = x
        # Only this computation feeds into the final answer
        score = (peak * 1.5) + (avg * 0.8) - (zero_crossings * 2)
        feature_vector.append(round(score, 6))
    return feature_vector

# Secondary irrelevant analysis
def compute_redundant_metrics(features):
    extremes = {
        'max_val': max(features),
        'min_val': min(features),
        'range': max(features) - min(features)
    }
    # This entire function is a distractor
    return {k: round(v, 4) for k, v in extremes.items()}

# Core diagnostic algorithm - only part that matters
def analyze_signal(feature_set):
    base = 0.0
    multiplier_sequence = [1.1, 0.9, 1.2, 0.8, 1.3, 0.7]
    for idx, val in enumerate(feature_set):
        # Key logic: alternating weighting based on index
        if idx % 2 == 0:
            base += val * multiplier_sequence[idx % 6]
        else:
            base -= val * 0.5
    # Final non-linear adjustment
    if base > 100:
        base = base * 0.95
    else:
        base = base * 1.05 + 10
    return int(round(base))

# Orchestration with decoy calls
if __name__ == '__main__':
    # Step 1: Collect raw data
    samples = collect_sensor_data()
    
    # Step 2: Clean signal (relevant)
    cleaned_signal = clean_signal(samples)
    
    # Step 3: Segment into frames (relevant)
    processed_frames = segment_frames(cleaned_signal)
    
    # Step 4: Apply unused FFT (red herring)
    fft_output = apply_fft_stub(processed_frames)
    
    # Step 5: Extract actual features (critical)
    extracted_features = extract_features(processed_frames)
    
    # Step 6: Compute useless metrics (distraction)
    redundant_stats = compute_redundant_metrics(extracted_features)
    
    # Step 7: Generate final diagnostic (ANSWER POINT)
    final_diagnostic = analyze_signal(extracted_features)
    
    # Step 8: Print result
    print(f"Result: {final_diagnostic}")