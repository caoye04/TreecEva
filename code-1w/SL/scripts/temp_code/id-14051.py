from collections import defaultdict
import math

# Simulated sensor data processing with noise filtering and pattern recognition
def preprocess_signal(raw_readings):
    filtered = []
    noise_floor = 0.05
    for val in raw_readings:
        if abs(val) > noise_floor:
            filtered.append(round(val * 100) / 100)
    return filtered

# Irrelevant helper: spectral weight calculation (unused in final path)
def compute_spectral_weight(seq):
    total = 0
    for i, x in enumerate(seq):
        total += x * math.sin(i)
    return total

# Misleading transformation: frequency folding (dead code path)
def fold_frequency(signal):
    folded = []
    for i in range(len(signal)//2):
        folded.append(signal[i] + signal[-(i+1)])
    return folded

# Core pattern analyzer: counts specific rising edge patterns above thresholds
def detect_pattern_segments(signal, config):
    segments = 0
    for i in range(1, len(signal)):
        delta = signal[i] - signal[i-1]
        if delta > config['rise_threshold'] and signal[i] > config['amplitude_min']:
            segments += 1
    return segments

# Decoy function: simulates calibration but returns dummy value
def run_calibration(sequence):
    if not sequence:
        return {'status': 'fail', 'level': 0}
    magnitude = sum(x**2 for x in sequence)
    return {'status': 'ok', 'level': magnitude // 100}

# Central analysis: combines pattern detection with mapped thresholds
def analyze_signal(buffer, threshold_lookup):
    base_patterns = detect_pattern_segments(buffer, {
        'rise_threshold': threshold_lookup['alpha'],
        'amplitude_min': threshold_lookup['beta']
    })
    
    # Distractor: unused secondary metric
    entropy_proxy = 0
    count_map = defaultdict(int)
    for x in buffer:
        bin_key = int(x * 10)
        count_map[bin_key] += 1
    for count in count_map.values():
        if count > 1:
            entropy_proxy -= count * math.log(count)
    
    # Red herring: complex but unused transformation chain
    transformed = [math.cos(x) for x in buffer if x > 0.1]
    squared_peaks = [y**2 for y in transformed if y < 0]
    peak_summation = sum(squared_peaks) if squared_peaks else 0.0
    
    # Critical logic: apply gamma adjustment to base pattern count
    gamma_factor = threshold_lookup['gamma']
    adjusted_score = base_patterns * (gamma_factor + 1)
    
    # Secondary effect: add bonus if certain rare condition met
    if len([x for x in buffer if x > 0.75]) >= 2:
        adjusted_score += 3
    
    # Final diagnostic computed from adjusted pattern score
    final_value = int(adjusted_score * 17)  # Prime multiplier for non-linearity
    return final_value

# Setup: synthetic signal generation
raw_data_stream = [
    0.01, -0.02, 0.03, 0.15, 0.22, 0.35, 0.18, 0.41, 0.62, 0.78,
    0.21, 0.33, 0.51, 0.88, 0.91, 0.44, 0.19, 0.67, 0.73, 0.55
]

# Irrelevant pre-processing trace
normalized_data = [round(x*1.05, 3) for x in raw_data_stream]
calibration_result = run_calibration(normalized_data)

# Actual processing path
pattern_buffer = preprocess_signal(raw_data_stream)

# Threshold configuration map (critical parameter input)
threshold_map = {
    'alpha': 0.12,   # rise threshold
    'beta': 0.30,    # amplitude minimum
    'gamma': 2       # gamma adjustment factor
}

# Dead code: simulated multi-channel merge (unused)
secondary_channel = [x * 0.5 for x in pattern_buffer if x > 0.4]
merged_signal = []
i, j = 0, 0
while i < len(pattern_buffer) and j < len(secondary_channel):
    merged_signal.append(pattern_buffer[i] + secondary_channel[j])
    i += 2
    j += 1

# Key execution point
final_diagnostic = analyze_signal(pattern_buffer, threshold_map)

# Output result
print(f"Result: {final_diagnostic}")