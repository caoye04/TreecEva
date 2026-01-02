import math

# Simulated neuroimaging data processing pipeline
def analyze_neural_pattern(frequency_bands):
    baseline = sum(frequency_bands) / len(frequency_bands)
    variance = sum((x - baseline) ** 2 for x in frequency_bands) / len(frequency_bands)
    coherence = math.exp(-variance / 100.0)

    # Irrelevant transformations (distractors)
    temp_spectrum = [x * 0.87 + 3 for x in frequency_bands]
    normalized = [max(0, min(100, (x - 5) * 2)) for x in temp_spectrum]
    entropy_proxy = -sum(x / 100 * math.log(x / 100 + 1e-9) for x in normalized)

    return coherence, variance, baseline


# Signal quality assessment heuristics (mostly unused)
def evaluate_artifact_suppression(signal_trace):
    peak_noise = max(signal_trace)
    rms_noise = math.sqrt(sum(x**2 for x in signal_trace) / len(signal_trace))
    suppression_ratio = (peak_noise / (rms_noise + 1e-6))

    # Dead code path (red herring)
    if suppression_ratio < 1.0:
        adjustment_factor = 0.0
        for i in range(len(signal_trace)):
            adjustment_factor += math.sin(signal_trace[i] / 10)
        return adjustment_factor

    return rms_noise


# Core diagnostic evaluation algorithm
def compute_filtration_index(data_stream):
    window_size = 4
    segments = [data_stream[i:i+window_size] for i in range(0, len(data_stream), window_size)]
    
    # Slice only complete segments
    valid_segments = [s for s in segments if len(s) == window_size]
    
    # Compute segment energies using lambda abstraction
    energy_calculator = lambda seg: sum(x**2 for x in seg)
    energies = [energy_calculator(seg) for seg in valid_segments]
    
    # Bitwise interference pattern analysis (distractor)
    signature = 0
    for e in energies[:3]:
        signature ^= int(e) & 0xFF
        signature = (signature << 1) | (signature >> 7)
    
    # Actual relevant logic
    avg_energy = sum(energies) / len(energies) if energies else 0
    fluctuation_index = sum(abs(energies[i] - energies[i-1]) for i in range(1, len(energies)))
    stability_metric = fluctuation_index / (avg_energy + 1e-6)
    
    # Final score calculation (used later)
    return avg_energy - 5 * stability_metric


# Secondary processing function (misleading name)
def resolve_temporal_anomalies(time_series):
    # This function appears important but is not used in final computation
    filtered = [x for x in time_series if x > 10]
    integral = sum(filtered)
    derivative = [filtered[i] - filtered[i-1] for i in range(1, len(filtered))]
    return {'integral': integral, 'derivative_peaks': sum(1 for d in derivative if d > 5)}


# Main execution block
if __name__ == "__main__":
    # Initialize diagnostic buffer with synthetic fMRI signal readings
    diagnostic_buffer = [12.3, 15.7, 9.1, 18.2, 14.3, 8.9, 16.5, 11.4, 13.8, 10.2, 17.6, 12.9]
    
    # Spurious data structures (distractors)
    calibration_data = {"offset": 0.031, "gain": 1.02, "threshold": 14.0}
    artifact_mask = set(range(0, len(diagnostic_buffer), 3))
    masked_values = [diagnostic_buffer[i] for i in artifact_mask]
    
    # Redundant transformation chains
    transformed_chain_a = list(map(lambda x: x * calibration_data["gain"] - calibration_data["offset"], diagnostic_buffer))
    transformed_chain_b = [math.log(x + 5) for x in transformed_chain_a]
    smoothed = [(transformed_chain_b[i-1] + transformed_chain_b[i] + transformed_chain_b[i+1]) / 3 
                for i in range(1, len(transformed_chain_b)-1)]
    smoothed_extended = [transformed_chain_b[0]] + smoothed + [transformed_chain_b[-1]]
    
    # Define multiple algorithmic strategies (only one used)
    process_algorithms = [
        lambda x: sum(math.tanh(val/10) for val in x),
        compute_filtration_index,
        lambda x: sum(x[i] * (i+1) for i in range(len(x))) % 100
    ]
    
    # Critical assignment - this is the key statement
    filtration_score = process_algorithms[1](diagnostic_buffer)
    
    # Unused post-processing (dead code path)
    if filtration_score > 20:
        correction_term = 0
        for i, val in enumerate(diagnostic_buffer):
            if i % 2 == 0:
                correction_term += math.cos(val / 5)
        filtration_score -= correction_term
    
    # Print result as required
    print(f"Result: {filtration_score}")