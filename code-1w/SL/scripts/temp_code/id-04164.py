from collections import defaultdict, Counter

# Simulated sensor data processing with diagnostic analysis
def preprocess_readings(raw_readings):
    processed = []
    temp_offset = 0.5
    for idx, val in enumerate(raw_readings):
        adjusted = val * 1.02 + temp_offset
        if idx % 3 == 0:
            adjusted -= 0.1
        processed.append(round(adjusted, 3))
    return processed

def generate_frequency_map(data):
    # Irrelevant helper - distractor function
    freq = defaultdict(int)
    for x in data:
        freq[x] += 1
    return freq

def compute_entropy(values):
    # Decoy function - looks important but unused
    counts = Counter(values)
    total = len(values)
    entropy = 0.0
    for count in counts.values():
        p = count / total
        entropy -= p * (p ** 0.5)  # Not real entropy, misleading
    return round(entropy, 4)

def extract_peaks(signal):
    peaks = []
    for i in range(1, len(signal) - 1):
        if signal[i-1] < signal[i] > signal[i+1]:
            peaks.append((i, signal[i]))
    return peaks

def shift_cipher(sequence, shift):
    # Unused transformation - red herring
    return [(x + shift) % 256 for x in sequence]

def transform_signal(peaks_data):
    transformed = []
    for index, value in peaks_data:
        if value > 100:
            transformed.append(value // 3)
        elif value > 50:
            transformed.append(value // 2)
        else:
            transformed.append(value)
    return transformed

def validate_sequence(seq):
    # Complex validation that isn't actually used in main logic
    if len(seq) < 3:
        return False
    for i in range(2, len(seq)):
        if seq[i] < seq[i-1] and seq[i-1] < seq[i-2]:
            return False
    return True

def reconstruct_timeline(indices, values):
    # Dead code path - never called
    timeline = {}
    for i, v in zip(indices, values):
        timeline[i] = v
    return timeline

def analyze_pattern(data, reference):
    score = 0
    for i, d in enumerate(data):
        if i >= len(reference):
            break
        diff = abs(d - reference[i])
        if diff < 5:
            score += 3
        elif diff < 10:
            score += 1
        else:
            score -= 2
    return score

def main_pipeline():
    # Core input data
    raw_sensor_data = [98, 45, 102, 67, 201, 89, 153, 76, 112, 95]
    
    # Step 1: Preprocess readings
    calibrated = preprocess_readings(raw_sensor_data)
    
    # Step 2: Extract significant peaks
    peak_events = extract_peaks(calibrated)
    
    # Step 3: Transform peak values into diagnostic units
    transformed_data = transform_signal(peak_events)
    
    # Irrelevant intermediate computations - distractions
    frequency_profile = generate_frequency_map(calibrated)
    dummy_shifted = shift_cipher([ord(c) for c in 'debug'], 5)
    entropy_metric = compute_entropy(calibrated)
    
    # Reference pattern for comparison
    key_sequence = [33, 22, 51, 38]
    
    # Final diagnostic analysis - this is the critical point
    final_diagnostic = analyze_pattern(transformed_data, key_sequence)
    
    # Extraneous post-processing
    if final_diagnostic > 10:
        final_diagnostic = (final_diagnostic * 2) % 17
    else:
        final_diagnostic = (final_diagnostic + 4) * 3
    
    print(f"Result: {final_diagnostic}")

if __name__ == "__main__":
    main_pipeline()