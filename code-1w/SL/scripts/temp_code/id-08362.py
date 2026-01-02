import itertools

# Simulated sensor data processing pipeline with diagnostic checks
def collect_sensor_data():
    raw_signals = [0.8, 1.2, -0.5, 3.1, -2.2, 4.0, 1.8, -0.9]
    timestamps = list(range(8))
    return list(zip(timestamps, raw_signals))

# Irrelevant auxiliary function (decoy)
def compute_entropy(data):
    total = 0.0
    for x in data:
        if x > 0:
            total -= x * (x).__log__()
    return round(total, 4)

# Signal normalization (relevant)
def normalize_signal(signal_pairs):
    values = [pair[1] for pair in signal_pairs]
    mean_val = sum(values) / len(values)
    std_dev = (sum((x - mean_val) ** 2 for x in values) / len(values)) ** 0.5
    normalized = [(ts, round((val - mean_val) / std_dev, 6)) for ts, val in signal_pairs]
    return normalized

# Frequency domain approximation via simple binning (distractor with partial relevance)
def estimate_dominant_frequency(signal):
    magnitude_bins = [0] * 4
    for _, val in signal:
        if val < -1:   magnitude_bins[0] += 1
        elif val < 0:  magnitude_bins[1] += 1
        elif val < 1:  magnitude_bins[2] += 1
        else:          magnitude_bins[3] += 1
    peak_bin = magnitude_bins.index(max(magnitude_bins))
    return peak_bin * 0.25  # Simulated frequency estimate

# Signal frame segmentation (relevant)
def segment_into_frames(normalized_signal, size=4):
    frames = []
    for i in range(0, len(normalized_signal), size):
        chunk = normalized_signal[i:i+size]
        if len(chunk) == size:
            frames.append(chunk)
    return frames

# Red herring transformation (dead code path - never called)
def encrypt_frame(frame_data):
    encrypted = []
    for ts, val in frame_data:
        shifted = (val * 127) % 256
        encrypted.append((ts ^ 0xAA, int(shifted)))
    return encrypted

# Core processing with bit manipulation and accumulation (relevant)
def process_frame(frame):
    processed_vals = []
    for ts, val in frame:
        # Apply phase shift based on timestamp parity
        if ts % 2 == 0:
            adjusted = val * 1.1
        else:
            adjusted = val * 0.9
        # Introduce artificial precision noise (to distract)
        noise = (ts * 17) % 11 / 100000
        adjusted += noise
        processed_vals.append(round(adjusted, 6))
    
    # Aggregate using modular arithmetic
    aggregate = 0
    for i, v in enumerate(processed_vals):
        contribution = int(abs(v) * 1000) % (i + 2)
        aggregate = (aggregate * 7 + contribution) % 997
    return aggregate

# Higher-order processing chain
def analyze_signal(frames):
    results = []
    
    # Distractor: precompute unused statistical profile
    all_vals = [v for frame in frames for _, v in frame]
    outlier_count = sum(1 for x in all_vals if abs(x) > 2.0)
    avg_abs = sum(abs(x) for x in all_vals) / len(all_vals)
    
    # Real work: process each valid frame
    for frame in frames:
        frame_hash = hash(tuple(v for _, v in frame))
        if frame_hash % 2 == 0:  # Conditional skip pattern (red herring condition, not actually impactful)
            pass  # Dead branch (misleading)
        processed = process_frame(frame)
        results.append(processed)
    
    # Accumulate final result using list comprehension and itertools
    filtered_results = [r for r in results if r % 2 == 1]  # Only odd aggregates
    shifts = itertools.cycle([1, 3, 5])
    shifted_sum = 0
    for val in filtered_results:
        shift_amount = next(shifts)
        shifted_sum += (val << 1) ^ shift_amount  # Bitwise mangling
    
    # Final diagnostic computation (answer point)
    baseline = sum(filtered_results) % 1000
    fluctuation = (shifted_sum // len(filtered_results)) % 1000 if filtered_results else 0
    final_diagnostic = (baseline * 3 + fluctuation * 2) % 100000
    
    # Irrelevant debug print (distractor)
    # print(f'Debug - Entropy of vals: {compute_entropy(all_vals)}')
    
    return final_diagnostic

# Entry point
if __name__ == '__main__':
    # Step 1: Collect raw sensor data
    raw_data = collect_sensor_data()
    
    # Step 2: Normalize signals
    normalized_signal = normalize_signal(raw_data)
    
    # Step 3: Estimate frequency (unused later - red herring)
    dominant_freq = estimate_dominant_frequency(normalized_signal)
    
    # Step 4: Segment into frames
    segmented_frames = segment_into_frames(normalized_signal)
    
    # Step 5: Process each frame
    processed_frames = []
    for f in segmented_frames:
        processed_frames.append(f)  # Just pass through; actual processing done in analyze_signal
    
    # Step 6: Analyze full signal stream
    final_diagnostic = analyze_signal(processed_frames)
    
    # Output target result
    print(f"Target result: {final_diagnostic}")