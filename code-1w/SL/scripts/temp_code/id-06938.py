import math

# Simulated bio-signal processing pipeline with diagnostic analysis

def generate_frequency_bands(baseline):
    # Irrelevant frequency band generation (distractor)
    alpha = [baseline * math.sin(i / 3) for i in range(5)]
    beta = [baseline * math.cos(i / 4 + 1) for i in range(5)]
    gamma = [(alpha[i] + beta[i]) / 2 for i in range(5)]
    return alpha, beta, gamma


def extract_peaks(signal, threshold=0.5):
    # Extracts peaks above threshold (partially relevant)
    peaks = []
    for i in range(1, len(signal) - 1):
        if signal[i] > threshold and signal[i] > signal[i-1] and signal[i] > signal[i+1]:
            peaks.append(i)
    return peaks or [0]


def compute_entropy(data):
    # Dead function — not used in final calculation (decoy)
    total = sum(data)
    if total == 0:
        return 0.0
    probs = [x / total for x in data]
    return -sum(p * math.log2(p) for p in probs if p > 0)


def filter_artifacts(samples, mode='median'):
    # Signal artifact removal — irrelevant path
    if mode == 'median':
        sorted_samples = sorted(samples)
        mid = len(sorted_samples) // 2
        return sorted_samples[mid]
    else:
        return sum(samples) / len(samples)


def validate_coherence(sequence):
    # Misleading coherence check — never called
    score = 0
    for a, b in zip(sequence, sequence[1:]):
        score += int(abs(a - b) < 0.3)
    return score / (len(sequence) - 1) if len(sequence) > 1 else 1.0


def transform_coordinates(x_vals, y_vals):
    # Distracting geometric transformation
    coords = []
    for i, (x, y) in enumerate(zip(x_vals, y_vals)):
        r = math.sqrt(x*x + y*y)
        theta = math.atan2(y, x)
        coords.append((r, theta + i*0.1))
    return coords


def analyze_signal_patterns(segments):
    # Core logic hidden among distractions
    cumulative_weight = 0
    pattern_scores = []
    
    for idx, seg in enumerate(segments):
        # Each segment is a tuple: (amplitude, duration, noise_level)
        amplitude, duration, noise = seg
        
        # Relevant logic: only high-amplitude, short-duration signals contribute
        if amplitude > 0.7 and duration < 2.0:
            # Compute weighted significance
            significance = amplitude * (1/duration) * (1 + noise)
            cumulative_weight += significance
            
        # Red herring: entropy-like accumulation (never used)
        dummy_entropy = 0
        for _ in range(3):
            dummy_entropy -= (significance/10) * math.log(significance/10 + 1e-8)
        
        # Store index-based adjustment (unused branch)
        if idx % 2 == 0:
            pattern_scores.append(amplitude * 100)

    # Final computation uses only cumulative_weight transformed
    normalized_index = int(cumulative_weight * 100) % 97
    
    # Apply secondary filter based on segment count
    if len(segments) >= 3:
        adjustment_factor = 3
    else:
        adjustment_factor = 1
    
    # Key result built from controlled logic chain
    base_diagnostic = normalized_index * adjustment_factor
    
    # Final red herring: unused conditional mutation
    if base_diagnostic > 50:
        temp_shift = math.floor(base_diagnostic / 7)
        # This alternate path is never taken due to input constraints
        alt = (base_diagnostic + temp_shift) % 89
    
    # Actual final value
    final_diagnostic = base_diagnostic + 13
    
    return final_diagnostic

# Main execution block
if __name__ == "__main__":
    # Input signal segments: (amplitude, duration, noise_level)
    signal_segments = [
        (0.85, 1.5, 0.12),
        (0.45, 3.2, 0.08),
        (0.92, 1.1, 0.15),
        (0.30, 0.8, 0.20),
        (0.78, 2.5, 0.10)
    ]

    # Irrelevant preprocessing steps
    freq_bands = generate_frequency_bands(0.6)
    all_peaks = [extract_peaks(fb) for fb in freq_bands]
    filtered_val = filter_artifacts([item for sublist in freq_bands for item in sublist])
    
    # Coordinate transformation on synthetic grid (distraction)
    x_data = [0.1, 0.3, 0.6, 0.8]
    y_data = [0.2, 0.5, 0.4, 0.9]
    transformed = transform_coordinates(x_data, y_data)
    
    # Real computation buried in middle
    final_diagnostic = analyze_signal_patterns(signal_segments)
    
    # Unused entropy validation
    decoy_sequence = [seg[0] for seg in signal_segments]
    # validate_coherence(decoy_sequence)  # Never assigned or used
    
    print(f"Result: {final_diagnostic}")