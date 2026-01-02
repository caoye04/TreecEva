import math

# Simulated sensor data processing with embedded diagnostics
def collect_sensor_data():
    raw_signals = [i * 0.5 + math.sin(i / 3) for i in range(20)]
    noise_floor = 0.25
    filtered = []
    for x in raw_signals:
        if abs(x) > noise_floor:
            filtered.append(x * 1.2)
    return filtered

# Irrelevant helper - distractor
def compute_entropy(data):
    total = 0.0
    for x in data:
        if x != 0:
            total -= x * math.log(abs(x))
    return total

# Data transformation with multiple steps and red herrings
def preprocess_frame(frame, gain=1.1, normalize=True):
    amplified = [gain * x for x in frame]
    if normalize:
        max_val = max(abs(min(amplified)), abs(max(amplified)))
        if max_val > 0:
            amplified = [x / max_val for x in amplified]
    # Dead code path - misleading
    if False:
        amplified = [math.tanh(x) for x in amplified]
    return amplified

# Complex conditional logic with early exits
def validate_frame_integrity(frame):
    if len(frame) == 0:
        return False
    checksum = sum(frame[i] * (i + 1) for i in range(len(frame)))
    if checksum < -10 or checksum > 10:
        return False
    # Additional validation
    zero_crossings = 0
    for i in range(1, len(frame)):
        if frame[i-1] * frame[i] < 0:
            zero_crossings += 1
    return zero_crossings % 2 == 1

# Main processing pipeline
def assemble_frames(signals):
    frames = []
    temp_buffer = []
    for idx, val in enumerate(signals):
        temp_buffer.append(val)
        if (idx + 1) % 4 == 0:
            frames.append(temp_buffer.copy())
            temp_buffer.clear()
    # Leftover handling - never reached due to length
    if temp_buffer:
        frames.append(temp_buffer)
    return frames

# Decoy function - looks important but unused
def compress_data(frames):
    compressed = []
    for f in frames:
        comp = []
        for a, b in zip(f[::2], f[1::2]):
            comp.append((a + b) / 2)
        compressed.append(comp)
    return compressed

# Critical analysis function with distractors
def analyze_signal(frames):
    diagnostics = []n    frame_ranks = []
    
    for i, f in enumerate(frames):
        # Real computation
        energy = sum(x**2 for x in f)
        phase_shift = sum(f[j] - f[j-1] for j in range(1, len(f)))
        
        # Distractor variables
        dummy_metric = math.cos(energy) * phase_shift
        placeholder = [abs(x) for x in f if x > 0.5]
        rank_score = len(placeholder) * energy
        
        frame_ranks.append((i, rank_score))
        
        # Only every second frame contributes to real diagnostic
        if i % 2 == 1:
            diagnostics.append(energy - phase_shift)
    
    # Sorting - irrelevant to final result
    frame_ranks.sort(key=lambda x: x[1], reverse=True)
    
    # Real final computation
    base = sum(diagnostics)
    adjustment = 0
    # Modular arithmetic red herring
    for d in diagnostics:
        adjustment += int(abs(d)) % 7
    
    # Final diagnostic depends only on base
    final_diagnostic = int(base * 100)  # Scale for precision
    
    # Dead assignment - misleading
    final_diagnostic = final_diagnostic + adjustment - adjustment
    
    return final_diagnostic

# Orchestration with decoy variables
if __name__ == "__main__":
    # Collect raw input
    signal_input = collect_sensor_data()  # 20 elements
    
    # Preprocess each sample individually - distractor chain
    processed_samples = []
    for s in signal_input:
        processed_samples.append(preprocess_frame([s]))  # Trivial case
    
    # Assemble into frames - actual relevant step
    raw_frames = assemble_frames(signal_input)  # 5 frames of 4 elements
    
    # Validate frames - side check with early returns
    valid_frames = []
    validation_log = []
    for f in raw_frames:
        is_valid = validate_frame_integrity(f)
        validation_log.append(is_valid)
        if is_valid:
            valid_frames.append(f)
    
    # Reconstruct using enumerate and zip - looks important
    reconstructed = []
    indices = [i for i, _ in enumerate(valid_frames)]
    for idx, frame in enumerate(valid_frames):
        offset = indices[idx] * 0.1
        adjusted = [x + offset for x in frame]
        reconstructed.append(adjusted)
    
    # Final analysis on original frames (not reconstructed!)
    final_diagnostic = analyze_signal(raw_frames)
    
    # Print required result
    print(f"Target result: {final_diagnostic}")