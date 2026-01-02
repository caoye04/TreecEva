import math

# Simulated sensor data processing with diagnostic analysis
def acquire_signal(raw_intensity, noise_floor=0.05):
    amplified = raw_intensity * 3.7
    filtered = amplified - noise_floor * 2.1
    return filtered

# Irrelevant transformation - distractor
def spectral_enhance(data_list):
    return [math.sin(x / 10) for x in data_list if x > 1]

# Unused function - red herring
def legacy_calibrate(x):
    return (x + 0.5) ** 2 if x < 5 else x * 0.9

# Core processing pipeline
raw_frames = [12, 15, 10, 18, 22, 8, 14]
baseline_shift = 0.8
offset_log = []

for i, frame in enumerate(raw_frames):
    adjusted = frame - baseline_shift
    if i % 2 == 0:
        adjusted *= 1.1
    else:
        adjusted *= 0.95
    offset_log.append(adjusted)

# Apply signal acquisition on transformed frames
temp_buffer = []
for val in offset_log:
    acquired = acquire_signal(val)
    temp_buffer.append(acquired)

# Misleading intermediate calculation - decoy result
aggregate_power = sum([x**2 for x in temp_buffer]) / len(temp_buffer)
suspicious_metric = aggregate_power * 0.03  # Dead-end computation

# Signal conditioning using list comprehension and zip
envelope = [abs(x) for x in temp_buffer]
scaled_envelope = [x * 0.75 for x in envelope]
modulation_indices = [i for i, x in enumerate(scaled_envelope) if x > 10]

# Frame pairing via zip - relevant for later analysis
paired_frames = list(zip(scaled_envelope[::2], scaled_envelope[1::2]))
energy_pairs = []
for a, b in paired_frames:
    energy = math.sqrt(a**2 + b**2)
    if energy > 12:
        energy_pairs.append(energy * 0.85)
    else:
        energy_pairs.append(energy * 1.05)

# Decoy statistical analysis
mean_energy = sum(energy_pairs) / len(energy_pairs)
variance_proxy = sum([(x - mean_energy)**2 for x in energy_pairs]) / len(energy_pairs)
entropy_approx = math.log(variance_proxy + 1)  # Not used

# Actual signal processing path
processed_frames = []
for i, val in enumerate(energy_pairs):
    if i in modulation_indices:  # Cross-reference with earlier list
        processed_frames.append(val * 1.2)
    else:
        processed_frames.append(val * 0.88)

# Diagnostic engine
threshold_map = {0: 9.5, 1: 10.2, 2: 9.8, 3: 10.5}
def analyze_signal(signal_list):
    total_weight = 0.0
    for idx, reading in enumerate(signal_list):
        base_weight = reading * 0.1
        if idx in threshold_map:
            if reading > threshold_map[idx]:
                total_weight += base_weight * 1.3
            else:
                total_weight += base_weight * 0.7
        else:
            total_weight += base_weight * 1.0
    return int(total_weight)  # Final diagnostic code

# Critical execution point
final_diagnostic = analyze_signal(processed_frames)
print(f"Result: {final_diagnostic}")