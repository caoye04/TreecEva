import itertools

# Simulated sensor data processing pipeline with diagnostic checks
raw_readings = [145, 256, 178, 99, 301, 212, 165, 88, 205]
threshold = 150
scaling_factor = 0.75
offset_correction = 12

# Irrelevant baseline metrics (distractor)
baseline_avg = sum(raw_readings) / len(raw_readings)
fluctuation_index = max(raw_readings) - min(raw_readings)
reading_count = len(raw_readings)

# Step 1: Apply scaling and offset correction (relevant)
corrected_readings = [(x * scaling_factor) + offset_correction for x in raw_readings]

# Step 2: Filter out low-amplitude noise below threshold (relevant)
filtered_readings = [val for val in corrected_readings if val > threshold]

# Step 3: Frame segmentation using windowing (relevant)
window_size = 3
strided_windows = [filtered_readings[i:i+window_size] for i in range(0, len(filtered_readings)-window_size+1)]

# Step 4: Compute moving RMS envelope (relevant)
rms_envelope = []
for window in strided_windows:
    squared_sum = sum(x ** 2 for x in window)
    rms = (squared_sum / len(window)) ** 0.5
    rms_envelope.append(round(rms, 3))

# Step 5: Identify peaks above dynamic threshold (relevant)
dynamic_threshold = sum(rms_envelope) / len(rms_envelope) * 1.1
peak_indices = [i for i, val in enumerate(rms_envelope) if val > dynamic_threshold]

# Step 6: Temporal clustering of peaks using gap analysis (relevant)
if peak_indices:
    clusters = [[peak_indices[0]]]
    for idx in peak_indices[1:]:
        if idx - clusters[-1][-1] <= 2:
            clusters[-1].append(idx)
        else:
            clusters.append([idx])
    dominant_cluster = max(clusters, key=len)
else:
    dominant_cluster = []

central_tendency = sum(dominant_cluster) / len(dominant_cluster) if dominant_cluster else 0

# Decoy signal transformation chain (dead code path - distractor)
def transform_signal(data, method='fft'):
    """Unused function - red herring"""
    if method == 'fft':
        return [sum(data[:len(data)//2]), sum(data[len(data)//2:])]
    elif method == 'wavelet':
        return [max(data), min(data), sum(data)/len(data)]
    return data

transformed = transform_signal(raw_readings, 'wavelet')
compression_ratio = 2.5
encoded_size = len(raw_readings) / compression_ratio
reconstructed = [x * 0.98 for x in raw_readings]  # Unused reconstruction

# Simulated frame processor with bit flag diagnostics (mixed relevant/distractor)
frame_diagnostics = []
for i, frame in enumerate(strided_windows):
    flag = 0
    if len(frame) == window_size:
        flag |= 1 << 0
    if rms_envelope[i] > dynamic_threshold:
        flag |= 1 << 1
    if i in peak_indices:
        flag |= 1 << 2
    if i % 2 == 0:
        flag |= 1 << 3  # Irrelevant timing flag
    if sum(frame) > 500:
        flag |= 1 << 4  # Energy threshold (partially relevant)
    frame_diagnostics.append(flag)

# Diagnostic aggregation via bitwise consensus (relevant)
consensus_flag = 0
for flag in frame_diagnostics:
    consensus_flag ^= flag  # XOR accumulation (bit diffusion)

# Extract only bits 0, 1, and 2 as valid indicators (mask out higher bits)
valid_mask = 0b111
masked_consensus = consensus_flag & valid_mask

# Process frames through statistical lens (relevant)
processed_frames = []
for env_val, flag in zip(rms_envelope, frame_diagnostics):
    score = env_val * ((flag & 0b11) + 1)  # Weight by lower two flag bits
    processed_frames.append(score)

# Final diagnostic engine (key logic)
def analyze_signal(frames):
    if not frames:
        return 0.0
    avg_frame = sum(frames) / len(frames)
    peak_response = max(frames)
    stability_ratio = (min(frames) / avg_frame) if avg_frame != 0 else 0
    # Composite metric with weighted combination
    diagnostic_score = (avg_frame * 0.4) + (peak_response * 0.35) + (stability_ratio * 100 * 0.25)
    return round(diagnostic_score, 4)

# Execution point of interest
final_diagnostic = analyze_signal(processed_frames)

# Print result for verification
print(f"Result: {final_diagnostic}")