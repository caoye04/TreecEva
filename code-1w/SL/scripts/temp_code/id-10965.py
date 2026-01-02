import math

# Simulated sensor data processing with diagnostic analysis
def collect_sensor_data():
    raw_samples = [i * 0.1 for i in range(100)]
    noise_floor = 0.05
    return [math.sin(x) + noise_floor * (x % 2) for x in raw_samples]

def filter_outliers(data, threshold=0.1):
    mean_val = sum(data) / len(data)
    return [x for x in data if abs(x - mean_val) < threshold]

def compute_envelope(signal):
    return [abs(x) * 1.5 for x in signal]

def slice_critical_window(data, start=20, end=80):
    return data[start:end]

def shift_phase(signal, steps=5):
    # Irrelevant transformation - not used in final path
    return signal[steps:] + signal[:steps]

def compute_spectral_power(signal):
    # Distractor: looks important but unused
    return sum(x ** 2 for x in signal) / len(signal)

def generate_synthetic_reference(length):
    # Dead code path - never actually used
    return [0.5 * math.cos(i * 0.2) for i in range(length)]

def detect_artifacts(signal):
    # Misleading intermediate result
    artifact_score = 0
    for x in signal:
        if x > 0.8 or x < -0.8:
            artifact_score += 1
    return artifact_score > 10

def integrate_segments(segments):
    # Real computation: flattens list of lists
    flattened = [item for sublist in segments for item in sublist]
    return sum(flattened) / len(flattened)

def classify_rhythm(pattern):
    # Decoy function with plausible name
    if len(pattern) == 0:
        return 'undefined'
    avg = sum(pattern) / len(pattern)
    return 'stable' if avg > 0.3 else 'irregular'

def analyze_signal(segment_list):
    # Core logic hidden among distractions
    merged = integrate_segments(segment_list)
    adjustment_factor = 1.75
    
    # Apply non-linear correction
    corrected = math.log(merged * 2 + 1) * adjustment_factor
    
    # Red herring: conditional that always evaluates false due to prior filtering
    if detect_artifacts([corrected]):
        corrected *= 0.5
    
    # Final transformation
    return int(corrected * 1000) / 1000  # Round to 3 decimals

# Begin main execution
sensor_data = collect_sensor_data()
temp_filtered = filter_outliers(sensor_data, threshold=0.15)
enveloped_signal = compute_envelope(temp_filtered)

# Create multiple data segments (some irrelevant)
segment_a = slice_critical_window(enveloped_signal, 10, 40)
segment_b = slice_critical_window(enveloped_signal, 40, 70)
segment_c = slice_critical_window(enveloped_signal, 70, 90)

# Assemble relevant segments
processed_segments = [segment_a, segment_b, segment_c]

# Irrelevant variables and operations (distractors)
spectral_baseline = compute_spectral_power(enveloped_signal)
phase_shifted = shift_phase(enveloped_signal, 10)
reference_template = generate_synthetic_reference(len(sensor_data))
rhythm_type = classify_rhythm(segment_a)

# Key statement
final_diagnostic = analyze_signal(processed_segments)

# Output result
print(f"Result: {final_diagnostic}")