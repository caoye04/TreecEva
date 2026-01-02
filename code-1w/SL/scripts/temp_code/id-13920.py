import math

# Simulated sensor data and diagnostic system
raw_readings = [0.88, -1.22, 3.14, 2.71, -0.55, 4.67, -3.14]
noise_floor = 0.1
sample_rate = 100

def apply_filter(data, threshold=0.5):
    # Irrelevant filtering function (not used in final path)
    return [x for x in data if abs(x) > threshold]

def generate_metadata(index, tag='SYS'):
    # Distractor: generates unused metadata
    return f'{tag}_{index}_LOG'

def transform_phase(signal):
    # Applies phase shift to signal (partially relevant)
    shifted = []
    for i, val in enumerate(signal):
        shifted.append(val * math.cos(i * math.pi / 4))
    return shifted

def amplify_components(signal, factor=1.0):
    # Amplifies signal — but only some components are later used
    amplified = [factor * x for x in signal]
    temp_normalization = sum(abs(x) for x in amplified) / len(amplified)  # red herring
    return amplified

def compute_envelope(signal):
    # Computes envelope using rectification and smoothing
    rectified = [abs(x) for x in signal]
    smoothed = []
    for i in range(len(rectified)):
        window = rectified[max(0, i-2):i+1]
        smoothed.append(sum(window) / len(window))
    return smoothed

def extract_peaks(envelope, min_threshold=0.5):
    # Extract peaks above threshold — dead code path
    peaks = []
    for i, val in enumerate(envelope):
        if val > min_threshold:
            peaks.append((i, val))
    return peaks

def calculate_entropy(signal):
    # Unused complex distractor function
    prob_dist = [abs(x) / sum(abs(y) for y in signal) for x in signal]
    entropy = -sum(p * math.log(p) for p in prob_dist if p > 0)
    return round(entropy, 4)

def reconstruct_signal(phased, envelope):
    # Combines two signal aspects — decoy operation
    return [a + b for a, b in zip(phased, envelope[:len(phased)])]

def analyze_signal(data):
    # Core analysis chain with key logic steps
    
    # Step 1: Transform phase
    phase_shifted = transform_phase(data)
    
    # Step 2: Amplify with fixed factor
    boosted = amplify_components(phase_shifted, factor=1.5)
    
    # Step 3: Compute envelope
    envelope = compute_envelope(boosted)
    
    # Step 4: Apply moving average filter (simulated via list comprehension)
    filtered = [sum(envelope[max(0,i-1):i+1]) / (i+1) for i in range(len(envelope))]
    
    # Step 5: Normalize around mean deviation
    mean_val = sum(filtered) / len(filtered)
    deviated = [abs(x - mean_val) for x in filtered]
    
    # Step 6: Detect significant deviations
    threshold = 0.75 * max(deviated)
    binary_flags = [1 if x >= threshold else 0 for x in deviated]
    
    # Step 7: Count transitions (0->1 or 1->0)
    transitions = 0
    for i in range(1, len(binary_flags)):
        if binary_flags[i] != binary_flags[i-1]:
            transitions += 1
    
    # Step 8: Final diagnostic score based on transition count and signal length
    adjustment = len(data) % 7
    final_score = (transitions * 100) + adjustment
    
    return int(final_score)

# Irrelevant preprocessing block (distractor)
log_tags = [generate_metadata(i, 'SENS') for i in range(len(raw_readings))]
entropy_diagnostic = calculate_entropy(raw_readings)

# Signal processing pipeline
processed_data = amplify_components(transform_phase(raw_readings), factor=1.2)
baseline_correction = [x - noise_floor for x in processed_data]  # unused branch

# Key execution point
final_diagnostic = analyze_signal(processed_data)

# Output result
print(f"Result: {final_diagnostic}")