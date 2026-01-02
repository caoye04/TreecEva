from collections import defaultdict, Counter
import itertools

# Simulated biomedical signal processing pipeline
# with extensive red herrings and irrelevant transformations

def analyze_waveform(samples):
    if len(samples) < 5:
        return 0
    peak = max(samples)
    baseline = sum(samples) / len(samples)
    variance = sum((x - baseline) ** 2 for x in samples) / len(samples)
    # Irrelevant transformation (dead path)
    normalized = [round((x - baseline) / (variance + 1e-5), 3) for x in samples]
    return peak - baseline

def compute_envelope(signal):
    envelope = []
    for i in range(1, len(signal) - 1):
        slope_fwd = signal[i + 1] - signal[i]
        slope_bwd = signal[i] - signal[i - 1]
        curvature = slope_fwd - slope_bwd
        envelope.append(abs(curvature))
    # Misleading intermediate result
    envelope_sum = sum(envelope) * 0.85
    return envelope

# Unused decoy function (distractor)
def decrypt_sequence(seq):
    shift = seq[0] % 7
    return [(val + shift) % 256 for val in seq]

# Real processing function buried among noise
def generate_phase_shift(data, factor=3):
    shifted = []
    for i, val in enumerate(data):
        phase = (i * factor) % 8
        if phase < 4:
            shifted.append(val + phase)
        else:
            shifted.append(val - (phase - 3))
    return shifted

# Complex metric processor with hidden logic chain
def process_metrics(signature, thresholds):
    temp_cache = defaultdict(float)
    flags = [False] * 5
    
    # Step 1: Extract frequency bands (only band_3 is used later)
    band_1 = [x for x in signature if x < thresholds['low']]
    band_2 = [x for x in signature if thresholds['low'] <= x < thresholds['mid']]
    band_3 = [x for x in signature if x >= thresholds['mid']]
    
    # Irrelevant statistical summary
    stats_summary = {
        'count': len(signature),
        'unique': len(set(signature)),
        'entropy': sum(Counter(signature).values()),
        'spike_ratio': len(band_1) / len(signature)
    }
    
    # Fake diagnostic path (never contributes to final result)
    if stats_summary['spike_ratio'] > 0.3:
        flags[0] = True
        adjustment = 0.9
    else:
        adjustment = 1.1
    
    # Hidden critical computation path (nested logic)
    cumulative = 0
    for idx, val in enumerate(band_3):
        if val % 4 == 0:
            cumulative += val // 4
        elif val % 3 == 0:
            cumulative -= val // 5
        else:
            cumulative += (val % 7)
    
    # Apply non-linear scaling (red herring with unused result)
    scaled_cumulative = round(cumulative * adjustment, 4)
    
    # Critical dependency on bit manipulation
    bit_influence = 0
    for val in band_3:
        bit_influence ^= (val & 15)  # XOR with lower 4 bits
    
    # Combine with combinatorics distractor
    pairs = list(itertools.combinations(band_3[:6], 2))
    pair_count = len(pairs)
    # But only one specific pair matters
    if len(pairs) > 10:
        special_pair_val = (pairs[5][0] + pairs[5][1]) // 2
    else:
        special_pair_val = 12
    
    # Final computation chain
    temp_cache['base'] = cumulative
    temp_cache['mod'] = bit_influence * 2
    temp_cache['bonus'] = special_pair_val
    
    # Actual answer derivation (non-obvious)
    final_score = temp_cache['base'] + temp_cache['mod']
    if len(band_3) > 4:
        final_score += temp_cache['bonus'] // 3
    
    # Redundant string encoding (irrelevant)
    status_code = ''.join([chr(97 + (final_score % 26)) for _ in range(3)])
    
    # Key assignment - this is the true answer
    final_diagnostic = int(final_score + len(thresholds))
    
    # Dead code paths below
    if final_diagnostic < 0:
        final_diagnostic = abs(final_diagnostic)
    elif final_diagnostic == 42:
        final_diagnostic *= 2
    
    return final_diagnostic

# Main execution block
if __name__ == '__main__':
    # Input data setup
    raw_signal = [12, 7, 3, 18, 21, 4, 9, 15, 25, 30, 8, 11, 14, 19, 22]
    
    # Irrelevant preprocessing steps
    filtered = [x for x in raw_signal if x != 7]
    inverted = [30 - x for x in filtered]
    analyzed = analyze_waveform(inverted)
    envelope_data = compute_phase_shift(inverted, factor=5)
    
    # Distractor dictionary with unused entries
    config_map = {
        'sampling_rate': 256,
        'gain': 2.1,
        'mode': 'diagnostic',
        'buffer_size': 1024
    }
    
    # Threshold configuration actually used in process_metrics
    threshold_map = {
        'low': 10,
        'mid': 15,
        'high': 25
    }
    
    # Real input signature derived through multiple steps
    health_signature = [x * 2 for x in raw_signal if x > 5]
    health_signature = [x + 1 for i, x in enumerate(health_signature) if i % 2 == 0]
    
    # Decoy list transformation
    shadow_copy = [x ^ 5 for x in health_signature]
    
    # Critical function call
    final_diagnostic = process_metrics(health_signature, threshold_map)
    
    # Output result as required
    print(f"Target result: {final_diagnostic}")