import itertools

# Simulated sensor data processing with diagnostic analysis
def generate_wave_components(base_freq, harmonics):
    return [base_freq * (i + 1) for i in range(harmonics)]

def apply_damping(signal, damp_factor):
    return [s * (damp_factor ** i) for i, s in enumerate(signal)]

def detect_anomaly(peaks, threshold=0.75):
    return len([p for p in peaks if p > threshold]) > 2

# Irrelevant helper - decoy function (dead code path)
def deprecated_filter(x):
    return [val for val in x if val % 2 == 0]

# Unused transformation chain
def transform_sequence(seq):
    shifted = [(x >> 2) ^ 3 for x in seq]
    inverted = [~x & 0xFF for x in shifted]
    return inverted

# Signal pre-processing with red herring variables
raw_input_stream = [18, 24, 36, 48, 60, 72]
scaling_factor = 0.85
offset_correction = 1.2

# Distractor: complex-looking but unused computation
entropy_score = sum((x & (x-1)) == 0 for x in raw_input_stream) * 3.14159
duplicate_check = len(raw_input_stream) != len(set(raw_input_stream))

# Real signal construction
frequencies = generate_wave_components(6, 5)
amplitudes = apply_damping([1.0, 0.8, 0.6, 0.4, 0.2], scaling_factor)

# Combine into composite wave (relevant)
composite_wave = []
for f, a in zip(frequencies, amplitudes):
    composite_wave.append(a * (f % 13))

# Intermediate transformation
processed_waves = []
for i, val in enumerate(composite_wave):
    if i % 2 == 0:
        processed_waves.append(int(val * 10) | 0b1010)
    else:
        processed_waves.append(int(val * 7) & 0b1111)

# Red herring list comprehension with no downstream use
even_more_features = [
    (x ** 0.5) + (i * 0.1) for i, x in enumerate(composite_wave)
    if x > 2.5
]

# Unused recursive filter (decoy)
def recursive_denoise(data, level=0):
    if level >= 3 or len(data) < 2:
        return data
    mid = len(data) // 2
    return recursive_denoise(data[:mid], level + 1) + recursive_denoise(data[mid:], level + 1)

# Critical analysis function
threshold_reference = [5.2, 6.1, 4.8, 7.3]

def analyze_signal(wave_data):
    # Bit manipulation mixed with arithmetic
    bit_analysis = sum((x ^ 0b101) & 0xF for x in wave_data)
    
    # Conditional expression chain
    base_score = bit_analysis if bit_analysis > 30 else bit_analysis * 2
    
    # Use of itertools: group consecutive even values
    grouped = [list(g) for k, g in itertools.groupby(wave_data, key=lambda x: x % 2 == 0) if k]
    group_count = len(grouped)
    
    # Comparison and logical combination
    has_large_group = any(len(g) >= 3 for g in grouped)
    magnitude_test = sum(wave_data) > 80
    
    # Final logic with short-circuit evaluation
    adjustment = 17 if (has_large_group or magnitude_test) and not (len(grouped) == 1) else 5
    
    # Key result calculation
    intermediate = (base_score + group_count * 8) - (adjustment * 2)
    
    # Additional red herring variables
    noise_floor = sum(1 for x in wave_data if x in (0, 1, 15))
    peak_density = len([x for x in wave_data if x > 10]) / (len(wave_data) or 1)
    
    final_diagnostic = abs(intermediate - 45) * 3
    
    # Return only one value despite multiple computations
    return final_diagnostic

# Execution point of interest
final_diagnostic = analyze_signal(processed_waves)

# Print required output
print(f"Result: {final_diagnostic}")