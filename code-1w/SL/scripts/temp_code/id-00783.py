import math

def analyze_pattern_sequence(sequence):
    magnitude = 0
    phase_accum = 0
    temp_buffer = []
    
    for i in range(len(sequence)):
        if i % 2 == 0:
            magnitude += sequence[i] ** 2
        else:
            phase_accum += math.sin(sequence[i])
        
        # Irrelevant tracking
        temp_buffer.append(magnitude * 0.1)
    
    normalized_mag = math.sqrt(magnitude) if magnitude > 0 else 0
    return normalized_mag, phase_accum

def generate_waveform_segments(freq_base, count):
    segments = []
    offset_correction = 0.5
    
    for i in range(count):
        val = freq_base * math.cos(i * math.pi / 4) + offset_correction
        segments.append(val)
    
    # Dead code path - never used
    if len(segments) > 10:
        segments = segments[:10]
    
    return segments

def calculate_interference(pat1, pat2):
    combined = []
    shift_log = []
    total_variance = 0
    
    for a, b in zip(pat1, pat2):
        diff = abs(a - b)
        total_variance += diff ** 2
        shift_log.append(diff * 0.75)
    
    avg_shift = total_variance / len(pat1) if pat1 else 0
    
    # Secondary computation that looks relevant but isn't used
    coherence_score = sum(1 for s in shift_log if s < 1.0)
    
    return avg_shift

def main():
    raw_input_data = [0.5, 1.2, -0.3, 0.8, 1.6, -1.1, 0.9, 0.4]
    
    # Process subset using slicing
    segment_primary = raw_input_data[1:6:2]  # [1.2, 0.8, -1.1]
    segment_secondary = raw_input_data[::-1][:5]  # Reverse and take first 5
    
    # First analysis with partial data
    mag_x, phase_x = analyze_pattern_sequence(segment_primary)
    
    # Generate auxiliary waveform
    aux_wave = generate_waveform_segments(freq_base=2.5, count=5)
    
    # Another irrelevant intermediate
    dummy_metric = sum(x**2 for x in aux_wave) / len(aux_wave)
    
    # Final interference calculation inputs
    pattern_a = [math.tanh(x) for x in segment_primary]
    pattern_b = [math.tanh(x) for x in aux_wave]
    
    # Key statement
    net_phase_shift = calculate_interference(pattern_a, pattern_b)
    
    # Print required result
    print(f"Result: {net_phase_shift}")
    
    return net_phase_shift

if __name__ == "__main__":
    main()