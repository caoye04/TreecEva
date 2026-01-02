import math

# Simulated sensor data processing with diagnostic analysis

def collect_sensor_readings():
    # Real data source (simplified)
    return [0.7, 1.2, -0.3, 4.5, 2.1, -1.0, 3.3, 0.0]


def filter_noise(readings, threshold=0.5):
    # Filters out low-amplitude noise
    filtered = []
    for val in readings:
        if abs(val) >= threshold:
            filtered.append(val)
    return filtered


def amplify_signal(signal, factor=2.0):
    # Amplifies meaningful signal components
    return [s * factor for s in signal]


def compute_envelope(signal):
    # Computes absolute envelope for burst detection
    return [abs(s) for s in signal]


def rolling_average(data, window=2):
    # Smooths data using moving average (unused in final path)
    result = []
    for i in range(len(data) - window + 1):
        result.append(sum(data[i:i+window]) / window)
    return result


def detect_bursts(envelope, burst_threshold=3.0):
    # Detects high-energy bursts in signal envelope
    bursts = []
    for i, amp in enumerate(envelope):
        if amp > burst_threshold:
            bursts.append(i)
    return bursts


def integrate_energy(signal):
    # Computes total energy (sum of squares)
    return sum([x**2 for x in signal])


def phase_shift_elements(arr):
    # Misleading transformation - not used in critical path
    shifted = [0] * len(arr)
    for i in range(len(arr)):
        shifted[i] = arr[(i + 1) % len(arr)] * 0.9
    return shifted


def extract_features(signal):
    # Extract statistical features from signal
    mean_val = sum(signal) / len(signal)
    variance = sum((x - mean_val)**2 for x in signal) / len(signal)
    peak = max(abs(x) for x in signal)
    return {
        'mean': mean_val,
        'variance': variance,
        'peak': peak,
        'length': len(signal)
    }


def generate_combinations(items):
    # Unused combinatorics function - red herring
    combos = []
    for i in range(len(items)):
        for j in range(i+1, len(items)):
            combos.append((items[i], items[j]))
    return combos


def time_align(frames, offset=1):
    # Shifts frame indices - irrelevant to final calculation
    aligned = {}
    for idx, frame in enumerate(frames):
        aligned[idx + offset] = frame
    return aligned


def reconstruct_waveform(envelope, phase_ref):
    # Attempts waveform reconstruction - dead end
    wave = []
    for e in envelope:
        if e > 0:
            wave.append(e * math.cos(phase_ref))
    return wave


def analyze_signal(frames):
    # Core diagnostic logic
    total_energy = integrate_energy(frames)
    
    # Feature extraction
    features = extract_features(frames)
    
    # Burst analysis
    envelope = compute_envelope(frames)
    bursts = detect_bursts(envelope, burst_threshold=2.5)
    
    # Diagnostic score components
    base_score = features['variance'] * 100
    burst_bonus = len(bursts) * 50
    
    # Distractor: complex but unused structure
    temp_analysis = {}
    for i, f in enumerate(frames):
        temp_analysis[i] = {
            'raw': f,
            'squared': f**2,
            'group': 'A' if f > 0 else 'B',
            'dummy_calc': (f * 17) % 3
        }
    
    # Additional irrelevant computation
    dummy_pairs = list(zip(frames, [x*0.5 for x in frames]))
    indexed_data = list(enumerate(dummy_pairs))
    
    # Critical diagnostic logic
    stability_factor = 1.0
    if features['mean'] < 0.5 and features['peak'] > 3.0:
        stability_factor = 0.8
    elif features['mean'] > 1.0:
        stability_factor = 1.2
    else:
        stability_factor = 1.0
    
    preliminary_diagnostic = (base_score + burst_bonus) * stability_factor
    
    # Final adjustment based on energy threshold
    if total_energy > 50:
        final_diagnostic = int(preliminary_diagnostic + 100)
    else:
        final_diagnostic = int(preliminary_diagnostic)
    
    # Unused but plausible-looking data transformation
    decoy_map = {}
    for i, (idx, item) in enumerate(indexed_data):
        decoy_map[i] = {"source": idx, "value": item[0], "flag": i % 3}
    
    return final_diagnostic

# Main execution flow
raw_readings = collect_sensor_readings()
processed_frames = filter_noise(raw_readings, threshold=0.4)
processed_frames = amplify_signal(processed_frames, factor=1.8)

# Dead code path - never called
# smoothed = rolling_average(processed_frames)
# aligned_data = time_align(processed_frames)

# Key statement
final_diagnostic = analyze_signal(processed_frames)

# Print result
print(f"Target result: {final_diagnostic}")