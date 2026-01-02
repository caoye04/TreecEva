import math

# System configuration constants (some irrelevant)
default_threshold = 0.75
sampling_rate = 44100
max_amplitude = 32767
noise_floor_db = -96

def generate_wave(frequency, duration):
    # Irrelevant function - not used in main logic
    return [math.sin(2 * math.pi * frequency * t / sampling_rate) for t in range(int(duration * sampling_rate))]

def analyze_peaks(signal_chunk):
    # Dead-end analysis path - never called
    peak_count = 0
    for i in range(1, len(signal_chunk) - 1):
        if signal_chunk[i] > signal_chunk[i-1] and signal_chunk[i] > signal_chunk[i+1]:
            peak_count += 1
    return peak_count

def filter_noise(raw_samples, noise_gate=0.01):
    # Only this function is actually used
    return [x for x in raw_samples if abs(x) > noise_gate]

def apply_envelope(signal_data, attack=0.1, release=0.3):
    # Unused audio envelope function - red herring
    length = len(signal_data)
    envelope = [0.0] * length
    for i in range(length):
        if i < attack * length:
            envelope[i] = i / (attack * length)
        elif i > length * (1 - release):
            envelope[i] = 1 - ((i - (1 - release) * length) / (release * length))
        else:
            envelope[i] = 1.0
    return [signal_data[i] * envelope[i] for i in range(length)]

def compute_entropy(values):
    # Misleading statistical computation - not part of main flow
    from collections import Counter
    counts = Counter([round(v, 2) for v in values])
    total = sum(counts.values())
    entropy = -sum((count/total) * math.log2(count/total) for count in counts.values())
    return round(entropy, 4)

def process_signal(data_stream, scale_factor):
    # Core transformation - relevant logic
    scaled = [x * scale_factor for x in data_stream]
    squared = [x ** 2 for x in scaled]
    summed = sum(squared)
    normalized = math.sqrt(summed / len(squared)) if squared else 0
    return round(normalized, 6)

# Simulated sensor input data (real source)
sensor_readings = tuple([0.05, -0.03, 0.12, 0.08, -0.11, 0.07, 0.0, -0.09, 0.13])

# Irrelevant preprocessing steps
decibel_levels = [20 * math.log10(abs(x) + 1e-10) for x in sensor_readings]
clipped_data = [min(max(x, -0.1), 0.1) for x in sensor_readings]

total_energy = sum([x**2 for x in clipped_data])
efficiency_ratio = total_energy / (len(clipped_data) * 0.01) if total_energy > 0 else 0

# Main processing pipeline begins here
filtered_data = filter_noise(list(sensor_readings), noise_gate=0.05)

# Multiple candidate calibration factors - only one used
calibration_lookup = {
    'mode_a': 1.7,
    'mode_b': 2.3,
    'active': 2.15  # This one will be used
}

calibration_factor = calibration_lookup['active']

reference_magnitude = math.sqrt(sum([x**2 for x in filtered_data]))
baseline_offset = sum(filtered_data) / len(filtered_data) if filtered_data else 0

# Apply secondary filtering based on phase (redundant but looks important)
phase_shifted = []
for idx, val in enumerate(filtered_data):
    adjusted = val - baseline_offset
    phase_compensated = adjusted * math.cos(math.pi * idx / 4)
    phase_shifted.append(phase_compensated)

# Final decision point
if len(filtered_data) >= 4:
    temp_buffer = [x * 1.01 for x in phase_shifted]  # Minor correction
    processed_clean = [x for x in temp_buffer if x != 0]
    
    # Nested conditional with decoy operations
    if sum(processed_clean) > 0:
        inverted = [1/x if x != 0 else 0 for x in processed_clean]
        harmonic_mean = len(inverted) / sum(inverted) if all(x != 0 for x in inverted) else 0
        
        # Actual key computation happens here
        final_output = process_signal(filtered_data, calibration_factor)
        
        # Dead-end branch that looks consequential
        if harmonic_mean > 2.0:
            final_output *= 0.9
        elif harmonic_mean < 0.5:
            final_output += 0.1
        
    else:
        final_output = -1.0
else:
    final_output = 0.0

# Decoy output variables
debug_snapshot = {
    'raw_count': len(sensor_readings),
    'filtered_count': len(filtered_data),
    'peak_to_avg': max(filtered_data, default=0) / reference_magnitude if reference_magnitude else 0,
    'computed_entropy': compute_entropy(filtered_data)
}

# Output the target result
print(f"Result: {final_output}")