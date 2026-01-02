from collections import defaultdict, Counter
import math

# Simulated sensor array data (real values)
sensor_readings = [3.2, 4.1, 2.8, 5.6, 4.4, 3.9, 6.1, 5.0, 4.7, 5.3]

timestamps = [1623456780 + i*30 for i in range(len(sensor_readings))]
fault_flags = [False] * len(sensor_readings)

# Irrelevant auxiliary data (distractor)
dummy_mapping = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
shadow_buffer = [x**2 for x in range(10)]
offset_lookup = defaultdict(lambda: 100)

# Signal preprocessing
scaling_factor = 1.8
scaled_readings = [round(x * scaling_factor, 2) for x in sensor_readings]

# Apply moving average filter (relevant)
def apply_filter(data, window=3):
    filtered = []
    for i in range(len(data)):
        start = max(0, i - window + 1)
        filtered.append(sum(data[start:i+1]) / (i - start + 1))
    return filtered

smoothed_signal = apply_filter(scaled_readings)

# Frequency domain analysis (partially relevant, partially red herring)
def compute_dominant_frequency(signal):
    n = len(signal)
    fft_result = []
    for k in range(n // 2):
        real = sum(signal[t] * math.cos(2 * math.pi * k * t / n) for t in range(n))
        imag = sum(-signal[t] * math.sin(2 * math.pi * k * t / n) for t in range(n))
        fft_result.append(math.sqrt(real**2 + imag**2))
    return max(fft_result) if fft_result else 0.0

# Unused function - dead code path (distractor)
def legacy_calibrate(data):
    return [x * 0.95 for x in data if x > 4.0]

# Decoy transformation (misleading intermediate)
transformed_chain = []
for x in smoothed_signal:
    if x > 7.0:
        transformed_chain.append(math.log(x) * 2)
    else:
        transformed_chain.append(x / 2)

# Real processing begins here
baseline = sum(smoothed_signal) / len(smoothed_signal)
deviations = [abs(x - baseline) for x in smoothed_signal]

# Create threshold map using statistical heuristics
threshold_map = defaultdict(float)
threshold_map['low'] = baseline - deviations[len(deviations)//4]
threshold_map['high'] = baseline + deviations[3*len(deviations)//4]
threshold_map['critical'] = threshold_map['high'] * 1.3

# Simulated device profiles (cross-reference distractor)
device_profiles = {
    'sensor_a': {'gain': 1.1, 'offset': 0.5},
    'sensor_b': {'gain': 0.9, 'offset': -0.3}
}

profile_summary = Counter([k.split('_')[1] for k in device_profiles.keys()])

# Core analysis function
def analyze_signal(signal, thresholds):
    # Bit manipulation for diagnostic signature (relevant)
    sig_int = int(abs(signal[0]) * 100) & int(abs(signal[-1]) * 100)
    sig_int ^= (sig_int << 3) % 1024
    sig_int = (sig_int ^ (sig_int >> 5)) % 500
    
    # Sequence slicing for pattern detection
    mid_segment = signal[len(signal)//4 : 3*len(signal)//4]
    peak_count = sum(1 for x in mid_segment if x > thresholds['high'])
    
    # Hidden dependency on modular arithmetic
    cycle_marker = len(signal) % 4
    adjustment = (cycle_marker * peak_count) % 7
    
    # Actual answer derivation (non-obvious)
    base_score = 0
    for i, val in enumerate(signal):
        if val > thresholds['critical']:
            base_score += i * 3
        elif val > thresholds['high']:
            base_score += i * 2
    
    # Final computation - this is where the answer comes from
    final_score = base_score - adjustment + sig_int
    
    # Irrelevant formatting (distractor)
    report = f"Diagnostic-{final_score:04d}: OK"
    metadata_stack = [{'level': i, 'valid': True} for i in range(final_score % 10)]
    
    return final_score

# Trigger execution point
processed_data = smoothed_signal[::2]  # Every other reading
final_diagnostic = analyze_signal(processed_data, threshold_map)
print(f"Result: {final_diagnostic}")