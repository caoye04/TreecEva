import math

# Simulated sensor data processing system for aerospace diagnostics
def collect_sensor_data():
    raw_readings = [i * 0.7854 + (i % 3) for i in range(15)]
    timestamps = [t * 100 + 50 for t in range(15)]
    metadata_flags = [0b1010, 0b1100, 0b1111, 0b0000]  # Irrelevant flag set
    return list(zip(timestamps, raw_readings))


def filter_noise(data_sequence):
    filtered = []
    noise_floor = 2.5
    for ts, val in data_sequence:
        if abs(val) > noise_floor:
            adjusted = val * 0.85
            filtered.append((ts, adjusted))
        else:
            filtered.append((ts, val * 0.1))  # Dampened low signals
    return filtered


def compute_envelope(signal_chain):
    envelope = []
    for index, (ts, sample) in enumerate(signal_chain):
        magnitude = abs(sample)
        phase_shift = math.sin(index * 0.5)
        enveloped = magnitude * (1 + phase_shift)
        envelope.append(enveloped)
    return envelope


def detect_peaks(envelope_values):
    peaks = []
    for i in range(1, len(envelope_values) - 1):
        if envelope_values[i] > envelope_values[i-1] and envelope_values[i] > envelope_values[i+1]:
            peaks.append((i, envelope_values[i]))
    return peaks[:5]  # Limit to first 5 peaks


def compress_frame(frame_data):
    # Dead function - never used in execution path
    return [x * 2 for x in frame_data if x > 1]


def integrate_segments(peaks_list):
    total_integral = 0.0
    base_offset = 0.97
    for pos, val in peaks_list:
        contribution = val * math.log(2 + pos) * base_offset
        total_integral += contribution
        base_offset *= 0.995
    return total_integral


def generate_checksum(sequence):
    # Decoy function: looks important but unused
    chk = 0
    for item in sequence:
        if isinstance(item, tuple):
            chk ^= int(item[0])
        else:
            chk ^= int(item * 100)
    return chk


def slice_window(data_stream, start=3, end=12):
    # Slicing with fixed window
    return data_stream[start:end]


def extract_features(windowed_data):
    feature_map = {}
    squared_sum = sum(x**2 for x in windowed_data)
    mean_val = sum(windowed_data) / len(windowed_data)
    variance = sum((x - mean_val)**2 for x in windowed_data) / len(windowed_data)
    feature_map['rms'] = math.sqrt(squared_sum / len(windowed_data))
    feature_map['skew_hint'] = (squared_sum / len(windowed_data)) / (variance + 1e-8)
    return feature_map


def finalize_diagnostic(features, integral_score):
    # Final fusion logic
    risk_factor = 1.0
    if features['rms'] > 5.0:
        risk_factor += 0.7
    if features.get('skew_hint', 0) > 3.5:
        risk_factor += 0.4
    
    # Core computation
    diagnostic_score = integral_score * risk_factor
    
    # Red herring variables
    temp_buffer = [diagnostic_score * 0.1 for _ in range(5)]
    debug_trace = {'stage': 'final', 'score_raw': integral_score, 'buffer_len': len(temp_buffer)}
    
    return diagnostic_score

# Misleading auxiliary transformation
def transform_coordinates(coord_list):
    transformed = []
    for i, c in enumerate(coord_list):
        lat = c[0] * math.cos(i)
        lon = c[1] * math.sin(i)
        transformed.append((lat, lon))
    return transformed

# Main execution chain
def main_pipeline():
    # Step 1: Collect raw data
    raw_frames = collect_sensor_data()  # Contains timestamped readings
    
    # Step 2: Filter out noise
    cleaned_frames = filter_noise(raw_frames)
    
    # Step 3: Extract values for envelope detection
    signal_values = [val for _, val in cleaned_frames]
    
    # Step 4: Apply slicing window (relevant)
    windowed_signal = slice_window(signal_values, start=2, end=13)
    
    # Step 5: Compute envelope of the signal
    envelope_curve = compute_envelope(list(enumerate(windowed_signal)))
    
    # Step 6: Detect significant peaks
    detected_peaks = detect_peaks(envelope_curve)
    
    # Step 7: Integrate peak contributions
    integrated_energy = integrate_segments(detected_peaks)
    
    # Step 8: Extract statistical features from windowed signal
    statistical_features = extract_features(windowed_signal)
    
    # Step 9: Final diagnostic synthesis
    final_diagnostic = finalize_diagnostic(statistical_features, integrated_energy)
    
    # === DO NOT MODIFY BELOW THIS LINE ===
    print(f"Result: {final_diagnostic}")
    return final_diagnostic

# Execute
result = main_pipeline()