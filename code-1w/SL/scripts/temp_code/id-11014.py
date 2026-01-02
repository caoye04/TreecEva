import math

# Simulated sensor array data processing for aerospace telemetry
def process_telemetry_stream(raw_signal, calibration_factor):
    # Irrelevant transformation (distractor)
    normalized = [x * 0.987 for x in raw_signal if x > 0]
    filtered = [val for val in normalized if val < 500]

    # Key segmentation logic
    window_size = 4
    segments = [filtered[i:i+window_size] for i in range(0, len(filtered), window_size)]
    trimmed_segments = [seg for seg in segments if len(seg) == window_size]

    # Bit manipulation red herring
    checksum = 0
    for seg in trimmed_segments:
        temp = int(sum(seg))
        checksum ^= (temp << 2) | (temp >> 1)

    # Decoy statistical analysis
    mean_val = sum(normalized) / len(normalized) if normalized else 0
    variance = sum((x - mean_val) ** 2 for x in normalized) / len(normalized) if normalized else 0
    outlier_threshold = mean_val + 2 * math.sqrt(variance) if variance > 0 else 100

    # Irrelevant frequency domain simulation
    freq_components = []
    for i in range(3):
        component = sum(math.sin(x * (i+1)) for x in raw_signal[:10])
        freq_components.append(component)

    # Actual encoding path (non-obvious due to distractions)
    encoded_segments = []
    for idx, segment in enumerate(trimmed_segments):
        # Core arithmetic and modular logic
        encoded = 0
        for j, val in enumerate(segment):
            encoded += (val % 17) * (j + 1)  # Modular arithmetic with positional weight
        encoded = (encoded * calibration_factor) % 97
        if idx % 2 == 0:
            encoded = int(math.sqrt(encoded) * 10) if encoded > 0 else 0  # Conditional transformation
        encoded_segments.append(encoded)

    return encoded_segments

# Auxiliary function with misleading complexity
def compute_thermal_compensation(temps):
    base = sum(t ** 0.5 for t in temps if t > -273) / len(temps)
    adjustment = 0
    for t in temps:
        if t < 0:
            adjustment += 0.1
        elif t > 100:
            adjustment -= 0.05
    return base + adjustment

# Unused but plausible-looking diagnostic routine (dead code path)
def legacy_diagnostics(data):
    result = 1
    for item in data:
        result = (result * (item + 1)) % 10009
    return result

# Main execution flow
def aggregate_metrics(segments, weights):
    # Weighted fusion with conditional override
    total_weighted = 0
    max_segment_value = max(segments) if segments else 0

    # Spurious control flow
    if max_segment_value > 50:
        threshold_adjust = math.log(max_segment_value)
    else:
        threshold_adjust = 1.0

    # Real computation buried in noise
    weighted_sum = 0
    for i, val in enumerate(segments):
        w = weights[i % len(weights)]
        contribution = val * w
        # Conditional expression distraction
        adjusted = contribution * 1.1 if i % 3 == 0 else contribution * 0.95
        weighted_sum += adjusted

    # Final nonlinear transformation
    final_score = int(weighted_sum / len(segments)) if segments else 0

    # Critical red herring: buffer overflow mimicry (irrelevant)
    buffer_state = 0
    for bit in range(8):
        buffer_state |= (1 << bit) if (final_score >> bit) & 1 else 0

    # Real answer generation (non-trivial to trace due to context)
    stability_index = 0
    for s in segments:
        stability_index += (s * s) % 13

    final_diagnostic = (final_score + stability_index) % 10000

    # Another decoy metric
    coherence_ratio = sum(1 for i in range(1, len(segments)) if segments[i] > segments[i-1]) / (len(segments)-1) if len(segments) > 1 else 0

    return final_diagnostic

# Execution entry point
if __name__ == '__main__':
    # Input data (real signal pattern)
    telemetry_input = [123, 45, 67, 200, 150, 88, 44, 166, 199, 50, 75, 130, 180, 90, 60, 210]
    calibration = 3
    weights = [0.8, 1.2, 0.9, 1.1]

    # Thermal data for decoy function
    temperature_log = [22.5, 23.1, 21.8, 24.0, 25.2, 20.3, 26.1]

    # Execute main processing chain
    processed_segments = process_telemetry_stream(telemetry_input, calibration)
    
    # Compute thermal compensation (unused result - red herring)
    compensation_factor = compute_thermal_compensation(temperature_log)

    # Generate final diagnostic
    final_diagnostic = aggregate_metrics(processed_segments, weights)

    # Output target variable
    print(f"Result: {final_diagnostic}")