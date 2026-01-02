import math

# Irrelevant signal constants (distractors)
BASE_FREQUENCY = 440.0
HARMONIC_TOLERANCE = 0.02
REFERENCE_PHASE = 1.57
MAX_ITERATIONS = 100

# Real working parameters
data_stream = [3, 7, 2, 8, 4, 6, 5]
scaling_factor = 1.5
correction_offset = -0.25

# Dead function - looks important but unused in final path
def legacy_filter(x):
    return [val for val in x if val > sum(x) / len(x)]

# Another red herring: complex frequency estimator (never called)
def estimate_tone(signal):
    total = 0.0
    for s in signal:
        total += math.sin(s * REFERENCE_PHASE)
    return total / len(signal)

# Decoy accumulator with misleading intermediate result
shadow_accumulator = 0
for i in range(len(data_stream)):
    shadow_accumulator += data_stream[i] * (i % 3 + 1)

# Actual processing begins here
weighted_values = []
for idx, value in enumerate(data_stream):
    weight = scaling_factor * (idx + 1) ** 0.5
    adjusted = value * weight + correction_offset
    weighted_values.append(adjusted)

# Simulated preprocessing step with conditional expression
preprocessed = [
    x * 1.1 if x > 6.0 else (x * 0.9 if x < 4.0 else x)
    for x in weighted_values
]

# Introduce bit manipulation red herring (unused)
event_flags = 0
for val in preprocessed:
    if int(abs(val)) & 1:
        event_flags |= 2
    if val > 5.0:
        event_flags |= 4

# Simulate noise floor adjustment (irrelevant to final result)
noise_floor = sum(preprocessed) * 0.01
filtered_signal = [x - noise_floor for x in preprocessed]

# Dummy transformation matrix (looks computational heavy but unused)
transform_matrix = [
    [math.cos(i * j * 0.1) for j in range(3)] 
    for i in range(3)
]

# Core logic disguised among distractions
intermediate_sum = sum(filtered_signal)
penalty_factor = len([x for x in filtered_signal if x < 0]) * 0.5
adjusted_sum = intermediate_sum - penalty_factor

# Conditional expression used in critical path
scaling_decision = 1.05 if adjusted_sum > 30 else 0.95
raw_diagnostic = adjusted_sum * scaling_decision

# Final analysis function with decoy logic inside
def analyze_signal(signal_chunk):
    base_metric = sum(signal_chunk) / len(signal_chunk)
    
    # Misleading complexity: FFT-like but fake
    fake_spectrum = []
    for k in range(4):
        re = im = 0
        for n, s in enumerate(signal_chunk):
            angle = 2 * math.pi * k * n / len(signal_chunk)
            re += s * math.cos(angle)
            im += s * math.sin(angle)
        fake_spectrum.append(math.sqrt(re*re + im*im))
    
    # This part is actually irrelevant
    spectral_entropy = 0.0
    spec_sum = sum(fake_spectrum)
    if spec_sum > 0:
        for amp in fake_spectrum:
            prob = amp / spec_sum
            if prob > 0:
                spectral_entropy -= prob * math.log(prob)
    
    # The real answer depends only on base_metric and fixed offset
    return int(base_metric + 7.3)  # deterministic truncation + offset

# Critical statement
processed_data = [math.log(x + 10) for x in filtered_signal]
final_diagnostic = analyze_signal(processed_data)

print(f"Result: {final_diagnostic}")