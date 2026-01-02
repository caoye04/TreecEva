import math

def preprocess_signal(raw_readings):
    filtered = [x for x in raw_readings if abs(x) > 0.1]
    baseline = sum(filtered) / len(filtered)
    return [x - baseline for x in filtered]

def compute_harmonic_distortion(waveform):
    # Irrelevant computation path (dead function)
    total_power = sum(x**2 for x in waveform)
    fundamental = max(waveform) ** 2
    return (total_power - fundamental) / total_power if total_power else 0

def generate_checksum(sequence):
    # Distractor: looks important but unused in final result
    checksum = 0
    for i, val in enumerate(sequence):
        checksum ^= int(val * 100) & 0xFF
    return checksum

def validate_coherence(samples, threshold=0.85):
    # Misleading intermediate: appears to affect flow but doesn't
    if len(samples) < 10:
        return False
    coherence = sum(1 for a, b in zip(samples, samples[1:]) if abs(a - b) < 0.5)
    ratio = coherence / (len(samples) - 1) if len(samples) > 1 else 0
    return ratio > threshold

def extract_phase_envelope(turbine_signals):
    envelope = []
    for signal_group in turbine_signals:
        analytic = [abs(x) for x in signal_group]
        peak = max(analytic) if analytic else 0
        envelope.append(peak * 0.87)
    return envelope

def decode_frequency_shift(signal, ref_freq=50.0):
    # Unused red herring function
    shift = 0
    for i in range(len(signal)):
        shift += math.sin(signal[i] * ref_freq) * 0.01
    return shift

def aggregate_metrics(sensor_data, calibration):
    # Core relevant logic starts here
    adjusted_readings = []
    for idx, reading in enumerate(sensor_data):
        calibrated_value = reading * calibration[idx % len(calibration)]
        adjusted_readings.append(calibrated_value)
    
    # Apply preprocessing (relevant)
    processed = preprocess_signal(adjusted_readings)
    
    # Compute diagnostic envelope (relevant)
    squared_filtered = [x**2 for x in processed if x > -1.0]
    if len(squared_filtered) == 0:
        squared_filtered = [0.0]
    
    # Simulate multi-stage transformation
    log_transform = [math.log(v + 1) for v in squared_filtered]
    averaged = sum(log_transform) / len(log_transform)
    
    # Introduce modular arithmetic masking
    mask_seed = len(log_transform) % 7
    masked = averaged * (mask_seed + 1)
    
    # Final calculation with case-sensitive flag emulation
    mode_flag = 'HIGH_RES'
    resolution_factor = 3.2 if mode_flag.lower() == 'high_res' else 1.0
    
    # Critical assignment
    final_diagnostic = int((masked * resolution_factor * 100) % 97843) + 10000
    
    # Dead code branches below
    if final_diagnostic < 0:
        final_diagnostic = -final_diagnostic
    elif final_diagnostic > 50000:
        temp_buffer = [final_diagnostic % i for i in range(2, 11) if i % 3 != 0]
        final_diagnostic += sum(temp_buffer) // len(temp_buffer)

    return final_diagnostic

# Simulated sensor input (real data)
turbine_data = [
    0.12, -0.34, 0.56, -0.78, 0.91, -1.05, 1.12, -0.43, 0.25, 0.67,
    -0.89, 1.01, -1.23, 0.44, -0.65, 0.76, -0.98, 1.09, -1.15, 0.33
]

calibration_sequence = [1.05, 0.98, 1.02, 1.11, 0.93]

# Trigger key computation
final_diagnostic = aggregate_metrics(turbine_data, calibration_sequence)

# Output result
print(f"Result: {final_diagnostic}")