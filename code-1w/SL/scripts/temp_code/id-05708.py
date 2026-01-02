from collections import Counter, defaultdict
from itertools import cycle, islice

# Simulated sensor network data processing with diagnostic logic

def collect_raw_readings():
    # Real data source (relevant)
    return [18, 23, 17, 45, 22, 38, 21, 19, 24, 41, 22, 16]

def filter_outliers(data, threshold=35):
    # Relevant filtering function
    return [x for x in data if x <= threshold]

def compute_checksum(seq):
    # Irrelevant utility: used nowhere critical
    return sum(x * (i + 1) for i, x in enumerate(seq)) % 1000

def generate_synthetic_noise(length, seed=1):
    # Distractor: generates fake data not used in final path
    return [(seed * i * 17) % 23 for i in range(length)]

def align_phase(readings):
    # Red herring transformation
    rotated = readings[-3:] + readings[:-3]
    normalized = [(x - min(rotated)) / (max(rotated) - min(rotated) + 1) for x in rotated]
    return [int(n * 100) for n in normalized]

def extract_peaks(signal, min_magnitude=20):
    # Relevant peak detection
    return [x for x in signal if x >= min_magnitude]

def count_transitions(seq):
    # Misleading temporal analysis (unused)
    up = down = 0
    for i in range(1, len(seq)):
        if seq[i] > seq[i-1]:
            up += 1
        elif seq[i] < seq[i-1]:
            down += 1
    return {'up': up, 'down': down}

def build_histogram(data):
    # Decoy analytics
    hist = defaultdict(int)
    for d in data:
        hist[d // 5] += 1
    return dict(hist)

def encode_signal(sequence):
    # Bit manipulation red herring
    encoded = 0
    for val in sequence[:8]:
        encoded = (encoded << 3) | (val & 0b111)
    return encoded ^ 0xABCD

def phase_shift_sequence(seq, shift_by=2):
    # Unused transformation path
    c = cycle(seq)
    return list(islice(c, shift_by, shift_by + len(seq)))

def aggregate_metrics(peaks, raw):
    # Partially relevant but overcomplicated
    avg_peak = sum(peaks) / len(peaks) if peaks else 0
    variance = sum((x - avg_peak) ** 2 for x in peaks) / len(peaks) if peaks else 0
    base_trend = (raw[-1] - raw[0]) / len(raw)
    return {
        'avg_peak': avg_peak,
        'variance': variance,
        'trend': base_trend,
        'peak_count': len(peaks)
    }

def analyze_readings(signals):
    # Core logic hidden among distractions
    filtered = filter_outliers(signals)
    peaks = extract_peaks(filtered)
    
    # Dummy branching with misleading variables
    temp_debug = [p * 1.5 for p in peaks if p % 2 == 0]
    debug_sum = sum(temp_debug)
    
    if len(peaks) > 3:
        subset = peaks[:4]
        adjusted = [s - 5 for s in subset]
        squared_errors = [(a - 15) ** 2 for a in adjusted]
        mean_error = sum(squared_errors) / len(squared_errors)
        if mean_error < 25:
            candidate = sum(adjusted) + int(mean_error)
        else:
            candidate = sum(subset) * 2
    else:
        candidate = 0
    
    # Final computation buried in logic
    mirror_val = signals[len(signals)//2]
    final_score = candidate + mirror_val
    
    # Dead branch: never executed due to data
    if final_score < 0:
        recovery_mode = True
        final_score = abs(final_score)
    
    # Actual answer derivation
    final_diagnostic = final_score * 2 - 17
    
    return final_diagnostic

# Main execution flow
raw_sensor_data = collect_raw_readings()
processed_signals = filter_outliers(raw_sensor_data)

# Irrelevant pre-processing chain
noise_floor = generate_synthetic_noise(len(raw_sensor_data))
mixed_signal = [a + b for a, b in zip(raw_sensor_data, noise_floor)]
phase_aligned = align_phase(mixed_signal)
histogram_profile = build_histogram(phase_aligned)
transition_stats = count_transitions(raw_sensor_data)
encoded_hash = encode_signal(raw_sensor_data)
shifted_cycle = phase_shift_sequence(raw_sensor_data)

# Critical operation
final_diagnostic = analyze_readings(processed_signals)

# Output result as required
print(f"Target result: {final_diagnostic}")