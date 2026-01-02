from collections import defaultdict, Counter
import math

# Irrelevant sensor simulation data
temperature_readings = [23.4, 24.1, 22.9, 25.6, 26.0, 24.8, 23.7]
humidity_readings = [45, 48, 50, 44, 47, 49, 51]

# Distractor: unused function
def legacy_calibrate(x):
    return [val * 0.98 for val in x if val > 20]

def preprocess_stream(data, mode='strict'):
    if mode == 'strict':
        cleaned = [x for x in data if x is not None and x >= 0]
        smoothed = []
        for i in range(len(cleaned)):
            window = cleaned[max(0, i-2):i+1]
            smoothed.append(sum(window) / len(window))
        return [round(x, 2) for x in smoothed]
    return data

def generate_key(signal, shift):
    base = 1
    for s in signal[:5]:
        base *= (int(s) + 1) if s > 0 else 1
    return (base % 97) + shift

# Complex configuration with red herrings
class DiagnosticsConfig:
    def __init__(self):
        self.thresholds = defaultdict(lambda: 1.0)
        self.thresholds['primary'] = 0.75
        self.thresholds['fallback'] = 1.2
        self.debug_mode = True
        self.max_iterations = 15
        self._internal_seed = 2024

def transform_sequence(seq, key):
    # Bit manipulation mixed with arithmetic
    transformed = []
    for idx, val in enumerate(seq):
        shifted = (val * 100) >> 1
        masked = shifted & 0xFF
        if idx % 3 == 0:
            masked ^= key
        elif idx % 3 == 1:
            masked += key % 17
        else:
            masked -= key // 10
        transformed.append(masked % 100)
    return transformed

# Misleading auxiliary function that looks important but is never called
def compute_entropy(data):
    counts = Counter(data)
    total = len(data)
    entropy = 0.0
    for count in counts.values():
        p = count / total
        entropy -= p * math.log2(p)
    return round(entropy, 3)

# Core logic buried among distractions
def analyze_pattern(data, config):
    score = 0
    streak = 0
    last = -1
    
    for val in data:
        if val > config.thresholds['primary'] * 45:
            score += val // 7
            streak += 1
            if streak == 3:
                score += 10
        else:
            streak = 0
        
        # Secondary check with hidden logic
        if val % 5 == 0 and val != last:
            score += 2
        last = val
    
    # Tertiary adjustment based on distribution
    unique_vals = set(data)
    if len(unique_vals) > 7:
        score += 5
    
    # Hidden offset
    offset = sum(1 for v in data if v in [12, 18, 22]) * 3
    return score + offset

# Unused but plausible-looking diagnostic routine
def validate_consistency(trace):
    return all(abs(trace[i] - trace[i-1]) < 15 for i in range(1, len(trace)))

# Main execution chain
if __name__ == '__main__':
    raw_signal = [0.88, 1.02, 0.75, 1.15, 0.94, 1.08, 1.22, 0.69, 1.31, 0.83, 0.97]
    
    # Irrelevant preprocessing branch
    filtered_noise = [x for x in raw_signal if 0.7 <= x <= 1.3]
    calibrated = [x * 1.02 for x in filtered_noise]
    
    # Distractor variables
    baseline_avg = sum(calibrated) / len(calibrated)
    deviation_score = sum(abs(x - baseline_avg) for x in calibrated)
    
    processed = preprocess_stream(calibrated)
    
    # Generate key using obscure logic
    int_sequence = [int(x * 50) for x in processed]
    access_key = generate_key(int_sequence, len(processed))
    
    # Transform into analysis domain
    transformed_data = transform_sequence(int_sequence, access_key)
    
    # Configure system
    config = DiagnosticsConfig()
    config.thresholds['primary'] = 0.8
    
    # Critical statement
    final_diagnostic = analyze_pattern(transformed_data, config)
    
    # Red herring: potential override path that never triggers
    if sum(transformed_data) < 0:
        final_diagnostic = -1  # Dead code
    
    # Another decoy calculation
    summary_stats = lambda data: {
        'range': max(data) - min(data),
        'peaks': len([d for d in data[1:-1] if data[i] > data[i-1] and data[i] > data[i+1]])
    }
    stats = summary_stats(transformed_data)
    
    print(f"Result: {final_diagnostic}")