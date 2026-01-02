import math

def generate_harmonic(frequency, phase, length=100):
    # Irrelevant signal generation function (dead end)
    return [math.sin(2 * math.pi * frequency * t / length + phase) for t in range(length)]

def apply_window(signal, window_type='hann'):
    # Distractor: windowing function not used in final computation
    n = len(signal)
    if window_type == 'hann':
        return [signal[i] * 0.5 * (1 - math.cos(2 * math.pi * i / (n-1))) for i in range(n)]
    return signal

def compute_magnitude(spectrum):
    # Red herring: computes magnitude but not used in answer
    return [math.sqrt(r**2 + i**2) for r, i in spectrum]

def shift_phase(signal, radians):
    # Unused transformation (distractor)
    return [math.sin(math.asin(x) + radians) for x in signal if -1 <= x <= 1]

def extract_envelope(signal):
    # Decoy analysis path
    return [max(signal[:i+1]) - min(signal[:i+1]) for i in range(len(signal))]

def build_filter(order, cutoff_ratio):
    # Generates filter coefficients; only one is actually used
    if order == 3:
        return [cutoff_ratio * (0.5 - math.cos(2 * math.pi * k / (order+1))) for k in range(order+1)]
    else:
        return [1.0] * (order + 1)

def merge_filters(primary, secondary, mode='cascade'):
    # Complex-looking but irrelevant combination logic
    if mode == 'cascade':
        return [a * b for a, b in zip(primary, secondary)]
    return primary

def process_signal(kernel, data_chunk):
    # Core relevant function (heavily masked by noise)
    convolution = []
    padding = len(kernel) // 2
    padded_data = [0] * padding + data_chunk + [0] * padding
    
    for i in range(len(data_chunk)):
        weighted_sum = sum(padded_data[i+j] * kernel[j] for j in range(len(kernel)))
        convolution.append(weighted_sum)
    
    # Real processing continues: transform and threshold
    transformed = [abs(x) ** 1.5 for x in convolution]
    threshold = sum(transformed) / len(transformed) * 0.75
    filtered = [x for x in transformed if x > threshold]  # Critical filtering step
    
    # Final answer derived here
    result = sum(filtered) / len(filtered) if filtered else 0
    return round(result, 6)

# Irrelevant setup variables
sample_rate = 44100
frequency_bands = [250, 500, 1000, 2000]
tone_modulation = [generate_harmonic(f/10000, 0.1) for f in frequency_bands]

# Distractor data structures
analysis_pipeline = {
    'pre_emphasis': True,
    'frame_size': 2048,
    'hop_length': 512,
    'features': ['mfcc', 'spectral_centroid']
}

# Fake filter bank construction (only one component used)
coarse_filter = build_filter(3, 0.3)
fine_filter = build_filter(5, 0.15)
composite_filter = merge_filters(coarse_filter, fine_filter, 'cascade')

# Actual relevant filter (but hard to distinguish)
filter_bank = [0.25, 0.5, 0.25]  # Simple moving average kernel

# Signal with embedded pattern
base_sequence = [16, -8, 24, -12, 32, -16]
time_series = []
for val in base_sequence:
    time_series.extend([val] * 4)  # Expands to 24 elements

# Additional red herring operations
windowed_chunk = apply_window(time_series[:16], 'hann')
envelope = extract_envelope(time_series)
spectral_rep = [(math.cos(x), math.sin(x)) for x in time_series]
magnitudes = compute_magnitude(spectral_rep)

# Key execution point — only this matters
filtered_amplitude = process_signal(filter_bank, time_series)

# Output required format
print(f"Target result: {filtered_amplitude}")