import math

# Simulated sensor data processing with red herrings and distractions
def preprocess_signal(raw_signal):
    filtered = [x for x in raw_signal if x > -50]  # Irrelevant filtering
    normalized = [val / max(filtered) for val in filtered]  # Distractor normalization
    return normalized

# Decoy function – looks important but unused in critical path
def compute_entropy(data):
    hist = {}
    for d in data:
        hist[d] = hist.get(d, 0) + 1
    total = len(data)
    entropy = 0
    for count in hist.values():
        p = count / total
        if p > 0:
            entropy -= p * math.log2(p)
    return round(entropy, 3)

# Another decoy: frequency analysis (dead code path)
def dominant_frequency(signal):
    period_counts = {}
    for i in range(1, min(10, len(signal))):
        matches = 0
        for j in range(len(signal) - i):
            if signal[j] == signal[j+i]:
                matches += 1
        period_counts[i] = matches
    return max(period_counts, key=period_counts.get)

# Real transformation function used in logic chain
def transform_sequence(seq, mode='cyclic'):
    shifted = seq[3:] + seq[:3]  # Left rotation by 3
    mirrored = shifted[::-1]     # Reverse the list
    processed = []
    for i, val in enumerate(mirrored):
        if i % 2 == 0:
            processed.append(int(val ** 0.5) * 2)
        else:
            processed.append(val // 4 + (i % 5))
    return processed

# Core analysis function that determines final result
def analyze_pattern(data, limit):
    segment = data[2:9:2]  # Slice: start=2, stop=9, step=2 → indices 2,4,6,8
    adjusted = [x - limit for x in segment]
    magnitude = sum(abs(x) for x in adjusted)
    penalty = 0
    for idx, val in enumerate(adjusted):
        if val > 0 and idx % 2 == 0:
            penalty += val * 0.5
    score = magnitude - penalty
    return int(round(score))

# --- Main execution block ---
if __name__ == "__main__":
    # Initial dataset: synthetic telemetry readings
    base_readings = [144, 81, 64, 169, 100, 121, 25, 9, 4, 36]
    
    # Irrelevant preprocessing steps (distractors)
    cleaned_signal = preprocess_signal(base_readings)
    entropy_value = compute_entropy(base_readings)  # Unused result
    
    # Secondary transformation path (unused alternative)
    alt_transform = [int(math.sqrt(x)) for x in base_readings if x >= 30]
    freq_guess = dominant_frequency(alt_transform)  # Dead call
    
    # Actual data path
    transformed_data = transform_sequence(base_readings, mode='cyclic')
    
    # Key parameters mixed among decoys
    calibration_offset = 7
    threshold = len(base_readings) - 5  # evaluates to 5
    buffer_limit = sum(base_readings) // 100  # distractor: evaluates to 74
    
    # Critical computation
    interim_mask = [i for i in range(len(transformed_data)) if transformed_data[i] % 2 == 0]
    masked_sum = sum(transformed_data[i] for i in interim_mask)  # Red herring usage
    
    # Core statement
    final_diagnostic = analyze_pattern(transformed_data, threshold)
    
    # Output requirement
    print(f"Result: {final_diagnostic}")