import math

def generate_wave_sequence(length, freq, phase=0):
    # Generates a list of wave values - some of which are unused later (distractor)
    return [math.sin(2 * math.pi * freq * (i / length) + phase) for i in range(length)]

def count_peaks(signal):
    # Counts local maxima in signal (used only for intermediate distraction)
    peaks = 0
    for i in range(1, len(signal) - 1):
        if signal[i-1] < signal[i] > signal[i+1]:
            peaks += 1
    return peaks

def calculate_interference(seq1, seq2):
    # Main logic: computes phase difference based on overlapping high-amplitude points
    matched_phases = []
    temp_buffer = []  # Unused tracking (distractor)
    
    for idx, (a, b) in enumerate(zip(seq1, seq2)):
        if abs(a) > 0.7 and abs(b) > 0.7:  # High amplitude coincidence
            phase_diff = abs(math.asin(a) - math.asin(b))
            matched_phases.append(phase_diff)
        else:
            # Dead code path: never executed due to conditions above, but looks relevant
            temp_buffer.append(idx * 0.1)  # Misleading accumulation
    
    # Real computation: average phase shift from matched points
    if matched_phases:
        avg_shift = sum(matched_phases) / len(matched_phases)
    else:
        avg_shift = 0
    
    # Additional irrelevant transformation (not used)
    normalized = [x / (avg_shift + 1e-5) for x in matched_phases]  # Distractor
    
    return int(round(avg_shift * 1000))  # Discretized result

# Generate two wave patterns with known characteristics
pattern_a = generate_wave_sequence(100, freq=0.1, phase=0.5)
pattern_b = generate_wave_sequence(100, freq=0.1, phase=1.0)

# Irrelevant pre-processing steps (distraction)
peak_count_a = count_peaks(pattern_a)
peak_count_b = count_peaks(pattern_b)
overlap_score = sum(1 for x, y in zip(pattern_a, pattern_b) if x * y > 0)  # Not used

# Core interference calculation
net_phase_shift = calculate_interference(pattern_a, pattern_b)

# Print final target result
print(f"Result: {net_phase_shift}")