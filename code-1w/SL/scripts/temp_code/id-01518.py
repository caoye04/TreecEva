from collections import defaultdict, Counter
import math

# Simulate a telemetry data processor with multiple noise filters and signal extraction paths
def analyze_frequency_bands(signal):
    band_energy = defaultdict(float)
    harmonics = [0] * 8
    temp_accum = 0

    for i, val in enumerate(signal):
        if i % 7 == 0:
            band_energy['low'] += abs(val) * 0.3
        elif i % 5 == 0:
            band_energy['mid'] += abs(val) ** 0.5 * 0.6
        elif i % 3 == 0:
            band_energy['high'] += val * val * 0.1
            temp_accum += val

    # Irrelevant harmonic analysis (dead logic path)
    for j in range(len(harmonics)):
        harmonics[j] = math.sin(j * math.pi / 4) * temp_accum

    return dict(band_energy)


def detect_anomaly_patterns(seq):
    counts = Counter(seq)
    anomalies = []
    total = sum(counts.values())
    threshold = total * 0.05

    # Misleading statistical filter
    for k, v in counts.items():
        if abs(k) > 50 and v < threshold:
            anomalies.append(k)

    # Dead code: never executed due to logic above
    if len(anomalies) > 100:
        return sorted(set(anomalies[:50]))
    else:
        return [x for x in anomalies if x % 7 != 0]  # Partial filter


def compute_entropy(data):
    freqs = {}
    for x in data:
        freqs[x] = freqs.get(x, 0) + 1
    entropy = 0.0
    n = len(data)
    for f in freqs.values():
        p = f / n
        entropy -= p * math.log2(p) if p > 0 else 0
    return round(entropy, 6)


def extract_sync_frame(signal):
    # Fake synchronization attempt
    window_size = 6
    best_score = -1
    sync_start = 0
    for i in range(len(signal) - window_size):
        slice_sum = sum(signal[i:i+window_size])
        if 10 < slice_sum < 15 and slice_sum > best_score:
            best_score = slice_sum
            sync_start = i
    return signal[sync_start:sync_start+window_size] if best_score > 0 else [0]*6


def apply_noise_gate(buffer, level=0.75):
    # Complex but irrelevant noise suppression
    filtered = []
    for x in buffer:
        if abs(x) > level:
            filtered.append(round(x * (1 + 0.1 * math.sin(x))))
        else:
            filtered.append(0)
    return [f for f in filtered if f != 0]


def reconstruct_phase_envelope(signal):
    envelope = []
    for i in range(1, len(signal)-1):
        prev, curr, nxt = signal[i-1], signal[i], signal[i+1]
        slope = (nxt - prev) / 2.0
        curvature = nxt - 2*curr + prev
        if abs(curvature) < 3:
            envelope.append(curr + slope * 0.5)
        else:
            envelope.append(curr)
    return envelope


def process_transmission_sequence(raw_data):
    # Main processing pipeline
    stage1 = [x * 1.5 for x in raw_data if x % 2 == 1]  # Keep only odd indices scaled
    
    # Distractor: unused transformation branch
    alt_path = [abs(y) ** 0.5 for y in raw_data if y < 0]
    if len(alt_path) > 10:
        alt_path = alt_path[:10]

    stage2 = [int(z) for z in stage1 if z > 0]
    
    # Red herring: anomaly detection that doesn't affect output
    _ = detect_anomaly_patterns(stage2)
    
    # Real processing continues
    freq_analysis = analyze_frequency_bands(stage2)
    low_power = freq_analysis.get('low', 0)
    mid_power = freq_analysis.get('mid', 0)
    high_power = freq_analysis.get('high', 0)
    
    # Signal reconstruction using phase envelope
    pre_signal = reconstruct_phase_envelope(stage2)
    
    # Final weighting: only low and high bands matter
    # Critical line: this determines the actual answer
    weighted_strength = low_power * 2.0 + high_power * 3.0
    
    # Noise gate applied but result not used
    _ = apply_noise_gate(pre_signal, level=0.9)
    
    # Sync frame extraction (not used in final result)
    _ = extract_sync_frame(stage2)
    
    # Entropy computed but irrelevant
    _ = compute_entropy(stage2)
    
    # Final signal depends only on weighted_strength and length of pre_signal
    adjustment = len(pre_signal) * 0.5
    final_signal = int(weighted_strength + adjustment)
    
    return final_signal

# Simulated sensor input (deterministic)
raw_data = list(range(-20, 35))

# Execution point of interest
final_signal = process_transmission_sequence(raw_data)

print(f"Target result: {final_signal}")