import math

# Simulated sensor data processing with diagnostic pipeline
def collect_samples(duration, sample_rate=100):
    samples = []
    for t in range(0, int(duration * sample_rate)):
        time_point = t / sample_rate
        # Real signal component (5Hz sine wave)
        signal = math.sin(2 * math.pi * 5 * time_point)
        # Noise injection (irrelevant for final result)
        noise = 0.1 * math.sin(2 * math.pi * 57 * time_point)  # Power line interference sim
        samples.append(signal + noise)
    return samples

# Irrelevant auxiliary function (decoy)
def compute_entropy(data):
    histogram = [0] * 20
    for x in data:
        idx = int((x + 1.5) * 5)
        if 0 <= idx < 20:
            histogram[idx] += 1
    entropy = 0
    total = len(data)
    for count in histogram:
        if count > 0:
            p = count / total
            entropy -= p * math.log2(p)
    return round(entropy, 4)

# Signal preprocessing with red herrings
def preprocess(samples):
    filtered = []
    squared_buffer = []  # Distractor: used in dead code path
    cumulative_energy = 0.0

    for i, s in enumerate(samples):
        # Moving average filter (real processing)
        window_start = max(0, i - 4)
        avg = sum(samples[window_start:i+1]) / (i + 1 - window_start)
        
        # Dead code path - misleading energy accumulation
        sq_val = s * s
        squared_buffer.append(sq_val)
        if len(squared_buffer) > 10:
            squared_buffer.pop(0)
        if len(squared_buffer) == 10 and i % 20 == 0:
            temp_energy = sum(squared_buffer)
            cumulative_energy += temp_energy  # Never used

        filtered.append(avg)
    
    # Decoy transformation (never called in critical path)
    def enhance_resolution(data):
        enhanced = []
        for x in data:
            enhanced.append(x * 1.05 if x > 0 else x * 0.95)
        return enhanced

    return filtered

# Frame segmentation with enumerate and zip (required features)
def segment_frames(signal, frame_size=16):
    frames = []
    for i in range(0, len(signal), frame_size):
        frame = signal[i:i + frame_size]
        if len(frame) == frame_size:
            frames.append(frame)
    
    # Misleading frame quality scoring (distractor)
    quality_scores = []
    for j, f in enumerate(frames):
        variance = sum((x - sum(f)/len(f))**2 for x in f) / len(f)
        peak_to_peak = max(f) - min(f)
        score = (variance * 0.7) + (peak_to_peak * 0.3)  # Not used later
        quality_scores.append(score)
    
    # Use enumerate and zip together (required python idiom)
    indexed_frames = list(enumerate(frames))
    paired_frames = list(zip(frames[:-1], frames[1:]))  # For differential analysis (unused)
    
    # Return only cleaned frames, but computation above adds distraction
    return frames

# Critical analysis function (short-circuited by condition)
def analyze_frame_complexity(frame_batch):
    complexity_metrics = []
    for frame in frame_batch:
        zero_crossings = 0
        for k in range(1, len(frame)):
            if frame[k-1] < 0 <= frame[k] or frame[k-1] >= 0 > frame[k]:
                zero_crossings += 1
        # Frequency domain proxy
        freq_proxy = zero_crossings / len(frame)
        complexity_metrics.append(freq_proxy * 100)
    return complexity_metrics

# Final diagnostic - key function containing answer
def analyze_signal(processed_frames):
    # Only use first 5 complete frames (critical constraint)
    batch = processed_frames[:5]
    
    # Compute frame averages (actual relevant logic)
    frame_averages = []
    for f in batch:
        frame_averages.append(sum(f) / len(f))
    
    # Hidden pattern: alternating sign correction due to phase shift
    corrected = []
    for idx, val in enumerate(frame_averages):
        correction = -1 if idx % 2 == 1 else 1
        corrected.append(val * correction)
    
    # Key calculation: weighted sum based on position
    weights = [0.1, 0.2, 0.3, 0.4, 0.5]
    weighted_sum = 0.0
    for i in range(len(corrected)):
        weighted_sum += corrected[i] * weights[i]
    
    # Secondary transformation (distraction)
    transformed = math.tanh(weighted_sum) * 1000
    normalized = abs(transformed) % 100  # Red herring
    
    # Tertiary decoy using tuple unpacking (suggested paradigm)
    stats = (min(corrected), max(corrected), len(corrected))
    min_c, max_c, count = stats  # Unpacking - irrelevant
    spread = max_c - min_c  # Not used
    
    # Final result derived from raw weighted sum (answer hidden here)
    final_score = int(round(weighted_sum * 1000))  # Scale up for integer answer
    
    # Early return trap (not taken)
    if final_score < 0:
        return -final_score
    
    return final_score

# --- Execution Pipeline ---
raw_data = collect_samples(duration=0.64, sample_rate=100)  # 64 samples per frame * 5 frames + buffer

# Dead code branch (control flow distractor)
if len(raw_data) > 100:
    reshaped = [raw_data[i:i+32] for i in range(0, len(raw_data), 32)]
    transposed = list(zip(*[r + [0]*(32-len(r)) for r in reshaped]))
else:
    pass  # Continue normal flow

processed_signal = preprocess(raw_data)
frames = segment_frames(processed_signal, frame_size=16)
final_diagnostic = analyze_signal(frames)

# Output result as required
print(f"Result: {final_diagnostic}")