import math

def generate_wave_pattern(frequency, phase, length):
    return [math.sin(2 * math.pi * (i * frequency + phase)) for i in range(length)]

def calculate_interference(signal_x, signal_y):
    interference = []
    for x, y in zip(signal_x, signal_y):
        interference.append(x * y)
    return interference

def compute_envelope_magnitude(wave):
    # Irrelevant helper function (dead code path)
    return sum(abs(val) for val in wave if val > 0.5)

def main():
    sample_length = 100
    base_freq = 0.1
    phase_offset_a = 0.25
    phase_offset_b = 0.75

    # Generate two wave patterns with different phases
    pattern_a = generate_wave_pattern(base_freq, phase_offset_a, sample_length)
    pattern_b = generate_wave_pattern(base_freq, phase_offset_b, sample_length)

    # Calculate constructive and destructive interference
    interference_result = calculate_interference(pattern_a, pattern_b)

    # Compute aggregate metrics
    total_energy = sum(val**2 for val in interference_result)
    peak_amplitude = max(interference_result) - min(interference_result)

    # Misleading intermediate calculations
    dummy_sum = 0
    for i, val in enumerate(interference_result):
        if i % 10 == 0:
            dummy_sum += val * math.cos(i)

    # Slice analysis: middle segment of interference
    mid_segment = interference_result[sample_length//4 : 3*sample_length//4]
    avg_mid = sum(mid_segment) / len(mid_segment)

    # Key computation: net phase shift based on zero-crossing approximation
    zero_crossings = 0
    for i in range(1, len(interference_result)):
        if interference_result[i-1] < 0 < interference_result[i] or interference_result[i-1] > 0 > interference_result[i]:
            zero_crossings += 1

    expected_crossings = 2 * base_freq * sample_length  # Theoretical for doubled frequency
    phase_deviation = abs(expected_crossings - zero_crossings) * 0.5

    # Final variable of interest
    net_phase_shift = int(round(phase_deviation * 100))

    # Print required result
    print(f"Result: {net_phase_shift}")

    # Unused variables to increase cognitive load
    normalization_factor = math.sqrt(total_energy) if total_energy else 1
    coherence_score = dummy_sum / (sample_length / 10 + 1)

if __name__ == "__main__":
    main()