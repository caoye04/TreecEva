from collections import defaultdict, Counter
from itertools import cycle, islice
import math

# Simulated sensor data processing with red herrings and complex flow
def generate_phase_map(resolution):
    return [math.sin(x * 0.1) for x in range(resolution)]

def compute_entropy(stream):
    counts = Counter(stream)
    total = len(stream)
    return -sum((count / total) * math.log2(count / total) for count in counts.values())

def shift_window(data, offset):
    return data[offset:] + data[:offset]

def evaluate_coherence(sequence):
    if len(sequence) < 2:
        return 0
    diffs = [abs(sequence[i] - sequence[i-1]) for i in range(1, len(sequence))]
    return sum(diffs) / len(diffs)

def detect_pulse(signal, threshold=0.7):
    peaks = [i for i, x in enumerate(signal) if abs(x) > threshold]
    return peaks if len(peaks) > 0 else [0]

def integrate_channels(primary, secondary, mode='weighted'):
    if mode == 'weighted':
        return [p * 0.7 + s * 0.3 for p, s in zip(primary, secondary)]
    else:
        return [max(p, s) for p, s in zip(primary, secondary)]

def filter_anomalies(dataset, limit=3):
    mean_val = sum(dataset) / len(dataset)
    std_dev = (sum((x - mean_val) ** 2 for x in dataset) / len(dataset)) ** 0.5
    return [x for x in dataset if abs(x - mean_val) <= limit * std_dev]

def derive_key_signature(seq):
    # Irrelevant transformation - decoy function
    transformed = [int(abs(x) * 100) % 7 for x in seq]
    freq = defaultdict(int)
    for t in transformed:
        freq[t] += 1
    return sorted(freq.items())

def analyze_signal(buffer, calibration):
    # Core logic begins here
    calibrated_buffer = [b * calibration[i % len(calibration)] for i, b in enumerate(buffer)]
    
    # Distractor: entropy computation not used in final result
    entropy_score = compute_entropy(calibrated_buffer)
    
    # Signal normalization
    max_val = max(abs(x) for x in calibrated_buffer)
    if max_val != 0:
        normalized = [x / max_val for x in calibrated_buffer]
    else:
        normalized = calibrated_buffer
    
    # Pulse detection
    pulse_indices = detect_pulse(normalized)
    first_pulse = pulse_indices[0] if pulse_indices else -1
    
    # Window shifting based on first pulse (only matters if positive)
    if first_pulse > 0:
        shifted = shift_window(normalized, first_pulse % len(normalized))
    else:
        shifted = normalized
    
    # Integration with dummy channel (red herring)
    dummy_channel = [math.cos(i * 0.05) for i in range(len(shifted))]
    fused_signal = integrate_channels(shifted, dummy_channel, mode='weighted')
    
    # Filtering anomalies - actually modifies signal
    clean_signal = filter_anomalies(fused_signal, limit=2.5)
    
    # Secondary coherence check
    coherence = evaluate_coherence(clean_signal)
    
    # Critical branching logic
    if coherence < 0.5:
        adjustment_factor = 2.0
    elif coherence < 1.0:
        adjustment_factor = 1.5
    else:
        adjustment_factor = 1.0  # This will be the case
    
    # Apply adjustment
    adjusted_signal = [x * adjustment_factor for x in clean_signal]
    
    # Final aggregation
    aggregate = sum(adjusted_signal) * 100
    
    # Decoy operations below
    phase_map = generate_phase_map(50)
    key_sig = derive_key_signature(adjusted_signal)
    windowed_entropy = [compute_entropy(list(islice(cycle(adjusted_signal), i, i+5))) for i in range(5)]
    
    # Final diagnostic value
    final_diagnostic = int(round(aggregate))
    
    # Dead code path - never executed due to above logic
    if len(key_sig) > 100:
        fallback = sum(math.tanh(x) for x in phase_map)
        final_diagnostic -= int(fallback)
    
    return final_diagnostic

# Main execution
if __name__ == '__main__':
    # Input data
    pattern_buffer = [0.1, -0.3, 0.5, 0.2, -0.4, 0.6, -0.1, 0.3]
    calibration_sequence = [1.1, 0.9, 1.05, 0.95]
    
    # Triggering computation
    final_diagnostic = analyze_signal(pattern_buffer, calibration_sequence)
    
    # Irrelevant post-processing
    diagnostics_log = defaultdict(list)
    diagnostics_log['values'].append(final_diagnostic)
    diagnostics_log['status'] = 'processed'
    
    # Result output (required format)
    print(f"Target result: {final_diagnostic}")