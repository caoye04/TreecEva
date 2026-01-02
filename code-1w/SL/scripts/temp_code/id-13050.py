import math

# System health monitoring simulation with signal encoding and noise filtering
def analyze_signal_integrity(raw_samples, threshold=0.75):
    filtered = [x for x in raw_samples if abs(x) > threshold]
    if len(filtered) == 0:
        return 0.0
    avg_power = sum(x * x for x in filtered) / len(filtered)
    peak_value = max(filtered, key=abs)
    return round(avg_power / (1 + abs(peak_value)), 3)

# Irrelevant helper: computes unused spectral density (red herring)
def compute_spectral_density(data):
    n = len(data)
    if n == 0:
        return 0.0
    squared_sum = sum(d ** 2 for d in data)
    return squared_sum / n if n > 0 else 0.0

# Signal encoder using bitwise manipulation and modular arithmetic
def encode_signal(value, mode='advanced'):
    shifted = (value << 2) & 0xFF
    toggled = shifted ^ 0b10101010
    if mode == 'basic':
        return toggled % 128
    return (toggled + 17) % 256

# Segment processor with conditional expression and distractor logic
def process_segment(segment_data, flags):
    base_score = sum(encode_signal(x) for x in segment_data)
    adjustment = 10 if 'optimize' in flags else -5
    # Complex conditional expression (required Python feature)
    normalized = base_score / (len(segment_data) if len(segment_data) > 0 else 1)
    secondary_metric = math.log2(normalized) if normalized > 1 else 0.0
    
    # Dead code path - never executed due to flag constraint (distractor)
    if 'legacy_mode' in flags:
        fallback = [x >> 1 for x in segment_data]
        secondary_metric += sum(fallback)

    return {
        'encoded_sum': base_score,
        'normalized': normalized,
        'diagnostic': secondary_metric,
        'size': len(segment_data)
    }

# Decoy function that looks important but isn't used in main flow
def generate_calibration_sequence(n):
    seq = []
    for i in range(n):
        val = (i * i + 3 * i + 7) % 101
        seq.append(val ^ (val >> 1))
    return seq

# Core aggregation with weighted combination and rounding behavior
def aggregate_metrics(segments, weight_vector):
    if not segments:
        return 0.0
    total_weighted = 0.0
    total_influence = 0.0
    for i, seg in enumerate(segments):
        weight = weight_vector[i % len(weight_vector)]
        # Key computation branch
        if seg['size'] > 0:
            metric = seg['normalized'] * seg['diagnostic']
            total_weighted += weight * metric
            total_influence += weight * seg['size']
    # Final adjustment based on average influence
    avg_influence = total_influence / len(segments)
    final_value = total_weighted + (avg_influence / 100)
    return round(final_value, 4)

# Unused noise modeling component (extensive red herring)
class NoiseModel:
    def __init__(self, level=1.0):
        self.level = level
        self.pattern = [math.sin(i / 10) * level for i in range(100)]

    def apply_filter(self, x):
        return x + self.pattern[abs(hash(str(x))) % 100]

# Main execution workflow
if __name__ == '__main__':
    # Input data: simulated sensor readings
    raw_input_stream = [0.1, 0.82, -1.3, 0.95, 0.4, -0.76, 1.1, 0.63]
    
    # Extract non-trivial components above noise floor
    significant_peaks = [x for x in raw_input_stream if abs(x) >= 0.75]
    
    # Compute irrelevant diagnostic (distractor)
    spectral_index = compute_spectral_density(raw_input_stream)
    
    # Encode each peak into diagnostic byte space
    encoded_peaks = [encode_signal(int(abs(p) * 50)) for p in significant_peaks]
    
    # Create multiple data segments for processing
    segment_pool = [
        [12, 8, 23],
        [19, 14],
        [7, 31, 11, 25]
    ]
    
    # Process each segment with different flags (only 'optimize' matters)
    processed_segments = []
    for idx, seg in enumerate(segment_pool):
        flags = ['optimize'] if idx % 2 == 0 else []
        result = process_segment(seg, flags)
        processed_segments.append(result)
    
    # Apply signal integrity analysis on raw peaks (unused result - misleading)
    phantom_diagnostic = analyze_signal_integrity(significant_peaks)
    
    # Weight vector for aggregation step
    weights = [0.8, 1.2, 0.9]
    
    # Critical statement: compute final diagnostic score
    final_diagnostic = aggregate_metrics(processed_segments, weights)
    
    # Print target result
    print(f"Target result: {final_diagnostic}")