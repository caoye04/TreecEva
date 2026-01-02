import itertools

# System health monitoring simulation with red herrings and complex data flow

def analyze_signal(samples):
    filtered = [x for x in samples if abs(x) > 0.5]
    return sum(filtered[i] * (-1)**i for i in range(len(filtered)))

def compute_entropy(data):
    from math import log2
    freq = {}
    for d in data:
        freq[d] = freq.get(d, 0) + 1
    entropy = 0
    total = len(data)
    for count in freq.values():
        p = count / total
        entropy -= p * log2(p)
    return round(entropy, 4)

def generate_waveform(phase, resolution=8):
    import math
    return [round(math.sin(phase + 2*math.pi*i/resolution), 3) for i in range(resolution)]

def validate_checksum(buffer):
    # Irrelevant validation function (dead end)
    checksum = 0
    for b in buffer:
        checksum = (checksum + b) % 256
    return checksum == 128

def integrate_subsystems(config, inputs):
    accumulator = 0
    for k, v in config.items():
        if len(k) % 2 == 0:
            accumulator += v * len(inputs.get(k, []))
    return accumulator + len(config)

# Main processing pipeline
raw_samples = [0.1, -0.7, 0.9, -1.2, 0.3, 0.0, -0.4, 1.5]
spectral_data = [abs(x) ** 2 for x in raw_samples]

# Generate multiple diagnostic traces (some irrelevant)
diag_a = analyze_signal(raw_samples)
diag_b = compute_entropy([int(x*10) for x in spectral_data if x > 0.5])
diag_c = len([x for x in spectral_data if x < 1.0])

# Simulated subsystem states (distraction block)
subsystem_config = {
    'nodeX': 3, 'ioQ': 7, 'ctrlR': 2, 'busM': 5
}
input_streams = {
    'nodeX': [1, 1], 'ctrlR': [1], 'busM': [1, 1, 1]
}
proxy_metric = integrate_subsystems(subsystem_config, input_streams)  # Red herring

# Waveform generation (partially relevant)
phase_state = diag_a % 3.14
reference_wave = generate_waveform(phase_state)
active_peaks = len([w for w in reference_wave if w > 0.7])

# Bit manipulation layer (distractor)
encoded_flag = 0
for val in [int(abs(x)*100) for x in reference_wave[:4]]:
    encoded_flag ^= val
    encoded_flag = (encoded_flag << 1) & 0xFF

# Core diagnostic chain (relevant path)
processing_chain = []
for i, sample in enumerate(raw_samples):
    if i % 2 == 0:
        processing_chain.append(sample ** 2)
    else:
        processing_chain.append(-abs(sample))

# Accumulate real diagnostics
diagnostics = []
diagnostics.append(round(sum(processing_chain), 3))
diagnostics.append(active_peaks)
diagnostics.append(len(reference_wave))

def aggregate_metrics(chain, metrics):
    base = metrics[0]
    multiplier = 1 + (metrics[1] / metrics[2])
    adjustment = 0
    
    # Complex conditional adjustment (nested logic)
    if base > 0:
        adjustment += 0.5
        if metrics[2] > 6:
            adjustment *= 2
            for x in chain:
                if x < 0:
                    adjustment += 0.1
                    break
    else:
        adjustment -= 1.0
    
    # Use of itertools to obscure main logic
    combinations = list(itertools.combinations([1, 2, 3], 2))
    combo_value = len(combinations)  # Always 3, but looks dynamic
    
    # Final computation (answer depends only on specific path)
    result = base * multiplier + adjustment + combo_value
    
    # Dead code branches (misleading)
    if validate_checksum([255, 128, 64]):
        result *= 0.9
    if encoded_flag > 200:
        result += 10
    
    return round(result, 4)

# Execute key statement
temp_buffer = [128, 255, 0, 128]  # Unused buffer (red herring)
final_diagnostic = aggregate_metrics(processing_chain, diagnostics)
print(f"Target result: {final_diagnostic}")