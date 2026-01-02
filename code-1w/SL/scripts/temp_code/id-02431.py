import math

# Simulated sensor fusion system for environmental monitoring
def collect_samples(duration, interval):
    samples = []
    t = 0
    while t < duration:
        # Real signal: damped harmonic + noise
        raw_value = 12.5 * math.exp(-0.1 * t) * math.cos(2 * math.pi * 0.3 * t) + 0.8
        samples.append(round(raw_value, 3))
        t += interval
    return samples

# Irrelevant helper - decoy function (dead code path)
def deprecated_filter(data):
    return [x for x in data if x > 5]  # Unused

# Signal processing pipeline
def normalize(signal):
    if not signal:
        return []
    max_val, min_val = max(signal), min(signal)
    if max_val == min_val:
        return [0.5] * len(signal)
    return [(x - min_val) / (max_val - min_val) for x in signal]

def window_smooth(signal, w=3):
    smoothed = signal[:]
    for i in range(1, len(signal) - 1):
        subset = signal[max(0, i - w//2):min(len(signal), i + w//2 + 1)]
        smoothed[i] = sum(subset) / len(subset)
    return smoothed

# Feature extraction
def extract_peaks(signal):
    peaks = []
    for i in range(1, len(signal) - 1):
        if signal[i] > signal[i-1] and signal[i] > signal[i+1]:
            peaks.append(i)
    return peaks

def compute_entropy(signal):
    from collections import Counter
    counts = Counter([round(x, 1) for x in signal])
    total = len(signal)
    entropy = -sum((count/total) * math.log2(count/total) for count in counts.values())
    return round(entropy, 4)

# Set-based interference: irrelevant classification groups
all_bands = {'alpha', 'beta', 'gamma', 'delta', 'theta'}
valid_bands = {'alpha', 'gamma', 'delta'}
dropped_bands = all_bands - valid_bands  # Decoy variable

# Core analysis chain
def preprocess_signal(raw_data):
    stage1 = [x for x in raw_data if abs(x) <= 20]  # Filter outliers
    stage2 = normalize(stage1)
    stage3 = window_smooth(stage3)  # Bug: typo - should be stage2
    stage3 = window_smooth(stage2)  # Correction
    return [round(x, 4) for x in stage3]

# Red herring: unused transformation tree
class LegacyProcessor:
    def __init__(self):
        self.depth = 2
    
    def transform(self, x):
        return math.tanh(x)  # Never instantiated

# Actual processing workflow
def analyze_frequency_components(signal):
    # Simulate FFT bins
    n = len(signal)
    components = []
    for k in range(n//4):
        real = sum(signal[i] * math.cos(2*math.pi*k*i/n) for i in range(n))
        imag = sum(-signal[i] * math.sin(2*math.pi*k*i/n) for i in range(n))
        magnitude = math.sqrt(real**2 + imag**2)
        components.append(magnitude)
    top_three = sorted(components, reverse=True)[:3]
    return round(sum(top_three), 3)

# Distractor: complex but unused combinatorics
def count_valid_subsequences(arr, threshold):
    count = 0
    n = len(arr)
    for i in range(1, 2**n):
        subset = [arr[j] for j in range(n) if (i & (1 << j))]
        if len(subset) >= 2 and max(subset) - min(subset) <= threshold:
            count += 1
    return count  # Computed but unused

# Main diagnostic logic
def generate_baseline_profile(length):
    profile = []
    for i in range(length):
        val = (math.sin(0.5 * i) + math.cos(0.3 * i)) / 2
        profile.append(max(0, val))
    return profile

def compare_with_baseline(processed, baseline):
    diff_sum = sum(abs(a - b) for a, b in zip(processed, baseline))
    return diff_sum / len(processed)

# Critical path with set operation distraction
def analyze_readings(signals):
    processed = preprocess_signal(signals)
    baseline = generate_baseline_profile(len(processed))
    
    # Extract key metrics
    peak_indices = extract_peaks(processed)
    entropy_score = compute_entropy(processed)
    freq_energy = analyze_frequency_components(processed)
    
    # Interference: irrelevant set operations on dummy categories
    mode_set = {'sensor_A', 'sensor_B', 'fusion_mode'}
    active_modes = {'sensor_A', 'fusion_mode'}
    inactive = mode_set - active_modes  # Misleading variable
    priority_flag = 'fusion_mode' in active_modes and len(inactive) < 2  # Truthy red herring
    
    # Core computation
    deviation = compare_with_baseline(processed, baseline)
    peak_factor = len(peak_indices) * 100
    
    # Final diagnostic formula
    raw_diagnostic = (freq_energy * 15) - (deviation * 50) + peak_factor
    final_diagnostic = int(round(raw_diagnostic + entropy_score * 10))
    
    # Decoy output line (not printed)
    debug_status = f"Analyzed {len(signals)} samples with {len(peak_indices)} peaks"
    
    return final_diagnostic

# Generate input data
raw_signals = collect_samples(duration=15, interval=0.5)

# Dead code path: unused combinatorial analysis
combinatorial_count = count_valid_subsequences(raw_signals, 0.75)

# Process signals
processed_signals = preprocess_signal(raw_signals)

# Trigger key statement
final_diagnostic = analyze_readings(processed_signals)

# Output result
print(f"Result: {final_diagnostic}")