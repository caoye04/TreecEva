import itertools

# Simulated sensor data processing pipeline for aerospace telemetry
raw_readings = [0.78, 0.63, 0.81, 0.59, 0.91, 0.67, 0.74, 0.62]
baseline_offset = 0.65
noise_floor = 0.08
calibration_sequence = (1.02, 0.98, 1.01, 0.99)

# Irrelevant calibration weights (distractor)
weights_matrix = [[0.1, 0.2], [0.3, 0.4]]
weight_sum = sum(sum(row) for row in weights_matrix)  # Dead computation

# Misleading signal smoothing (unused path)
def smooth_signal(data, factor=0.3):
    result = [data[0]]
    for i in range(1, len(data)):
        result.append(result[-1] * factor + data[i] * (1 - factor))
    return result

# Fake frequency analysis (never called)
def compute_harmonics(signal):
    harmonics = []
    for i in range(1, 5):
        harmonics.append(sum(itertools.repeat(signal[j % len(signal)] * i, 1))[0] for j in range(4))
    return [sum(h) for h in harmonics]

# Actual preprocessing
adjusted_readings = [x - baseline_offset for x in raw_readings]
filtered_readings = [x for x in adjusted_readings if abs(x) > noise_floor]
scaled_readings = [x * calib for x, calib in zip(filtered_readings, itertools.cycle(calibration_sequence))]

# Complex frame builder with tuple unpacking and filtering
def build_frames(data):
    frames = []
    iterator = iter(data)
    try:
        while True:
            a, b, c = next(iterator), next(iterator), next(iterator)
            if a + b > c:
                frames.append((a, b, c, (a**2 + b**2)**0.5))
    except StopIteration:
        pass
    return frames

processed_frames = build_frames(scaled_readings)

# Decoy transformation chain
temp_amplitudes = [max(frame[:-1]) for frame in processed_frames if len(frame) == 4]
rolling_avg = 0
for i, amp in enumerate(temp_amplitudes):
    rolling_avg = (rolling_avg * i + amp) / (i + 1) if i > 0 else amp
threshold_check = rolling_avg > 0.15  # Misleading indicator

# Real diagnostic logic buried in distractions
def analyze_signal(frames):
    valid_count = 0
    hypotenuse_sum = 0.0
    ratio_accum = 0.0
    
    # Red herring variables
    dummy_state = {'flag': False, 'count': 0}
    debug_trace = []
    
    for frame in frames:
        a, b, c, hyp = frame
        if c <= hyp:  # Geometric validity
            valid_count += 1
            hypotenuse_sum += hyp
            if a > 0 and b > 0:
                ratio_accum += (a + b) / hyp
                
        # Distractor logic
        if a < 0:
            dummy_state['flag'] = True
        debug_trace.append(len(dummy_state))  # Useless logging

    # Core calculation disguised among side effects
    if valid_count == 0:
        return 0
    
    avg_ratio = ratio_accum / valid_count
    penalty = len(debug_trace) * 0.01  # Minor obfuscation
    intermediate = (hypotenuse_sum * avg_ratio) - penalty
    
    # Final non-linear transformation
    return int(intermediate * 100) ^ 12345  # Bitwise mix to hide result

final_diagnostic = analyze_signal(processed_frames)
print(f"Target result: {final_diagnostic}")