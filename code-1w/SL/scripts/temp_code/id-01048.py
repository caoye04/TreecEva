import math

def generate_wave_sequence(frequency, duration, sample_rate=10):
    timesteps = [i / sample_rate for i in range(int(duration * sample_rate))]
    return [math.sin(2 * math.pi * frequency * t) for t in timesteps]

def extract_peaks(signal, threshold=0.5):
    peaks = []
    for i in range(1, len(signal) - 1):
        if signal[i] > threshold and signal[i-1] < signal[i] > signal[i+1]:
            peaks.append(i)
    return peaks

def align_sequences(seq1, seq2):
    # Misleading function - never used in final computation
    min_len = min(len(seq1), len(seq2))
    return [(seq1[i], seq2[i]) for i in range(min_len)]

def calculate_interference(pat_a, pat_b):
    interference = 0
    phase_accumulator = 0.0
    amplitude_tracker = []
    
    for i, (a, b) in enumerate(zip(pat_a, pat_b)):
        product = a * b
        phase_shift = math.atan2(a, b) if b != 0 else math.pi / 2
        phase_accumulator += phase_shift
        
        if i % 3 == 0:
            smoothed = (a + b) / 2
            amplitude_tracker.append(smoothed * 0.5)  # Distractor: not used later
        
        if product > 0.25:
            interference += 1
        elif product < -0.25:
            interference -= 1
    
    # Irrelevant aggregation
    avg_amplitude = sum(amplitude_tracker) / len(amplitude_tracker) if amplitude_tracker else 0
    dummy_metric = math.log(1 + abs(avg_amplitude))
    
    return int(abs(phase_accumulator)) + interference

# Main simulation setup
frequency_a = 2.5
frequency_b = 3.0
duration = 4.0

pattern_a = generate_wave_sequence(frequency_a, duration)
pattern_b = generate_wave_sequence(frequency_b, duration)

# Extract features (distractor step - not used in final calculation)
peaks_a = extract_peaks(pattern_a)
peaks_b = extract_peaks(pattern_b)

# Simulate alignment (unused)
aligned_data = align_sequences(pattern_a, pattern_b)

# Core computation
net_phase_shift = calculate_interference(pattern_a, pattern_b)

# Additional noise variables
normalization_factor = math.sqrt(len(pattern_a))
effective_bandwidth = frequency_a * frequency_b / normalization_factor
scaling_constant = sum(1 for x in pattern_a if x > 0) // 10

Result: net_phase_shift