def preprocess_signal(raw_data, threshold=0.5):
    """Normalize and filter signal data above threshold."""
    normalized = [x / max(raw_data) for x in raw_data]
    filtered = list(filter(lambda x: x > threshold, normalized))
    return filtered

# Irrelevant helper function (decoy)
def compute_entropy(data):
    import math
    freq_map = {}
    for x in data:
        freq_map[x] = freq_map.get(x, 0) + 1
    total = len(data)
    entropy = 0
    for count in freq_map.values():
        p = count / total
        entropy -= p * math.log2(p) if p > 0 else 0
    return round(entropy, 6)

# Unused signal transformation (dead code path)
def transform_phase(signal):
    return [complex(x, -x).conjugate() for x in signal]

# Simulate sensor readings (distraction: realistic but irrelevant)
bio_signals = [120, 85, 93, 77, 110, 68, 99, 81]
sample_rate = 256  # Hz (unused)
amplitude_envelope = [max(bio_signals[i:i+2]) for i in range(len(bio_signals)-1)]

# Real processing chain begins
raw_input_stream = [45, 22, 67, 33, 89, 56, 77, 12, 68]
noise_floor = sum(raw_input_stream) / len(raw_input_stream)
adjusted_samples = [x - noise_floor * 0.1 for x in raw_input_stream]

# Apply preprocessing
processed_samples = preprocess_signal(adjusted_samples, threshold=0.4)

# Secondary distraction: unrelated statistical analysis
deviation_from_mean = [abs(x - sum(adjusted_samples)/len(adjusted_samples)) for x in adjusted_samples]
outlier_flags = [1 if x > 20 else 0 for x in deviation_from_mean]  # unused

# Mapping with enumerate and zip (required idiom)
indexed_weights = {i: weight for i, weight in enumerate([0.8, 1.1, 0.9, 1.2, 1.0, 0.7])}
synchronized_pairs = list(zip(processed_samples, [0.5, 0.6, 0.7, 0.8, 0.9]))

# Core diagnostic logic
weighted_sum = 0
for i, val in enumerate(processed_samples):
    weight = indexed_weights.get(i % 6, 1.0)
    weighted_sum += val * weight * 100

# Additional red herring: complex frequency simulation (irrelevant)
frequencies = [i * sample_rate / len(bio_signals) for i in range(len(bio_signals))]
harmonic_distortion = sum([f / 1000 for f in frequencies if f > 100])

# Actual analysis function
def analyze_signal(cleaned_signal):
    base_score = 0
    for x in cleaned_signal:
        if x > 0.6:
            base_score += int(x * 50)
        else:
            base_score -= int(x * 25)
    
    # Introduce bit manipulation (complex concept)
    score_bits = base_score ^ 0b110101
    score_bits = (score_bits << 2) | (score_bits >> 5)
    final_masked = score_bits & 0xFFFF
    
    # Final adjustment using case conversion (suggested paradigm)
    tag = "CRITICAL" if final_masked > 5000 else "NORMAL"
    adjustment = len(tag.lower()) - len(tag.upper())  # always 0, misleading!
    
    return final_masked + adjustment

# Execute critical statement
final_diagnostic = analyze_signal(processed_samples)
print(f"Result: {final_diagnostic}")