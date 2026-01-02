import math

# Simulated bio-signal processing pipeline with extensive distractions
def preprocess_signal(raw_samples):
    filtered = []
    noise_floor = 0.041
    gain_boost = 1.87
    temp_accum = 0.0

    for x in raw_samples:
        if abs(x) < noise_floor:
            continue
        boosted = x * gain_boost
        if boosted > 1.0:
            boosted = 1.0
        elif boosted < -1.0:
            boosted = -1.0
        filtered.append(boosted)

    return filtered


def compute_entropy(values):
    # Irrelevant entropy calculation (dead end)
    from collections import Counter
    counts = Counter([round(v, 1) for v in values])
    total = len(values)
    entropy = 0.0
    for count in counts.values():
        p = count / total
        if p > 0:
            entropy -= p * math.log2(p)
    return round(entropy, 3)


def generate_harmonic_series(n, factor=1.0):
    # Distractor: generates unused harmonic patterns
    return [factor / (i + 1) for i in range(n)]


def shift_cipher(text, offset):
    # Completely irrelevant function – red herring
    result = ''
    for char in text:
        if char.isalpha():
            base = ord('a') if char.islower() else ord('A')
            result += chr((ord(char) - base + offset) % 26 + base)
        else:
            result += char
    return result


def extract_features(signal_chunk):
    magnitude_peaks = [abs(x) for x in signal_chunk if abs(x) > 0.5]
    avg_magnitude = sum(magnitude_peaks) / len(magnitude_peaks) if magnitude_peaks else 0.0

    # Real feature: peak count above dynamic threshold
    dynamic_t = 0.75 if len(magnitude_peaks) > 3 else 0.6
    significant = len([p for p in magnitude_peaks if p > dynamic_t])

    # Fake feature extraction path
    shadow_metrics = []
    for i in range(len(signal_chunk)):
        if i % 3 == 0:
            shadow_metrics.append(math.sin(signal_chunk[i]) ** 2)

    # Only 'significant' is carried forward; others are distractions
    return {'peak_count': significant, 'avg_mag': avg_magnitude, 'shadow': shadow_metrics}


def transform_sequence(seq):
    # Bit manipulation distraction
    bit_modified = []
    for val in seq:
        int_val = int(abs(val) * 100)
        transformed = ((int_val << 2) ^ 0xA3) & 0xFF
        bit_modified.append(transformed)
    return bit_modified


def analyze_pattern(data, limit):
    # Core logic buried in noise
    score = 0
    adjustment = 0

    # Linear search through data with conditional branching
    for item in data:
        if item < 0:
            adjustment += 1
            continue
        if item == 0:
            break
        score += int(item * 100)

    # Critical computation
    if adjustment > 0:
        score = score // (adjustment + 1) if adjustment < 5 else score // 5

    # Conditional expression - part of final result
    modifier = 1.25 if score > limit else 0.85

    # Final transformation using list comprehension (required feature)
    refined = [x for x in range(score - 2, score + 3) if x % 2 == 1]
    result = sum(refined) * modifier

    # Decoy operations
    _ = [math.sqrt(z) for z in refined if z > 0]
    _ = shift_cipher('debug', score % 26)

    return int(result)

# Main execution with multiple distractions
if __name__ == '__main__':
    # Simulated neural impulse readings
    raw_neural_data = [0.12, -0.33, 0.81, 0.94, -0.76, 0.03, 0.68, -0.89, 0.45, 0.0]

    # Irrelevant baseline reference
    reference_tones = generate_harmonic_series(10, 0.66)

    # Step 1: Preprocess signal (filter noise)
    cleaned = preprocess_signal(raw_neural_data)

    # Step 2: Extract features (only one field used later)
    features = extract_features(cleaned)

    # Step 3: Transform data using bit operations (partially relevant)
    transformed_data = transform_sequence(cleaned)

    # Unused variables - red herrings
    sample_entropy = compute_entropy(cleaned)
    calibration_key = shift_cipher('encrypt', 7)
    dummy_lookup = {i: chr(65 + (i % 26)) for i in range(20)}

    # Key control flow with early termination condition
    threshold = 40
    if features['avg_mag'] < 0.4:
        final_diagnostic = -999
    else:
        # Critical call
        final_diagnostic = analyze_pattern(transformed_data, threshold)

    # Print required output
    print(f"Target result: {final_diagnostic}")