import math

# Irrelevant helper function (dead code path)
def normalize_vector(v):
    norm = sum(x ** 2 for x in v) ** 0.5
    return [x / norm for x in v] if norm > 0 else v

# Distractor: Unused signal processing chain
class FilterBank:
    def __init__(self, bands):
        self.bands = bands
        self.gain = 1.0

    def apply(self, x):
        return [xi * self.gain for xi in x]

# Core logic: Pattern analyzer with red herrings
def extract_features(seq):
    length = len(seq)
    peaks = [i for i in range(1, length - 1) if seq[i] > seq[i-1] and seq[i] > seq[i+1]]
    troughs = [i for i in range(1, length - 1) if seq[i] < seq[i-1] and seq[i] < seq[i+1]]
    
    # Real feature: alternating pattern score
    alternations = 0
    for i in range(1, length):
        if (seq[i] - seq[i-1]) * (seq[i-1] - (seq[i-2] if i >= 2 else seq[i-1])) < 0:
            alternations += 1
    
    # Irrelevant derived metrics (distractors)
    avg = sum(seq) / length if length else 0
    variance = sum((x - avg) ** 2 for x in seq) / length if length else 0
    entropy_proxy = -sum(x * math.log(abs(x) + 1e-8) for x in seq) / length
    
    return {
        'peak_count': len(peaks),
        'trough_count': len(troughs),
        'alternation_score': alternations / length if length else 0,
        'mean_val': avg,  # distractor
        'variance': variance,  # distractor
        'entropy_like': entropy_proxy  # distractor
    }

# Secondary analysis with conditional logic
def evaluate_stability(features, sensitivity):
    base_score = features['alternation_score'] * 100
    
    # Real decision path
    adjustment = 0
    if features['peak_count'] > features['trough_count']:
        adjustment += 5
    elif features['trough_count'] > features['peak_count']:
        adjustment -= 3
    
    # Distractor: unused complex calculation
    decay_factor = math.exp(-sensitivity * features['variance'])
    dummy_score = base_score * decay_factor + features['entropy_like']
    
    return base_score + adjustment

# Main analyzer with slicing and conditional expression
def analyze_pattern(signal, threshold):
    if len(signal) < 3:
        return 0
    
    # Use slicing to focus on core segment (middle 60%)
    trim_offset = len(signal) // 5
    trimmed = signal[trim_offset:-trim_offset] if trim_offset else signal
    
    # Extract meaningful features
    features = extract_features(trimmed)
    
    # Evaluate dynamic stability
    stability = evaluate_stability(features, sensitivity=0.4)
    
    # Compute noise ratio (distractor)
    noise_estimate = sum(1 for x in trimmed if abs(x) < 0.1)
    noise_ratio = noise_estimate / len(trimmed) if trimmed else 0
    
    # Critical computation path
    baseline = 42.0
    modifier = 1.75 if features['alternation_score'] > threshold else 0.85
    
    # Final diagnostic uses conditional expression and multiple dependencies
    preliminary = (stability * modifier) + baseline
    final_diagnostic = preliminary if preliminary > 50 else 50  # floor at 50
    
    # Dead code branch (never reached due to logic above)
    if noise_ratio > 0.8:
        fallback = sum(trimmed) * 100
        final_diagnostic = max(final_diagnostic, fallback)
    
    return final_diagnostic

# Generate signal with embedded pattern
phase = [math.sin(0.3 * i) + 0.5 * math.sin(0.7 * i + 1.2) for i in range(50)]
noisy_phase = [p + 0.05 * math.cos(5 * i) for i, p in enumerate(phase)]  # high-freq noise
signal_sequence = [round(x, 3) for x in noisy_phase]  # final signal

# Add irrelevant data structure
lookup_table = {i: round(math.tanh(x), 4) for i, x in enumerate(signal_sequence)}
decoy_array = [abs(x) ** 0.5 for x in signal_sequence if x < 0]

# Execute main analysis
temp_result = sum(signal_sequence[i] for i in range(0, len(signal_sequence), 5))  # distractor sum
flag = True if temp_result > 10 else False  # misleading flag

final_diagnostic = analyze_pattern(signal_sequence, threshold=0.65)
print(f"Result: {final_diagnostic}")