import math

# Simulated sensor data preprocessing for a biomedical device
def acquire_signal(baseline, noise_factor, samples):
    signal = []
    for i in range(samples):
        raw = baseline + math.sin(i * 0.5) * 3.2
        noisy = raw + (noise_factor * (i % 7)) / 4.0
        signal.append(noisy)
    return signal[:samples]

# Irrelevant auxiliary function – dead code path (distractor)
def legacy_filter(data):
    filtered = []
    for x in data:
        if x > 2.0:
            filtered.append(x * 0.8)
    return filtered

# Signal envelope detection using RMS over windows
def compute_envelope(signal, window_size):
    envelope = []
    for i in range(0, len(signal) - window_size + 1, window_size // 2):
        segment = signal[i:i + window_size]
        rms = math.sqrt(sum([x**2 for x in segment]) / len(segment))
        envelope.append(rms)
    return envelope

# Spectral centroid approximation (simplified)
def spectral_centroid(magnitudes):
    total_power = sum(magnitudes)
    if total_power == 0:
        return 0.0
    weighted_sum = sum(i * mag for i, mag in enumerate(magnitudes))
    return weighted_sum / total_power

# Main processing pipeline
baseline_offset = 1.5
acquisition_noise = 0.9
sensor_samples = 64

raw_data = acquire_signal(baseline_offset, acquisition_noise, sensor_samples)

# Apply moving average smoothing (redundant but plausible)
smoothed = []
window_len = 4
for i in range(len(raw_data)):
    start = max(0, i - window_len + 1)
    segment = raw_data[start:i+1]
    smoothed.append(sum(segment) / len(segment))

# Segment into analysis blocks
block_size = 8
segments = [smoothed[i:i + block_size] for i in range(0, len(smoothed), block_size)]

# Compute time-domain features per segment
td_features = []
for seg in segments:
    mean_val = sum(seg) / len(seg)
    variance = sum((x - mean_val) ** 2 for x in seg) / len(seg)
    zero_crossings = sum(1 for i in range(1, len(seg)) if seg[i] * seg[i-1] < 0)
    td_features.append({'mean': mean_val, 'variance': variance, 'zero_crossings': zero_crossings})

# Frequency domain approximation via FFT-like binning (simulated)
def simulate_frequency_binning(time_block):
    bins = [0] * 4
    for j, sample in enumerate(time_block):
        phase = math.sin(j * 0.785)
        magnitude = abs(sample * phase)
        bin_idx = j // 2 % 4
        bins[bin_idx] += magnitude
    return bins

frequency_representations = []
for s in segments:
    freq_bins = simulate_frequency_binning(s)
    frequency_representations.append(freq_bins)

# Extract spectral centroids
spectral_analysis = [spectral_centroid(fb) for fb in frequency_representations]

# Combine time and frequency features (unused fusion – distractor)
comprehensive_features = []
for (t, f) in zip(td_features, spectral_analysis):
    fused_score = (t['mean'] * 0.3) + (t['variance'] * 0.4) + (f * 0.3)
    comprehensive_features.append(fused_score)

# Unused intermediate result (misleading)
aggregate_fusion = sum(comprehensive_features) / len(comprehensive_features) if comprehensive_features else 0

# Processed segments used in final analysis
processed_segments = []
for idx, (seg, sc) in enumerate(zip(segments, spectral_analysis)):
    # Slice central portion of each segment
    center_slice = seg[len(seg)//4 : len(seg)*3//4]
    avg_center = sum(center_slice) / len(center_slice)
    # Use enumerate to add positional weight
    position_weight = 1.0 + (idx * 0.1)
    weighted_centroid = sc * position_weight
    processed_segments.append({
        'centroid': weighted_centroid,
        'center_avg': avg_center,
        'length': len(center_slice)
    })

# Decoy function that is never called (dead code)
def calibrate_system(ref_data):
    adjustment = 0
    for val in ref_data:
        adjustment += math.log(abs(val) + 1) * 0.1
    return adjustment

# Another red herring: irrelevant bit manipulation on indices
bitwise_flag = 0
for i, seg in enumerate(processed_segments):
    temp_flag = (i << 2) ^ int(seg['center_avg'])
    bitwise_flag ^= temp_flag

# Final diagnostic computation
threshold_reference = 2.75
def analyze_signal(segments):
    total_response = 0.0
    for s in segments:
        # Primary logic: combine centroid and center average with non-linear scaling
        if s['centroid'] > threshold_reference:
            contribution = s['centroid'] * math.log(s['center_avg'] + 2)
        else:
            contribution = s['center_avg'] * math.sqrt(s['centroid'] + 1)
        total_response += contribution
    # Final transformation
    final_index = total_response * 0.85
    return int(final_index)  # Discrete diagnostic code

# Key execution point
final_diagnostic = analyze_signal(processed_segments)
print(f"Result: {final_diagnostic}")