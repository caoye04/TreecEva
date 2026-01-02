import math

# Simulated sensor data processing for a satellite transmission protocol
def analyze_frequency_band(data, threshold=0.7):
    above_threshold = [x for x in data if x > threshold]
    return len(above_threshold) / len(data) if data else 0

def generate_harmonic_sequence(n):
    return [math.sin(i * 0.5) + math.cos(i * 0.3) for i in range(n)]

def extract_peaks(signal):
    peaks = []
    for i in range(1, len(signal) - 1):
        if signal[i] > signal[i-1] and signal[i] > signal[i+1]:
            peaks.append(signal[i])
    return peaks[:5]

def shift_window(sequence, offset):
    return sequence[offset:] + sequence[:offset]

def calculate_entropy(data):
    from collections import Counter
    counts = Counter(data)
    total = len(data)
    entropy = 0
    for count in counts.values():
        p = count / total
        if p > 0:
            entropy -= p * math.log2(p)
    return round(entropy, 6)

def filter_artifacts(segment):
    # Removes values close to known interference frequencies
    return [x for x in segment if not (0.44 < abs(x) < 0.46 or 0.88 < abs(x) < 0.92)]

def integrate_segments(segments):
    combined = []
    for seg in segments:
        combined.extend([x * 1.05 for x in seg])
    return combined

def process_transmission(raw_slices):
    # Irrelevant: debug counters
    debug_passes = 0
    temp_results = []
    snapshot_log = []

    cleaned_slices = []
    for s in raw_slices:
        filtered = filter_artifacts(s)
        if len(filtered) > 3:
            shifted = shift_window(filtered, 2)
            cleaned_slices.append(shifted)
        else:
            cleaned_slices.append(filtered)

    # Distractor: unused transformation
    flattened = [item for sublist in raw_slices for item in sublist]
    baseline_entropy = calculate_entropy([int(abs(x)*100) for x in flattened[:20]])

    # Core logic begins
    integrated = integrate_segments(cleaned_slices)
    
    # Apply harmonic correction
    harmonics = generate_harmonic_sequence(len(integrated))
    corrected = [a + b*0.1 for a, b in zip(integrated, harmonics)]

    # Slice into chunks for analysis
    chunk_size = 6
    chunks = [corrected[i:i+chunk_size] for i in range(0, len(corrected), chunk_size)]
    
    # Analyze each chunk
    quality_scores = []
    for c in chunks:
        if len(c) == chunk_size:
            score = analyze_frequency_band(c, 0.65)
            quality_scores.append(score)
        else:
            # Dead code path — never executed due to truncation below
            quality_scores.append(-1.0)

    # Truncate to first 4 full chunks only
    truncated = corrected[:24]  # 4 chunks of 6

    # Extract peaks as secondary validation
    peak_values = extract_peaks(truncated)
    
    # Final computation
    avg_peak = sum(peak_values) / len(peak_values) if peak_values else 0
    base_signal = sum(truncated) * 1000
    adjustment = int(avg_peak * 100) * 1.5
    
    # Misleading intermediate
    dummy_metric = len([x for x in truncated if x < 0])  # unused
    buffer_checksum = sum([int(x * 10) % 3 for x in truncated])  # decoy

    final_signal = int(base_signal + adjustment)  # Key assignment

    # Red herring: unrelated diagnostic
    diagnostics = {
        'version': '2.1',
        'mode': 'passive',
        'readings': len(truncated)
    }

    # Output result
    print(f"Result: {final_signal}")
    return final_signal

# Generate input slices from synthetic source
source_stream = generate_harmonic_sequence(32)
segmented = [source_stream[i:i+8] for i in range(0, len(source_stream), 8)]
signal_slices = segmented[:3]  # Take first three segments

# Execution point of interest
final_signal = process_transmission(signal_slices)