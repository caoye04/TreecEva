import itertools

# Simulate a signal processing pipeline with filtering and transformation

def generate_frequency_bands(baseline, count):
    return [baseline * (i + 1) for i in range(count)]

# Irrelevant helper: generates harmonic overtones (not used in final computation)
def generate_overtones(frequency, levels):
    return [frequency * (2 ** i) for i in range(levels)]

# Signal distortion simulation (partially relevant but only one component used)
def apply_distortion(signal, intensity=0.1):
    return [s + (intensity * s ** 0.5) for s in signal]

# Main filtering logic
def filter_noise(sequence, threshold):
    # Uses list comprehension with conditional filtering
    clean_seq = [x for x in sequence if abs(x) > threshold]
    temp_debug = sum([1 for x in sequence if abs(x) <= threshold])  # distractor: unused count
    return clean_seq

# Transformation via lambda-based mapping
def amplify_signal(seq, factor):
    amplifier = lambda x: round(x * factor, 3)
    return list(map(amplifier, seq))

# Aggregation using windowed averages (some red herring logic here)
def compute_envelope(signal, window_size=3):
    envelope = []
    padded = [0] * (window_size // 2) + signal + [0] * (window_size // 2)
    for i in range(len(signal)):
        window = padded[i:i+window_size]
        avg = sum(window) / len(window)
        envelope.append(round(avg, 3))
    return envelope

# Core processing function
def process_transmission(raw_data, threshold):
    # Step 1: Initial filtering
    filtered = filter_noise(raw_data, threshold)
    
    # Distractor: Compute but don't use envelope
    dummy_envelope = compute_envelope(filtered, window_size=2)
    envelope_length = len(dummy_envelope)  # semi-relevant but unused
    
    # Step 2: Amplify relevant components
    boosted = amplify_signal(filtered, 1.25)
    
    # Step 3: Apply distortion (only the first few elements matter due to truncation later)
    distorted = apply_distortion(boosted, intensity=0.08)
    
    # Step 4: Truncate to significant portion (first 5 elements)
    truncated = distorted[:5]
    
    # Step 5: Final aggregation using weighted sum
    weights = [0.1, 0.2, 0.3, 0.2, 0.2]
    weighted_sum = sum(truncated[i] * weights[i] for i in range(len(truncated)))
    
    # Additional irrelevant calculation (simulates diagnostic trace)
    peak_value = max(truncated) if truncated else 0
    avg_value = sum(truncated) / len(truncated) if truncated else 0
    diagnostic_score = (peak_value * 0.7) + (avg_value * 0.3)  # dead-end computation
    
    return round(weighted_sum, 4)

# Setup: Generate base signal
base_signals = generate_frequency_bands(12.0, 6)
noise_threshold = 24.0

# Add synthetic noise and pattern
signal_sequence = [base_signals[i] * ((-1)**i) for i in range(len(base_signals))]
signal_sequence[2] *= 0.5  # weaken one component
signal_sequence.append(5.0)  # sub-threshold noise
signal_sequence.append(-3.0)  # another sub-threshold

# Inserting unused data structure to increase cognitive load
signal_stats = {
    "count": len(signal_sequence),
    "positive_count": len([x for x in signal_sequence if x > 0]),
    "negative_count": len([x for x in signal_sequence if x < 0]),
    "zero_count": len([x for x in signal_sequence if x == 0])
}

# Unused recursive helper (dead code path)
def count_above_recursive(arr, limit):
    if not arr:
        return 0
    return (1 if arr[0] > limit else 0) + count_above_recursive(arr[1:], limit)

# Critical execution point
final_signal = process_transmission(signal_sequence, noise_threshold)

# Output result
print(f"Result: {final_signal}")